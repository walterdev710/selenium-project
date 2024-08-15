from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time


class InternetSpeedBot:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Firefox(service=self.service)
        self.up = 0
        self.down = 0
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        
        self.start_btn = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        self.start_btn.click()
        
        time.sleep(60)
        
        self.down = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        
        
        print(f"down:{self.down}")
        print(f"up:{self.up}")
        self.driver.quit()
    def tweeter_at_provider(self, promised_down, promised_up):
        if promised_down < float(self.down) or promised_up < float(self.up):
            print(f"Your internet speed is lower than they promised. down:{self.down}/up:{self.up} when promised down:{promised_down}, up:{promised_up}")