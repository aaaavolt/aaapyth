import requests
import config
conf = config.myConfig()
conf.read_file()
URL  = conf.get_test_url()
HEADERS = {"User-Agent":conf.get_user_agent()}

class Page:
    def __init__(self,url=""):
        self.url = url
        self.page_text = ""
    def get_page(self):
        response = requests.get(url=URL, headers=HEADERS)
        if response.status_code == 200:
            print(response.text)
        else:
            print(response.status_code)
if __name__ == "__main__":
    page = Page(url=URL)
    page.get_page()
    print(page.page_text)