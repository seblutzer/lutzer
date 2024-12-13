import tkinter as tk
from tkinter import ttk  # Para usar a Combobox
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

# Dicionário com as chaves e suas posições
points = {
    'Ability 1': [70, 540],
    'Ability 2': [200, 540],
    'Ability 3': [330, 540],
    'Next': [200, 730],
    'Revive': [200, 600],
    'Resume': [200, 780],
    'Outside box': [263, 780],
    'Challenge': [315,450],
    'Start Challenge': [200, 695]
}

# Função para executar as ações
def executar_acoes():
    #choose_level()
    for i in range(10000):
        # Press the arrow keys successively with an interval of 1 second
        pyautogui.press(move())
        pyautogui.click(random.choice([points['Ability 1'][0], points['Ability 2'][0], points['Ability 3'][0]]), points['Ability 1'][1]) # Choose a ramdom skill Path
        pyautogui.click(points['Next'][0], points['Next'][1])  # Click Next
        pyautogui.click(points['Revive'][0], points['Revive'][1])  # Revive if Needed
        pyautogui.click(points['Resume'][0], points['Resume'][1]) # Resume
        time.sleep(0.5)
        if i % 10 == 0 and i != 0:
            pyautogui.click(points['Outside box'][0], points['Outside box'][1]) # Click outside the challenge box
            pyautogui.click(points['Challenge'][0], points['Challenge'][1]) # Click in the 3rd challenge box
            time.sleep(0.2)
            pyautogui.click(points['Start Challenge'][0], points['Start Challenge'][1]) # Start the match

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
    app.destroy()

# Função para realizar a marcação de um ponto
def mark_point(selected_key_combobox, status_label):
    # Obter a chave selecionada pela Combobox
    selected_key = selected_key_combobox.get()

    # Verificar se alguma chave foi selecionada
    if not selected_key:
        status_label.config(text="Escolha uma opção antes de marcar!")
        return

    # Avisar o usuário para posicionar o mouse
    status_label.config(text=f"Posicione o mouse para {selected_key}. Marcaremos em 2 segundos...")

    # Usar uma thread para evitar travar a interface
    def worker():
        time.sleep(2)  # Esperar 2 segundos
        current_position = [pyautogui.position().x, pyautogui.position().y]  # Capturar a posição do mouse
        points[selected_key] = current_position  # Salvar a posição na chave do dicionário
        status_label.config(text=f"{selected_key} atualizado para posição {current_position}!")
        print(f"{selected_key} atualizado para posição {current_position}!")

    threading.Thread(target=worker).start()


# Criar a interface gráfica
app = tk.Tk()
app.title("Marcar Ponto")
app.geometry("150x110")

# Configurar os botões
btn_start = tk.Button(app, text="Start", command=start_task)
btn_start.pack()

# Rótulo explicativo
tk.Label(app, text="Selecione uma opção e clique em 'Marcar Ponto':").pack()

# Variável para armazenar a seleção do menu suspenso
selected_key_var = tk.StringVar(app)
selected_key_var.set("Options")  # Configurar valor padrão

# Criar o menu suspenso (OptionMenu)
options_menu = tk.OptionMenu(app, selected_key_var, *points.keys())
options_menu.pack()

# Botão para marcar o ponto
mark_button = tk.Button(app, text="Mark Point", command=lambda: mark_point(selected_key_var, status_label))
mark_button.pack()

# Rótulo para exibir o status
status_label = tk.Label(app, text="", fg="blue")
status_label.pack()

# Rodar o loop principal
app.mainloop()