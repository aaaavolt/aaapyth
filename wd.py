from selenium import webdriver 
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# print(driver.page_source)
# driver.quit()
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pprint
import os
import config
from bs4 import BeautifulSoup

class Wd:
    def __init__(self, headless=True):
        self.headless = headless
        self.__driver = self._start_driver()

    def _start_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        conf = config.MyConfig()
        conf.read_file()

        options.add_argument(f"user-agent={conf.get_user_agent()}")
        driver = webdriver.Chrome(options=options)
        return driver
    def get_driver(self):
        return self.__driver
    def open_url(self,url):
        self.get_driver().get(url=url)

    def get_element(self, by=By.CSS_SELECTOR, value = None):
                    return self.get_driver().find_element(by, value)
                    
                    
    def get_elements(self, by=By.CSS_SELECTOR, value = None):
                    return self.get_driver().find_elementw(by, value)       
    def close(self):
           return self.get_driver().close()
    def get_page_source(self):
           return self.get_driver().page_source

    def quit(self)  :
           return self.get_driver().quit()     

    def wait(self, seconds):
           time.sleep(seconds)
    def execute_script(self,script, *args):
           return self.get_driver().execute_script(script=script, *args)
    def take_screenshot(self,file_path):
           self.get_driver().save_screenshot(file_path)
    def write(self, string, filename):
            soup = BeautifulSoup(string, "html.parser")
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(soup.prettify())
            print(f"{filename}") 
    def write_to_file(self, filename="index.html"):
        if filename in os.listdir():
            inp = input("y n")
            if inp == 'y':
                self.write(self.get_page_source(), filename)
                      
    
            else:
                print("ыыы")
        else:
              self.write(self.get_page_source(), filename)    
if __name__ == "__main__":
      wd = Wd(True)
      conf = config.MyConfig()
      conf.read_file()
    #   URL = conf.get_test_url()
      URL = "https://flowwow.com/bakery-products/tort-fistashkoviy-4336/"
      wd.open_url(url=URL)
      wd.write_to_file(filename="index.html")
      wd.take_screenshot("screen.png")
      wd.quit()      
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

