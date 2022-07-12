import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@given(u'user in the login page')
def launchbrowser(context):
    context.driver = webdriver.Edge(executable_path="C:/Users/Raviraj/Desktop/edgedriver_win64/msedgedriver.exe")


@when(u'user enter username as "{user}" and password is "{pwd}"')
def userdetails(context, user, pwd):
    context.driver.get("https://www.air.irctc.co.in/")
    context.driver.maximize_window()
    time.sleep(3)
    context.driver.find_element(by=By.XPATH, value="//button[text()='Later']").click()
    context.driver.find_element(by=By.XPATH, value="//header/nav[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/a[1]").click()
    time.sleep(3)
    context.driver.find_element(by=By.NAME, value="userId").send_keys(user)
    time.sleep(3)
    context.driver.find_element(by=By.NAME, value="password").send_keys(pwd)
    time.sleep(3)


@when(u'user click on login')
def submitdetails(context):
    context.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Login')]").click()
    time.sleep(3)


@then(u'user will verify the title of the page')
def verifytitle(context):
    print(context.driver.title)
    context.driver.close()
