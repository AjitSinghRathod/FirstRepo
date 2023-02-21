from  selenium import webdriver

driver = webdriver.Chrome("/home/sterlite/learn/chromedriver")
url="https://www.amarujala.com/tags/nesw-in-hindi"
path="/html/body/div[1]/div/div/div/div/nav/ul/li[6]/a"

driver.get(url)
v=driver.find_element("xpath", path)
print(v.text)
