
import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.sheinindia.in/c/sverse-5939-37961?query=%3Arelevance%3Agenderfilter%3Amen"
BOT_TOKEN = "7478317580:AAFSME2QXzPBkCohCLkoyNi566mLEtCs4dU"
CHAT_ID = "5628944669"

last_count = None

def send_msg(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": msg})

print("🔍 SHEINVERSE MEN stock watcher started")
send_msg("✅ SHEINVERSE MEN watcher ON")

while True:
    try:
        r = requests.get(
            URL,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=20
        )

        soup = BeautifulSoup(r.text, "html.parser")

        # Product cards (images with product links)
        products = soup.select("a[href*='/p-']")

        current_count = len(set(p["href"] for p in products))

        print("MEN products found:", current_count)

        if last_count is not None and current_count > last_count:
            send_msg(
                f"🔥 SHEINVERSE MEN UPDATE!\n"
                f"New MEN stock added 🎉\n"
                f"Old: {last_count} → New: {current_count}\n"
                f"Jaldi app open karo!"
            )

        last_count = current_count

    except Exception as e:
        print("Error:", e)

    time.sleep(60)
