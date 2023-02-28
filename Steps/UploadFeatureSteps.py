from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

locators = {
    "txt_file": "id:uploadfile_0"
}


@given(u'Open chrome browser')
def open_chrome_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@given(u'Navigate to page "{url}"')
def navigate_to_page(context, url):
    context.driver.get(url)


@when(u'I upload "{file_name}"')
def upload_file(context, file_name):
    default_path = "{0}\TestData\{1}"
    #get_element(context, locators.get("txt_file")).send_keys(default_path.format(os.getcwd(), file_name))
    context.driver.find_element(By.ID, "uploadfile_0").send_keys(default_path.format(os.getcwd(), file_name))


@when(u'I accept terms of service')
def upload_file(context):
    context.driver.find_element(By.ID, "terms").click()


@when(u'I click Submit')
def click_submit(context):
    context.driver.find_element(By.ID, "submitbutton").click()


@then(u'File upload message should be "{expected_msg}"')
def verify_file_uploaded(context, expected_msg):
    wait = WebDriverWait(context.driver, 10)
    msg_element = wait.until(ec.visibility_of_element_located((By.ID, "res")))
    msg = msg_element.get_attribute("textContent")
    assert expected_msg == msg, f"Expected: '{expected_msg}' but found '{msg}'"


@then(u'File Upload Demo Page presented')
def verify_upload_page_presented(context):
    ec.title_is("File Upload Demo")
    ec.visibility_of_element_located("xpath://input[@type='file' and @id='uploadfile_0']")
    ec.text_to_be_present_in_element("xpath://div[@id='uploadwindow']/span", "Select file to send(max 196.45 MB)")
    ec.text_to_be_present_in_element("xpath://input[@id='terms' and @type='checkbox']/..", " I accept terms of service")
    ec.visibility_of_element_located("xpath://button[text()='Submit File']")


def get_element(context, locator):
    return context.driver.find_element("id:uploadfile_0")
