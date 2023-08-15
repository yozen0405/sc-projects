"""
File: game1.py
Name:Albert
--------------------------
This program shows what a gamble
"""
import random
ENTER_TURN = 3
MAGNIFICATION = [15, 7, 3]
A_COIN = 100
B_COIN = 100


def main():
    print('幸運high翻天 !')
    print('Initial coin : ', 'A COIN:', A_COIN, '    B COIN:', B_COIN)
    color = ans_str_give('', False)
    print('The card : ', color_print(color[2]), ' 1,2,3,4,5,6,7,8,9,10,11,12,13\033[0m')
    turn = random.randint(1,2)
    if turn == 1:
        turn = 'a'
    else:
        turn = 'b'
    a_dict = []
    b_dict = []
    card_lst = add_card()
    a_coin = A_COIN
    b_coin = B_COIN
    round_num = 1
    while True:
        print('-'*20, 'Round',round_num,'-'*20)
        for i in range(2):
            if turn == 'a':
                print('\033[1;35mTurn A !\033[0m')
                a_dict = turn_input(a_coin)
                for key in a_dict:
                    a_coin -= a_dict[key]
                turn = 'b'
            else:
                print('\033[1;36mTurn B !\033[0m')
                b_dict = turn_input(b_coin)
                for key in b_dict:
                    b_coin -= b_dict[key]
                turn = 'a'
        while True:
            ans_num = random.randint(1,13)
            ans_str = ans_str_give(color[2],True)
            if ans_str + str(ans_num) in card_lst:
                card_lst.remove(ans_str + str(ans_num))
                break
        coin_lst = detect(a_dict,b_dict,ans_str[1],ans_num,color[1])
        a_coin += coin_lst[0]
        b_coin += coin_lst[1]
        print('The ans is: ', color_print(ans_str[2]),ans_num)
        print(f'\033[1;35mA$ : {a_coin} \033[0m, \033[1;36mB$ : {b_coin}\033[0m')
        if card_lst is None:
            break
        break_s = str(input('over ?(press enter directly) : '))
        if break_s != '':
            break
        round_num += 1
    print('-' * 20, 'RESULT', '-' * 20)
    if a_coin > b_coin:
        print('\033[1;35mA win !\033[0m')
    elif b_coin > a_coin:
        print('\033[1;36mB win !\033[0m')
    else:
        print('\033[1;33mEven !\033[0m')
    print(f'\033[1;35mA$ : {a_coin} \033[0m, \033[1;36mB$ : {b_coin}\033[0m')


def color_print(color):
    if color == '1':
        return '♣'
    if color == '2':
        return '♠'
    if color == '3':
        return '\033[1;31m♥\033[0m'
    if color == '4':
        return '\033[1;31m♦\033[0m'


def add_card():
    lst = []
    for j in range(1,5):
        for i in range(1,14):
            if j == 1:
                lst.append('♣b1'+str(i))
            elif j == 2:
                lst.append('♠b2'+str(i))
            elif j == 3:
                lst.append('♥r3'+str(i))
            elif j == 4:
                lst.append('♦r4'+str(i))
    return lst


def turn_input(coin):
    dict = {}
    total = 0
    i = 0
    while i != ENTER_TURN:
        num = str(input('chose from 1~13(or 100 to quit) :'))
        if num.isdigit():
            if int(num) <= 13 or int(num) == 100:
                num = int(num)
                if num not in dict:
                    if num == 100:
                        return dict
                    else:
                        bet_money = str(input('input the money you want to bet :'))
                        while not bet_money.isdigit():
                            print('\033[1;31m TypeError: illegal format\033[0m')
                            bet_money = str(input('input the money you want to bet :'))
                        bet_money = int(bet_money)
                        while bet_money + total > coin:
                            print('\033[1;31m VariableError: no enough money !\033[0m')
                            bet_money = int(input('input the money you want to bet :'))
                        dict[num] = bet_money
                        total += bet_money
                        i += 1

                else:
                    print('\033[1;31m ChosenError: you already choose before\033[0m')
            else:
                print('\033[1;31m IndexError: the number you input out of range\033[0m')
        else:
            print('\033[1;31m TypeError: illegal format\033[0m')
    return dict


def ans_str_give(s,limit):
    ans = random.randint(1,4)
    while limit:
        ans = random.randint(1,4)
        if ans != int(s):
            limit = False
    if ans == 1:
        return '♣b1'
    elif ans == 2:
        return '♠b2'
    elif ans == 3:
        return '♥r3'
    elif ans == 4:
        return '♦r4'


def detect(a,b,ans_str,ans_num,current_color):
    a_coin = 0
    b_coin = 0
    if ans_num == 13:
        lst = [13,12]
    elif ans_num == 1:
        lst = [1,2]
    else:
        lst = [ans_num,ans_num-1,ans_num+1]
    for i in range(len(lst)):
        for int in a:
            if int == lst[i]:
                if i == 0:
                    if current_color == ans_str:
                        a_coin += a[int]*MAGNIFICATION[0]
                    else:
                        a_coin += a[int]*MAGNIFICATION[1]
                else:
                    a_coin += a[int]*MAGNIFICATION[2]
        for int in b:
            if int == lst[i]:
                if i == 0:
                    if current_color == ans_str:
                        b_coin += b[int]*MAGNIFICATION[0]
                    else:
                        b_coin +=b[int]*MAGNIFICATION[1]
                else:
                    b_coin += b[int]*MAGNIFICATION[2]
    return [a_coin,b_coin]


if __name__ == '__main__':
    main()