from selenium import webdriver
import requests
import time

# 使用 Chrome 的 WebDriver
browser = webdriver.Chrome()

# 開啟 Pchome 首頁
browser.get("https://24h.pchome.com.tw/?gclid=CjwKCAjww5r8BRB6EiwArcckC1ltizGmpoNB0xeL7V2-Fuh-4NkxtIfMCMTGbaAt-bffMHt6v1viDRoCSdAQAvD_BwE")
time.sleep(2)

# 尋找網頁中的搜尋框
inputElement = browser.find_element_by_id("keyword")
time.sleep(0.5)

# 在搜尋框中輸入文字
inputElement.send_keys("藍牙耳機")
time.sleep(0.5)

# 送出搜尋
search = browser.find_element_by_id("doSearch")
search.click()
time.sleep(0.5)

# 點擊第一則
# 以下是用xpath
# browser.find_element_by_xpath("//div[@id='ItemContainer']/dl/dd[2]/h5/a").click()
# 以下是用css_selector
browser.find_element_by_css_selector("h5.prod_name > a").click()

# 將該商品加入購物車
# browser.find_elements_by_xpath("//*[text()='加入24H購物車']").click()
# browser.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()
# browser.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()
#driver.find_element_by_link_text（"加入24H購物車")
a = browser.find_element_by_xpath("//*[@id='ButtonContainer']")
print(a)


# 點擊右下角結帳


# 登入帳密
