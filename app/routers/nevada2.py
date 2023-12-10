import pandas as pd
import requests

from io import StringIO

from bs4 import BeautifulSoup

from incapsula import IncapSession, MaxRetriesExceeded, RecaptchaBlocked, WebsiteResourceParser


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://www.nvsos.gov/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


class MyResourceParser(WebsiteResourceParser):
    # List of arguments to pass into BeautifulSoup().find() method.
    extra_find_iframe_args = [
        ('iframe', {'src': 'https://www.nvsos.gov'})
    ]


incap_session = IncapSession(resource_parser=MyResourceParser)
try:
    response = incap_session.get(
        'https://www.nvsos.gov/sos/businesses'
    )
except (RecaptchaBlocked, MaxRetriesExceeded) as e:
    raise

cookies = {
    "ASP.NET_SessionId": "jg1x5ubs3z2uvyw3zdfbbhcq",
    "ESSCookieEncypt": "!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO"
                       "+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=",
    "incap_ses_159_2373390": "O2EGW28h3RNTJvSmv+E0Ag35Z2UAAAAAuH3vyQ01+sKPHBFP5Wsu4Q==",
    "incap_ses_269_2373390": "pRjSAEYQUSsrHgNtMa67A9QbYWUAAAAAGrwOrb0zMR1X33witZmt3Q==",
    "nlbi_2373390": "6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN",
    "nlbi_2373390_2147483392": "F9CKc6PTJDHW2eWhM+c3awAAAACXmoEelcgskolLed8e3H73",
    "reese84": "3:Qpndh/M7bSJqZWDKQ3orBw==:6dPW9uJZLLCoKkA1YgsZE+FLnK0XpdG2bkyREez0rdcXbEL"
               "+47ztEWE7mQN7SY1B4FeI4C6usIZdsvOZf7bjCWS9P2giLs8QLxgIqR6DV8uczhIlfT5bB8qfmTky1a4sPPGztHR9Exg92g9eAqT6k1"
               "MEhs7m4PdduTU5C+scOEmYhYLsLUSvgoqq9D9IPCU/RWNck9HSWWeK53uIT8tiUP3C6lJKTMtDBT7qvWob6DKXu7sQZQVQcbWpq4Y6w"
               "SE6shlmGCJyGyr5SY93gGzQlAJUFbya7Vhez4ygrGV92nyjkscfdxXU9eFHNfrK/8eX0kbknoanQGwZn2U6OdVB0wLSrQxpJi1ilQpi"
               "xgyK847djVifKsOHgDAKbyXLYcjuwphsKlhegv+NPB09zlik9O9ocXAHhCcaF8fUw8dpSgudq7yDBNFNoQ6ZEeZeonWis3acEji3y6K"
               "xIJJpfmkeMAyU+oRBTjCTjO3nGs+e7iIUi5n3a7EKKUOtDDaiVDLp:Wjts0g1m/8WOmZQsOXUqZznmCm4RCmaRnSV4boaT6Ok=",
    "visid_incap_2373390": "L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto"
}


session = requests.Session()

response3 = session.get(
    'https://www.nvsos.gov/sos/businesses',
    headers=headers
)

soup = BeautifulSoup(response3.text, 'html.parser')

script_src = None
iframe_src = None

# if <meta name="ROBOTS"/> is present
if soup.find_all('meta', attrs={'name': 'ROBOTS'}):
    # then find script src="/_Incapsula_Resource?
    script_src = soup.find_all('script')[0]['src']
    iframe_src = soup.find_all('iframe')[0]['src']

if iframe_src:
    response2 = session.get(
        f'https://www.nvsos.gov{iframe_src}',
        headers=headers
    )
elif script_src:
    response2 = session.get(
        f'https://www.nvsos.gov{script_src}',
        headers=headers
    )
else:
    print("No script or iframe found")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Prefer': 'safe',
    'Referer': 'https://www.nvsos.gov/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

response3 = session.post(
    'https://www.nvsos.gov/_Incapsula_Resource?SWCGHOEL=v2&dai=66251468279054981&cts=g5HqTwVo4xqNqE38HrAX9mApMo9V'
    '%2fIb9cF9gK8FomBytpkFXtkqeDg82kHYR8ONh',
    headers=headers,
)

response4 = session.get(
    'https://esos.nv.gov/EntitySearch/OnlineEntitySearch',
    headers=headers,
    cookies=cookies,
)
assert response4.status_code == 200

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Prefer': 'safe',
    'Referer': 'https://esos.nv.gov/EntitySearch/OnlineEntitySearch',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://esos.nv.gov',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'QuickSearch.BusinessId': '',
    'QuickSearch.NVBusinessNumber': '',
    'QuickSearch.StartsWith': 'false',
    'QuickSearch.Contains': 'true',
    'QuickSearch.ExactMatch': 'false',
    'QuickSearch.Allwords': 'false',
    'QuickSearch.BusinessName': 'Real-Estate',
    'QuickSearch.PrincipalName': '',
    'QuickSearch.AgentName': '',
    'QuickSearch.MarkNumber': '',
    'QuickSearch.Classification': '',
    'QuickSearch.Goods': '',
    'QuickSearch.ApplicantName': '',
    'QuickSearch.All': 'true',
    'QuickSearch.EntitySearch': 'false',
    'QuickSearch.MarkSearch': 'false',
    'AdvancedSearch.BusinessTypeID': '',
    'AdvancedSearch.BusinessStatusID': '',
    'g-recaptcha-response': '',
}

response4 = session.post(
    'https://esos.nv.gov/EntitySearch/OnlineBusinessAndMarkSearchResult',
    headers=headers,
    data=data,
)

assert response3.status_code == 200

tables = pd.read_html(StringIO(response4.text))
num_pages = tables[1][0][0].split(",")[0].split(" of ")[1]

for i in range(2, int(num_pages) + 1):
    data = f'undefined&sortby=&stype=a&pidx={i}'
    response = session.post(
        'hvOnlineBusinessAndMarkSearchResultPagination',
        headers=headers,
        data=data,
    )
    tables = pd.read_html(StringIO(response.text))
    pd.concat([tables, tables[1]], ignore_index=True)
