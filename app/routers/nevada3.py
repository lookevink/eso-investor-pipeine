from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as pw:
        desktop_chrome = pw.devices['Desktop Chrome']
        browser = await pw.chromium.launch(
            headless=False
        )
        context = await browser.new_context(
            **desktop_chrome,
            locale='en-US'
        )
        headers = {
            'authority': 'www.nvsilverflume.gov',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://www.nvsilverflume.gov/home',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36',
        }
        await context.set_extra_http_headers(
            headers
        )
        page = await context.new_page()
        await page.goto('https://www.nvsilverflume.gov/home')
        await page.wait_for_timeout(2000)
        await page.evaluate("window.scrollTo(0, 100)")
        await page.wait_for_timeout(1000)
        await page.get_by_text("Business Entity Search").click()
        await page.wait_for_url("https://esos.nv.gov/EntitySearch/OnlineEntitySearch")
        # await browser.close()


if __name__ == '__main__':
    asyncio.run(main())



"""
curl 'https://www.nvsilverflume.gov/redirectToCenuity/be' --compressed -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Prefer: safe' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: JSESSIONID=7A355EF6E4175C539BB4440036E61B4F; ESSCookieEncypt=!/yvUsOF6DKDfApGj+pcpa7ZMcUZSD+cRPJGMB7VJHoBVkVA/zwLjWwskKi6BaC/EhTKNJpSz4XtF+eF/SGba9004Y9tShrgfRfdYBRDegNpAyk2/NYO0Gt91FNcEZR0oSiKxIZgCi6EjZz+x/tSedlhpVS+B7jQ=; visid_incap_2376406=XSqqSnS4ReC0Kijq5Age3/X7YGUAAAAAQUIPAAAAAACdPSdiRemwAHlBemRSodgw; nlbi_2376406=ef+hEzgK5l6MHfqWMjQ6+gAAAABOa7Fcw8MRlGPprMfj5Azg; nlbi_2376406_2147483392=jLM9Alcp+wsCd3DxMjQ6+gAAAADcUC1r5FS8KdLUl2sdt4Qu; reese84=3:mhZvxO0hwxyE5w7k/U7h9w==:rlbYOCZehKInsclmpb0386jWPmdqpoDuQMYm/k+v3xyYnlmaJvbpe2jH4hAxcIuJFPXek2l/rtrvpwb21eoscYi7e0Q86N0tWo27rTxF84B94F6p6WRcqKGB55AV/GRLy+HEcoGIXkCkJEqVhPI4NWAaPZ2IakzOv/5z4+fKYvjJEARNWnU/fHXTbuTiuYwEVEOuemSemDEHffFuD6NTi4muMQ9tzoJDjSEKl8Zs8ll57gm9VS2GwYq8tOHTWXwSYL3G5pGcBNe9gh4raZSfsOCgMnzmjq2o4f3hlfHIAXqBVn+mQP8DXmoI6Q+yzUNpegRZFaqfxvFknPIeWArEuHJZO4HXZG+EDy+fIZh50pNbj6F6lyUC5vFFL646EV7o9HLG8LKulo/h2nNIGYuWZ5ZNtvNVzYyH6mQkHvHwQKc/49ojuM0fRo8lxSxmA4BbT1MPaJyOBlOEOjszlonVKQbrAnmWQGOEtwMR3i3Qf2Rj0sA8UPhFEf3miJj85dt8:GvrxPusXyhtQfs3Ixah1S9/1kp2uTWdvvbmKRflm+YU=; incap_ses_159_2376406=dV5cUOO9JFNM7meqv+E0AgL2b2UAAAAAvjM2pjqL9eYooEtF4/2ayw==' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'TE: trailers'

curl 'https://esos.nv.gov/Search/BE' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Prefer: safe' -H 'Referer: https://www.nvsilverflume.gov/' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: visid_incap_2373390=L5fG2I2USai6mFyjtyzBcQn4YGUAAAAAQUIPAAAAAAAN2FiLysaqfD9B6MrCdKto; nlbi_2373390_2147483392=I1XPT+cU3m5SwmeBM+c3awAAAAATxoXJudHRFYDNhmgSNIUM; ESSCookieEncypt=!WHynVN82TLCsAauj+pcpa7ZMcUZSD1r724NeD8LSaBM8e9o/aaybcVdt/VCloL5sXDmipGW1FETvAS6jCfl/KrLjO+W5wTYKAQbEfKiGSIqgpdYnu8mgPZldA8CKN+At60n5Y5eefg1vn+HMkC5S3oJyqMSxWCc=; nlbi_2373390=6vFTcz8jeRLLySXBM+c3awAAAABjMNsp4kXcLQJxkm1QD5UN; reese84=3:Yq2ZzHmoX6Hr45+zGIbuuw==:iwlOlnejIBiHOaU8db/x4dSOlOtyXdPpyJRWQ3lbCMNVmZfvz2QkxKI9X9iH1M7s7fvcKROqwPID1qiurjo5MLhNib5q2+Wd93By2i7e+5hkP6WEIVyfNdRw1gv1f5XPA/8kTxs/E0vLFyqaExHli6EaKCNxGQGyQWcPJCWrj5ew1WMWZaSBkzeXKJg0gD89Yl9Ctcz3dp90S/gHHL/jCDHM6SD78VhbiLBBCsN6r3iDzfp6NeVBC6gNWLZUfFg9L5AvZzMeJRR+N3qmWhbg1qpOI1oaU2eS6PBFLL00u9qpDRsDf9hwWNu5YYScVm6r9brRMkAWaVshPoMcwXL4anLbxDi1t/sUQRzRk0ly2NOQ7g/yNkNULSW1fDbKvlpk2r5Uf8ZrEbEGZ2vUEEoUPy3HHt5fUwslfU6MO3yHvCqg9LtKPIRLd5R/r6QVMivGckkwtJI/IVBKN20mDAB587JD0S4koRewkNWnOq7xnPISqv05IOSO1Qp/aYBZrkqRElT2e4Rf+F3UZd965IMRpA==:7JO+tEGuBxG+zc3utLeXtuxzIqWKxw0JY+Ddz/Z52yg=; ASP.NET_SessionId=jg1x5ubs3z2uvyw3zdfbbhcq; incap_ses_159_2373390=/NjoDg33FjNIcmiqv+E0Arv3b2UAAAAA5EOnfm3O9XbjhRZW6/hgaA==' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: cross-site' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'TE: trailers'
"""

