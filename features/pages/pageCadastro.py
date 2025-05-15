from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class cadastroPage:
    def __init__(self, driver):
        self.driver = driver

    def clicarBotaoCadastro(self):
        self.driver.find_element(By.XPATH, "//*[@id='root']/main/form/div[6]/span[2]/a").click()

    def preencheEmail(self, email):
        self.driver.find_element(By.NAME, "email").send_keys(email)

    def preencheSenha(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def confirmacaoSenha(self, confirm_password):
        self.driver.find_element(By.NAME, "confirmPassword").send_keys(confirm_password)

    def enviar(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".sc-dhKdcB.iFaZzk"))
        ).click()

    def cadastroSucesso(self):
        mensagem = WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "sucess"))
        )
        assert "Usuário cadastrado com sucesso" in mensagem.text, "Mensagem de sucesso não apareceu ou está errada"

    def erroEmail(self):
        erro = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Usuario ja existente com email informado']"))
        )
        assert "Usuario ja existente com email informado" in erro.text

    def erroSenha(self):
        erro = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='As senhas precisam ser iguais']"))
        )
        assert "As senhas precisam ser iguais" in erro.text

    def formatoInvalidoEmail(self):
        erro = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Digite um e-mail válido']"))
        )
        assert "Digite um e-mail válido" in erro.text