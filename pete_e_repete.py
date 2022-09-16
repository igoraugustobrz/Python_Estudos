resposta = input("Tinha dois cachorrinhos, o Pete e o Repete. O Pete morreu, quem sobrou?\n").upper()

while resposta == "REPETE":
    resposta = input("Tinha dois cachorrinhos, o Pete e o Repete. O Pete morreu, quem sobrou?\n").upper()

if resposta != "REPETE":
    print("Acabou com a graça :( ")
