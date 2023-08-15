import random
import math

player_num_lst = []
player_lst = []
card_list = []
init_score = 0
reveal = 0
no_str = "×"


def main():
    global player_num_lst
    global player_lst
    global card_list
    global reveal
    init_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '+', '=',
                 '/', '-', 'x', 'y', 'z']
    l = len(init_list)
    target_number = random.randint(-100,100)
    for i in range(l):
        ind = random.randint(0, len(init_list) - 1)
        card_list.append(init_list[ind])
        init_list.remove(init_list[ind])
    while True:
        player_amount = input('\033[1;32mPlease enter the number of the player: \033[0m')
        if player_amount.isdigit():
            if int(player_amount) > 4 or int(player_amount) < 2:
                print('\033[1;31m Error: the number you input out of is inappropriate\033[0m')
            else:
                break
        else:
            print('\033[1;31m TypeError: illegal format\033[0m')

    init_player_lst = []
    for i in range(int(player_amount)):
        player_num_lst.append(init_score)
    for i in range(int(player_amount)):
        init_player_lst.append(str(input(f'\033[1;35mEnter player {i + 1}: \033[0m')))

    for i in range(int(player_amount)):
        ind = random.randint(0, len(init_player_lst) - 1)
        player_lst.append(init_player_lst[ind])
        init_player_lst.remove(init_player_lst[ind])
    print(f'--------------------')
    print(f'\033[1;33mplayer turn:\033[0m')
    for i in range(int(player_amount)):
        print(f'{i + 1}: {player_lst[i]}')
    print(f"\033[1;35m{player_lst[0]}\033[0m\033[1;33m will have bonus round!\033[0m")
    print_table(l, card_list)
    for i in range(int(len(card_list)/int(player_amount))): # need one more round
        print(f"\033[1;35mRound\033[0m\033[1;33m {i+1}:\033[0m")
        for j in range(int(player_amount)):
            print(f"\033[1;33mIt's {player_lst[j]}'s turn:\033[0m")
            icon_identify(target_number, j)
            print_table(l, card_list)
            print_num()
            if reveal == 1:
                print(f"\033[1;33mtarget number: {target_number}\033[0m")
            else:
                print(f"\033[1;33mtarget number: ?\033[0m")
    print(f"\033[1;35mRound\033[0m\033[1;33m {int(len(card_list)/int(player_amount))+1}:\033[0m")
    for j in range(len(card_list) % int(player_amount)):
        print(f"\033[1;33mIt's {player_lst[j]}'s turn:\033[0m")
        icon_identify(target_number, j)
        print_table(l, card_list)
        print_num()
        if reveal == 1:
            print(f"\033[1;33mtarget number: {target_number}\033[0m")
        else:
            print(f"\033[1;33mtarget number: ?\033[0m")
    win_function(target_number)


def win_function(target_number):
    global player_num_lst
    global player_lst
    gap_lst = []
    sort_gap_lst = []
    player_rank = []
    repeat = []
    for i in range(int(len(player_lst))):
        gap_lst.append(abs(player_num_lst[i]-target_number))
    for j in range(int(len(player_lst))):
        sort_gap_lst.append(gap_lst[j])
    sort_gap_lst.sort()
    for k in range(len(player_num_lst)):
        tmp = sort_gap_lst[k]

        num = gap_lst.index(tmp)
        if tmp in repeat:
            print(f"\033[1;33m{player_rank.index(tmp)+1}. {player_lst[num]}\033[0m\033[1;37m: {player_num_lst[num]}\033[0m")
        else:
            print(f"\033[1;33m{len(player_rank)+1}. {player_lst[num]}\033[0m\033[1;37m: {player_num_lst[num]}\033[0m")
            repeat.append(tmp)
        gap_lst[num] = -1
        player_rank.append(tmp)


def print_table(l, card_list):
    global no_str
    print("\033[1;36mtable:\033[0m")
    print("\033[1;35m—————\033[0m" * int(math.sqrt(l)))
    for i in range(int(math.sqrt(l))):
        for j in range(int(math.sqrt(l))):
            if j == int(math.sqrt(l)) - 1:
                if card_list[i * int(math.sqrt(l)) + j] == no_str:
                    print(f"\033[1;35m| \033[0m\033[1;37m{card_list[i * int(math.sqrt(l)) + j]}\033[0m \033[1;35m|\033[0m")
                else:
                    print(f"\033[1;35m| \033[0m{card_list[i * int(math.sqrt(l)) + j]} \033[1;35m|\033[0m")
            else:
                if card_list[i * int(math.sqrt(l)) + j] == no_str:
                    print(f"\033[1;35m| \033[0m\033[1;37m{card_list[i * int(math.sqrt(l)) + j]}\033[0m ", end="")
                else:
                    print(f"\033[1;35m| \033[0m{card_list[i * int(math.sqrt(l)) + j]} ", end="")
        print("\033[1;35m—————\033[0m" * int(math.sqrt(l)))


def print_num():
    global player_num_lst
    global player_lst
    print("\033[1;36mnum:\033[0m")
    print("\033[1;36m—————\033[0m" * 5)
    for i in range(len(player_num_lst)):
        print(f"\033[1;35m{player_lst[i]}\033[0m:\033[1;37m{player_num_lst[i]}\033[0m")
    print("\033[1;36m—————\033[0m" * 5)


def icon_identify(target_num, round_player_index):
    global player_num_lst
    global reveal
    global card_list
    round_player_name = player_lst[round_player_index]
    while True:
        icon = input('\033[1;32mChoose the icon: \033[0m')
        if icon in card_list:
            if icon == '0':
                print(f'\033[1;33mYou got a 0\033[0m')
                print(f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '1':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 1
                    print(f'\033[1;33mYou got a -1\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 1
                    print(f'\033[1;33mYou got a +1\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '2':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 2
                    print(f'\033[1;33mYou got a -2\033[0m')
                    print(f'\033[1;33m{round_player_name}: {player_num_lst[round_player_index]}\033[0m')
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 2
                    print(f'\033[1;33mYou got a +2\033[0m')
                    print(f'\033[1;33m{round_player_name}: {player_num_lst[round_player_index]}\033[0m')
            elif icon == '3':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 3
                    print(f'\033[1;33mYou got a -3\033[0m')
                    print(f'\033[1;33m{round_player_name}: {player_num_lst[round_player_index]}\033[0m')
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 3
                    print(f'\033[1;33mYou got a +3\033[0m')
                    print(f'\033[1;33m{round_player_name}: {player_num_lst[round_player_index]}\033[0m')
            elif icon == '4':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 4
                    print(f'\033[1;33mYou got a -4\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 4
                    print(f'\033[1;33mYou got a +4\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '5':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 5
                    print(f'\033[1;33mYou got a -5\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 5
                    print(f'\033[1;33mYou got a +5\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '6':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 6
                    print(f'\033[1;33mYou got a -6\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 6
                    print(f'\033[1;33mYou got a +6\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '7':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 7
                    print(f'\033[1;33mYou got a -7\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 7
                    print(f'\033[1;33mYou got a +7\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '8':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 8
                    print(f'\033[1;33mYou got a -8\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 8
                    print(f'\033[1;33mYou got a +8\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '9':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 9
                    print(f'\033[1;33mYou got a -9\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 9
                    print(f'\033[1;33mYou got a +9\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '!':
                num = random.randint(0, 1)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] - 10
                    print(f'\033[1;33mYou got a -10\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] + 10
                    print(f'\033[1;33mYou got a +10\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '@':
                while True:
                    player_name = input(f'\033[1;33mWhich opponent’s number you want to change:\033[0m')
                    if player_name in player_lst:
                        break
                    else:
                        print(f'\033[1;31m TypeError: {player_name}_not_found\033[0m')
                ind = player_lst.index(player_name)
                tmp = player_num_lst[ind]
                player_num_lst[ind] = player_num_lst[round_player_index]
                player_num_lst[round_player_index] = tmp
            elif icon == '#':
                print(
                    f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '$':
                print(
                    f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                print(f'\033[1;33mAttention!\033[0m')
                print(f'\033[1;33m{round_player_name} announced the target number\033[0m')
                reveal = 1
                print(f'\033[1;33mThe target number is {target_num}\033[0m')
            elif icon == '%':
                num = random.randint(0, 3)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] % 2
                    print(f'\033[1;33mYou got a %2\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] % 3
                    print(f'\033[1;33mYou got a %3\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 2:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] % 5
                    print(f'\033[1;33mYou got a %5\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 3:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] % 10
                    print(f'\033[1;33mYou got a %10\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '^':
                num = random.randint(0,2)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] * player_num_lst[
                        round_player_index]
                    print(f'\033[1;33mYou got a ^2\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    print(f'\033[1;33mYou got a ^1\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 2:
                    tmp1 = int(math.sqrt(abs(player_num_lst[round_player_index])))
                    if player_num_lst[round_player_index] < 0:
                        player_num_lst[round_player_index] = tmp1*(-1)
                    elif player_num_lst[round_player_index] == 0:
                        player_num_lst[round_player_index] = 0
                    else:
                        player_num_lst[round_player_index] = tmp1
                    print(f'\033[1;33mYou got a ^0.5\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '&':
                num = random.randint(0, 3)
                ran_num = random.randint(1, 10)
                if num == 0:
                    player_num_lst[round_player_index] = ran_num + 1 + player_num_lst[round_player_index]
                    print(f'\033[1;33mYou got a &1\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = ran_num + 2 + player_num_lst[round_player_index]
                    print(f'\033[1;33mYou got a &2\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 2:
                    player_num_lst[round_player_index] = -ran_num - 1 + player_num_lst[round_player_index]
                    print(f'\033[1;33mYou got a &(-1)\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 3:
                    player_num_lst[round_player_index] = -ran_num - 2 + player_num_lst[round_player_index]
                    print(f'\033[1;33mYou got a &(-2)\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '*':
                num = random.randint(0, 5)
                if num == 0:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] * 2
                    print(f'\033[1;33mYou got a *2\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 1:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] * 1
                    print(f'\033[1;33mYou got a *1\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 2:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] * (-2)
                    print(f'\033[1;33mYou got a *(-2)\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 3:
                    player_num_lst[round_player_index] = player_num_lst[round_player_index] * (-1)
                    print(f'\033[1;33mYou got a *(-1)\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 4:
                    player_num_lst[round_player_index] = int(player_num_lst[round_player_index] * 0.5)
                    print(f'\033[1;33mYou got a *0.5\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
                elif num == 5:
                    player_num_lst[round_player_index] = int(player_num_lst[round_player_index] * (-0.5))
                    print(f'\033[1;33mYou got a *(-0.5)\033[0m')
                    print(
                        f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '+':
                num = random.randint(1, 10)
                player_num_lst[round_player_index] = player_num_lst[round_player_index] + num
                print(f'\033[1;33mYou got a +{num}\033[0m')
                print(
                    f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '=':
                while True:
                    player_name = input(f'\033[1;33mWhich opponent’s number you want to divide: \033[0m')
                    if player_name in player_lst:
                        if player_name == round_player_name:
                            print(f'\033[1;31m NerdError: {player_name} is literally U, u noob\033[0m')
                        else:
                            break
                    else:
                        print(f'\033[1;31m TypeError: {player_name}_not_found\033[0m')
                average = int((player_num_lst[round_player_index]+player_num_lst[player_lst.index(player_name)])/2)
                player_num_lst[round_player_index] = average
                player_num_lst[player_lst.index(player_name)] = average
                print(
                    f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '/':
                num = random.randint(1, 10)
                player_num_lst[round_player_index] = int(player_num_lst[round_player_index] / num)
                print(f'\033[1;33mYou got a /{num}\033[0m')
                print(
                    f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == '-':
                num = random.randint(1, 10)
                player_num_lst[round_player_index] = player_num_lst[round_player_index] - num
                print(f'\033[1;33mYou got a -{num}\033[0m')
                print(
                    f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == 'x':
                while True:
                    str = input(f'\033[1;33mHow much u wanna adjust: \033[0m')
                    if str[0] == "+":
                        if str[1:].isdigit():
                            if int(str[1:]) > 10:
                                print(f'\033[1;31m TypeError: out of range\033[0m')
                            else:
                                player_num_lst[player_lst.index(round_player_name)] += int(str[1:])
                                break
                        else:
                            print(f'\033[1;31m TypeError: illegal format\033[0m')
                    elif str[0] == "-":
                        if str[1:].isdigit():
                            if int(str[1:]) > 10:
                                print(f'\033[1;31m TypeError: out of range\033[0m')
                            else:
                                player_num_lst[player_lst.index(round_player_name)] -= int(str[1:])
                                break
                        else:
                            print(f'\033[1;31m TypeError: illegal format\033[0m')
                    else:
                        print(f'\033[1;31m TypeError: illegal format\033[0m')
                print(
                    f"\033[1;35m{round_player_name}'s number\033[0m\033[1;37m: {player_num_lst[round_player_index]}\033[0m")
            elif icon == 'y':
                while True:
                    player_name = input(f'\033[1;33mWhich opponent’s number you want to adjust: \033[0m')
                    if player_name in player_lst:
                        if player_name == round_player_name:
                            print(f'\033[1;31m NerdError: u should use x instead of y \033[1;37mQAQ\033[0m')
                        else:
                            break
                    else:
                        print(f'\033[1;31m TypeError: {player_name}_not_found\033[0m')
                while True:
                    str = input(f'\033[1;33mHow much u wanna adjust: \033[0m')
                    if str[0] == "+":
                        if str[1:].isdigit():
                            if int(str[1:])>10:
                                print(f'\033[1;31m TypeError: out of range\033[0m')
                            else:
                                player_num_lst[player_lst.index(player_name)] += int(str[1:])
                                break
                        else:
                            print(f'\033[1;31m TypeError: illegal format\033[0m')
                    elif str[0] == "-":
                        if str[1:].isdigit():
                            if int(str[1:]) > 10:
                                print(f'\033[1;31m TypeError: out of range\033[0m')
                            else:
                                player_num_lst[player_lst.index(player_name)] -= int(str[1:])
                                break
                        else:
                            print(f'\033[1;31m TypeError: illegal format\033[0m')
                    else:
                        print(f'\033[1;31m TypeError: illegal format\033[0m')
                print(
                    f"\033[1;35m{player_name}'s number\033[0m\033[1;37m: {player_num_lst[player_lst.index(player_name)]}\033[0m")
                print(f'\033[1;35madjustion done !\033[0m')

            elif icon == 'z':
                while True:
                    player_name = input(f'\033[1;33mWhich opponent’s number you want to adjust: \033[0m')
                    if player_name in player_lst:
                        break
                    else:
                        print(f'\033[1;31m TypeError: {player_name}_not_found\033[0m')
                while True:
                    str = input(f'\033[1;33mHow much u wanna adjust: \033[0m')
                    if str[0] == "+":
                        if str[1:].isdigit():
                            if int(str[1:]) > 10:
                                print(f'\033[1;31m TypeError: out of range\033[0m')
                            else:
                                player_num_lst[player_lst.index(player_name)] += int(str[1:])
                                break
                        else:
                            print(f'\033[1;31m TypeError: illegal format\033[0m')
                    elif str[0] == "-":
                        if str[1:].isdigit():
                            if int(str[1:]) > 10:
                                print(f'\033[1;31m TypeError: out of range\033[0m')
                            else:
                                player_num_lst[player_lst.index(player_name)] -= int(str[1:])
                                break
                        else:
                            print(f'\033[1;31m TypeError: illegal format\033[0m')
                    else:
                        print(f'\033[1;31m TypeError: illegal format\033[0m')
                print(
                    f"\033[1;35m{player_name}'s number\033[0m\033[1;37m: {player_num_lst[player_lst.index(player_name)]}\033[0m")
                print(f'\033[1;35madjustion done !\033[0m')
            ind = card_list.index(icon)
            card_list[ind] = no_str
            break
        elif icon == no_str:
            print('\033[1;31m NoobError: what are u doing :<\033[0m')
        else:
            print('\033[1;31m TypeError: illegal format\033[0m')


if __name__ == '__main__':
    main()