import os
import re
import time
import requests
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

# Konfigurasi
PRIVATE_FAVORITES_URL = "https://www.pixiv.net/en/users/[USER_ID]/bookmarks/artworks?rest=hide"
DOWNLOAD_DIR = "./pixiv_private_favorites"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.pixiv.net/"
}


def save_cookies(context, path="cookies.json"):
    cookies = context.cookies()
    with open(path, "w", encoding="utf-8") as f:
        import json
        json.dump(cookies, f)
    print("[💾] Cookies saved.")


def load_cookies(context, path="cookies.json"):
    import json
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        cookies = json.load(f)
    context.add_cookies(cookies)
    print("[🍪] Cookies loaded.")


def get_artwork_links(page):
    print("[📥] Mengakses halaman Private Favorites...")
    page.goto(PRIVATE_FAVORITES_URL)
    page.wait_for_selector('div[role="presentation"]')

    print("[⬇️] Scroll ke bawah untuk memuat semua artwork...")
    last_height = 0
    for _ in range(20):  # Max 20x scroll
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    links = []
    anchors = page.query_selector_all('a[href*="/artworks/"]')
    for a in anchors:
        href = a.get_attribute("href")
        if href and href not in links:
            links.append(href)

    print(f"[🎯] Total ditemukan {len(links)} artwork.")
    return list(set(links))


def get_image_urls(page, artwork_url):
    print(f"[🔍] Membuka artwork: {artwork_url}")
    page.goto(artwork_url)
    page.wait_for_selector('div[role="presentation"] img')

    # Buka image viewer
    page.locator('div[role="presentation"] img').first.click()
    time.sleep(1)
    page.wait_for_selector('img.sc-1u32lqo-0', timeout=5000)

    img_urls = []
    try:
        total_text = page.locator('div[data-test="viewer-footer-text"]').text_content()
        total = int(total_text.split('/')[-1])
    except:
        total = 1

    for i in range(total):
        img_elem = page.locator('img.sc-1u32lqo-0').first
        src = img_elem.get_attribute("src")
        if src:
            img_urls.append(src.split("?")[0])

        if total > 1 and i < total - 1:
            next_btn = page.locator('button[data-action="next"]')
            if next_btn:
                next_btn.click()
                time.sleep(1)

    close_btn = page.locator('button[data-action="close"]')
    if close_btn:
        close_btn.click()
    return img_urls


def download_image(url, path, cookies):
    try:
        cookies_dict = {c['name']: c['value'] for c in cookies}
        response = requests.get(url, headers=HEADERS, cookies=cookies_dict, stream=True)
        response.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
        print(f"[✅] Berhasil mengunduh: {os.path.basename(path)}")
    except Exception as e:
        print(f"[❌] Gagal unduh {url}: {str(e)}")


def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        if os.path.exists("cookies.json"):
            load_cookies(context)
            page.goto("https://www.pixiv.net/")
            time.sleep(3)
        else:
            print("🔐 Silakan login secara manual di browser yang terbuka...")
            page.goto("https://accounts.pixiv.net/login")
            input("✅ Tekan ENTER setelah selesai login...")
            save_cookies(context)

        cookies = context.cookies()
        links = get_artwork_links(page)

        for idx, url in enumerate(links, 1):
            print(f"\n[{idx}/{len(links)}] Memproses: {url}")
            img_urls = get_image_urls(page, url)

            if not img_urls:
                print("⚠️  Tidak ditemukan gambar.")
                continue

            artwork_id = re.search(r'artworks/(\d+)', url).group(1)
            for i, img_url in enumerate(img_urls):
                ext = os.path.splitext(urlparse(img_url).path)[1]
                filename = f"{artwork_id}_p{i}{ext}" if len(img_urls) > 1 else f"{artwork_id}{ext}"
                path = os.path.join(DOWNLOAD_DIR, filename)
                if os.path.exists(path):
                    print(f"[📂] Sudah ada: {filename}")
                    continue
                download_image(img_url, path, cookies)
                time.sleep(1)

        print("\n🎉 Semua gambar selesai diunduh!")
        context.close()
        browser.close()


if __name__ == "__main__":
    main()
