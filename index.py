import threading
import time

TEMPO_LIMITE_SEM_INTERACAO = 3600
Mostrar texto das mensagens anteriores
        opcao1 = input()
#Apadrinhe um pet------------------------------------------------------------------------------------------
    elif opcao1 == "2": 
        reiniciar_contagem_tempo()
        print("""
Olá! 🐱❤🐶
Apadrinhar um pet é um gesto incrível de solidariedade! 
Ao se tornar padrinho ou madrinha, você ajuda financeiramente um animal em necessidade. 💌

Para apadrinhar um amigo peludo através do Projeto Lunaar, visite:
https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c93808487b565700187b58b8d5a000e

Juntos, podemos fazer a diferença na vida desses animais. 🏡💕""")
        opcao1 = input()
#Doação--------------------------------------------------------------------------------------------
    elif opcao1 == "3": 
        reiniciar_contagem_tempo()
        print("""
Olá! 🐱🐾
Seja parte da mudança e faça a diferença na vida dos animais. Suas doações 
são essenciais para apoiar as ONGs que trabalham incansavelmente por eles! 🫶

Para doar à ONG "É o Bicho":
Chave Pix -> CNPJ: 42.442.070/0001-40

Para doar à ONG "Projeto Lunaar":
Chave Pix -> CNPJ: 39.469.916/0001-20

Cada contribuição conta! Juntos, podemos proporcionar um futuro melhor para 
nossos amiguinhos de quatro patas. ❤🐶
""")
        opcao1 = input()
#ONGs participantes-----------------------------------------------------------------------------------------------
    elif opcao1 == "4":
        reiniciar_contagem_tempo() 
        print("""
Sobre qual das ONGs abaixo você gostaria de conhecer mais? 
              
1 - É o Bicho
2 - Projeto Lunaar
              
""")    
        opcao2 = input()
        if opcao2 == "1":
            reiniciar_contagem_tempo()
            print("""
A É o Bicho MT! surgiu em 2015, inicialmente focada em proteger cães e gatos 
em situação de vulnerabilidade, vítimas de abandono ou maus-tratos em Cuiabá/MT. 
Em 2020, expandiram para incluir animais silvestres e formalizaram-se como 
associação em 2021. A diretoria, composta por oito voluntárias, financia suas 
ações por meio de doações e campanhas. 🐾💙
""")
            opcao1 = input()
        elif opcao2 == "2":
            reiniciar_contagem_tempo()
            print("""
O Projeto LUNAAR - Luta e União de Amigos para Animais em Risco nasceu em outubro
de 2017, liderado por Tainá Marques, estudante de Nutrição da UFMT. O foco inicial 
era ajudar cerca de 800 gatos nas áreas das faculdades da UFMT. Criaram uma 
campanha inovadora, arrecadando frascos vazios de desodorantes em aerosol, 
protegendo o meio ambiente e auxiliando os animais. Com 40 voluntários e 54 pontos 
de coleta, o projeto expandiu para incluir o Pantanal como seu primeiro shopping 
com ponto de coleta. 🐾💙
""")
            opcao1 = input()
Mostrar texto das mensagens anteriores
Ocultar texto das mensagens anteriores

Em qui., 14 de dez. de 2023 às 18:00, Leonardo Andrade <leonardolimaandrade40@gmail.com> escreveu:
import threading
import time

TEMPO_LIMITE_SEM_INTERACAO = 5

atendimento_encerrado = False
start_time = time.time()

def contagem_regressiva():
    global opcao1, opcao2, atendimento_encerrado, start_time
    opcao1 = opcao2 = " "
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time > TEMPO_LIMITE_SEM_INTERACAO:
            atendimento_encerrado = True
            print("Excedeu o tempo limite de atendimento.")
            break
        time.sleep(1)
        
        if opcao1=="encerrar"or opcao2=="encerrar": 
            atendimento_encerrado = True
            break
        
def reiniciar_contagem_tempo():
    global start_time
    start_time = time.time()

thread_contagem_regressiva = threading.Thread(target=contagem_regressiva)
thread_contagem_regressiva.start()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def inicio():
    print("""Olá """ + nome +""", tudo bem? 
Bem vindo ao nosso sistema de atendimento eletrônico da CiberPatinhas! 
É um prazer atendê-lo(a)!""")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def opcoes():
    reiniciar_contagem_tempo()
    print("""
Pra gente continuar, digite apenas o número da opção:

1 - Adoção
2 - Apadrinhe um pet
3 - Doação
4 - ONGs participantes

""")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menus(): 
    global opcao1, opcao2
    atendimento_encerrado = False
    reiniciar_contagem_tempo()
#Adoção---------------------------------------------------------------------------------------------------
    if opcao1 == "1": 
        reiniciar_contagem_tempo()
        print("""
Olá! 🐶🐱
Se você está pensando em adotar um amiguinho peludo, confira essas ONGs incríveis:

É o Bicho - Adote amor e alegria. 🐾
https://docs.google.com/forms/d/e/1FAIpQLSejXnvjJ6eqYsB7Lewy3Vq8VsC2RDghUJZpTPp_BbT05vzdpg/viewform

Projeto Lunaar - Faça a diferença na vida de um pet. 🏡
https://api.whatsapp.com/send?phone=5565992701706&text=Ol%C3%A1,%20eu%20quero%20adotar!%20

Adotar é um gesto maravilhoso! Se precisar de mais informações, estou aqui para te ajudar. 🐕🐈""")
#Apadrinhe um pet------------------------------------------------------------------------------------------
    elif opcao1 == "2": 
        reiniciar_contagem_tempo()
        print("""
Olá! 🐱❤🐶
Apadrinhar um pet é um gesto incrível de solidariedade! 
Ao se tornar padrinho ou madrinha, você ajuda financeiramente um animal em necessidade. 💌

Para apadrinhar um amigo peludo através do Projeto Lunaar, visite:
https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c93808487b565700187b58b8d5a000e

Juntos, podemos fazer a diferença na vida desses animais. 🏡💕""")
#Doação--------------------------------------------------------------------------------------------
    elif opcao1 == "3": 
        reiniciar_contagem_tempo()
        print("""
Olá! 🐱🐾
Seja parte da mudança e faça a diferença na vida dos animais. Suas doações 
são essenciais para apoiar as ONGs que trabalham incansavelmente por eles! 🫶

Para doar à ONG "É o Bicho":
Chave Pix -> CNPJ: 42.442.070/0001-40

Para doar à ONG "Projeto Lunaar":
Chave Pix -> CNPJ: 39.469.916/0001-20

Cada contribuição conta! Juntos, podemos proporcionar um futuro melhor para 
nossos amiguinhos de quatro patas. ❤🐶
""")
            
#ONGs participantes-----------------------------------------------------------------------------------------------
    elif opcao1 == "4":
        reiniciar_contagem_tempo() 
        print("""
Sobre qual das ONGs abaixo você gostaria de conhecer mais? 
              
1 - É o Bicho
2 - Projeto Lunaar
              
""")    
        opcao2 = input()
        if opcao2 == "1":
            reiniciar_contagem_tempo()
            print("""
A É o Bicho MT! surgiu em 2015, inicialmente focada em proteger cães e gatos 
em situação de vulnerabilidade, vítimas de abandono ou maus-tratos em Cuiabá/MT. 
Em 2020, expandiram para incluir animais silvestres e formalizaram-se como 
associação em 2021. A diretoria, composta por oito voluntárias, financia suas 
ações por meio de doações e campanhas. 🐾💙
""")
        elif opcao2 == "2":
            reiniciar_contagem_tempo()
            print("""
O Projeto LUNAAR - Luta e União de Amigos para Animais em Risco nasceu em outubro
de 2017, liderado por Tainá Marques, estudante de Nutrição da UFMT. O foco inicial 
era ajudar cerca de 800 gatos nas áreas das faculdades da UFMT. Criaram uma 
campanha inovadora, arrecadando frascos vazios de desodorantes em aerosol, 
protegendo o meio ambiente e auxiliando os animais. Com 40 voluntários e 54 pontos 
de coleta, o projeto expandiu para incluir o Pantanal como seu primeiro shopping 
com ponto de coleta. 🐾💙
""")
        elif opcao2 == "encerrar":
            pass
        elif opcao2 == "inicio":
            pass
        else:
            print("Essa opção não existe! Tenta de novo! ☺")
    elif opcao1 =="encerrar" :
        pass
    elif opcao1 == "inicio":
        pass
    else:
        print("Essa opção não existe! Tenta de novo! ☺")



#----------------------------------------------------inicio do código------------------------------------------------------------
comecar = input()
nome = " "
if nome == " ":
    print("""Olá! Eu sou o Assistente Virtual da CiberPatinhas! 🤖🐾

Para começar, me diga por favor, qual o seu nome? (⚠ Somente o nome)""")
nome = input()
print("\n")

inicio()
opcoes()
opcao1 = input()
menus()

while atendimento_encerrado == False and opcao1!="encerrar"and opcao2!="encerrar":
    start_time = time.time()
    print("\n--------------------------------------------------------------\n")
    opcoes()
    opcao1 = input()
    menus()
    if opcao1 == "inicio" or opcao2 == "inicio":
        print("\n\n\n")
        inicio()
        opcoes()
        opcao1 = input()
        menus()
        
thread_contagem_regressiva.join()
    
print("\nAtendimento encerrado!")