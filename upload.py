# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, os, json, threading
# import pywinauto
def get_driver():
    # driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)
    driver = webdriver.Chrome()
    return driver

def handle_dialog(element_initiating_dialog, dialog_text_input, driver):
    def _handle_dialog(_element_initiating_dialog):
        _element_initiating_dialog.click() # thread hangs here until upload dialog closes
    t = threading.Thread(target=_handle_dialog, args=[element_initiating_dialog] )
    t.start()
    time.sleep(1) # poor thread synchronization, but good enough

    upload_dialog = driver.switch_to_active_element()
    upload_dialog.send_keys(dialog_text_input)
    upload_dialog.send_keys(Keys.ENTER)

def image_upload(url):
    driver = get_driver()
    driver.get(url)
    email_edit = driver.find_element_by_xpath('//*[@id="page_username-input"]')
    pw_edit = driver.find_element_by_xpath('//*[@id="page_password-input"]')
    login_button = driver.find_element_by_xpath('//*[@id="page_signin"]')
    if email_edit and pw_edit and login_button:
        email_edit.click()
        email_edit.send_keys("truths@inboxbear.com")
        time.sleep(1)
        pw_edit.click()
        pw_edit.send_keys("testing123")
        time.sleep(20)
        # login_button.click()
        time.sleep(2)
        
    driver.get("https://www.zazzle.com/mens_basic_dark_t_shirt-235188229222196359")

    # ///////////////////////image upload///////////////////////////
    add_button = driver.find_element_by_xpath('//*[@class="Button Button--Submit Button--Medium"]')
    add_button.click()
    time.sleep(2)
    folder = os.getcwd()+"/image/"
    files_path = [folder + x for x in os.listdir(folder)]
    imagelist = []
    textlist = []
    for file in files_path:
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() != '.txt':
            imagelist.append(file)
        else:
            textlist.append(file)
    for image_path in imagelist:
        path = image_path
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"][@name="image"]'))).send_keys(path)
        # time.sleep(2)
        # start the upload
        # dialogWindow = pywinauto.application.Application()
        # windowHandle = pywinauto.findwindows.find_windows(title=u'Open', class_name='#32770')[0]
        # window = dialogWindow.window_(handle=windowHandle)
        # # this is the element that I would like to access (not sure)
        # toolbar = window.Children()[41]
        # # send keys:
        # toolbar.TypeKeys("path/to/the/folder/")
        # # insert file name:
        # window.Edit.SetText(path)
        # # click on open:
        # window["Open"].Click()
        time.sleep(12)

    # ////////////////text upload///////////////////////
    for text_path in textlist:
        text_file = open(text_path, "r")
        description = text_file.read()
        buttons = driver.find_elements_by_xpath('//*[@class="Button Button--Submit Button--Medium"]')
        text_button = buttons[2]
        text_button.click()
        text_area = driver.find_element_by_xpath('//*[@class="TextArea-textarea"]')
        text_area.send_keys(description)
        add_text_btn = driver.find_element_by_xpath('//*[@class="Button Button--Submit Button--Small Button--isIcon"]')
        add_text_btn.click()
        time.sleep(2)


site_urls = ['https://www.zazzle.com/lgn/signin']
for url in site_urls:
    image_upload(url)

