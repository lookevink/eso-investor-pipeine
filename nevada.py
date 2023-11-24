import pandas as pd
import requests

from io import StringIO

cookies = {
    'visid_incap_2373390': 'L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto',
    'incap_ses_269_2373390': 'y9CcMaB4ahtrAvRsMa67Awn4YGUAAAAAGL+IoOuDFpOiQp+xaVOlCQ==',
    'nlbi_2373390_2147483392': 'QaG0QlhjOSNFptlCM+c3awAAAACoPpg4NUrpUI347Yx8a4J3',
    'ESSCookieEncypt': '!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=',
    'nlbi_2373390': '6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN',
    'reese84': '3:FV/UGSiKXSbJGV2XyDnKkA==:1qI5ZNvUoAeHZZ0W1rpahxjyNlhO0sQyzVVz58G/7LoSu4SY8i7swjTLDKSCOwJCNnRZDzwS9V3MxuIRKHpIESvt8PeMuKXhBYC2pPLRcS6H45tepPH7f7RMOnqa1FoZ20vW9cKIh7vI33rgRXke3dQipc6fZWGNw+9s75P6tDGyRsOW91k1NwYXSBqK6bh+fJZhJGtTyParcRtok3A/kBqrczhKgo1dh1XVCvzWA43zbY6Fpi/vwIelL10Er5UWifIdfVsuITGZGGoQCU2eJ6KahTL7K6fy0vWK3qXcmdOL5WZC5ZrbNNXBjN0ZZfN4t5JaMLu0XKyLv3ql39TSI2EF8rVAMXaL8K+jezkwplgY/kMvKhqRPWngw/xErEI1nzCpPaTcdcCavqf931o9lR4Pa068Xd+ITALES3OH86Xqo7bVGmSUH68fe8ZDa+XSSUQjcPtZ8noV2QuZhSieVO70Mls3HLgK+4jI103M4MX2Ye8G4xHnIWPpUyl0Q9Rs:YwE+KLTBkFQ025F35B7Ak+BvGZiPpq7BrGmyxbORchY=',
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
    'Cookie': 'visid_incap_2373390=L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto; incap_ses_269_2373390=y9CcMaB4ahtrAvRsMa67Awn4YGUAAAAAGL+IoOuDFpOiQp+xaVOlCQ==; nlbi_2373390_2147483392=QaG0QlhjOSNFptlCM+c3awAAAACoPpg4NUrpUI347Yx8a4J3; ESSCookieEncypt=!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=; nlbi_2373390=6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN; reese84=3:FV/UGSiKXSbJGV2XyDnKkA==:1qI5ZNvUoAeHZZ0W1rpahxjyNlhO0sQyzVVz58G/7LoSu4SY8i7swjTLDKSCOwJCNnRZDzwS9V3MxuIRKHpIESvt8PeMuKXhBYC2pPLRcS6H45tepPH7f7RMOnqa1FoZ20vW9cKIh7vI33rgRXke3dQipc6fZWGNw+9s75P6tDGyRsOW91k1NwYXSBqK6bh+fJZhJGtTyParcRtok3A/kBqrczhKgo1dh1XVCvzWA43zbY6Fpi/vwIelL10Er5UWifIdfVsuITGZGGoQCU2eJ6KahTL7K6fy0vWK3qXcmdOL5WZC5ZrbNNXBjN0ZZfN4t5JaMLu0XKyLv3ql39TSI2EF8rVAMXaL8K+jezkwplgY/kMvKhqRPWngw/xErEI1nzCpPaTcdcCavqf931o9lR4Pa068Xd+ITALES3OH86Xqo7bVGmSUH68fe8ZDa+XSSUQjcPtZ8noV2QuZhSieVO70Mls3HLgK+4jI103M4MX2Ye8G4xHnIWPpUyl0Q9Rs:YwE+KLTBkFQ025F35B7Ak+BvGZiPpq7BrGmyxbORchY=; ASP.NET_SessionId=jg1x5ubs3z2uvyw3zdfbbhcq',
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
    'ESSCookieEncypt': '!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=',
    'nlbi_2373390': '6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN',
    'reese84': '3:FV/UGSiKXSbJGV2XyDnKkA==:1qI5ZNvUoAeHZZ0W1rpahxjyNlhO0sQyzVVz58G/7LoSu4SY8i7swjTLDKSCOwJCNnRZDzwS9V3MxuIRKHpIESvt8PeMuKXhBYC2pPLRcS6H45tepPH7f7RMOnqa1FoZ20vW9cKIh7vI33rgRXke3dQipc6fZWGNw+9s75P6tDGyRsOW91k1NwYXSBqK6bh+fJZhJGtTyParcRtok3A/kBqrczhKgo1dh1XVCvzWA43zbY6Fpi/vwIelL10Er5UWifIdfVsuITGZGGoQCU2eJ6KahTL7K6fy0vWK3qXcmdOL5WZC5ZrbNNXBjN0ZZfN4t5JaMLu0XKyLv3ql39TSI2EF8rVAMXaL8K+jezkwplgY/kMvKhqRPWngw/xErEI1nzCpPaTcdcCavqf931o9lR4Pa068Xd+ITALES3OH86Xqo7bVGmSUH68fe8ZDa+XSSUQjcPtZ8noV2QuZhSieVO70Mls3HLgK+4jI103M4MX2Ye8G4xHnIWPpUyl0Q9Rs:YwE+KLTBkFQ025F35B7Ak+BvGZiPpq7BrGmyxbORchY=',
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
    'Cookie': 'visid_incap_2373390=L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto; incap_ses_269_2373390=y9CcMaB4ahtrAvRsMa67Awn4YGUAAAAAGL+IoOuDFpOiQp+xaVOlCQ==; nlbi_2373390_2147483392=QaG0QlhjOSNFptlCM+c3awAAAACoPpg4NUrpUI347Yx8a4J3; ESSCookieEncypt=!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=; nlbi_2373390=6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN; reese84=3:FV/UGSiKXSbJGV2XyDnKkA==:1qI5ZNvUoAeHZZ0W1rpahxjyNlhO0sQyzVVz58G/7LoSu4SY8i7swjTLDKSCOwJCNnRZDzwS9V3MxuIRKHpIESvt8PeMuKXhBYC2pPLRcS6H45tepPH7f7RMOnqa1FoZ20vW9cKIh7vI33rgRXke3dQipc6fZWGNw+9s75P6tDGyRsOW91k1NwYXSBqK6bh+fJZhJGtTyParcRtok3A/kBqrczhKgo1dh1XVCvzWA43zbY6Fpi/vwIelL10Er5UWifIdfVsuITGZGGoQCU2eJ6KahTL7K6fy0vWK3qXcmdOL5WZC5ZrbNNXBjN0ZZfN4t5JaMLu0XKyLv3ql39TSI2EF8rVAMXaL8K+jezkwplgY/kMvKhqRPWngw/xErEI1nzCpPaTcdcCavqf931o9lR4Pa068Xd+ITALES3OH86Xqo7bVGmSUH68fe8ZDa+XSSUQjcPtZ8noV2QuZhSieVO70Mls3HLgK+4jI103M4MX2Ye8G4xHnIWPpUyl0Q9Rs:YwE+KLTBkFQ025F35B7Ak+BvGZiPpq7BrGmyxbORchY=; ASP.NET_SessionId=jg1x5ubs3z2uvyw3zdfbbhcq',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

for i in range(2, int(num_pages) + 1):
    data = f'undefined&sortby=&stype=a&pidx={i}'
    response = session.post(
        'https://esos.nv.gov/EntitySearch/OnlineBusinessAndMarkSearchResultPagination',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    tables = pd.read_html(StringIO(response.text))
    print(tables[0])
    print(tables[1])
