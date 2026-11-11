"""Cookie and tracker scan for a privacy audit.

Loads a public web page in a fresh browser (no consent given), records every cookie
and third-party request, and writes two CSV files. Run it before and after
clicking "Accept" / "Reject" to compare.

Usage:
    pip install playwright && playwright install chromium
    python cookie_scan.py https://www.example.com before_consent
"""
import csv, sys
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

url, label = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "scan")
host = urlparse(url).hostname
parts = host.split(".")
site = host if len(parts) < 2 or host.replace(".", "").isdigit() else ".".join(parts[-2:])
mine = lambda d: d.lstrip(".").endswith(site)
requests = []

with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context()
    page = ctx.new_page()
    page.on("request", lambda r: requests.append(urlparse(r.url).hostname or ""))
    page.goto(url, wait_until="load", timeout=60000)
    page.wait_for_timeout(5000)  # let delayed tags fire
    cookies = ctx.cookies()
    browser.close()

with open(f"cookies_{label}.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "domain", "first_or_third_party", "expires_days", "secure", "http_only", "same_site"])
    for c in cookies:
        party = "first" if mine(c["domain"]) else "third"
        days = round((c["expires"] - __import__("time").time()) / 86400) if c["expires"] > 0 else "session"
        w.writerow([c["name"], c["domain"], party, days, c["secure"], c["httpOnly"], c.get("sameSite")])

third = sorted({h for h in requests if h and not mine(h)})
with open(f"third_party_hosts_{label}.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["host"]); [w.writerow([h]) for h in third]

print(f"{len(cookies)} cookies ({sum(not mine(c['domain']) for c in cookies)} third-party), {len(third)} third-party hosts")
