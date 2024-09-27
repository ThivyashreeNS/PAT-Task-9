from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Class for data for username & password
class Data:
   username = "standard_user"
   password = "secret_sauce"
   url = "https://www.saucedemo.com/"

# Class for web-elements locator
class Locators:
   username_locator = "user-name"
   password_locator = "password"
   login_button = "login-button"

# Class for webpage automation with constructor
class Automation(Data,Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)

    # Login method
    def login(self):
        try:
            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.username)
            sleep(2)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.password)
            sleep(2)
            self.driver.find_element(by=By.ID, value=self.login_button).click()
        except Exception as error:
            print("ERROR : ", error)

    # fetch the TITLE of the web application
    def fetch_title(self):
        return self.driver.title

    # fetch the URL of the web application
    def fetch_url(self):
        return self.driver.current_url

    # method to fetch the webpage contents
    def fetch_page_contents(self):
        return self.driver.page_source

    # method to save the contents to a file
    def save_page_contents_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.fetch_page_contents())

    # shutdown the selenium automation
    def shutdown(self):
        self.driver.close()



if __name__ == "__main__":

   # object for the class Automation
   obj = Automation()
   # Accessing class methods using object
   obj.login()
   # Fetching and printing the URL and TITLE
   print("Current URL:", obj.fetch_url())
   print("Page Title:", obj.fetch_title())

   # Saving the contents of the webpage into the text file
   obj.save_page_contents_to_file("Webpage_task_11.txt")
   print("Page contents saved to file: Webpage_task_11.txt")

   obj.shutdown()









