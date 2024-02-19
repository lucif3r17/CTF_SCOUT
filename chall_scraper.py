from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


print("#########################################")
print("#                                       #")
print("#      Welcome to Chall_Scraper!        #")
print("#                                       #")
print("#    Your ultimate CTF challenge tool   #")
print("#                                       #")
print("#########################################")


username = input("Enter your username: ")
password = input("Enter your password: ")

browser = webdriver.Firefox()
browser.get("https://picoctf.org/")

login = browser.find_element(By.XPATH,"//li[@id='userlogin']")
login.click()
sleep(10)

username_field = browser.find_element(By.ID,"username")
password_field = browser.find_element(By.ID,"password")
submit = browser.find_element(By.XPATH,"//button[@type='submit']")

username_field.send_keys(username)
password_field.send_keys(password)
submit.click()
sleep(10)

cross = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div[1]/h5/button")
cross.click()
practice  = browser.find_element(By.XPATH,"/html/body/div/div/div[4]/nav/div/div[2]/ul/li[2]")
practice.click()

categories = []
num_challs = []
for i in range(2, 8):
    xpath = f'//*[@id=\"root\"]/div/div[4]/div/div[3]/div[1]/div/div[5]/ul/li[{i}]'
    element = browser.find_element(By.XPATH, xpath)
    categories.append(element.text)
    num_chall = int(element.text.split('(')[-1].strip(")"))
    num_challs.append(num_chall)

tot_categories = len(categories)

for i in range(tot_categories):
    xpath = f'//*[@id=\"root\"]/div/div[4]/div/div[3]/div[1]/div/div[5]/ul/li[{i+2}]'
    category = browser.find_element(By.XPATH, xpath)
    category.click()
    sleep(3)
    cat = f"cat_{i+1}"
    globals()[cat] = []

    pages = int(num_challs[i] / 12)+1
    for j in range(pages):

        chall = browser.find_elements(By.XPATH, "//div[@class='card-body']//h4")
        for c in chall:
            globals()[cat].append(c.text)

        if j != pages-1 : 
            next_button = browser.find_element(By.XPATH, "//a[@aria-label='Next' and @href='#' and contains(@class, 'page-link')]")
            next_button.click()
            sleep(1)

# Create a directory to save the challenges
dir_name = "picoCTF"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

for i in range(tot_categories):
    cat = f'cat_{i+1}'
    category_challs = globals()[cat]
    category_ = categories[i]
    path = os.path.join(os.getcwd(), dir_name, category_)

    if not os.path.exists(path):
        os.makedirs(path)

    for c in category_challs:
        sub_path = os.path.join(path, c)
        os.makedirs(sub_path)
