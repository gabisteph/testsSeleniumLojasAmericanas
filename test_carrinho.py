import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_setup_tearDown import TestUpAndDown


    

class ShopCar(TestUpAndDown):
    def test_car(self):
        driver = self.driver
        try:
            # Preenche o produto que quero pesquisar
            print("Digitar produto")
            search = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "conteudo"))
            )
            search.send_keys("notebook")
            time.sleep(10)
            
            # Clica no botão de pesquisa
            print("Clicar no botão de pesquisa")
            driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/header/div[1]/div[1]/div/div[1]/form/button').click()
            time.sleep(10)

            # Clicar no produto
            print("Clicar no produto")
            driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/main/div/div[1]/div[3]/div[1]').click()
            time.sleep(10)
        
            # Clicar no botão de comprar
            print("Clicar no botão de comprar")
            driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/main/div[3]/div/div[2]/div/div[1]/div[3]/a/span').click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "comprar"))
            ).click()
            print("Achou botão de comprar")
            time.sleep(20)

            # Botão de confirmação produto usado
            print("Clicar no botão de confirmação produto usado")
            continue_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "sim, continuar"))
            )
            continue_link.click()
            print("Clicou no botão de confirmação produto usado")
            
            # Ignorar seguro e ir para carrinho
            print("Ignorar seguro")
            driver.find_element(By.CSS_SELECTOR, '.styles__ButtonUI-sc-1ua2cx8-0').click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "não incluir serviço e ir pra cesta"))
            ).click()
            time.sleep(10)

            # Capturar imagem da tela final
            screenshot_path = "Assets/carrinho.png"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot salva em: {screenshot_path}")
            time.sleep(2)

        except Exception as e:
            print(f"Erro busca: {e}")
            self.fail(f"Falha adicionar ao carrinho: {e}")

if __name__ == "__main__":
    unittest.main()
