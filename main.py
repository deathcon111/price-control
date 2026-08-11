from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests

kabum = "https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia"
pichau = "https://www.pichau.com.br/hardware/placa-de-video/nvidia"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"

#response = requests.get(url, headers={"User-Agent": USER_AGENT})
#with open("requests.html", "w", encoding="utf-8") as file:
#    file.write(response.text)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context(user_agent=USER_AGENT)
    page = context.new_page()
    page.goto(kabum)
    content_kabum = page.content()
    page.goto(pichau)
    content_pichau = page.content()

#with open("kabum.html", "w", encoding="utf-8") as file:
#    file.write(content_kabum)

#with open("pichau.html", "w", encoding="utf-8") as file:
#    file.write(content_pichau)