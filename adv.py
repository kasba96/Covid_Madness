print("Hello World")

affirm = ["yes", "yeah", "yee", "y"]
negate = ["no", "nope", "n", "nah bro", "nah"]
inventory = []

def begin():
    '''Prints the welcome message'''

    print("Welcome to Covid Madness")

# OUTCOMES



def pass_out(why):
    '''In: Passing in the string showing player why they passed out.

    Result:
    Prints message telling player they passed out and why.'''

    print(f"You passed out. {why} rip")
    exit()

# ROOMS
def kitchen_adv():
    '''Actions in kitchen.'''

    print("You walk into the kitchen and go to heat up some water in the ")
    print("microwave. The microwave clock shows 5 pm. You could have sworn")
    print("that your last memory of being awake was around this time.")

def bedroom_adv():
    '''Actions in bedroom.'''

    print("You went to look for your phone in the bedroom. ")
    print("Looking at the bed made you feel even more tired.")
    lie_down = input("Do you want to lie down? (Yee/Nah bro) > ")
    if lie_down.lower() in affirm:
        pass_out("Laying in your bed made you fall asleep.")
    elif lie_down.lower() in negate:
        global inventory
        inventory.append("phone")
        print("Good stuff. You check the time. It's 5:15 pm! Let's go to")
        print("the kitchen and make some coffee for a night of productivity!")

    else:
        print("Sorry, but you have to make a decision here my guy.")
        bedroom_adv()

# END ROOMS

def start_adventure():
    '''Starts adventure by allowing players to make choices.'''

    print("You wake up in your bed in the morning feeling groggy, except ")
    print("you're not in your bed, you're on the couch. And it's not morning,")
    print("you have no idea what time it is.")
    print("Do you want to grab your phone in the bedroom and check the time")
    print("first, or do you want to make some coffee? ")
    room_picked = input("(Bedroom/Kitchen) > ")
    if room_picked == "Bedroom":
        bedroom_adv()
    elif room_picked == "Kitchen":
        kitchen_adv()
    else:
        print("Sorry, you have to pick either the Kitchen or your Bedroom. :(")
        start_adventure()

def main():
    '''Prompts for player's name and stores it.
    Starts the game.'''

    player_name = input("What's your name, oh isolated one? ")
    print(f"Your name is {player_name}.")
    response = input("Is that correct? (Yee/Nah bro) > ")
    if response.lower() in affirm:
        start_adventure()
    elif response.lower() in negate:
        main()
    else:
        print("You're supposed to type in 'Yee' or 'Nah bro'. Try again lol")



if __name__ == '__main__':
    begin()
    main()
