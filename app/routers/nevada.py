import pandas as pd
import requests

from io import StringIO

cookies = {
    'visid_incap_2373390': 'L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto',
    'incap_ses_269_2373390': 'y9CcMaB4ahtrAvRsMa67Awn4YGUAAAAAGL+IoOuDFpOiQp+xaVOlCQ==',
    'nlbi_2373390_2147483392': 'QaG0QlhjOSNFptlCM+c3awAAAACoPpg4NUrpUI347Yx8a4J3',
    'ESSCookieEncypt': '!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO'
                       '+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=',
    'nlbi_2373390': '6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN',
    'reese84': '3:FV/UGSiKXSbJGV2XyDnKkA==:1qI5ZNvUoAeHZZ0W1rpahxjyNlhO0sQyzVVz58G',
    'ASP.NET_SessionId': 'jg1x5ubs3z2uvyw3zdfbbhcq',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://esos.nv.gov/EntitySearch/OnlineBusinessAndMarkSearchResult',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://esos.nv.gov',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Cookie': 'visid_incap_2373390=L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto; '
              'incap_ses_269_2373390=y9CcMaB4ahtrAvRsMa67Awn4YGUAAAAAGL+IoOuDFpOiQp+xaVOlCQ==; '
              'nlbi_2373390_2147483392=QaG0QlhjOSNFptlCM+c3awAAAACoPpg4NUrpUI347Yx8a4J3; '
              'ESSCookieEncypt=!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl'
              '/KrLjO+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=; '
              'nlbi_2373390=6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN; '
              'reese84=3:FV/UGSiKXSbJGV2XyDnKkA==:1qI5ZNvUoAeHZZ0W1rpahxjyNlhO0sQyzVVz58G'
              '/7LoSu4SY8i7swjTLDKSCOwJCNnRZDzwS9V3MxuIRKHpIESvt8PeMuKXhBYC2pPLRcS6H45tepPH7f7RMOnqa1FoZ20vW9cKIh7vI33r'
              'gRXke3dQipc6fZWGNw+9s75P6tDGyRsOW91k1NwYXSBqK6bh+fJZhJGtTyParcRtok3A/kBqrczhKgo1dh1XVCvzWA43zbY6Fpi/vwIe'
              'lL10Er5UWifIdfVsuITGZGGoQCU2eJ6KahTL7K6fy0vWK3qXcmdOL5WZC5ZrbNNXBjN0ZZfN4t5JaMLu0XKyLv3ql39TSI2EF8rVAMXa'
              'L8K+jezkwplgY/kMvKhqRPWngw/xErEI1nzCpPaTcdcCavqf931o9lR4Pa068Xd+ITALES3OH86Xqo7bVGmSUH68fe8ZDa+XSSUQjcPt'
              'Z8noV2QuZhSieVO70Mls3HLgK+4jI103M4MX2Ye8G4xHnIWPpUyl0Q9Rs:YwE+KLTBkFQ025F35B7Ak+BvGZiPpq7BrGmyxbORchY=; '
              'ASP.NET_SessionId=jg1x5ubs3z2uvyw3zdfbbhcq',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
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

session = requests.Session()
response = session.post(
    'https://esos.nv.gov/EntitySearch/OnlineBusinessAndMarkSearchResult',
    cookies=cookies,
    headers=headers,
    data=data,
)

tables = pd.read_html(StringIO(response.text))

print(tables[0])
print(tables[1])

num_pages = tables[1][0][0].split(",")[0].split(" of ")[1]

cookies = {
    'visid_incap_2373390': 'L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto',
    'incap_ses_269_2373390': 'y9CcMaB4ahtrAvRsMa67Awn4YGUAAAAAGL+IoOuDFpOiQp+xaVOlCQ==',
    'nlbi_2373390_2147483392': 'QaG0QlhjOSNFptlCM+c3awAAAACoPpg4NUrpUI347Yx8a4J3',
    'ESSCookieEncypt': '!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO'
                       '+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=',
    'nlbi_2373390': '6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN',
    'reese84': '3:FV/UGSiKXSbJGV2XyDnKkA==:1qI5ZNvUoAeHZZ0W1rpahxjyNlhO0sQyzVVz58G'
               '/7LoSu4SY8i7swjTLDKSCOwJCNnRZDzwS9V3MxuIRKHpIESvt8PeMuKXhBYC2pPLRcS6H45tepPH7f7RMOnqa1FoZ20vW9cKIh7vI33'
               'rgRXke3dQipc6fZWGNw+9s75P6tDGyRsOW91k1NwYXSBqK6bh+fJZhJGtTyParcRtok3A/kBqrczhKgo1dh1XVCvzWA43zbY6Fpi/vw'
               'IelL10Er5UWifIdfVsuITGZGGoQCU2eJ6KahTL7K6fy0vWK3qXcmdOL5WZC5ZrbNNXBjN0ZZfN4t5JaMLu0XKyLv3ql39TSI2EF8rVA'
               'MXaL8K+jezkwplgY/kMvKhqRPWngw/xErEI1nzCpPaTcdcCavqf931o9lR4Pa068Xd+ITALES3OH86Xqo7bVGmSUH68fe8ZDa+XSSUQ'
               'jcPtZ8noV2QuZhSieVO70Mls3HLgK+4jI103M4MX2Ye8G4xHnIWPpUyl0Q9Rs:YwE+KLTBkFQ025F35B7Ak+BvGZiPpq7BrGmyxbORc'
               'hY=',
    'ASP.NET_SessionId': 'jg1x5ubs3z2uvyw3zdfbbhcq',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://esos.nv.gov/EntitySearch/OnlineBusinessAndMarkSearchResult',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://esos.nv.gov',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Cookie': 'visid_incap_2373390=L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto; '
              'incap_ses_269_2373390=y9CcMaB4ahtrAvRsMa67Awn4YGUAAAAAGL+IoOuDFpOiQp+xaVOlCQ==; '
              'nlbi_2373390_2147483392=QaG0QlhjOSNFptlCM+c3awAAAACoPpg4NUrpUI347Yx8a4J3; '
              'ESSCookieEncypt=!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl'
              '/KrLjO+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=; '
              'nlbi_2373390=6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN; '
              'reese84=3:FV/UGSiKXSbJGV2XyDnKkA==:1qI5ZNvUoAeHZZ0W1rpahxjyNlhO0sQyzVVz58G'
              '/7LoSu4SY8i7swjTLDKSCOwJCNnRZDzwS9V3MxuIRKHpIESvt8PeMuKXhBYC2pPLRcS6H45tepPH7f7RMOnqa1FoZ20vW9cKIh7vI33r'
              'gRXke3dQipc6fZWGNw+9s75P6tDGyRsOW91k1NwYXSBqK6bh+fJZhJGtTyParcRtok3A/kBqrczhKgo1dh1XVCvzWA43zbY6Fpi/vwIe'
              'lL10Er5UWifIdfVsuITGZGGoQCU2eJ6KahTL7K6fy0vWK3qXcmdOL5WZC5ZrbNNXBjN0ZZfN4t5JaMLu0XKyLv3ql39TSI2EF8rVAMXa'
              'L8K+jezkwplgY/kMvKhqRPWngw/xErEI1nzCpPaTcdcCavqf931o9lR4Pa068Xd+ITALES3OH86Xqo7bVGmSUH68fe8ZDa+XSSUQjcPt'
              'Z8noV2QuZhSieVO70Mls3HLgK+4jI103M4MX2Ye8G4xHnIWPpUyl0Q9Rs:YwE+KLTBkFQ025F35B7Ak+BvGZiPpq7BrGmyxbORchY=; '
              'ASP.NET_SessionId=jg1x5ubs3z2uvyw3zdfbbhcq',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

for i in range(2, int(num_pages) + 1):
    data = f'undefined&sortby=&stype=a&pidx={i}'
    response = session.post(
        'hvOnlineBusinessAndMarkSearchResultPagination',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    tables = pd.read_html(StringIO(response.text))
    print(tables[0])
    print(tables[1])


cookies = {
    'visid_incap_2373390': 'L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto',
    'incap_ses_269_2373390': 'pRjSAEYQUSsrHgNtMa67A9QbYWUAAAAAGrwOrb0zMR1X33witZmt3Q==',
    'nlbi_2373390_2147483392': 'oYlUX7wARCHkudeTM+c3awAAAADEgVpPabaV9D/WlwtAOi9M',
    'ESSCookieEncypt': '!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO'
                       '+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=',
    'nlbi_2373390': '6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN',
    'reese84': '3:fJWfimJnLMZqf6HNI5oZzw==:MXsNQ+U7+c7BNv1nYl8vF2EZPNV47'
               '+ryEOthylkA7HH2BKFOArL6r2YBTIEyWqS70xEqJTJXuMBh2cpyGepLDOtKkLTUbUdUrY0MUL0uoaJ'
               '+WOVvpogyYRkzmODYOqCUJD9acd5GeWubYdAUH+/kEWsUvgNW/MCONri8tMSLcDTdaxUg2o7n+ByFOqti5I7pRJW8MhmbRo'
               '+/7iRZbeFbONkny9iydK7dVFRs1WgSgmgugmBkVGY61/9S4of+zsWyRL8NXDj4I3eUbWSgNL6gwR'
               '+vTQHpCYBDmFqH2u42396VvTt4GqidsB4XmyE3/ikbiLB9BlEA5C+OTeaVnjW+JLFISGHCquVEf0Gw+Z02sN'
               '/8Eu1FxOy2tyfffq5rxwuEF'
               '/OZSlrSOCGy5K70SDVQPwzwVHTRolpHgxBZDpmufq8DCC4IPoIrkAK9dxWOwZGrzwvr2FkjToLfH8sRHrTgHyRAtEg+s3F3TChP3'
               '+eS9xCo8BM66JuSaQc7XCE3rBmGQ2L/MOlNGhhD51pRljNNhg==:dtkDh7eiYvOk2ZabwqmQNjcHzA6lye1Jy3KRkrOG/fg=',
    'ASP.NET_SessionId': 'jg1x5ubs3z2uvyw3zdfbbhcq',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://esos.nv.gov/EntitySearch/OnlineBusinessAndMarkSearchResult',
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
}

data = {
    'businessId': '1192458',
}

response = session.post('https://esos.nv.gov/EntitySearch/BusinessInformation', cookies=cookies, headers=headers,
                        data=data)
