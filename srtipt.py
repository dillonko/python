#!/usr/bin/python

# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?

my_int = 7

# Change the value of my_int to 3 on line 8!

my_int = 3

# Here's some code that will print my_int to the console:
# The print keyword will be covered in detail soon!

print my_int


============== new script===============
# meal.py

# Assign the variable total on line 8!

meal = 44.50
tax  = 0.0675
tip  = 0.15

meal  = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)

======================== new script========
# string01.py

# Assign your variables below, each on its own line!
caesar  = "Graham"
praline = "John"
viking  = "Teresa"


# Put your variables above this line

print caesar
print praline
print viking

==================== new script ======================

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
WORD = "MONTY"
fifth_letter = WORD [4]

print fifth_letter

================ new script ========================

parrot = "Norwegian Blue"
len(parrot)

print len(parrot)

===================== new script ======================

parrot = "norwegian blue"

print parrot.upper()

=================== new script ========================
parrot = "norwegian blue"

print parrot.lower()

=================== new script =========================

"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)

=================== new script =========================

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

=================== new script =========================

"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print the_machine_goes

=================== new script =========================

# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)

=================== new script =========================

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

=================== new script =========================

name  = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s " \
"and your favorite color is %s." % (name, quest, color)

=================== new script =========================

# Write your code below, starting on line 3!

my_string = "fuck you"
print len(my_string)
print my_string.upper()

=================== new script =========================

from datetime import datetime

now = datetime.now()
print str(now.month) +"/"+ str(now.day) +"/" + str(now.year) +" "+ str(now.hour) +":"+ str(now.minute) +":" + str(now.second)

=================== new script =========================
# this is a poker game
# Simple Blackjack game
# From Dillon by Dillon

from random import randint
from sys import exit
from time import sleep

# player starts with money
p_cash = 15

# randomly create a new card
class NewCard(object):
    def __init__(self):
        # card can be between 2 and 14
        self.value = randint(2,14)
        # Assign the card key based on its value (A = 11, J = 12, Q = 13, K = 14)
        if self.value == 11:
            self.key = 'A'
        elif self.value == 12:
            self.key = 'J'
        elif self.value == 13:
            self.key = 'Q'
        elif self.value == 14:
            self.key = 'K'
        else:
            self.key = self.value
        # make the value of Jacks, Queens, and Kings 10
        if self.value > 11:
            self.value = 10
        #TODO: make Aces 1 or 11

# Tell the player their cards
def print_p_cards():
    print('Player: {0}: {1}'.format(p_total, p_cards))

# Tell the player the dealer's cards
def print_d_cards():
    print('Dealer: {0}: {1}'.format(d_total, d_cards))

# starts a new game
def deal():

    sleep(1)
    p_bet = 0
    # initial bet starts above maximum
    if p_cash > 0:
        while (p_bet > 20) or (p_bet < 1):
            print('This table has a $1 minimum and $20 maximum')
            p_bet = input("You have ${0}. Enter your bet or press (q) to quit $".format(p_cash))
            #TODO: check if empty
            if p_bet[0] == 'q':
                print("Thanks for visiting Luke's Casino. Enjoy your ${0}!".format(p_cash))
                exit()
            else:
                try:
                    p_bet = float(p_bet)
                except:
                    print('Bet must be a dollar amount')
                    p_bet = 0
            if p_bet > p_cash:
                p_bet = 0
                print("You don't have that much!")
    else:
        print('You have run out of money. Get out of here, bum!')
        exit()

    # dealer's hand
    global d_card1
    global d_card2
    global d_total
    global d_cards
    d_card1 = NewCard()
    d_card2 = NewCard()
    d_total = (d_card1.value + d_card2.value)
    d_cards = [str(d_card1.key), str(d_card2.key)]
    # player's hand
    global p_card1
    global p_card2
    global p_total
    global p_cards
    p_card1 = NewCard()
    p_card2 = NewCard()
    p_total = (p_card1.value + p_card2.value)
    p_cards = [str(p_card1.key), str(p_card2.key)]
    # tell the player the cards
    print("\nLet's go")
    if d_total == 21:
        print_d_cards()
    else:
        print("Dealer: {0}: ['{1}', '?']".format(d_card1.value, d_card1.key))

    print_p_cards()
    #TODO: add insurance option if dealer shows Ace
    # check for blackjack on initial deal
    if d_total == 21 and p_total == 21:
        print('You both have Blackjack! Tie!')
        deal()
    elif d_total == 21 and p_total != 21:
        print('Dealer has Blackjack! You lost ${0}!\n'.format(p_bet))
        p_cash -= p_bet
        deal()
    elif d_total != 21 and p_total == 21:
        print('Blackjack! You won ${0}!\n'.format(p_bet * 1.5))
        p_cash += p_bet * 1.5
        deal()
    else:
        while p_total <= 21:
            p_act = str(input('\nWould you like to (h)it or (s)tand? '))
            #TODO: add split and double
            if (p_act[0] == 's') or (p_total == 21):
                print_p_cards()
                print_d_cards()

                while d_total < 17:
                    d_new_card = NewCard()
                    d_total += d_new_card.value
                    d_cards.append(str(d_new_card.key))
                    sleep(1)
                    print('The dealer hits')
                    print_d_cards()

                global p_cash
                if p_total == d_total:
                    print('Tie!\n')
                elif p_total < d_total and d_total <= 21:
                    print('You lost ${0}!\n'.format(p_bet))
                    p_cash -= p_bet
                else:
                    print('You won ${0}!\n'.format(p_bet))
                    p_cash += p_bet
                deal()
            elif p_act[0] == 'h':
                p_new_card = NewCard()
                p_total += p_new_card.value
                p_cards.append(str(p_new_card.key))
                print_p_cards()

        print('Bust! You lost ${0}!\n'.format(p_bet))
        p_cash -= p_bet
        deal()

# opening statement
print("Welcome please sit at the blackjack table.")
deal()

=================== new script =========================

import this
love = "love"
what = this
this = love
love = this
raw_input = "a pity?"
love != "this"
it = "real"
inlove = "islands in the sky"
fools = "them, and now you are one of them"
reality=39
inlove=str(inlove)[0:2]
fools=str(fools[0:3])+str(fools[7])
meaning=3
it_=str(raw_input)[3:5]
life=str(meaning + reality)
print fools+" "+it_+" "+inlove+" "+"true"+" - "
print "The meaning of life is "+life


=================== new script =========================

#!/usr/bin/python
 
import web
 
urls = ('/(.*)', 'hello')
app = web.application(urls, globals())
 
class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'
 
if __name__ == "__main__":
    app.run()


=================== new script =========================

from BaseHTTPServer  import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path=self.path
        print path
        ans=path
        self.wfile.write(ans)
        return

    def log_request(self, code=None, size=None):
        print('Request')

    def log_message(self, format, *args):
        print('Message')

if __name__ == "__main__":
    try:
        server = HTTPServer(("0.0.0.0", 8000), MyHandler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        print(' received, shutting down server')

=================== new script =========================

print "Hello this is a piglatin word translater."
print "Please enter a valid word."
print "  "
ans = raw_input("what word would you like to use? ")
if ans.isalpha() == True:
  print "this is not a word please try again"
elif ans.isalpha() == False:
  print "you typed a word thats so great."

=================== new script =========================

def pyglatin():
  print "  "
  print "Hello this is a piglatin word translater."
  print "Please enter a valid word."
  print "  "
  ans = raw_input("what word would you like to use? ")
  if ans.isalpha() and ans > 1:
    a = ans[0:1]
    b = ans + a + "ay"
    print a
  else:
    print "Thats not a word"

pyglatin()  

=================== new script =========================

#!/usr/bin/python

#pyglatin game

def pyglatin():
  print "Welcome to the English to Pig Latin translator!"
  print "Please enter a valid word."
  print "  "
  original = raw_input("what word would you like to use? ")
  if original.isalpha() and original > 1:
    a = original[0:1]
    b = original + a + "ay"
    c = b[1:len(b)]
    print c
  else:
    print "Thats not a word"

pyglatin()  

=================== new script =========================
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
========================================================

=================== new script =========================
original = raw_input('Enter a word:')
word  = original.lower()
first = original[0]

if condition:
    if other_condition:
        # Do something
    else:
        # Do something else!
else:
    # Do yet another thing
=================== new script =========================

def shut_down():
    s = input('would you like to shutdown?')
    if s = "Yes" or "YES" or "yes" or "y" or "Y":
        print("Shutting down...")
    elif s = "No" or "no" or "NO" or "n" or "N":
        print("Shutdown aborted!")
    else:
        print("Sorry, I didn't understand you.")
        return shut_down()

shut_down()

=================== new script =========================
=================== new script =========================
=================== new script =========================
=================== new script =========================
