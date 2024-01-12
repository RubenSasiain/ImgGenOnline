import os
import time
from datetime import datetime

import matplotlib.pyplot as plt
import requests
from PIL import Image
from selenium import webdriver


def getSeleniumConfig():
    return webdriver.Chrome()

def getImgUrl(driver,query):
    search_url = f'https://image.pollinations.ai/prompt/{query}'
    driver.get(search_url)
    img_tag = driver.find_element('tag name', 'img')
    return img_tag.get_attribute('src')

def getImageName():
    now = str(datetime.now()).replace('.', '').replace(':', '').replace(' ', '').replace('-', '')
    return f'generated{now}.jpg'

def saveOrDelete(driver, img_url,image_name):
    us_input = input('¿Save? (y/n): ').lower()
    driver.close()
    if us_input == 'y':
        img_data = requests.get(img_url).content
        with open(image_name, 'wb') as f:
            f.write(img_data)

        img = Image.open(image_name)
        save_path = 'C:/Users/ruben/OneDrive/Imágenes/Generados'
       
        img.save(os.path.join(save_path, image_name))
        print(f'Image saved in {os.path.join(save_path, image_name)}')
        os.remove(image_name)

def doSearch(query):
    driver = getSeleniumConfig()
    img_url = getImgUrl(driver,query)
    image_name = getImageName()
    saveOrDelete(driver,img_url,image_name)

if __name__ == "__main__":
    #ingresa el texto a buscar y dar formato
    user_inp = 'str'

    while (user_inp != "."):
        print("To finish insert .")
        user_inp = input('Insert the prompt: ')

        if user_inp != ".":
            formatted_query = user_inp.replace(',', '%20').replace(' ', '')
            doSearch(formatted_query)


