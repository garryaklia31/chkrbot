
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def check_email(email):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://login.xfinity.com/login")
        time.sleep(3)

        email_input = driver.find_element(By.ID, "user")
        email_input.clear()
        email_input.send_keys(email)
        driver.find_element(By.ID, "sign-in").click()

        time.sleep(3)
        error_msg = driver.find_elements(By.CLASS_NAME, "cimsg-error")

        if error_msg:
            text = error_msg[0].text
            if "invalid" in text.lower() or "couldn’t find" in text.lower():
                return f"{email} ❌ Not Registered"
            elif "incorrect" in text.lower():
                return f"{email} ✅ Registered"
            else:
                return f"{email} ❓ Unknown response"
        return f"{email} ❓ No error detected"
    except Exception as e:
        return f"{email} ⚠️ Error: {str(e)}"
    finally:
        driver.quit()

def check_emails_from_file(file_path):
    with open(file_path, "r") as f:
        emails = [line.strip() for line in f if line.strip()]
    
    results = []
    for email in emails:
        if "@gmail.com" in email:
            results.append(check_email(email))
        else:
            results.append(f"{email} ⚠️ Skipped (Not a Gmail)")
    
    return "\n".join(results)
