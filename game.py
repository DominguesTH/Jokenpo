# ===Módulos
from lib.jokenpo import jokenpo
from emoji import emojize
from time import sleep
from colorama import Fore, Back, Style, init, deinit
from random import randint

# ======= Variáveis ==========
# --Emojis
hang = emojize(":call_me_hand:")
jokenpo1 = emojize(":raised_fist:")
jokenpo2 = emojize(":right-facing_fist:")

# --cores
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
resetcolor = Style.RESET_ALL
# ============================
print('='*21)
print(f"{magenta}  É HORA DO JOKENPÔ {resetcolor}")
print('='*21)
sleep(1)
print("  FAÇA SUA JOGADA")
print('-'*21)
sleep(1.5)
while True:
    print(f'''{green} Suas opções:{blue} 
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA {resetcolor}''')

    computador = randint(0, 2)
    while True:
        jogador = int(input(f'{yellow}Qual vai ser sua jogada?: {resetcolor}'))
        if jogador >= 0 and jogador <= 2:
            break
        else:
            print(f'{red}ERRO! Digite uma opção válida. {resetcolor}')

    print('-'*6, f'{"COMPUTADOR":^2}', '-'*6)
    sleep(1)
    print(emojize(f'{red} JO {jokenpo1} '))
    sleep(1)
    print(emojize(f" KEN {jokenpo2} {resetcolor}"))
    sleep(1)
    jokenpo(jogador=jogador, computador=computador)
    continuar = str(input('Quer jogar novamente? [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break
    elif continuar in 'S':
        continue

sleep(1)
print(f'{blue}~~~~ FOI LEGAL JOGAR COM VOCÊ...')
sleep(1)
print(f'~~~~ ATÉ A PRÓXIMA {hang} {resetcolor}')
sleep(1)
print(f'{red}----- FIM -----{resetcolor}')
