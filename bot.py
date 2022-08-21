import os
def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}{nome},O russo Yuri Gagarin (1934-1968) foi a primeira pessoa a viajar para o espaço, o que aconteceu em 12 de abril de 1961.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome},O Monte Everest tem 8.848 metros de altitude e localiza-se no Nepal, um país asiático que faz fronteira com a China e com a Índia.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome},O corpo humano tem 206 ossos: 22 na cabeça, 1 no pescoço, 6 no ouvido, 44 no tórax, 7 no abdômen, 62 nos membros inferiores e 64 nos membros inferiores.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome},Chove muito em Belém, porque a cidade é quente e muita úmida. A chuva costuma cair todos os dias quase à mesma hora depois do horário mais quente. Assim, é comum as pessoas combinarem coisas pensando na chuva (Você vai antes ou depois da chuva?).{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome},Mais pesado é essa barra que é gostar de você <3 {os.linesep}')
    else:
        print('Digite apenas 1,2,3,4 ou 5')
def start():
    # Apresentar o chatbot
    print("Olá seja bem vindo ao meu botcurioso!")
    # Pedir o nome
    nome = input("Digite seu nome: ")
    # Perdir o email
    email = input("Digite seu e-mail: ")
    # Oferecer o menu de opções
    resposta = input(f"O que gostaria de saber hoje? {os.linesep}[1] - Quem foi a primeira pessoa a viajar no Espaço?{os.linesep}[2] - Qual a montanha mais alta do mundo? {os.linesep}[3] - Quantos ossos temos no nosso corpo?{os.linesep}[4] - Que cidade brasileira é conhecida por chover todos os dias quase à mesma hora? {os.linesep}[5] - O que é mais pesado: 1 quilo de algodão ou 1 quilo de ferro?{os.linesep}")
    # Porcessar a resposta enviada
    processar_resposta(resposta,nome)



if __name__== '__main__':
    start()