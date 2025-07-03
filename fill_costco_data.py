import pandas as pd
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import time
from config import CSV_FILE
SOURCE = "costco"
CURRENCY = "USD"

async def extract_product_data(page, url):
    try:
        print(f"🔍 Scraping: {url}")
        await page.goto(url, wait_until="load", timeout=60000)

        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        title_tag = soup.find('h1', {'automation-id': 'productName'})
        title = title_tag.text.strip() if title_tag else "Could not scrape."
        brand = title.split()[0] if title != "Could not scrape." else ""

        price_tag = soup.find('span', {'automation-id': 'productPriceOutput'})
        price = price_tag.text.strip() if price_tag else ""

        desc_items = soup.select('ul.pdp-features li')
        description = ', '.join([li.text.strip() for li in desc_items]) if desc_items else ""

        return {
            "brand": brand,
            "product_title": title,
            "price": price,
            "price_available": "TRUE" if price else "FALSE",
            "currency": CURRENCY,
            "source": SOURCE,
            "description": description,
            "additional_image": "",
            "additional_description": "",
        }

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return {
            "brand": "",
            "product_title": "Could not scrape.",
            "price": "",
            "price_available": "FALSE",
            "currency": CURRENCY,
            "source": SOURCE,
            "description": "Could not scrape.",
            "additional_image": "",
            "additional_description": "",
        }

async def main():
    df = pd.read_csv(CSV_FILE)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--disable-http2"])
        context = await browser.new_context(ignore_https_errors=True, user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        ))
        page = await context.new_page()

        for idx, row in df.iterrows():
            url = str(row.get("product_url", "")).strip()
            if not url:
                continue

            data = await extract_product_data(page, url)

            for key, value in data.items():
                df.at[idx, key] = str(value)

            time.sleep(3)  # Slow down scraping to avoid blocks

        await browser.close()

    df.to_csv(CSV_FILE, index=False)
    print("✅ CSV updated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
