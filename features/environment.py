from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from features.pages.pageLogin import PaginaLogin


def before_scenario(context, scenario):
    options = Options()
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/")
    context.pageLogin = PaginaLogin(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()