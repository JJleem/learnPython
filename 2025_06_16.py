from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://naver.com")

page.screenshot(path="./screenshot/screenshot.png")



# def plus (a,b):
#     return a + b

# plus(1,2)