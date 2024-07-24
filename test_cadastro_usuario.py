import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_setup_tearDown import TestUpAndDown
from PIL import Image


class TestCadastroUsuario(TestUpAndDown):
    def test_cadastro_usuario(self):
        driver = self.driver
        try:
            # Acessar a página de cadastro
            driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/header/div[1]/div[1]/div/div[2]/button').click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "cadastrar"))
            ).click()
            print("ACHOU BOTÃO DE CADASTROOOOO")

        # Preencher o formulário de cadastro
            print("preencher o nome")
            nome_campo = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "name"))
            )
            nome_campo.send_keys("Cristiane Liz Helena Martins")
            print("preencher o nome social")

            time.sleep(3)
            

            driver.find_element(By.NAME, "socialName").send_keys("Cris")

            time.sleep(3)

            
        # Selecionar gênero
            print("clicar gênero")
            genero = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/form/div[3]/div[2]/label[1]'))
            )
            genero.click()
            
            time.sleep(3)


        # Preencher data de nascimento
            driver.find_element(By.NAME, "birthDate").send_keys("20031999")
            time.sleep(3)


        # Preencher CPF
            driver.find_element(By.NAME, "cpf").send_keys("99353111200")

        # Preencher telefone
            driver.find_element(By.NAME, "phone").send_keys("(92) 98785-4321")

        # Preencher e-mail
            driver.find_element(By.NAME, "email").send_keys("danigspm29@gmail.com")

        # Preencher senha
            driver.find_element(By.NAME, "password").send_keys("Senh@123")
            time.sleep(3)
        
       
        # Submeter o formulário
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/button[2]').click()
            time.sleep(6)
        # Capturar imagem da tela após o cadastro
            screenshot_path = "Assets/confirmaCadastro.png"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot salva em: {screenshot_path}")

        # # Esperar pela mensagem de sucesso ou verificar se a página foi redirecionada
        #     WebDriverWait(driver, 10).until(
        #         EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Cadastro realizado com sucesso")
        #     )
        #     print("Teste Cadastro Usuário: Sucesso.")
        except Exception as e:
            print(f"Erro no teste Cadastro Usuário: {e}")
            self.fail(f"Falha no teste Cadastro Usuário: {e}")

if __name__ == "__main__":
    unittest.main()