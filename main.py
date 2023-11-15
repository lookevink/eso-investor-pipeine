import logging
import time
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import requests
from bs4 import BeautifulSoup, Tag
import re
import csv
from io import StringIO

logging.basicConfig(level=logging.INFO)
app = FastAPI()


class EntityNames(BaseModel):
    """
    Represents a list of entity names.

    Attributes:
        names (list[str]): The list of entity names.

    """
    names: list[str] = Field(..., example=["Venture REI", "Another Co"])


def extract_entity_numbers(html: str) -> list[str]:
    """
    Extracts entity numbers from HTML content.

    Args:
        html (str): The HTML content to extract entity numbers from.

    Returns:
        list[str]: A list of entity numbers extracted from the HTML.

    """
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', {'class': 'BlueLink'})
    pattern = re.compile(r'entityNumber=([\w\d]+)')
    return [match[1] for link in links if (match := pattern.search(link.get('href')))]


def write_csv_data(csv_writer: csv.DictWriter, business_name: str, table: Tag):
    """
    Writes data from an HTML table to a CSV file using the provided CSV writer.

    Args:
        csv_writer (csv.DictWriter): The CSV writer object.
        business_name (str): The business name associated with the data.
        table (bs4.element.Tag): The HTML table element containing the data.

    """
    rows = table.find_all('tr')
    headers = [header.text for header in rows[0].find_all('th')]
    for row in rows[1:]:
        cells = row.find_all('td')
        row_data = {headers[i]: cells[i].text.strip() for i in range(len(cells)) if headers[i] in ['Title', 'Name',
                                                                                                   'Address']}
        if business_name:
            row_data['BusinessName'] = business_name
        csv_writer.writerow(row_data)


@app.post("/az/get_member_data/")
async def get_entity_data(entities: EntityNames) -> object:
    """
    Retrieves entity data from the Arizona Corporation Commission website for the given list of entity names.

    Args:
        entities (EntityNames): The list of entity names.

    Returns:
        object: A StreamingResponse object containing the entity data in CSV format.

    """
    logging.info("Starting the get_entity_data function")
    csv_output = StringIO()
    csv_writer = csv.DictWriter(csv_output, fieldnames=['Title', 'Name', 'Address', 'BusinessName'])
    csv_writer.writeheader()

    for entity_name in entities.names:
        logging.info(f"Processing entity: {entity_name}")
        time.sleep(5)  # Rate limit wait
        response = requests.post(
            "https://ecorp.azcc.gov/EntitySearch/Search",
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=f'model%5BSearchCriteria%5D%5BquickSearch%5D%5BBusinessName%5D={entity_name}'
        )

        if response.status_code != 200:
            logging.warning(f"Entity {entity_name} returned {response.status_code}. Skipping.")
            continue

        entity_numbers = extract_entity_numbers(response.json().get('Data', ''))
        logging.info(f"Found {len(entity_numbers)} entity numbers for entity {entity_name}")

        for entity_number in entity_numbers:
            response = requests.get(
                f"https://ecorp.azcc.gov/BusinessSearch/BusinessInfo?entityNumber={entity_number}"
            )
            soup = BeautifulSoup(response.text, 'html.parser')
            business_name = soup.find(
                'label',
                {'for': 'Business_BusinessName'}).find_next('div').text.strip() if soup.find(
                'label', {'for': 'Business_BusinessName'}
            ) else None
            print(f"Processing business {business_name}")
            for table in soup.find_all('table', id='grid_principalList'):
                write_csv_data(csv_writer, business_name, table)

    csv_output.seek(0)
    return StreamingResponse(csv_output, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=output.csv"
    })
