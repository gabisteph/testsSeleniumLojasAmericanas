import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_setup_tearDown import TestUpAndDown
from PIL import Image


class PesquisarProduto(TestUpAndDown):
    def test_search(self):
        driver = self.driver
        try:
        # preenche produto que quero pesquisar
            print("Digitar produto")
            search = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "conteudo"))
            )
            search.send_keys("sofá")
            time.sleep(10)
            
        # clica no botão de pesquisa
            print("clicar no botão de pesquisa")
            driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/header/div[1]/div[1]/div/div[1]/form/button').click()
            time.sleep(10)
        

        # Capturar imagem da tela final
            screenshot_path = "Assets/pesquisarProduto.png"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot salva em: {screenshot_path}")
            time.sleep(10)

        # Esperar pela mensagem de sucesso ou verificar se a página foi redirecionada
            # WebDriverWait(driver, 10).until(
            #          EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Cadastro realizado com sucesso")
            # )
            # print("Teste Cadastro Usuário: Sucesso.")
        except Exception as e:
            print(f"Erro busca: {e}")
            self.fail(f"Falha no teste de pequisa: {e}")

if __name__ == "__main__":
    unittest.main()

