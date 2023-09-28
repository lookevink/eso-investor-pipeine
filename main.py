from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import requests
from bs4 import BeautifulSoup
import re
import csv
from io import StringIO
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()


class EntityNames(BaseModel):
    names: list[str] = Field(..., example=["Venture REI", "Another Co"])


@app.post("/az/get_member_data/")
async def get_entity_data(entities: EntityNames):
    entity_names_list = entities.names
    csv_output = StringIO()
    fieldnames = ['Title', 'Name', 'Address', 'BusinessName']
    csv_writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    csv_writer.writeheader()

    for entity_name in entity_names_list:
        entity_numbers = []
        url = "https://ecorp.azcc.gov/EntitySearch/Search"
        payload = f'model%5BSearchCriteria%5D%5BquickSearch%5D%5BBusinessName%5D={entity_name}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()

        data = response_data.get('Data', None)
        if data is None:
            logging.warning(
                f"No data received for entity {entity_name}. Skipping.")
            continue

        soup = BeautifulSoup(data, 'html.parser')
        links = soup.find_all('a', {'class': 'BlueLink'})
        pattern = re.compile(r'entityNumber=(\d+)')

        for link in links:
            href = link.get('href')
            match = pattern.search(href)
            if match:
                entity_number = match.group(1)
                entity_numbers.append(entity_number)

        for entity_number in entity_numbers:
            url = f"https://ecorp.azcc.gov/BusinessSearch/BusinessInfo?entityNumber={entity_number}"
            response = requests.request("GET", url)
            soup = BeautifulSoup(response.text, 'html.parser')
            business_name = None

            label = soup.find('label', {'for': 'Business_BusinessName'})
            if label:
                business_name_div = label.find_next('div')
                if business_name_div:
                    business_name = business_name_div.text.strip()

            tables = soup.find_all('table')
            for table in tables:
                if table.get('id') == 'grid_principalList':
                    rows = table.find_all('tr')
                    headers = [
                        header.text for header in rows[0].find_all('th')]

                    for row in rows[1:]:
                        cells = row.find_all('td')
                        row_data = {headers[i]: cells[i].text.strip() for i in range(
                            len(cells)) if headers[i] in ['Title', 'Name', 'Address']}
                        if business_name:
                            row_data['BusinessName'] = business_name

                        csv_writer.writerow(row_data)

    csv_output.seek(0)
    return StreamingResponse(csv_output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=output.csv"})
