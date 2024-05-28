## USING PYTHON SELENIUM AUTOMATION AND THE URL: https://www.saucedemo.com/
# DISPLAY THE COOKIE CREATED BEFORE LOGIN AND AFTER LOGIN IN THE CONSOLE.
# AFTER YOU LOGIN INTO THE DASHBOARD OF THE ZEN PORTAL KINDLY DO LOGOUT ALSO :-

# VERIFY THAT THE COOKIES ARE BEING GENERATED DURING THE LOGIN PROCESS.


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = 'https://www.saucedemo.com/'
url2 = 'https://www.zenclass.in/login'
url3 = 'https://www.zenclass.in/dashboard'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)

# Printing cookies in console before login in saucedemo:
print("Cookies before login saucedemo:")
print(driver.get_cookies())
print(driver.current_url)
sleep(3)

# Filling username:
element_of_name = driver.find_element(By.ID, "user-name")
element_of_name.send_keys("standard_user")

# Filling password:
element_of_first_password = driver.find_element(By.ID, "password")
element_of_first_password.send_keys("secret_sauce")

# Clicking login button:
xpath_of_login_button = "//input[@id='login-button']"
element_of_login_first = driver.find_element(By.XPATH, xpath_of_login_button)
element_of_login_first.click()
sleep(5)

# Printing cookies in console after login n saucedemo:
print("Cookies after login saucedemo:")
print(driver.get_cookies())
print(driver.current_url)

# Printing cookies in console before login in Zen portal:
driver.get(url2)
print("Cookies before login Zenportal:")
print(driver.get_cookies())
print(driver.current_url)
sleep(3)

# Filling username in zen portal:
element_of_username = driver.find_element(By.NAME, 'email')
element_of_username.send_keys('dineshkumar523@yahoo.com')

# Filling password in zen portal:
element_of_password = driver.find_element(By.NAME, 'password')
element_of_password.send_keys('Sai@16403957')

# Clicking login button in zen portal:
Xpath_of_login_button = '//button[@type="submit"]'
element_of_login = driver.find_element(By.XPATH, Xpath_of_login_button)
element_of_login.click()

# Printing cookies in console after login in zenportal:
print("Cookies after login Zenportal:")
print(driver.get_cookies())
print(driver.current_url)
sleep(5)

# Printing cookies in console after login in dashboard:
driver.get(url3)
print("Cookies after login dashboard:")
print(driver.get_cookies())
print(driver.current_url)
sleep(3)

# Clicking logout button in dashboard:
Xpath_of_Dashboard_logout = ' //span[@data-toggle="dropdown"]'
element_dashboard_logout = driver.find_element(By.XPATH, Xpath_of_Dashboard_logout)
sleep(5)
element_dashboard_logout.click()
element_dashboard_logout_final = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div/div/div/div/button[2]')
sleep(5)
element_dashboard_logout_final.click()

# Printing cookies in console after full logout in zen portal:
print("Cookies after full logout of Zenportal :")
print(driver.get_cookies())
sleep(3)
driver.quit()


