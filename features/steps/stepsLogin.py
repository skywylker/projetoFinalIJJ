from behave import when, then
from pages.pageLogin import PaginaLogin

@when("O usuário preenche e-mail e senha vazios")
def preencher_campos_vazios(context):
    context.pageLogin.preencher_email("")
    context.pageLogin.preencher_senha("")

@when("O usuário preenche apenas a senha")
def preencher_somente_senha(context):
    context.pageLogin.preencher_email("")
    context.pageLogin.preencher_senha("abc.123")

@when("O usuário preenche apenas o e-mail")
def preencher_somente_email(context):
    context.pageLogin.preencher_email("csilva@gmail.com")
    context.pageLogin.preencher_senha("")

@when("O usuário preenche e-mail inválido e senha válida")
def email_invalido_senha_valida(context):
    context.pageLogin.preencher_email("errado@email.com")
    context.pageLogin.preencher_senha("abc.123")

@when("O usuário preenche e-mail válido e senha inválida")
def email_valido_senha_invalida(context):
    context.pageLogin.preencher_email("csilva@gmail.com")
    context.pageLogin.preencher_senha("errado123")

@when("O usuário preenche com credenciais inválidas")
def preencher_credenciais_erradas(context):
    context.pageLogin.preencher_email("umemail@qualquer.com")
    context.pageLogin.preencher_senha("hakunamatata")

@when("O usuário preenche com credenciais válidas")
def preencher_credenciais_validas(context):
    context.pageLogin.preencher_email("csilva@gmail.com")
    context.pageLogin.preencher_senha("abc.123")

@when("O usuário clica no botão de login")
def clicar_login(context):
    context.pageLogin.clicar_botao_login()

@then("O usuário deve ser redirecionado para a homepage")
def validar_redirecionamento(context):
    context.pageLogin.verificar_login_sucesso()

@then("O sistema não realiza o login")
def validar_falha_login(context):
    context.pageLogin.verificar_falha_login()
