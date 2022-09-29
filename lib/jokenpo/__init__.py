from colorama import Fore, Back, Style, init, deinit
from emoji import emojize
from time import sleep
# ======= Variáveis ==========
# --Emojis
pedra = emojize(":oncoming_fist:")
papel = emojize(":hand_with_fingers_splayed:")
tesoura = emojize(":victory_hand:")
jokenpo1 = emojize(":raised_fist:")
jokenpo2 = emojize(":right-facing_fist:")

# --cores
red = Fore.RED
black = Fore.BLACK
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.BLUE
green = Fore.GREEN
white = Fore.WHITE
cyan = Fore.CYAN
resetcolor = Style.RESET_ALL
# ============================


def jokenpo(jogador, computador):
    if computador == 0:
        print(emojize(f"{green} PÔ {pedra} {resetcolor}", ))
        sleep(1)
        print('-=-'*10)
        print(f'O computador escolheu {cyan} PEDRA: {resetcolor}{pedra}')
        print('-'*30)
    elif computador == 1:
        print(emojize(f"{green} PÔ {papel} {resetcolor}", ))
        sleep(1)
        print('-=-'*10)
        print(f'O computador escolheu {cyan}PAPEL{resetcolor}: {papel}')
        print('-'*30)
    elif computador == 2:
        print(emojize(f"{green} PÔ {tesoura} {resetcolor}", ))
        sleep(1)
        print('-=-'*10)
        print(f'O computador escolheu {cyan}TESOURA{resetcolor}: {tesoura}')
        print('-'*30)
    if jogador == 0:
        print(emojize(f"Você escolheu {cyan}PEDRA{resetcolor}: {pedra}", ))
        print('-=-'*10)
    elif jogador == 1:
        print(emojize(f"Você escolheu {cyan}PAPEL{resetcolor}: {papel}", ))
        print('-=-'*10)
    elif jogador == 2:
        print(
            emojize(f"Você escolheu {cyan}TESOURA{resetcolor}: {tesoura}", ))
        print('-=-'*10)

    if computador == 0:  # computador jogou "pedra"
        if jogador == 0:
            return print('-'*5, f"{yellow}EMPATE{resetcolor}", '-'*5)
        elif jogador == 1:
            return print('-'*5, f"{green}VOCÊ VENCEU{resetcolor}", '-'*5)
        elif jogador == 2:
            return print('-'*5, f"{red}COMPUTADOR VENCEU{resetcolor}", '-'*5)
    elif computador == 1:  # computador jogou "Papel"
        if jogador == 0:
            return print('-'*5, f"{red}COMPUTADOR VENCEU{resetcolor}", '-'*5)
        elif jogador == 1:
            return print('-'*5, f"{yellow}EMPATE{resetcolor}", '-'*5)
        elif jogador == 2:
            return print('-'*5, f"{green}VOCÊ VENCEU!{resetcolor}", '-'*5)
    elif computador == 2:  # computador jogou "Tesoura"
        if jogador == 0:
            return print('-'*5, f"{green}VOCÊ VENCEU!{resetcolor}", '-'*5)
        elif jogador == 1:
            return print('-'*5, f"{green}VOCÊ PERDEU!{resetcolor}", '-'*5)
        elif jogador == 2:
            return print('-'*5, f"{yellow}EMPATE{resetcolor}", '-'*5)
