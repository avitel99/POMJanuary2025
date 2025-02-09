import random
import sys
with open("google-10000-english-usa-no-swears.txt", "r") as file:
    content = file.read()
    wordlist=content.split()
score = 0
mon = 0
life = 5
def intro():
    print('Welcome to the Hangman Game! Please enter your name:')
    name = input()
    print('Hello ', name, ' ! ',
          'The goal of the game is to guess as many words as possible before running out of lives. You will'
          ' start with 5 lives. The game will end once you reach 0 lives. You can buy more lives for $7 '
          'each. You currently have 0$. You can make more money by solving math problems. To start the '
          'game type start. To get more money type money. If you want to buy more lives, type buy.'
          , sep='')
    options = ['money', 'start', 'buy']
    choice = input()
    while choice not in options:
        print('That is not a valid choice. Write money to gain money or write start to start the game.')
        choice = input()
    if choice == 'money':
        money()
    elif choice == 'start':
        game()
    else:
        buy()
def money():
    global mon
    print(
        'Money can be used to buy lives. You can gain $1 for every arithmetics problem that you solve or $3 for every '
        'algebra problem. Careful, any wrong answer will cost you $2. If you want to solve arithmetic problems, type '
        'arithmetic. If you want to solve algebra problems, type algebra, to go back, type back.')
    options = ['back', 'arithmetic', 'algebra']
    choice = input()
    while choice not in options:
        print('That is not a valid choice. If you want to solve arithmetic problems, type arithmetic. If you want to '
              'solve algebra problems, type algebra, to go back, type back.')
        choice = input()
    if choice == 'back':
        print('Would you like to buy lives, start the game, or earn money? To start the game, type start. To get more '
              'money type money. If you want to buy more lives, type buy.')
        options = ['money', 'start', 'buy']
        choice = input()
        while choice not in options:
            print('That is not a valid choice. Write money to gain money or write start to start the game.')
            choice = input()
        if choice == 'money':
            money()
        elif choice == 'start':
            game()
        else:
            buy()
    elif choice == 'algebra':
        print('type stop to exit.')
        while True:
            a = algebra()
            if a == 0:
                money()
            else:
                mon +=a
    else:
        print('type stop to exit.')
        while True:
            a = arithmetics()
            if a == 0:
                money()
            else:
                mon +=a
def arithmetics():
    operations = ['+', '-', '*', '/']
    n = random.randint(0, 3)
    if n == 0 or n == 1:
        a = random.randint(0, 10000)
        b = random.randint(0, 10000)
    elif n == 2:
        a = random.randint(0, 99)
        b = random.randint(0, 99)
    else:
        b = random.randint(1, 50)
        a = b * random.randint(0, 20)
    print('What is', a, operations[n], b, '?')
    while True:
        try:
            ans = int(input())
            break
        except ValueError:
            print('Would you like to exit? yes or no?')
            x = input()
            if x == 'yes':
                return 0
            else:
                print('Then please enter a valid answer')
    if ans == eval(f'{a} {operations[n]} {b}'):
        print('Correct! +$1')
        return 1
    else:
        print('The correct answer is:',eval(f'{a} {operations[n]} {b}'),'.-$2')
        return -1
def algebra():
    global mon
    x1 = x2 = 0
    while x2 == x1 or x1 * x2 == 0:
        x1 = random.randint(-20, 20)
        x2 = random.randint(-20, 20)
    sign = ['+', '-']
    print('Solve the following polynomial:')
    print('find both roots (write them in one line, separated by a space)')
    if -x1 - x2 > 0 and x1 * x2 > 0:
        print('x²+', - x1 - x2, 'x+', x1 * x2, sep='')
    elif -x1 - x2 > 0 and x1 * x2 < 0:
        print('x²+', -x1 - x2, 'x', x1 * x2, sep='')
    elif -x1 - x2 < 0 and x1 * x2 > 0:
        print('x²', -x1 - x2, 'x+', x1 * x2, sep='')
    else:
        print('x²', -x1 - x2, 'x', x1 * x2, sep='')
    while True:
        try:
            a1, a2 = map(int, input().split())
            break
        except ValueError:
            print('Would you like to exit? yes or no?')
            x = input()
            if x == 'yes':
                return 0
            else:
                print('Then please enter a valid answer')
    if a1 == x1 and a2 == x2 or a1 == x2 and a2 == x1:
        print('That is correct, +$3!')
        return 3
    else:
        print('the correct answer is:', x1, x2,'-$2')
        return -2
def buy():
    global mon,life
    print('You currently have',life,'lives and $',mon,'.A life costs $7. Would you like to buy another life (type yes'
                                                      ' or no)?')
    options = ['yes','no']
    choice = input()
    while choice not in options:
        print('That is not a valid choice. Would you like to buy another life (type yes or no)?')
        choice = input()
    if choice == 'yes':
        if mon>=7:
            mon-=7
            life+=1
            print('+1 life.')
        else:
            print('You do not have enough money.')
        buy()
    else:
        print('Would you like to buy lives, start the game, or earn money? To start the game, type start. To get more '
              'money type money. If you want to buy more lives, type buy')
        options = ['money', 'start', 'buy']
        choice = input()
        while choice not in options:
            print('That is not a valid choice. Write money to gain money or write start to start the game.')
            choice = input()
        if choice == 'money':
            money()
        elif choice == 'start':
            game()
        else:
            buy()
def game():
    global life
    alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w',
           'x', 'y', 'z']
    while True:
        word = list(wordlist[random.randint(0, len(wordlist) - 1)])
        ans = ['_' for _ in range(len(word))]
        while life != 0 and ans != word:
            print(*ans)
            u = input()
            if alf.count(u) == 0:
                print('You already said that!')
            elif word.count(u) != 0:
                print('Correct!')
                for i in range(len(word)):
                    if word[i] == u:
                        ans[i] = u
                alf.pop(alf.index(u))
            else:
                life -= 1
                print('That is incorrect! Lives:', life * '♡')
                alf.pop(alf.index(u))
        if life == 0:
            print('You have 0 lives left, the word was: ', *word, ' Thank you for playing.',sep='')
            sys.exit()
        else:
            print(*ans)
            print('You win! +1 point. Would you like to play again (type play), buy more lives (type buy), or earn money'
                  ' (type money)?')
            options = ['money', 'play', 'buy']
            choice = input()
            while choice not in options:
                print('That is not a valid choice. would you like to play again (type play), buy more lives (type buy),'
                      ' or earn money (type money)?')
                choice = input()
            if choice == 'money':
                money()
            elif choice == 'play':
                game()
            else:
                buy()

intro()
