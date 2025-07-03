import asyncio, os, aiohttp
import pandas as pd
from playwright.async_api import async_playwright
from config import CSV_FILE
from config import OUTPUT_DIR
from config import BASE_URL

os.makedirs(OUTPUT_DIR, exist_ok=True)

new_image_urls = {}
image_counter = 27

async def download_image(url, product_id):
    global image_counter
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                content = await resp.read()
                filename = f"{image_counter}.png"
                file_path = os.path.join(OUTPUT_DIR, filename)
                with open(file_path, 'wb') as f:
                    f.write(content)
                new_image_urls[product_id] = f"{BASE_URL}/{filename}"
                image_counter += 1

async def handle_url(playwright, product_id, product_url):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()

    image_captured = asyncio.Event()

    async def handle_request(route, request):
        if "bfasset" in request.url and request.resource_type == "image":
            if not image_captured.is_set():
                image_captured.set()
                await download_image(request.url, product_id)
        await route.continue_()

    await context.route("**/*", handle_request)
    try:
        await page.goto(product_url, timeout=30000)
        await asyncio.wait_for(image_captured.wait(), timeout=10)
    except Exception as e:
        print(f"❌ Error on {product_id}: {e}")
    await browser.close()

async def main():
    df = pd.read_csv(CSV_FILE)
    async with async_playwright() as p:
        for _, row in df.iterrows():
            await handle_url(p, str(row['product_id']), row['product_url'])
    df['image'] = df['product_id'].map(new_image_urls)
    df.to_csv(CSV_FILE, index=False)
    print("✅ Image URLs updated!")

if __name__ == "__main__":
    asyncio.run(main())
