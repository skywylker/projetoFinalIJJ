from behave import given, when, then
from pages.pageCadastro import cadastroPage

@given("que o usuário não possui conta e está na página de login")
def iniciar_cadastro(context):
    context.pageCadastro = cadastroPage(context.driver)

@when("O usuário clica no link de registro")
def clicarRegistro(context):
    context.pageCadastro.clicarBotaoCadastro()

@when("O usuário preenche um e-mail válido")
def preencherEmailValido(context):
    context.pageCadastro.preencheEmail("qsilva@gmail.com")

@when("O usuário preenche um e-mail inválido")
def preencherEmailInvalido(context):
    context.pageCadastro.preencheEmail("lsilvagmail.com")

@when("O usuário preenche uma senha válida")
def preencherSenha(context):
    context.pageCadastro.preencheSenha("Abc.123@#")

@when("O usuário confirma a senha corretamente")
def confirmarSenhaCorreta(context):
    context.pageCadastro.confirmacaoSenha("Abc.123@#")

@when("O usuário confirma a senha incorretamente")
def confirmarSenhaErrada(context):
    context.pageCadastro.confirmacaoSenha("mockingjay")

@when("O usuário finaliza o cadastro")
def finalizarCadastro(context):
    context.pageCadastro.enviar()

@then("Deve visualizar a mensagem de sucesso de cadastro")
def verificarSucesso(context):
    context.pageCadastro.cadastroSucesso()

@then("Deve visualizar a mensagem de e-mail já existente")
def verificarEmailJaExistente(context):
    context.pageCadastro.erroEmail()

@then("Deve visualizar a mensagem de senhas diferentes")
def verificarSenhasDiferentes(context):
    context.pageCadastro.erroSenha()

@then("Deve visualizar a mensagem de e-mail inválido")
def verificarFormatoEmailInvalido(context):
    context.pageCadastro.formatoInvalidoEmail()