from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.expected_conditions import presence_of_element_located



class Scraper:
    def __init__(self, *args, **kwargs):
        self.chrome_path = r'/Users/maion/bin/chromedriver' 
        self.driver = webdriver.Chrome(executable_path=self.chrome_path)
        self.driver.get("https://portal.xpi.com.br")
        # return super().__init__(*args, **kwargs)


    def minha_conta(self):
        return self.driver.find_element_by_xpath("""//*[@id="yield-portal-header"]/header/section[2]/div/nav/ul/li[1]/span""").click() 

    def notas_corretagens(self): 
        return self.driver.find_element_by_xpath("""//*[@id="yield-portal-header"]/header/section[2]/div/nav/ul/li[1]/ul/li[2]/dl/dd[4]/a""").click()   

    def combo_box(self):
        return Select(self.driver.find_element_by_xpath("""//*[@id="Data"]"""))

    def define_tipo_relatorio(self):
        return self.driver.find_element_by_xpath("""//*[@id="rdbXP"]""").click()

    def gera_relatorio(self):
        return self.driver.find_element_by_xpath("""//*[@id="stNotasCor"]/article/div/div/span[4]/button""").click()

    def baixa_relatorio(self):
        return self.driver.find_element_by_xpath("""//*[@id="icon"]""")

    def patrimonio(self):
        return  self.driver.find_element_by_xpath("""/html/body/div[2]/section/div[3]/div[1]/div/div[4]/p[1]/span/span""").text  
scraper = Scraper()
