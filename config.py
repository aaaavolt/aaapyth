import configparser
import os

class MyConfig:
    def __init__(self, filename = "config.ini"):
        self.__filename = filename
        self.__config = configparser.ConfigParser()

    def get_filename(self):
        return self.__filename
        
    def get_config(self):
        return self.__config
        
    def get_user_agent(self):
        return self.get_config().get("Requests","user_agent")
        
    def get_sections(self):
        return self.get_config().sections()
        
    def get_test_url(self):
        return self.get_config().get("Urls","test_url")
        
    def read_file(self):
        if self.get_filename() not in os.listdir():
            print(f"{self.get_filename()} netu")
        else:
            self.get_config().read(self.get_filename())
            print(f"{self.get_filename()} schitali")

if __name__ == "__main__":
    conf = MyConfig()
    conf.read_file()
    print(conf.get_user_agent())
    print(conf.get_test_url())