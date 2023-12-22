from tkinter import *
from tkinter import ttk
from tkinter import font
import random

def game(r, c): #пользователь сделал свой ход
    all_buttons[r][c]["text"] = player_1
    all_buttons[r][c]["state"] = DISABLED
    global free_places, computer, winner
    free_places -= 1
    if free_places == 0 and winner == "": #если игра завершилась вничью
        game_over()
    else:
        flag, winner = check_win() #проверяем возможность выигрыша после данного хода
        computer = False
        if flag == True and winner != "":
            game_over()
        else:
            computer_move(player_2, player_2) #компьютер делает свой ход. Каждый раз проверяем возможность выигрыша
            if computer == True:
                flag, winner = check_win()
                if flag == True and winner!="":
                    game_over()
            else:
                computer_move(player_1, player_2)
                if computer == False: #если нет выигрышных стратегий, компьютер делает случайный ход
                    while True:
                        r = random.randint(0, 2)
                        c = random.randint(0, 2)
                        if all_buttons[r][c]["text"] == "":
                            computer_move_is_true(r, c)
                            break
                        if free_places == 0:
                            break
                flag, winner = check_win()
                if flag == True and winner!='':
                    game_over()
                    
def computer_move_is_true(r, c): #компьютер уже сделал свой ход
    global free_places, computer, player_2
    free_places-=1
    all_buttons[r][c]["text"] = player_2
    all_buttons[r][c]["state"] = DISABLED
    computer = True
    
def computer_move(player_1, player_2): #компьютер делает свой ход
        global free_places, computer
        for i in range(3): #Выбор наилучшей стратегии
            if all_buttons[i][0]["text"] == all_buttons[i][1]["text"] == player_1 and all_buttons[i][2]["text"] == "":
                computer_move_is_true(i, 2)
                break
            elif all_buttons[i][0]["text"] == all_buttons[i][2]["text"]== player_1 and all_buttons[i][1]["text"] == "":
                computer_move_is_true(i, 1)
                break
            elif all_buttons[i][1]["text"] == all_buttons[i][2]["text"]==player_1 and all_buttons[i][0]["text"] == "":
                computer_move_is_true(i, 0)
                break
        if computer == False:
            for i in range(3):
                if all_buttons[0][i]["text"] == all_buttons[1][i]["text"]==player_1 and all_buttons[2][i]["text"] == "":
                    computer_move_is_true(2, i)
                    break
                elif all_buttons[0][i]["text"] == all_buttons[2][i]["text"]==player_1 and all_buttons[1][i]["text"] == "":
                    computer_move_is_true(1, i)
                    break
                elif all_buttons[1][i]["text"] == all_buttons[2][i]["text"]==player_1 and all_buttons[0][i]["text"] == "":
                    computer_move_is_true(0, i)
                    break           
        if computer == False:
            if all_buttons[0][2]["text"] == all_buttons[1][1]["text"]==player_1 and all_buttons[2][0]["text"] == "":
                computer_move_is_true(2, 0)
            elif all_buttons[0][2]["text"] == all_buttons[2][0]["text"]==player_1 and all_buttons[1][1]["text"] == "":
                computer_move_is_true(1, 1)    
            elif all_buttons[2][0]["text"] == all_buttons[1][1]["text"]==player_1 and all_buttons[0][2]["text"] == "":
                computer_move_is_true(0, 2)
            elif all_buttons[0][0]["text"] == all_buttons[1][1]["text"]==player_1 and all_buttons[2][2]["text"] == "":
                computer_move_is_true(2, 2)                
            elif all_buttons[0][0]["text"] == all_buttons[2][2]["text"]==player_1 and all_buttons[1][1]["text"] == "":
                computer_move_is_true(1, 1)                
            elif all_buttons[1][1]["text"] == all_buttons[2][2]["text"]==player_1 and all_buttons[0][0]["text"] == "":
                computer_move_is_true(0, 0)

def check_win(): #проверка выигрыша: выиграл ли уже кто-то
    for i in range(3):
        if all_buttons[i][0]["text"] == all_buttons[i][1]["text"] == all_buttons[i][2]["text"]:
            return True, all_buttons[i][0]["text"]
    for i in range(3):
        if all_buttons[0][i]["text"] == all_buttons[1][i]["text"] == all_buttons[2][i]["text"]:
            return True, all_buttons[0][i]["text"]
    if all_buttons[0][2]["text"] == all_buttons[1][1]["text"] == all_buttons[2][0]["text"]:
        return True, all_buttons[0][2]["text"]
    if all_buttons[0][0]["text"] == all_buttons[1][1]["text"] == all_buttons[2][2]["text"]:
        return True, all_buttons[0][0]["text"]
    return False, ""

def start_new_game(root_2): #начать новую игру
    root_2.destroy()
    global player_1, player_2, free_places
    free_places = 9
    winner = ""
    player_1, player_2 = player_2, player_1
    for r in range(3):
        for c in range(3):
            all_buttons[r][c]["text"] = ""
            all_buttons[r][c]["state"] = NORMAL

def game_over(): #игра завершена
    global winner
    root_2 = Tk()
    root_2.title("Игра окончена!")
    root_2.geometry("400x100+450+300")
    root_2["background"] = "floral white"
    winner_name = ""
    if winner == player_1:
        winner_name = "Вы победили!"
    elif winner == player_2:
        winner_name = "Компьютер победил!"
    else:
        winner_name = "Ничья"
    font2 = font.Font(root_2, family= "Verdana", size=13, weight="bold", slant="italic")
    label_1 = ttk.Label(root_2, text = f"{winner_name}", font = font2, background = "floral white")
    label_1.place(x = 120, y = 10, width = 300)
    label_2 = ttk.Label(root_2, text = f"Вы играли за {player_1}, теперь играете за {player_2}", font = font2, background = "floral white")
    label_2.place(x = 30, y = 40)
    btn_1 = Button(root_2, text = "Новая игра", command = lambda: start_new_game(root_2), background = "white", activebackground = "white")
    btn_1.place(x = 160, y = 70)
    
root = Tk()
root.title("Крестики-нолики")
root.geometry(f"320x300+500+200")
player_1 = "X" #игрок 1
player_2 = "O" #игрок 2
all_buttons = [[], [], []] #все кнопки
winner = "" #победитель
flag = False #для проверки возможности выигрыша в функции check_win
free_places = 9 #количество свободных мест на игровом поле
computer = False #проверка, сделал ли компьютер ход
    
for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)

for r in range(3):
    for c in range(3):
        btn = Button(text = "", command = lambda row = r, column = c: game(row, column), font = "Arial 14",
                     width = 106, background = "#F8F8FF", activebackground = "old lace")
        all_buttons[r].append(btn) 
        btn.grid(row = r, column = c, sticky = "nsew")        
    
root.mainloop()