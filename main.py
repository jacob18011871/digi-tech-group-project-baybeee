
#--------Functions -----------
def intro():
    player_name = input("Hey gambler! Do you know where you are right now? Unfortuntely we can't carry on until we know your name. Can you tell us?")
    print(player_name, "? Glad you remembered. Now I should probably catch you up on recent events.. Everything's gone to absolute sh*t.")
    print("After spending your childs college fund (and losing), you are now stuck inside a Casino. Unfortunetly you find yourself trying to gamble back your debt with a few minor family relics.")
    print("Since you've woken up, it becomes apparent that the situation you're in is dire. Civilisations accross the globe have collapsed, torn apart and simply forgotten. Checking in on yourself you see that you are fine for now but everyone around you is mostly sick and infected with a virus called RAV26 that has inhereted most of the world. You decide to set off on foot to try find a way to make it all better. ")

#function for health
def hp():
    health = 5
    if health < 0:   
        score = 395

# ----------- Main Code --------------

intro()

