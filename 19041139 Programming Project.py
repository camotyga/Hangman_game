#Oghenetega Emagha Programming Project
import random
import turtle

#shows the parameters for the turtle console
t = turtle.Turtle()
t.pen(pensize = 5, speed = 10)
turtle.Screen().bgcolor("yellow")
turtle.title("19041139 4COM1037-0206 Programming Project")


def hangman():
    list_of_words = ["tutorial","video","programming","python","codingDeveloper","computer","laptop","studying","javascript","keyboard","phone","television","books","bookshelf","processses","linux","unbuntu","science","scientist","cryptography","hacking","mathematics","brain"]
    word = random.choice(list_of_words)
    turns = 8
    guessmade = ""
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")
    
#shows the result of what happens when a the guessed letter is a part of the word to guess
    while len(word)>0:
        main_word = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

#congratulates the player for correctly guesing the word
        if main_word == word:
            print(main_word)
            print("Congratulations!!! The word was", word, "!")
            break

        print("guess the word", main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("Invalid charcter! Try again:")
            guess = input()
            
#if the letter guessed is not in the word however, a piece of the ambulance is drawn for each incorrect guess
        if guess not in word:
            turns  = turns - 1

            if turns == 7:
                print("7 turns left!")
                print("_ _ _ _ _ _ _")
                t.pencolor("blue")
                t.fillcolor("white")
                t.begin_fill()
                t.penup()
                t.goto(-205,-75)
                t.pendown()
                t.forward(300)
                t.left(90)
                t.forward(200)
                t.left(90)
                t.forward(300)
                t.left(90)
                t.forward(200)
                t.left(90)
                t.penup()
                t.end_fill()
            if turns == 6:
                print("6 turns left!")
                print("_ _ _ _ _ _ _")
                t.begin_fill()
                t.penup()
                t.goto(95,-75)
                t.pendown()
                t.forward(150)
                t.left(90)
                t.forward(150)
                t.left(90)
                t.forward(150)
                t.left(90)
                t.forward(150)
                t.left(360)
                t.penup()
                t.end_fill()
            if turns == 5:
                print("5 turns left!")
                print("_ _ _ _ _ _ _")
                t.color("blue")
                t.begin_fill()
                t.penup()
                t.goto(-175, -75)
                t.pendown()
                t.circle(40)
                t.penup()
                t.end_fill()
            if turns == 4:
                print("4 turns left!")
                print("_ _ _ _ _ _ _")
                t.color("blue")
                t.begin_fill()
                t.penup()
                t.goto(75, -75)
                t.pendown()
                t.circle(40)
                t.left(90)
                t.penup()
                t.end_fill()
            if turns == 3:
                print("3 turns left!")
                print("_ _ _ _ _ _ _")
                t.pencolor("blue")
                t.fillcolor("white")
                t.begin_fill()
                t.goto(120,10)
                t.pendown()
                t.forward(75)
                t.left(90)
                t.forward(45)
                t.left(90)
                t.forward(75)
                t.left(90)
                t.forward(45)
                t.left(90)
                t.penup()
                t.end_fill()
            if turns == 2:
                print("2 turns left!")
                print("_ _ _ _ _ _ _")
                t.pencolor("blue")
                t.fillcolor("red")
                t.begin_fill()
                t.goto(-75,125)
                t.pendown()
                t.forward(40)
                t.left(90)
                t.forward(20)
                t.left(90)
                t.forward(40)
                t.left(90)
                t.forward(20)
                t.penup()
                t.end_fill()
            if turns == 1:
                print("1 turns left! Be careful!")
                print("_ _ _ _ _ _ _")
                t.color("red")
                t.begin_fill()
                t.goto(-75,95)
                t.pendown()
                t.forward(90)
                t.left(90)
                t.forward(40)
                t.left(90)
                t.forward(90)
                t.left(90)
                t.forward(40)
                t.left(180)
                t.penup()
                t.end_fill()

#when the number of turns reaches 0, th amblance is completed and the players game is over
            if turns == 0:
                t.color("red")
                t.begin_fill()
                t.goto(-98.75,68.75)
                t.pendown()
                t.forward(90)
                t.right(90)
                t.forward(40)
                t.right(90)
                t.forward(90)
                t.right(90)
                t.forward(40)
                t.right(90)
                t.penup()
                t.end_fill()
                t.color("green")
                style = ("Courier",45,"bold")
                t.goto(200,200)
                t.write("Game Over :( ", font = style, align = "right")
                t.hideturtle()
                print("Game over :(")
                print("The word was", word)
                break
                
                
                
                

#intro, asks the player to intoduce themselves and welcomes them to the game
intro = input("Welcome player! What is your name?")
name = intro.upper()
print("Hello", name, "!")
print("_ _ _ _ _ _ _ _ _")
print("You have 8 attempts to guess the word")
hangman()

