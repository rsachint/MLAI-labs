import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time

driver = webdriver.Chrome('chromedriver')

url = "https://www.google.com/search?q=cardboard+box&tbm=isch&ved=2ahUKEwjCvM-f-4L_AhVkk9gFHUFtAiQQ2-cCegQIABAA&oq=cardboard+box&gs_lcp=CgNpbWcQAzIKCAAQigUQsQMQQzIHCAAQigUQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOggIABCABBCxAzoHCCMQ6gIQJzoECCMQJ1AAWK8yYNYzaAJwAHgDgAGRBYgBwzGSAQswLjEuOC40LjEuNJgBAKABAaoBC2d3cy13aXotaW1nsAEKwAEB&sclient=img&ei=kT9oZIKwBuSm4t4PwdqJoAI&bih=746&biw=1536&rlz=1C1ONGR_enIN1012IN1012"

driver.get(url)

#scrolls the page 4 times to bottom and waits for 5 seconds for images to render
for i in range(4):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
    
    #clicks show more button in the end of the page to load more images
    # get_show_more = driver.find_elements(By.CLASS_NAME,'mye4qd')
    
    # if get_show_more:
    #     get_show_more.click()

imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")

src = []
for img in imgResults:
    src.append(img.get_attribute('src'))

#Tune the range to get more images
for i in range(200):    
    urllib.request.urlretrieve(str(src[i]),"sample_data/box{}.jpg".format(i))

