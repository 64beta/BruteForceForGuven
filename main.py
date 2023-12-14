def funcR(i):

    time.sleep(0.1)

    input_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/form/div[2]/input")
    input_element.clear()
    input_element.send_keys(str(i))
    time.sleep(0.2)

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/form/button").click()
    time.sleep(0.5)
    if i % 10:
        pass
    else:
        time.sleep(0.4)
    if driver.current_url == "https://sinaqnetice.com/index.php?menu=resultMAN&opt=PARTICIPANT":
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/button").click()

    else:
        ID = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]").text
        CLASS = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]").text
        if "/" in  driver.find_element(By.XPATH,"/html/body/div[1]/div[9]").text:
            POINT = driver.find_element(By.XPATH, "/html/body/div[1]/div[396]").text + " " + driver.find_element(By.XPATH, "/html/body/div[1]/div[395]").text +" / "+ driver.find_element(By.XPATH, "/html/body/div[1]/div[398]").text + " " + driver.find_element(By.XPATH, "/html/body/div[1]/div[397]").text
        else:
         POINT = driver.find_element(By.XPATH, "/html/body/div[1]/div[299]").text

        NAME = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]").text
        SURNAME = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]").text
        GROUP = driver.find_element(By.XPATH, "/html/body/div[1]/div[8]").text
        print(fr"Id : {ID} Class : {CLASS} Point : {POINT} Name&Surname : {NAME} {SURNAME} Group: {GROUP}")
        driver.back()
        time.sleep(0.25)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://sinaqnetice.com/index.php?menu=resultMAN&opt=PARTICIPANT")
time.sleep(2)
i = 2000000
select = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/form/div[1]/select")
select = Select(select)

select.select_by_visible_text("Qrup İmtahanı - Güvən sınaq 10")
assert "Qrup İmtahanı - Güvən sınaq 10" in select.first_selected_option.text
while(True):
 try :
     funcR(i)
     i+=1
 except:
     driver.get("https://sinaqnetice.com/index.php?menu=resultMAN&opt=PARTICIPANT")
     time.sleep(2)
     select = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/form/div[1]/select")
     select = Select(select)
     select.select_by_visible_text("Qrup İmtahanı - Güvən sınaq 10")
     assert "Qrup İmtahanı - Güvən sınaq 10" in select.first_selected_option.text
