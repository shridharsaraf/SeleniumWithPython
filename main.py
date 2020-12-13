#This code is same as the master code just commenting has done to create a branch strategy.
from selenium import  webdriver  #it will import the selenium webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.saucedemo.com/") #this is the url used to perform the automation test
print(driver.title)
time.sleep(3) #it will sleep for 3 seconds 
user_input=driver.find_element_by_name("user-name") #it will search for the "user name" in the webpage
user_input.send_keys("standard_user") #this line will auto fill the username box by "standard_user"
time.sleep(3)
user_pwd=driver.find_element_by_name("password") #This line will search for the password box
user_pwd.send_keys("secret_sauce") #This line will fill the box with 'secret_sauce"
time.sleep(3)
login_button=driver.find_element_by_id("login-button").click() #this line will find the login button and click on the login value
time.sleep(3)
product=driver.find_element_by_class_name("inventory_item_name").click() #This code is used to expand the product details
time.sleep(3)
cart=driver.find_element_by_xpath("//*[@id='inventory_item_container']/div/div/div/button").click() #It will click on the add to cart button
time.sleep(3)
cartbox=driver.find_element_by_class_name("shopping_cart_container").click() 
time.sleep(3)
checkout=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[2]/a[2]").click()
time.sleep(3)
f_name=driver.find_element_by_id("first-name")
f_name.send_keys("Shridhar")
time.sleep(3)
name=driver.find_element_by_xpath("//*[@id='last-name']")
name.send_keys("Saraf")
time.sleep(3)
Zip=driver.find_element_by_id("postal-code").send_keys("585103")
time.sleep(3)
Continue=driver.find_element_by_xpath("//*[@id='checkout_info_container']/div/form/div[2]/input").click()
time.sleep(3)
finish=driver.find_element_by_xpath("//*[@id='checkout_summary_container']/div/div[2]/div[8]/a[2]").click() #This line will click on the finish button at the end of all operations
time.sleep(3)
driver.quit() #Finally this line will quit the browser
