action = "test pick A or B surely"
a = " hi! im A! "
b = " hey! im b. "
answer = input("{}\nA.{} B. {}".format(action, a, b)).lower()
if answer == a or answer == "a":
    print("congrats you picked A")
elif answer == b or answer == "b":
    print("congrats you picked B")
else:
    print("you didnt type in anything")
    print("game over")