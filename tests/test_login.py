import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import config as cf

logger = logging.getLogger(__name__)


class TestEsh:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.load_element_timeout = cf.load_element_timeout
        self.url = cf.esh_url

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get(self.url)
        try:
            # I searched here for the title but searching for other objects on screen will work
            _ = WebDriverWait(self.driver, timeout=self.load_element_timeout).until(
                ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Powering next generation banking')]"))
            )
        except TimeoutError as e:
            assert 0, "got timeout while waiting for user name item"
        # Add creds
        # Type email address
        logger.info("inserting email")
        self.driver.find_element(By.ID, ":r1:").send_keys(cf.email)
        # Type password
        logger.info("inserting password")
        self.driver.find_element(By.ID, ":r2:").send_keys(cf.password)
        # click "Login" button
        logger.info("clicking login")
        self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()
        try:
            # Wait for a fictional element
            logger.info("wait for element in new page")
            element = WebDriverWait(self.driver, timeout=self.load_element_timeout).until(
                ec.presence_of_element_located((By.LINK_TEXT, "Table of Contents"))
            )
        except TimeoutError as e:
            # Handle timeout exception
            err_msg = "got timeout while waiting for 'Table of Contents'"
            logger.error(err_msg)
            assert 0, err_msg

        # you can do stuff with element here
        logger.info("do stuff with element")
        # Test has finished successfully
        logger.info("login test has finished successfully")
        assert 1
