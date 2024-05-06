import os
import time
from dotenv import load_dotenv
from crewai_tools import tool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()


class LinkedinToolException(Exception):
    def __init__(self):
        super().__init__("You need to set the LINKEDIN_EMAIL and LINKEDIN_PASSWORD env variables")


def post_on_linkedin_fn() -> str:
    """
    A tool that can be used to post on LinkedIn
    """
    linkedin_username = os.environ.get("LINKEDIN_EMAIL")
    linkedin_password = os.environ.get("LINKEDIN_PASSWORD")

    if not (linkedin_username and linkedin_password):
        raise LinkedinToolException()
    
    driver = webdriver.Chrome()


    driver.get("https://www.linkedin.com/")
    username = driver.find_element(By.ID,"session_key")
    username.send_keys(linkedin_username) #### YOUR LINKEDIN USERNAME 
    username.send_keys(Keys.RETURN)
    password = driver.find_element(By.ID,"session_password")
    password.send_keys(linkedin_password) #### YOUR LINKEDIN PASSWORD
    password.send_keys(Keys.RETURN)
 
    time.sleep(2)
	
    add_post_button = driver.find_element(By.CSS_SELECTOR,'.artdeco-button.artdeco-button--muted.artdeco-button--4.artdeco-button--tertiary.ember-view.share-box-feed-entry__trigger')		
    add_post_button.click();
	
    time.sleep(2)

    post_text_area = driver.find_element(By.CSS_SELECTOR,".ql-editor.ql-blank")	
    post_reader = open("results/result.txt", "r")
    post = post_reader.read()
    post_text_area.send_keys(post)

    time.sleep(2)
    post_send_button = driver.find_element(By.CSS_SELECTOR,'.share-actions__primary-action.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')	
    post_send_button.click();

    time.sleep(3)

    driver.quit()
    return "Success"



@tool("PostOnLinkedin")
def post_on_linkedin_tool() -> str:
    """
    A tool that can be used to post on LinkedIn
    """
    return post_on_linkedin_fn()