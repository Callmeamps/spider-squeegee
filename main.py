from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

BLOG = "https://blog.callmeamps.one"
PROPERTY24 = "https://www.property24.com/auctions?sp=pid%3d1"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(PROPERTY24)
    print(page.url)
    #print(page.content())
    auction_page = page.content()
    auction_soup = BeautifulSoup(auction_page, "html")
    
    auction_properties = page.query_selector("//div.js_listingResultsContainer//a")
    
    print(auction_properties)
    FILE = "property24.html"
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(page.content())
        for auction_property in auction_properties:
            #print(f"Property Details:\n{auction_property}\n\n\n")
            f.write(auction_property.inner_text())
    print("added successfully")
    browser.close()