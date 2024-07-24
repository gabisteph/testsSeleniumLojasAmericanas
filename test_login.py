import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_setup_tearDown import TestUpAndDown
from PIL import Image


class TestLogin(TestUpAndDown):
    def test_login(self):
        driver = self.driver
        try:
            # Acessar a página de cadastro
            driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/header/div[1]/div[1]/div/div[2]/button/span/span').click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "entrar"))
            ).click()
            time.sleep(3)
            print("ACHOU BOTÃO DO LOGIN")

        # Preencher o formulário de login
            print("preencher o email de login")
            login = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "login"))
            )
            login.send_keys("yiloxa6192@ikangou.com")
            time.sleep(10)
        # Preencher senha
            print("preencher senha")
            driver.find_element(By.NAME, "password").send_keys("Senha123")
            time.sleep(10)
            
       
        # Submeter o formulário
            driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div/form/div[4]/button').click()
            time.sleep(5)

        # Capturar imagem da tela após o login
            screenshot_path = "Assets/userLogin.png"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot salva em: {screenshot_path}")

        # Esperar pela mensagem de sucesso ou verificar se a página foi redirecionada
            # WebDriverWait(driver, 10).until(
            #          EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Cadastro realizado com sucesso")
            # )
            # print("Teste Cadastro Usuário: Sucesso.")
        except Exception as e:
            print(f"Erro login: {e}")
            self.fail(f"Falha no teste login: {e}")

if __name__ == "__main__":
    unittest.main()

