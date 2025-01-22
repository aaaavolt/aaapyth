import config
import wd
from bs4 import BeautifulSoup
class Bsp:
    def __init__(self, headless=False):
        self.__driver = wd.Wd(headless=headless)
        self.url = ""
        self.html_page = ""
    def get_driver(self):
        return self.__driver
    def get_html_page(self, url):
        self.get_driver().open_url(url=url)
        self.html_page = BeautifulSoup(self.get_driver().get_page_source(),
                                         'html.parser')
        self.get_driver().quit()


if __name__ == "__main__":
    bsp = Bsp(True)
    conf = config.myConfig()
    conf.read_file()
    URL = conf.get_test_url()
    bsp.get_html_page(URL)
