from selenium import webdriver
import Engine
import time
from selenium.webdriver.chrome.options import Options
import ConfigHandler


chrome_options = Options()


if ConfigHandler.HEADLESS=="yes":
    chrome_options.add_argument("--headless")

#Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=r'path_to_chromedriver',options=chrome_options)
#
Engine.init(webdriver)
time.sleep(5)
Engine.update(webdriver)

webdriver.close()
webdriver.quit()
