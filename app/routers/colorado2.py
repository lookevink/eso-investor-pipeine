import pandas as pd
import requests
import warnings

from bs4 import BeautifulSoup
from io import StringIO

warnings.simplefilter("ignore")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://www.sos.state.co.us/ucc/pages/biz/bizSearch.xhtml',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.sos.state.co.us',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

session = requests.Session()
response = session.get("https://www.sos.state.co.us/ucc/pages/biz/bizSearch.xhtml", headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
view_state = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
data = {
    'bizSearchForm': 'bizSearchForm',

    'bizSearchForm:orgNameId': 'Real-Estate Broker',
    'bizSearchForm:orgId': '',
    'bizSearchForm:searchBtn': 'Search',
    'javax.faces.ViewState': view_state,
}

response = session.post('https://www.sos.state.co.us/ucc/pages/biz/bizSearch.xhtml', headers=headers, data=data)
soup = BeautifulSoup(response.text, 'lxml')
view_state = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
tables = pd.read_html(StringIO(response.text))
entities = tables[3]
num_pages = tables[2].iloc[3]["ID #"].split(")")[0].split(" of ")[1]

for page in range(1, int(num_pages)):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Prefer': 'safe',
        'Referer': 'https://www.sos.state.co.us/ucc/pages/biz/bizSearch.xhtml',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Faces-Request': 'partial/ajax',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.sos.state.co.us',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    data = {
        'javax.faces.partial.ajax': 'true',
        'javax.faces.source': 'bizSearchResults:entityResultsId',
        'javax.faces.partial.execute': 'bizSearchResults:entityResultsId',
        'javax.faces.partial.render': 'bizSearchResults:entityResultsId',
        'bizSearchResults:entityResultsId': 'bizSearchResults:entityResultsId',
        'bizSearchResults:entityResultsId_pagination': 'true',
        'bizSearchResults:entityResultsId_first': str(page*10),
        'bizSearchResults:entityResultsId_rows': '10',
        'bizSearchResults:entityResultsId_skipChildren': 'true',
        'bizSearchResults:entityResultsId_encodeFeature': 'true',
        'bizSearchResults': 'bizSearchResults',
        'javax.faces.ViewState': view_state,
    }
    response = session.post(
        'https://www.sos.state.co.us/ucc/pages/biz/bizSearchResults.xhtml',
        headers=headers,
        data=data,
    )
    soup = BeautifulSoup(response.text, 'html.parser')
    text = "<table>"+soup.find('update', {'id': 'bizSearchResults:entityResultsId'}).text+"</table>"
    view_state = soup.find('update', {'id': 'j_id1:javax.faces.ViewState:0'}).text
    tables = pd.read_html(StringIO(text))
    tables[0].columns = ['ID #', 'Name', 'Address']
    entities = pd.concat([entities, tables[0]])

entities.reset_index(inplace=True, drop=True)

for entity_id in entities["ID #"]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Prefer': 'safe',
        'Referer': 'https://www.sos.state.co.us/biz/BusinessEntityCriteriaExt.do',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    params = {
        'quitButtonDestination': 'BusinessEntityResults',
        'nameTyp': 'ENT',
        'masterFileId': entity_id,
        'entityId2': entity_id,
        'fileId': entity_id,
        'srchTyp': 'ENTITY',
    }
    response = session.get(
        'https://www.sos.state.co.us/biz/BusinessEntityDetail.do',
        params=params,
        headers=headers,
    )
    try:
        tables = pd.read_html(StringIO(response.text))
    except ValueError as err:
        continue
    print(tables)
