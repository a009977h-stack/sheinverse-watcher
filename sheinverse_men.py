from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://www.sheinindia.in/c/sverse-5939-37961?query=%3Arelevance%3Agenderfilter%3Amen"

BOT_TOKEN = os.environ.get("7478317580:AAFSME2QXzPBkCohCLkoyNi566mLEtCs4dU")
CHAT_ID = os.environ.get("5628944669")

LAST_FILE = "last.txt"


def send_msg(msg):
    api = f"https://api.telegram.org/bot7478317580:AAFSME2QXzPBkCohCLkoyNi566mLEtCs4dU/sendMessage"
    r = requests.get(api, params={"chat_id":5628944669, "text": msg})
    print("Telegram status:", r.status_code)


def get_product_count():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, timeout=60000)
        page.wait_for_timeout(8000)

        products = page.query_selector_all("a[href*='/p-']")
        browser.close()

        links = set()
        for p in products:
            href = p.get_attribute("href")
            if href:
                links.add(href)

        return len(links)


# ---- MAIN ----
current_count = get_product_count()
print("Current count:", current_count)

if os.path.exists(LAST_FILE):
    with open(LAST_FILE, "r") as f:
        last_count = int(f.read())
else:
    last_count = 0

print("Last count:", last_count)

if current_count > last_count:
    send_msg(
        f"🔥 SHEINVERSE MEN STOCK UPDATE\n"
        f"{last_count} → {current_count}\n"
        f"Jaldi app open karo!"
    )

with open(LAST_FILE, "w") as f:
    f.write(str(current_count))
