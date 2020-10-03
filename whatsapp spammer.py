from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\\Ankan-HP\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\chromedriver.exe')
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')
driver.find_element_by_css_selector("span[title='" + input("") + "']").click()
inputString = input("")
tries=int(input(""))
for i in range(tries):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
