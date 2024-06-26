import time
weapon = "Axe"
blood = 55
HP = 100
Stamina = 100
Alchemist_HP = 1250
if HP == 0:
        print("You died. Game over.")
        exit()


action = "You walk into a small room. A window lets you see the full moon along with some clouds. There is a primitive elevator which leads to the top of the tower, although it looks shoddy... unsafe and almost DEFINITELY lethal. You could also climb up the tower, but that would be tiring... the risk is great. What do you do?"
a = " Take the risk, and use the Elevator "
b = " Don't take the risk, and climb up the tower. "
answer = input("{}\nA.{} B. {}".format(action, a, b)).lower()
if answer == a or answer == "a":
        print("Putting everything on the line, you jump onto the elevator and pull the switch. The elevator begins RACING up the tower, leaving you barely without breath. The elevator comes at a complete sudden STOP at the top, throwing you into the roof. You survive, barely.(- 50 hp)")
        HP -= 50
elif answer == b or answer == "b":
        print("Using skills you learnt from the Mountain, you begin climbing up the walls of the tower. This exhausts you.(-50 Stamina, -1 Turn)")
        Stamina -= 50
else:
        print("You grabbed your karambit and reduced your lifespan by ∞.")
        print("game over.")

print("You stumble out of the tower onto the long bridge, which leads directly into the main Observatory. You look off into the beautiful full moon, constellations filling the sky. It gives you a feeling of reassurance. (+100 Health, +100 Stamina, +5 turns). You walk up to the Observatory, and open the doors.")
HP += 50
Stamina += 100
time.sleep(5)
action = "Do you enter the Observatory?"
a = " Enter the Observatory and maybe find a way to cure yourself. "
b = " End this nightmare. "
c = " Go back to the lab... maybe you missed something..? "
answer = input("{}\nA.{} B. {} C. {}".format(action, a, b, c)).lower()
if answer == a or answer == "a":
        print("You enter the Observatory.")
elif answer == b or answer == "b":
        print("You decide to end this insanity. You grab the rails of the bridge, and swiftly you launch yourself over the edge... aaand you immediately regret it! You race to find anything in your bag to help youself, theres nothing useful! The ground is approaching, but wait! You forgot about th-")
        time.sleep(10)
        print("*splat*")
        print("game over.")
        exit()
        

elif answer == c or answer == "c":
        print("You take the elevator down back into the lab. You wander around, looking for anything you missed. You find a cabinet labelled 'PANACEA', and you open it. A small bright vial, and a code reading '90120'. You grab the vial and open it. It's bright blue. You decide to drink it... and you feel better? You dont feel cured... but like you just took painkillers. (+10 turns). You decide to go back to the eleva- *you are MAULED by a cannibal*")
        time.sleep(10)
        print("game over.")
        exit()
        

else:
        print("You grabbed your karambit and reduced your lifespan by ∞.")
        print("game over.")
        exit()
print("You walk in on the Alchemist and some strange device with a bright substance swirling around inside.")
time.sleep(2.5)
print("'Welcome, my mute friend!' The Alchemist welcomes.")
print("The device is filled with a bright substance, aswell as a red substance. Maybe its blood?")
time.sleep(2.5)
print("'Do you like my Catalyst? Nothing fancy really. A required tool for any aspiring Alchemist.'")
print("'...anyway, how many monsters did you slaughter this time? How much blood do you have?")
print("(You have", blood, "litres of blood.)")
time.sleep(2.5)
action = "'Would you be so kind as to put them in my Catalyst here?'"
time.sleep(2)
a = " Put the blood in the Catalyst "
b = " Refuse "
answer = input("{}\nA.{} B. {}".format(action, a, b)).lower()
if answer == a or answer == "a":
        print("You pour all of your blood into the Catalyst, mixing the red and bright blue substances... creating a bright purple glow.")
        time.sleep(5)
elif answer == b or answer == "b":
        print("'No? What do you mean no?'")
        time.sleep(3)
        print("The Alchemist takes the blood anyway, and pours it in himself, hurting you in the process accidentally. 'Sorry.' He says. (-20 Stamina)")
        time.sleep(5)
print("The Alchemist activates the Catalyst, mixing around the substance.")
time.sleep(1.5)
print("'Are you familiar with the myth of the Panacea?'")
time.sleep(2.5)
print("'The cure to all disease...'")
time.sleep(2.5)
print("'...distilled from the essence of life itself.'")
time.sleep(1)
print("'Well, if you believe the old alchemists...'")
print("'A bunch of horsesh*t! Thats all this is. A bunch of tales from old fools. Tales, for gullible children. I mean, just look at you...'")
time.sleep(6)
print("'Dependence. Loss of empathy. Lust for violence. Insanity. Endless death...'")
time.sleep(6)
print("'Nothing good can come from messing with the essence of life...'")
time.sleep(5)
print("'...but then again, I've scoured the entire island, scavenging the remains of the dead...'")
print("'...and the bellies of the living too. Few were willing. Many begged for mercy.'")
time.sleep(5)
print("The Catalyst finishes, producing a bright blue substance, glowing. It pours it into a flask, which The Alchemist grabs and holds up.")
time.sleep(2)
print("'Is this all I've got left? The false hope of a bunch of childrens stories...?")
time.sleep(5)
print("Seems The Alchemist really doesn't believe in the Panacea.")
time.sleep(3)
print("'...Pathetic.'")
time.sleep(1.5)
print("The Alchemist takes a sip from the Panacea.")
print("He falls to the ground. In a sudden flash, though...")
time.sleep(5)
print("He rises up, looking refreshed and less sick. A smile emerges on his now blue eyes and mouth.")
time.sleep(4)
print("'...actually... this feels AWESOME!'")
time.sleep(3)
print("'I've never felt anything quite like it!'")
time.sleep(2)
print("'Be a good sport and bring me more blood... I'll send you back!'")
print("Looks like he knows about how you end up back in the Casino after every run... looks like he's also keen on sending you back there himself!")
time.sleep(5)
print("!! The Alchemist approaches !!")
time.sleep(2)
print("'I'll send you back!'")
print("You have", HP, "HP! Prepare!")
action = "The Alchemist pulls out a massive syringe, intending to pierce you! He charges up..!"
a = "Attack!"
b = "Dodge!"
c = "Parry!"
d = "Block!"
answer = input("{}\nA.{} B. {} C. {} D. {}".format(action, a, b, c, d)).lower()
if answer == a or answer == "a":
        print("You grab your", weapon, "and attempt to swing at him. You land one shot before he charges at you! You are pierced and heavily damaged! (-65 HP), (-20 Alchemist's HP)")
        HP -= 65 
        Alchemist_HP -= 20
elif answer == b or answer == "b":
        print("You just barely manage to dodge The Alchemist as he charges past, but he immediately charges again! You are hit full force! (-80 HP)")
        HP -= 80
elif answer == c or answer == "c":
        print("You raise your axe... and you parry his attack! He falls back. Your axe has been damaged, however!")
elif answer == d or answer == "d":
        print("You raise your axe... and you block his attack! However, he charges again, breaking your axe and damaging you! (-40 HP)")
        HP -= 40
else:
        print("The Alchemist charges directly at you, piercing you with his syringe! Your lack of action causes it to kill you! (-100 HP)")
        HP -= 100