import unittest

from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class TestUpAndDown(unittest.TestCase):

    def setUp(self):
        try:
            options = EdgeOptions()
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            options.add_argument(f'user-agent={user_agent}')
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            self.driver = Edge(options=options)
            self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
            self.driver.get('https://www.americanas.com.br/')
            self.driver.maximize_window()
            print("Setup completo: Navegador iniciado e maximizado.")
        except Exception as e:
            print(f"Erro no setup: {e}")
            self.fail(f"Falha no setup: {e}")
            
        # Fechar o modal de propaganda se aparecer
        try:
            fechar_modal = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="rsyswpsdk"]/div/div[2]/div/div/div/div/a[1]'))
            )
            fechar_modal.click()
            print("MODAL FOI FECHADO COM SUCESSOOOO")
        except:
            print("Modal de propaganda não apareceu ou já estava fechado.")

    def tearDown(self):
        try:
            self.driver.quit()
            print("TearDown completo: Navegador fechado.")
        except Exception as e:
            print(f"Erro no teardown: {e}")