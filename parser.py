import wd
import config
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
        self.html_page = BeautifulSoup(
            self.get_driver().get_page_source(),
            'html.parser'
        )
        self.url = url
        self.get_driver().quit()

    def get_product_category(self):
        return "Торт"

    def get_product_url(self):
        return self.url

    def get_product_photo_url(self):
        photo_url = self.html_page.find_all("img", class_="main-image-content is-zoom") 
        return photo_url[0]['src']
        

    def get_product_price(self):
        product_price = self.html_page.find_all("span", class_="footer-price") 
        return product_price[0].find("span").contents[0]


    def get_product_weight(self):
        weight = self.html_page.find_all("p", class_="pre-line property-text")
        return weight[0].get_text().strip().split()[0]
        

    def get_product_added(self):

        added = self.html_page.find_all("div", class_="info-text")
        return added[2].get_text().strip().split()[0]

    def get_shop_shop_name(self):
        shop_name = self.html_page.find_all("p", class_="shop-name")
        return shop_name[0].get_text().strip()

    def get_shop_url(self):
        shop_url = self.html_page.find_all("a", class_="shop-link")
        return shop_url[0]['href']

    def get_shop_rating(self):
        shop_rating = self.html_page.find_all("p", class_="shop-rating")
        return shop_rating[0].get_text().strip().split()[0]

    def get_product_rating(self):

        product_rating = self.html_page.find_all("div", class_="el-rate")
        return product_rating[0]['aria-valuenow']

    def get_product_bought(self):
        product_bought = self.html_page.find_all("p", class_="shop-score")
        spans = product_bought[0].find_all("span")
        return spans[3].get_text().strip().split()[0]
    
    def get_product_name(self):
        name = self.html_page.find_all("div", class_="name-wrapper")
        return name[0].get_text().strip()

if __name__ == "__main__":
    bsp = Bsp(True)
    conf = config.MyConfig()
    conf.read_file()
    URL = conf.get_test_url()
    bsp.get_html_page(URL) 
    print(bsp.get_product_name())
    print(bsp.get_product_weight())
    print(bsp.get_product_photo_url())
    print(bsp.get_product_price())
    print(bsp.get_product_added())
    print(bsp.get_shop_shop_name())
    
    print(bsp.get_shop_url())
    print(bsp.get_shop_rating())
    print(bsp.get_product_rating())
    print(bsp.get_product_bought())