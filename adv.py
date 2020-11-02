import time

print("Hello World")

affirm = ["yes", "yeah", "yee", "y"]
negate = ["no", "nope", "n", "nah bro", "nah"]
inventory = ["body odour"]
bedroom = ["phone", "phone charger"]
kitchen = ["coffee"]
livingroom = ["laptop", "yoga mat", "laptop charger", "couch"]
cups = 0

def begin():
    '''Prints the welcome message'''

    print("Welcome to Covid Madness")

# HELPERS
def represents_posint(x: str):
    '''Returns True if x is a string representing a positive integer. e.g. "2", "35".
    If not, returns False.'''

    try:
        int(x)
        #check if it's positive
        if int(x) > 0:
            return True
        else:
            return False
    except ValueError:
        return False
# END HELPERS

# ACTIONS
def check_inventory():
    '''Prints the player's current inventory.'''

    global inventory
    print(f"Inventory: {inventory}")

def pass_out(why):
    '''In: Passing in the string showing player why they passed out.

    Result:
    Prints message telling player they passed out and why.'''

    global inventory
    global cups
    #check if game won
    if "love" in inventory and "winner" in inventory and "coffee" in inventory:
        print("Congratulations!")
        print("You had all the things you needed for a good day. You exercised,")
        print("showered, did some work and stayed in touch with loved ones.")
        print("You were so productive today and you're ready for tomorrow!")
        exit()
    #check if all tasks done but drank too much coffee
    elif "love" in inventory and "winner" in inventory and "lots of coffee" in inventory:
        print("Unfortunately you drank too much coffee and you'll be staring")
        print("at the ceiling for a while.")
        time.sleep(int(cups))
        print("Congratulations!")
        print("You had all the things you needed for a good day. You exercised,")
        print("showered, did some work and stayed in touch with loved ones.")
        print("Since you're going to bed late, you won't be up early. Let's ")
        print("drink less caffeine from now on!")
        exit()
    #check if called mom
    elif "love" in inventory and "winner" not in inventory:
        print("You passed out early, but talking to mom helped a lot. She's great!")
    #didn't satisfy main requirement. call your mom lol
    else:
        print(f"You passed out. {why} rip")
        exit()

def call():
    '''Calls family. Outcome of call depends on player's inventory.'''

    global inventory
    #check if assignment done
    if "dopamine" in inventory:
        #check if exercise done
        if "endorphins" in inventory:
            #check if showered
            if "sweat" and "body odour" not in inventory:
                print("You call your mom feeling accomplished and")
                print("refreshed. She tells you she's happy to see you")
                print("looking so fresh and joyful. You feel loved and")
                print("head over to the bedroom.")
                inventory.append("love")
                inventory.append("winner")
                bedroom_adv()
        else:
            print("You call mom but you feel groggy. The conversation")
            print("doesn't go so well. Mom says you look tired and asks if ")
            print("you're getting enough sleep.")
            inventory.append("love")
            pass_out("You had nothing else to do")
    else:
        print("You call mom but you feel a little stressed. The conversation")
        print("doesn't go so well, but she tells you she loves you.")
        inventory.append("love")
        pass_out("You had nothing else to do")
# END ACTIONS

# ROOMS
def shower_room():
    '''Actions in the shower.'''

    #three second pause
    time.sleep(2)
    global inventory
    inventory.remove("body odour")
    if "sweat" in inventory:
        #removes sweat added from exercise
        inventory.remove("sweat")
    print("Wow! You feel refreshed and you don't smell anymore, yay!")

def living_room():
    '''Actions in the living room.'''

    print("You walk into the living room.")
    global inventory
    global livingroom
    print(f"You see what's in here: {livingroom}")
    #exercise task
    if "yoga mat" in livingroom:
        print("There's a yoga mat on the floor.")
        print("Do you want to do some exercise?")
        exercise = input("Yes/No > ")
        if exercise.lower() in affirm:
            time.sleep(2)
            inventory.append("endorphins")
            inventory.append("sweat")
            livingroom.remove("yoga mat") #exercise can only be done once
            print("Great job! You got in a good workout and you feel great.")
            print("Look at that! You got your daily dose of endorphins.")
            check_inventory()
        else:
            print("Rip. It's hard sometimes, but you need to stay healthy bro.")
        #shower task #shower can only be done once
        print("Take a shower, maybe?")
        shower = input("Y/N > ")
        if shower.lower() in affirm:
            shower_room()
        else:
            print("It's hard, but you need to maintain hygiene bro.")
            pass_out("You fell asleep on the couch.")
    if "laptop" in livingroom:
        #laptop task
        print("Your laptop's here. It'd be nice to finish that assignment")
        print("that's due next week.")
        work = input("Do assignment? (Y/N) > ")
        if work.lower() in affirm:
            time.sleep(5)
            inventory.append("dopamine")
            inventory.append("relief")
            livingroom.remove("laptop") #work can only be done once
            print("Wow! You're on a roll! You feel accomplished after all that")
            print("work. Let's call mom!")
            print("Oops. Your laptop is about to die. Let's get the charger?")
            charge = input("Charge laptop? (Y/N) > ")
            #charging laptop after doing laptop task automatically calls mom
            if charge.lower() in affirm:
                call()
            else:
                print("Your laptop died.")
                pass_out("You fell asleep on the couch")
        else:
            print("Rip. Let's talk to mom?")
            call_mom = input("Y/N > ")
            if call_mom.lower() in affirm:
                call()
            else:
                #not calling mom ends game
                print("You feel sleepy on the couch. You rest your head a")
                print("little and ...zzzzzz")
                pass_out("You had nothing to do.")



def kitchen_adv():
    '''Actions in kitchen.'''

    print("You walk into the kitchen and go to heat up some water in the ")
    print("microwave. The microwave clock shows 4:10 pm. How many cups of ")
    print("coffee do you want to make?")
    cup_no = input("> ")
    if represents_posint(cup_no) == True:
        global cups
        #saves the choice here to affect sleeping time later
        cups = cup_no
        if int(cup_no) == 1:
            inventory.append("coffee")
            print("Great! Now let's figure out what to do.")
            living_room()
        elif int(cup_no) > 1:
            inventory.append("lots of coffee")
            print("Woah, that's a lot of coffee to be drinking this late.")
            print("Hope we can go to bed on time...")
            living_room()
        else:
            print("That's not a proper answer...")
            kitchen_adv()
    else:
        print("The NUMBER of cups my dude.")
        kitchen_adv()



def bedroom_adv():
    '''Actions in bedroom.'''

    print("You enter the bedroom. ")
    print("Looking at the bed makes you feel more tired.")
    lie_down = input("Do you want to lie down? (Yee/Nah bro) > ")
    if lie_down.lower() in affirm:
        pass_out("Laying in your bed made you fall asleep.")
    elif lie_down.lower() in negate:
        global inventory
        inventory.append("phone")
        global bedroom
        bedroom.remove("phone")
        print("Good stuff. You check the time. It's 4 pm! Let's go to")
        print("the kitchen and make some coffee for a night of productivity!")
        kitchen_adv()

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
