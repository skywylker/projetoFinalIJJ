from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginaLogin:
    def __init__(self, driver):
        self.driver = driver

    def preencher_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        ).send_keys(email)

    def preencher_senha(self, senha):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys(senha)

    def clicar_botao_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".sc-eqUAAy.dFhnRi"))
        ).click()

    def verificar_login_sucesso(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("products")
        )
        assert "products" in self.driver.current_url, "Não foi redirecionado para a página de produtos"

    def verificar_falha_login(self):
        WebDriverWait(self.driver, 10).until_not(
            EC.url_contains("products")
        )
        assert "products" not in self.driver.current_url, "Foi redirecionado para produtos quando deveria falhar"
