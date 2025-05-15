Feature: Login de usuário

  Scenario: Login com dados válidos
    When O usuário preenche com credenciais válidas
    And O usuário clica no botão de login
    Then O usuário deve ser redirecionado para a homepage

  Scenario: Login com dados inválidos
    When O usuário preenche com credenciais inválidas
    And O usuário clica no botão de login
    Then O sistema não realiza o login

    Scenario: Login com e-mail e senha vazios
    When O usuário preenche e-mail e senha vazios
    And O usuário clica no botão de login
    Then O sistema não realiza o login

  Scenario: Login apenas com senha
    When O usuário preenche apenas a senha
    And O usuário clica no botão de login
    Then O sistema não realiza o login

  Scenario: Login apenas com e-mail
    When O usuário preenche apenas o e-mail
    And O usuário clica no botão de login
    Then O sistema não realiza o login

  Scenario: Login com e-mail inválido e senha válida
    When O usuário preenche e-mail inválido e senha válida
    And O usuário clica no botão de login
    Then O sistema não realiza o login

  Scenario: Login com e-mail válido e senha inválida
    When O usuário preenche e-mail válido e senha inválida
    And O usuário clica no botão de login
    Then O sistema não realiza o login
