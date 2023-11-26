import pandas as pd
import requests

from io import StringIO


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://www.sos.state.co.us/biz/BusinessEntityCriteriaExt.do?resetTransTyp=Y',
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

data = {
    'docWorkThruDt': '11/20/2023',
    'searchName': 'Real-Estate Broker',
    'mstrTmkId': '',
    'resetTransTyp': 'Y',
    'cmd': [
        'Search',
        'Search',
    ],
}

session = requests.Session()
session.get("https://www.sos.state.co.us/biz/BusinessEntityCriteriaExt.do")
response = session.post(
    'https://www.sos.state.co.us/biz/BusinessEntityCriteriaExt.do',
    headers=headers,
    data=data,
)

tables = pd.read_html(StringIO(response.text))
entities = tables[4]

num_pages = tables[3][0][0].split(".")[1].split(" of ")[1]

for page in range(1, int(num_pages) + 1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Prefer': 'safe',
        'Referer': f'https://www.sos.state.co.us/biz/BusinessEntityResults.do?&cmd=passgo&pi1={page-1}',
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
    response = session.get(
        f'https://www.sos.state.co.us/biz/BusinessEntityResults.do?&cmd=passgo&pi1={page}',
        headers=headers,
    )
    tables = pd.read_html(StringIO(response.text))
    entities = pd.concat([entities, tables[4]])

print(entities)


