import pandas as pd
import requests

from io import StringIO

# cookies = {
#     'JSESSIONID': '0000cmSD73o7ScNAJQ4uHfJ0Tq6:1g5fhlp7f',
#     'TS01132dd1': '01a7dc464c2571df9192f733404e8297e05b92fab204df9d7665c6bafd60b42e239ff1a975b62f9e86008c0b0e76f6b18cfd67052c7812ca4c8bd9c81ae4a8e27d623826e9',
#     'cf_clearance': 'SjeMfqjY0s.hZ4WJVHlQWq__eS5eMULZxAsX.HYg7Gk-1700939686-0-1-7111f292.6b282b26.2610ad72-0.2.1700939686',
#     'TS0145d5bf': '01a7dc464c32e8af421924ceddde07da48f39729025920de48256a513e62de16a26b08ad822354fb6f784769230f894d8f9ed2f13560a4076529b579e50e7f8fb93b9f3796',
#     '__cf_bm': '8xX2ELaNzjycpY8dTrZ1qFfqqNkYbWZAwMu9tjcko30-1700938903-0-AR4XX6nCRxhZUW8OrBCItbLHYQL10nK0AXq23dzKPgKHhMQUg/u7Ai1GhFQe1KC/DtvkCM3iiyzk4vhaziGKIpo=',
#     'menuheaders': '-1c',
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://www.sos.state.co.us/biz/AdvancedSearchCriteria.do',
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
    'dateFrom': '',
    'dateTo': '',
    'includeEntity': 'true',
    'searchName': 'REAL-ESTATE BROKER',
    'personName_lastName': '',
    'personName_firstName': '',
    'personName_middleName': '',
    'personName_suffixName': '',
    'entityName': '',
    # 'g-recaptcha-response': '',
    'cmd': 'Search',
}

session = requests.Session()
session.get("https://www.sos.state.co.us/")
response = session.post('https://www.sos.state.co.us/biz/AdvancedSearchCriteria.do', headers=headers, data=data)

tables = pd.read_html(StringIO(response.text))

print(tables[0])
print(tables[1])
print(tables[2])
print(tables[3])
print(tables[4])
print(tables[5])
print(tables[6])
print(tables[7])
print(tables[8])
print(tables[9])
print(tables[10])
print(tables[11])
print(tables[12])
print(tables[13])
print(tables[14])
print(tables[15])
print(tables[16])
print(tables[17])
print(tables[18])
print(tables[19])
print(tables[20])
print(tables[21])
print(tables[22])
print(tables[23])
print(tables[24])
print(tables[25])