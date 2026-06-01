nickname = input("Digite o nickname: ")
jogo = input("Digite o jogo escolhido: ")
email = input("Digite o e-mail: ")

if nickname == "" or len(nickname) < 4 or jogo == "" or email == "":
    print("Preencha todos os campos obrigatórios.")
else:
    print("Inscrição realizada com sucesso!")
