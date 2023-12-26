from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def navigate_to_consigned(driver: WebDriver):
    # Find button menu and open
    wait = WebDriverWait(driver, 10)
    btn_menu = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[4]/user-menu/div')))
    driver.execute_script("arguments[0].classList.add('open-menu');", btn_menu)

    # Find butti]on navegate and click
    driver.find_element(by=By.XPATH, value='//*[@id="header"]/div[4]/user-menu/div/nav/div/div[3]/ul/li[2]/a').click()


def navigate_to_proposal(driver: WebDriver):
    driver.get("https://consignado.santander.com.br/Comissao45/MenuWeb/Consultas/Fatura/UI.CL.Fatura.aspx")
    # wait = WebDriverWait(driver, 20)
    # link = driver.find_element(By.CSS_SELECTOR, 'a[id="ctl00_ContentPlaceHolder1_j0_j1_DataListMenu_ctl03_LinkButton2"]')

    # print(link)

    # for link in links:
    #     print(link.text)

    # btn_hover = driver.find_element(by=By.XPATH, value='//*[@id="cph_Menu1n1"]/table/tbody/tr/td[1]/a')
    # driver.execute_script("arguments[0].classList.add('cph_Menu1_12');", btn_hover)
# ctl00_ContentPlaceHolder1_j0_j1_DataListMenu_ctl03_LinkButton2
# ctl00_ContentPlaceHolder1_j0_j1_DataListMenu_ctl03_LinkButton2
# ctl00_ContentPlaceHolder1_j0_j1_DataListMenu_ctl03_LinkButton2