# testcase 41
import re
import time
from selenium import webdriver
driver=webdriver.Chrome()
#connect to local host
driver.get("http://localhost:8888")
driver.maximize_window()
time.sleep(2)
#login with vaild credentials
driver.find_element_by_name('user_name').send_keys('admin')
driver.find_element_by_name('user_password').send_keys('manager')
driver.find_element_by_id('submitButton').click()
time.sleep(1)
#select organisations and press find dupilicated image button
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td[6]/a').click()
driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td[6]/table/tbody/tr/td[3]/a/img').click()
#click ticker symbol and select forward button
driver.find_element_by_xpath('//*[@id="availList"]/option[5]').click()
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[4]/td[2]/div/input[1]').click()
time.sleep(1)
#select find dupilicate and logout the application.
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[5]/td/input[1]').click()
driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[3]/table/tbody/tr/td[2]/img")
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[3]/table/tbody/tr/td[2]/img').click()
time.sleep(2)
driver.close()

#testcase 42:
import re
import time
from selenium import webdriver
driver=webdriver.Chrome()
#connect to local host
driver.get("http://localhost:8888")
driver.maximize_window()
time.sleep(2)
#login with vaild credentials
driver.find_element_by_name('user_name').send_keys('admin')
driver.find_element_by_name('user_password').send_keys('manager')
driver.find_element_by_id('submitButton').click()
time.sleep(1)
#select organisations and press find dupilicated image button
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td[6]/a').click()
driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td[6]/table/tbody/tr/td[3]/a/img').click()
#select member of and press forword button and click  find dupilicate and logout
driver.find_element_by_xpath('//*[@id="availList"]/option[7]').click()
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[4]/td[2]/div/input[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[5]/td/input[1]').click()
time.sleep(2)
driver.close()

#testcase: 43
import re
import time
from selenium import webdriver
driver=webdriver.Chrome()
#connect to local host
driver.get("http://localhost:8888")
driver.maximize_window()
time.sleep(2)
#login with vaild credentials
driver.find_element_by_name('user_name').send_keys('admin')
driver.find_element_by_name('user_password').send_keys('manager')
driver.find_element_by_id('submitButton').click()
time.sleep(1)
#select organisations and press find dupilicated image button
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td[6]/a').click()
driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td[6]/table/tbody/tr/td[3]/a/img').click()
#select employees and click forward botton
driver.find_element_by_xpath('//*[@id="availList"]/option[9]').click()
#press find dupilicate button and logout the application
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[4]/td[2]/div/input[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[5]/td/input[1]').click()
time.sleep(2)
driver.close()

#testcase: 44
import re
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
driver=webdriver.Chrome()
#connect to local host
driver.get("http://localhost:8888")
driver.maximize_window()
time.sleep(2)
#login with vaild credentials
driver.find_element_by_name('user_name').send_keys('admin')
driver.find_element_by_name('user_password').send_keys('manager')
driver.find_element_by_id('submitButton').click()
time.sleep(1)
#select organisations and press find dupilicated image button
driver.find_element_by_xpath("//a[text()='Organizations']").click()
driver.find_element_by_xpath("//img[@title='Find Duplicates']").click()
#select ownership and select forward button
sel=Select(driver.find_element_by_id('availList'))
sel.select_by_value("12")
driver.find_element_by_name("Button").click()
#press find dupilicate button and logout the application
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[4]/td[2]/div/input[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[5]/td/input[1]').click()
time.sleep(2)
driver.close()

#testcase:45
import re
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
driver=webdriver.Chrome()
#connect to local host
driver.get("http://localhost:8888")
driver.maximize_window()
time.sleep(2)
#login with vaild credentials
driver.find_element_by_name('user_name').send_keys('admin')
driver.find_element_by_name('user_password').send_keys('manager')
driver.find_element_by_id('submitButton').click()
time.sleep(1)
#select organisations and press find dupilicated image button
driver.find_element_by_xpath("//a[text()='Organizations']").click()
driver.find_element_by_xpath("//img[@title='Find Duplicates']").click()
#select industry and press forward button
sel=Select(driver.find_element_by_id('availList'))
sel.select_by_value("14")
driver.find_element_by_name("Button").click()
time.sleep(3)
#press find dupilicate button and logout the application
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[4]/td[2]/div/input[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="mergeDup"]/form/table/tbody/tr[5]/td/input[1]').click()
time.sleep(2)
driver.close()
