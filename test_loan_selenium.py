import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()

def test_successful_loan_approval(driver):
    driver.get("http://127.0.0.1:5000")
    
    driver.find_element(By.ID, "age").send_keys("28")
    driver.find_element(By.ID, "salary").send_keys("50000")
    driver.find_element(By.ID, "credit_score").send_keys("750")
    driver.find_element(By.ID, "existing_loan").send_keys("5000")
    driver.find_element(By.ID, "requested_amount").send_keys("200000")
    driver.find_element(By.ID, "submit_btn").click()

    result = driver.find_element(By.ID, "result_status").text
    assert "APPROVED" in result

def test_poor_credit_score_rejection(driver):
    driver.get("http://127.0.0.1:5000")
    
    driver.find_element(By.ID, "age").send_keys("32")
    driver.find_element(By.ID, "salary").send_keys("40000")
    driver.find_element(By.ID, "credit_score").send_keys("520")
    driver.find_element(By.ID, "existing_loan").send_keys("0")
    driver.find_element(By.ID, "requested_amount").send_keys("50000")
    driver.find_element(By.ID, "submit_btn").click()

    result = driver.find_element(By.ID, "result_status").text
    assert "REJECTED: Low credit score" in result
