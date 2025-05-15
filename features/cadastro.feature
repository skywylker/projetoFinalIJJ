Feature: Cadastro de novos usuários

  Scenario: Cadastro com dados válidos
    Given que o usuário não possui conta e está na página de login
    When O usuário clica no link de registro
    And O usuário preenche um e-mail válido
    And O usuário preenche uma senha válida
    And O usuário confirma a senha corretamente
    And O usuário finaliza o cadastro
    Then Deve visualizar a mensagem de sucesso de cadastro

  Scenario: Cadastro com e-mail já registrado
    Given que o usuário não possui conta e está na página de login
    When O usuário clica no link de registro
    And O usuário preenche um e-mail válido
    And O usuário preenche uma senha válida
    And O usuário confirma a senha corretamente
    And O usuário finaliza o cadastro
    Then Deve visualizar a mensagem de e-mail já existente

  Scenario: Cadastro com senhas diferentes
    Given que o usuário não possui conta e está na página de login
    When O usuário clica no link de registro
    And O usuário preenche um e-mail válido
    And O usuário preenche uma senha válida
    And O usuário confirma a senha incorretamente
    And O usuário finaliza o cadastro
    Then Deve visualizar a mensagem de senhas diferentes

  Scenario: Cadastro com e-mail mal formatado
    Given que o usuário não possui conta e está na página de login
    When O usuário clica no link de registro
    And O usuário preenche um e-mail inválido
    And O usuário preenche uma senha válida
    And O usuário confirma a senha corretamente
    And O usuário finaliza o cadastro
    Then Deve visualizar a mensagem de e-mail inválido