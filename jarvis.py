import sys
import requests
import json
import apis

def square(n):
    """ Square numbers

    >>> square(2)
    4
    >>> square(3)
    8
    """
    return n*n

def dispatcher(command, arg):
    """Checks implements command and then reprompts the user. If command is weather, dispatcher
    prints weather forcast for arg. If command is square dispatcher prints the
    arg and square of arg. If command is go away it exits dispatcher function with
    a passive aggressive goodbye message. If command is bye exits with pleasant farewell."""
    if command == "weather":
        print("Here's the weather forcast for "+arg)
        print(apis.fetch_weather(arg))
    if command == "square":
        print("The square of " + arg + " is " + str(square(int(arg))))
    elif command == "go away":
        print("It sounds like you no longer need my assistance")
        print("Very well. Goodbye!")
        return
    elif command == "bye":
        print("Goodbye! Have a good day!")
        return
    # Reprompt the user.
    prompter()


def prompter():
    """ asks for things """

    command = (input("How may I help you?: [weather, square, go away, bye]")).lower()
    if command == "weather":
        city = input("Sure thing! What city?")
        dispatcher(command, city)
    if command == "square":
        num = input("I love math! What number?")
        dispatcher(command, num)
    elif command == "stocks": # TODO
        pass
    else:
        dispatcher(command, "")

def starter(cliargs):
    # TODO: Finish up command line interface
    print("DEBUG: Called with ", cliargs[1:])

    print("Summoning Jarvis")
    print("Good evening!")

    if (len(cliargs) > 1):
        command = cliargs[1]
        arg = cliargs[2]
        # TODO: Call dispatcher with args instead of prompting user.
        dispatcher(command, arg)
    else:
        prompter()

#this is a comment
def dance():
    """Every personal assistant should know how to dance!"""
    print("left right chachacha left right chacha\n left left right right dip up chachacha")
    return

if __name__ == "__main__":
    starter(sys.argv)
