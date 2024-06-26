
#--------Functions -----------

def intro():
    player_name = input("Hey gambler! Do you know where you are right now? Unfortuntely we can't carry on until we know your name. Can you tell us?")
    print(player_name, "? Glad you remembered. Now I should probably catch you up on recent events.. Everything's gone to absolute sh*t.")

#function for health
def health():
    health = 5
    if health < 0:
        pass
# function for doing something (an action)
def action():
    pass

def ending():
    # text is not final, placeholder text
    action = "You walk into a small room. A window lets you see the full moon along with some clouds. There is a primitive elevator which leads to the top of the tower, although it looks shoddy... unsafe and almost DEFINITELY lethal. You could also climb up the tower, but that would be tiring... the risk is great. What do you do?"
    a = " Take the risk, and use the Elevator "
    b = " Don't take the risk, and climb up the tower. "
    answer = input("{}\nA.{} B. {}".format(action, a, b)).lower()
    if answer == a or answer == "a":
        print("Putting everything on the line, you jump onto the elevator and pull the switch. The elevator begins RACING up the tower, leaving you barely without breath. The elevator comes at a complete sudden STOP at the top, throwing you into the roof. You survive, barely.(- 50 hp)")
    elif answer == b or answer == "b":
        print("Using skills you learnt from the Mountain, you begin climbing up the walls of the tower")
    else:
        print("You grabbed your karambit and reduced your lifespan by ∞.")
        print("game over.")


# ----------- Main Code --------------

