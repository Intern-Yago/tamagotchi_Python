import time


class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 20
        self.saude = 80
        self.idade = 1
        self.felicidade = 75

    def AlterarNome(self, novoNome):
        self.nome = novoNome

    def AlterarFome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0

    def AlterarSaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0

    def AlterarFelicidade(self, valorFeliz):
        self.felicidade += valorFeliz
        if self.felicidade > 100:
            self.felicidade = 100
        elif self.felicidade < 0:
            self.felicidade = 0

    def AlterarIdade(self):
        self.idade += 1

    def RetornarNome(self):
        return self.nome

    def RetornarFome(self):
        return self.fome

    def RetornarSaude(self):
        return self.saude

    def RetornarIdade(self):
        return self.idade

    def RetornarHumor(self):
        humor = self.saude + self.fome
        return humor

    def RetornarFelicidade(self):
        return self.felicidade


nomeB = input('Qual o nome que deseja colocar no seu bichinho? ')
Bichinho = BichinhoVirtual(nome=nomeB)
dias = 0
while (Bichinho.saude > 0) and (Bichinho.fome < 100) and (Bichinho.felicidade > 0):
    if dias == 365:
        print('\n****************************************************')
        print(f'Parabéns! {Bichinho.nome} está fazendo aniverário')
        Bichinho.AlterarIdade()
        print(f'Agora ele possue {Bichinho.idade} anos')
        print('****************************************************')
        dias = 0
        time.sleep(4)
    Bichinho.AlterarFome(+2)
    Bichinho.AlterarSaude(-2)
    Bichinho.AlterarFelicidade(-2)
    resposta = input(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \nOlá meu nome é {Bichinho.nome}. O que você deseja fazer comigo agora? \n1- Alimentar (-10 de fome)
2- Dormir (+10 de saúde)\n3- Brincar (+5 de felicidade)\n4- Alterar nome\n5- Visualizar humor\n6- Visualizar idade
7- Visualizar fome\n8- Visualizar saúde\n9- Visualizar felicidade\nResposta: """)
    print('\n')
    if resposta == '1':
        Bichinho.AlterarFome(-10)
        print("-10 de fome! Me sinto mais forte!")
    elif resposta == '2':
        Bichinho.AlterarSaude(+10)
        print("+10 de saúde! Me sinto mais saudável!")
    elif resposta == '3':
        print('+5 de felicidade! Estou me divertindo muito!')
        Bichinho.AlterarFelicidade(+5)
    elif resposta == '4':
        nome2 = input('Qual nome deseja colocar? \n')
        Bichinho.AlterarNome(nome2)
    elif resposta == '5':
        print("Humor: ", Bichinho.RetornarHumor())
    elif resposta == '6':
        print("Idade: ", Bichinho.RetornarIdade())
    elif resposta == '7':
        print("Fome: ", Bichinho.RetornarFome())
    elif resposta == '8':
        print("Saude: ", Bichinho.RetornarSaude())
    elif resposta == '9':
        print('Felicidade: ', Bichinho.RetornarFelicidade())
    else:
        print('Escolha um número válido!')
        dias -= 1
    dias += 1
print("""\n------------------------------------------\n __         __
/  \.-" "-./  \
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\nVocê me deixou morrer!""")
if Bichinho.saude == 0:
    print('*********** SAÚDE = 0 ***********')
if Bichinho.fome == 100:
    print('*********** FOME = 100 ***********')
if Bichinho.felicidade == 0:
    print('*********** FELICIDADE = 0 ***********')
