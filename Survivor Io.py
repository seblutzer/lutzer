import tkinter as tk
import pyautogui
import time
import threading
import random

move_list = []


def move():
    global move_list
    # Lista de opções possíveis
    options = ['up', 'down', 'left', 'right']

    # Filtrar as opções que ainda não foram escolhidas
    available_options = [option for option in options if option not in move_list]

    # Sortear uma opção das disponíveis
    move = random.choice(available_options)
    move_list.append(move)  # Adicionar o movimento à lista

    # Reiniciar a lista se todos os movimentos foram escolhidos
    if len(move_list) == 4:
        move_list = []

    return move

# Função para executar as ações
def executar_acoes():
    #choose_level()
    for i in range(250):
        # Press the arrow keys successively with an interval of 1 second
        pyautogui.press(move())
        pyautogui.click(random.choice([70, 200, 330]), 540) # Choose a ramdom skill Path
        pyautogui.click(200, 730)  # Click Next
        pyautogui.click(200, 600)  # Revive if Needed
        pyautogui.click(200, 780)
        time.sleep(0.5)
        if i % 10 == 0 and i != 0:
            pyautogui.click(263, 780) # Click outside the challenge box
            pyautogui.click(315, 450) # Click in the 3rd challenge box
            time.sleep(0.2)
            pyautogui.click(200, 695) # Start the match

# Função chamada ao pressionar o botão "Começar"
def start_task():
    btn_start.config(state='disabled')

    # Executar as ações em uma thread para não travar a interface
    task_thread = threading.Thread(target=executar_acoes)
    task_thread.start()

    # Voltar os botões ao normal após a execução
    def enable_buttons():
        task_thread.join()
        btn_start.config(state='normal')

    watching_thread = threading.Thread(target=enable_buttons)
    watching_thread.start()


# Função chamada ao pressionar o botão "Terminar" (simplesmente fecha o programa)
def stop_program():
    janela.destroy()

def mark_point():
    time.sleep(2)
    print(pyautogui.position())

# Criar a janela principal
janela = tk.Tk()
janela.title("Survivor.IO challenges")

janela.attributes('-topmost', True)

# Configurar os botões
btn_start = tk.Button(janela, text="Start", command=start_task)
btn_start.pack(pady=10)

btn_mark = tk.Button(janela, text="Mark Point", command=mark_point)
btn_mark.pack(pady=10)

# Iniciar o loop da interface
janela.mainloop()
