# CHALLENGE - Gerador de senha SEGURA. 

# - Esse gerador deve conter:
#     - Uma funcionalidade que gere senhas novas
#     - Uma funcionalidade que torne uma senha existente segura se ela não for.
#     - Uma funcionalidade que dada uma senha, diz se ela é segura ou não.

# ### REGRAS:

# - O código precisa estar no github. (Crie um repositório público com o projeto).
# - As funcionalidades precisam estar em funções.
# - Uma senha segura deve conter:
#     - Letra maiúscula
#     - Letra minúscula
#     - Números
#     - Simbolos (@#$%¨&*)

#  ||||||| FUNÇÕES  |||||||

def criar_nova_senha():
    print(" =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 1:              ||")
    print(" ||                                              ||")
    print(" ||      - Uma senha segura deve conter:         ||")
    print(" ||           -- Letra maiúscula                 ||")
    print(" ||           -- Letra minúscula                 ||")
    print(" ||           -- números                         ||")
    print(" ||           -- Simbolos (@#$%¨&*)              ||")
    print(" ||                                              ||")
    print(" ==================================================")
    password = input('Digite sua senha com base nos requisitos')

 







def tratar_senha_fraca():
    print(" =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 2:              ||")
    print(" ||                                              ||")
    print(" ||   - Você deve colocar sua senha existente:   ||")
    print(" ||      -- iremos retornar uma senha mais forte ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" ==================================================")

def verifica_senha_segura():
    print(" =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 3:              ||")
    print(" ||                                              ||")
    print(" ||   - Você deve colocar sua senha existente:   ||")
    print(" ||    -- Verificamos se a senha é segura ou não ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" ==================================================")


 

#  ||||||| MENU |||||||


def menu():
    print(" =================================================")
    print(" ||                                             ||")
    print(" ||   Selecione uma opção:                      ||")
    print(" ||                                             ||")
    print(" ||   1. Criar Nova Senha                       ||")
    print(" ||   2. Tratar senha fraca deixando mais forte ||")
    print(" ||   3. Verifica se a senha é segura ou não    ||")
    print(" ||   0. Sair                                   ||")
    print(" ||                                             ||")
    print(" =================================================")

    while True:
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            criar_nova_senha()
        elif escolha == "2":
            tratar_senha_fraca()
        elif escolha == "3":
            verifica_senha_segura()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções listadas.")

#  ||||||| PROJETO MAIN |||||||

if __name__ == "__main__":
    menu()
1