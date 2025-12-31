import requests
from bs4 import BeautifulSoup

URL = "https://www.sheinindia.in/c/sverse-5939-37961?query=%3Arelevance%3Agenderfilter%3Amen"
BOT_TOKEN = "7478317580:AAFSME2QXzPBkCohCLkoyNi566mLEtCs4dU"
CHAT_ID = "5628944669"

def send_msg(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": msg})

r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(r.text, "html.parser")

products = soup.select("a[href*='/p-']")
current_count = len(set(p["href"] for p in products))

# store last count in GitHub artifact (simple trick)
try:
    with open("last.txt", "r") as f:
        last_count = int(f.read())
except:
    last_count = None

if last_count is not None and current_count > last_count:
    send_msg(
        f"🔥 SHEINVERSE MEN UPDATE!\n"
        f"{last_count} → {current_count}\n"
        f"Jaldi app open karo!"
    )

with open("last.txt", "w") as f:
    f.write(str(current_count))
