from io import StringIO

import pandas as pd
import requests

session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://icis.corp.delaware.gov',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://icis.corp.delaware.gov',
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

response1 = session.get("https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx", headers=headers)

view_state = response1.text.split('id="__VIEWSTATE" value="')[1].split('"')[0]
view_state_generator = response1.text.split('id="__VIEWSTATEGENERATOR" value="')[1].split('"')[0]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://icis.corp.delaware.gov',
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
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
    'ctl00$hdnshowlogout': '',
    'ctl00$hdnfilingtype': '',
    'as_sitesearch': '',
    'ctl00$ContentPlaceHolder1$frmEntityName': 'Real-Estate Broker',
    'ctl00$ContentPlaceHolder1$frmFileNumber': '',
    'ctl00$ContentPlaceHolder1$hdnPostBackSource': '',
    'ctl00$ContentPlaceHolder1$lblMessage': '',
    'ctl00$ContentPlaceHolder1$btnSubmit': 'Search',
}

response2 = session.post(
    'https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx',
    headers=headers,
    data=data,
)

if "Please complete the reCAPTCHA" in response2.text:
    print("reCAPTCHA detected.")
    exit(1)
else:
    try:
        tables = pd.read_html(StringIO(response2.text), attrs={"id": "tblResults"})
    except ValueError as err:
        print(err)
        tables = []

    for table in tables:
        print(table)

# NOTE: Delaware has a captcha, so we need to have long sleeps between requests.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://icis.corp.delaware.gov',
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

view_state = response2.text.split('id="__VIEWSTATE" value="')[1].split('"')[0]
view_state_generator = response2.text.split('id="__VIEWSTATEGENERATOR" value="')[1].split('"')[0]

data = {
    '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$rptSearchResults$ctl00$lnkbtnEntityName',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
    'ctl00$hdnshowlogout': '',
    'ctl00$hdnfilingtype': '',
    'as_sitesearch': '',
    'ctl00$ContentPlaceHolder1$frmEntityName': 'Real-Estate Broker',
    'ctl00$ContentPlaceHolder1$frmFileNumber': '',
    'ctl00$ContentPlaceHolder1$hdnPostBackSource': '',
    'ctl00$ContentPlaceHolder1$lblMessage': '',
}

response3 = requests.post(
    'https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx',
    headers=headers,
    data=data,
)

print(response3.text)