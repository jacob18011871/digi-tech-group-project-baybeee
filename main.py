#--------Functions -----------
import time
QUESTION_FORMAT = "{}\nA.{} B.{} C.{}"
#weapons = "Axe"

def intro():
    player_name = input("Hey gambler! Do you know where you are right now? Unfortuntely we can't carry on until we know your name. Can you tell us?")
    print(player_name, "? Glad you remembered. Now I should probably catch you up on recent events..")
    time.sleep(2) 
    print("Everything's gone to absolute sh*t.")
    time.sleep(4)
    print("After spending your childs college fund (and losing), you are now stuck inside a Casino. Unfortunetly you find yourself trying to gamble back your debt with a few minor family relics.")
    time.sleep(3)
    print("Since you've woken up, it becomes apparent that the situation you're in is dire. Civilisations accross the globe have collapsed, torn apart and simply forgotten. Checking in on yourself you see that you are fine for now but everyone around you is mostly sick and infected with a virus called RAV26 that has inhereted most of the world. You decide to set off on foot to try find a way to make it all better. ")
#Stage 2 is where the story starts to progress and they have options to explore

def stage2():   
    print("Looking out the window, you see that the weather and conditions are safe to exit the Casino. However there is an upstairs and a downstairs that leads to a basement.")
    time.sleep(6)
    action = "Do you wish to explore the basement or discover what might be upsatirs or simply leave the Casino?"   
    a = "a Walk upstairs"
    b = "b Go down to the basement"
    c= "c Leave the Casino"
    action = input(QUESTION_FORMAT.format(action, a, b, c)).lower()
    # VIP ROOM EVENTS
    if action == a or action == "a":    
        print("You walk upstairs and find an abandoned VIP room, there is lots of old stored cash and weaponry.")
        action = "Unfortunetly you only have enough space to carry the cash or the weapons to leave with."  
        a = "a Take the cash!!" 
        b = "b Grab the weapon"   
        c= "c Leave the Casino"   
        action = input(QUESTION_FORMAT.format(action, a, b, c)).lower()   
        action == a or action == "a"   
        print("Well done you are now rich! But actually it doesn't matter because the economy collapsed months ago while you were gambling! Perhaps it could serve another use. :D ")
        time.sleep(4)
    elif action == b or action == "b":  
        print("A mighty weapon of choice!" "You have decided to take with you an Axe." "This is good forprotecting yourself against enemies.")  

    elif action == c or action == "c":  
        print("Leaving behind the wonderful addicitng environment of the Casino, you step outwards into the harsh outdoors where you are compelled to aviod the virus and survive.")    
        time.sleep(6)   
        print("Tramping in the cover of dark buildings and park trails you catch sight of a Train Station nearby perfectly settled and ready for action.")  
        time.sleep(5)   

        action = "Is it time to hitch a ride?"  
        a = "Ride the train" 
        b = "Carry on the trail"
        #If they carry on walking they end up at the zoo thats in the inner city   
        c= "Rob the train"   
        #They get a fully loaded shotgun
        action = input(QUESTION_FORMAT.format(action, a, b, c)).lower() #BASEMENT EVENTS
    elif action == b or action == "b":  
        print("Hastily walking down the eerie basement you smell a stench so awful it stinks of zombies. Because you've inhaled this you have just made yourself more sick and it was infact a zombie that had passed a little over an hour ago.")  
    #Minus a few health points 
    HP =95
#-------------------function for health----------------------------

blood =0 #In Litres
HP =100 #Health points can drastically change depending on how sick they are or what they are attacking
# ----------- Main Code --------------


intro() 

stage2()
