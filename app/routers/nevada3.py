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
