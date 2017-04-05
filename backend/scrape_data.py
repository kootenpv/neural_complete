import requests
import just
import lxml.html
from selenium import webdriver

USERNAME = ""
PASSWORD = ""

driver = webdriver.Chrome(executable_path="/Users/pascal/Downloads/chromedriver")

# login
driver.get("https://github.com/login")
driver.find_element_by_id("login_field").send_keys(USERNAME)
driver.find_element_by_id("password").send_keys(PASSWORD)
driver.find_element_by_id("password").submit()

# start collecting links
links = set()
query = "keras lstm language:python filename:*.py"
for i in range(1, 60):
    try:
        url = "https://github.com/search?p={}&q={}&ref=searchresults&type=Code&utf8=%E2%9C%93"
        driver.get(url.format(i, query))
        tree = lxml.html.fromstring(driver.page_source)
        page_links = [x for x in tree.xpath('//a/@href') if "/blob/" in x and "#" not in x]
        links.update(page_links)
        print(i, len(links))
    except KeyboardInterrupt:
        break

# visit and save source files
base = "https://github.com"
for num, link in enumerate(links):
    url = base + link
    html = requests.get(url).text
    tree = lxml.html.fromstring(html)
    xpath = '//*[@class="blob-code blob-code-inner js-file-line"]'
    contents = "\n".join([x.text_content() for x in tree.xpath(xpath)])
    # note that link conveniently starts with / like a webpath
    just.write(contents, "data" + link)
    print(num, len(contents))

other_options = []
# bigquery
