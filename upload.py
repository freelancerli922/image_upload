# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
import time, os, json

def get_driver():
    # driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)
    driver = webdriver.Firefox()
    return driver

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
        time.sleep(3)
        # login_button.click()
        time.sleep(2)
        driver.get("https://www.zazzle.com/create")

    body = driver.page_source


    url = 'https://www.zazzle.com/up/isapi/designall.dll?type=service&action=upload&sessionqs=0&output=js&comm_mode=ajax&cg=1'
    crsf = body.split('"csrfToken":')[-1].split(',')[0]

    # crsf = '"767b3d702211f0a6"'
    # driver.close()

    url = 'https://www.zazzle.com/up/isapi/designall.dll?type=service&action=upload&sessionqs=0&output=js&comm_mode=ajax&cg=1'
    # data = {'dir':'/uploads/', 'submit':'Submit'}
    files = {'file':('1.jpg', open('1.jpg', 'rb'))}
    r = requests.post(url, files=files)
    print(r.content)

    uploaded_images = json.loads(r.content)["children"]
    for image in uploaded_images:
        url = 'https://www.zazzle.com/svc/my/mediabrowser/NotifyChangedImageList'
        image_id = image['attributes']['id'].lower()
        datas = {"changedIds":"[\"{}\"]".format(image_id),"csrf":crsf,"client":"js"}
        headers = {
            'Content-type': 'application/json',
            # 'accept-encoding':'gzip, deflate, br',
            # 'accept-language':'en-US,en;q=0.9',
            # 'content-length':'99',
            # 'cookie':'us=890A99AB-DF34-45CF-A782-A261AD17488C; NSC_xxx01=ffffffff09099e0445525d5f4f58455e445a4a423660; _ga=GA1.2.688207428.1521008558; _gid=GA1.2.452139422.1521008558; NSC_smw=ffffffff09099a0b45525d5f4f58455e445a4a423660; NSC_vq=ffffffff09099d6a45525d5f4f58455e445a4a423660; zm=AQABAAAA7REAABRbDC6mqUFzUWSMEyFzT6jLaJGc6L8nBGh-UKAZ6F76MMNvuKT66JhCHJn3WgB6DuRCoiwJ9QM6qh-zCznfDUTzwxKGfCsvL-f8w3YdTMsI-9JU7c69eBnz3uslLh5hkd468TKKHv8zh3ITKJ86CTxWbefP_UbtlDYZMxnQqaSn8fDcc1e_3YeZFtfqE7JShkj8AcIFz38qjOzkB-T4qf2NQbEmRBh9zkLJjamV1ccJ_0sYzL8; zs=8BDC8F59-0BBE-44B3-B654-91FC3629526A%7c238059915219723352%7c13165501839%7cAQABAAAA7REAABSRBzM9x0PHEar7glv6T-5GpIG7qawY0xQngiqtNJpw1uR3x4y-Qw9M9Tv2b04AphJYf8-nCPG9g93_o5i0-ahjdAMxYw%7c; general%5Fmaturity=2; bx=zlng%3den%26zlng_x%3d131692896000000000%26promoanim%3d1%26promoanim_x%3d131655109580087923%26lsr%3d250132743741107740%26lsr_x%3d131693766186333411%26udnm%3dtruths%26udnm_x%3d131655036418835484; bs=pis%3d86%26zshopurl%3dz%2fcustom%2fclothing%3fcyo%253Dclothing%26ps%3d60; _br_uid_2=uid%3D5169876493919%3Av%3D12.0%3Ats%3D1521008560444%3Ahc%3D77',
            # 'origin':'https://www.zazzle.com',
            # 'referer':'https://www.zazzle.com/womens_basic_t_shirt-235643286926699897',
            # 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }
        rsp = requests.post(url, json=datas, headers=headers)
        print rsp.content



    # ////////////////////////selenium upload///////////////////////
    # driver.find_element_by_id("IdOfInputTypeFile").send_keys(os.getcwd()+"/image.png")

site_urls = ['https://www.zazzle.com/lgn/signin']

for url in site_urls:
    image_upload(url)