from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# import pyautogui
from time import sleep
# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 2.5
# wait = WebDriverWait(driver, 10)
results = []

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 20)
    driver.maximize_window()
    # driver.get("http://www.cremesp.org.br/?siteAcao=GuiaMedico&pesquisa=proc")
    # driver.get("https://portal.xpi.com.br/acoes-opcoes-futuros/notas-corretagem/RelatorioPDF?data=19/02/2014&type=xp")
    # driver.get("https://portal.xpi.com.br/acoes-opcoes-futuros/notas-corretagem/")
    driver.get("https://portal.xpi.com.br")
    
    # driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)
    sleep(60*2)
    # wait.until(presence_of_element_located((By.XPATH, '//*[@id="Data"]')))
    # x = None
    # while not x:
    # x, y = pyautogui.locateCenterOnScreen('imnot2.png')

    # pyautogui.click(x-120, y)
    # sleep(2)
    # x, y = pyautogui.locateCenterOnScreen('continuar.png')
    # pyautogui.click(x,y)
    # pyautogui.click(x,y)
    # results = driver.find_element_by_xpath('//*[@id="viewerContainer"]')
    results = driver.find_element_by_class_name('dvBodyRelatorio')
    
    print(results.text)
    # for i, result in results.iteritems():
    #     print("#{}: {} ({})".format(i, result.text, result.get_property("href")))

    # url = "http://www.cremesp.org.br/?siteAcao=GuiaMedico&pesquisa=proc"

# /html/body/div[3]/div[1]/div[4]/div[1]/table[1]