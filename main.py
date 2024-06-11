class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print("You move to", self.current_room.name)
            print(self.current_room.description)
        else:
            print("You can't go that way.")

def main():
    # Define the rooms
    room1 = Room("Room 1", "This is room 1", {})
    room2 = Room("Room 2", "This is room 2", {})
    room3 = Room("Room 3", "This is room 3", {})
    room4 = Room("Room 4", "This is room 4", {})

    # Connect the rooms
    room1.exits = {"east": room2}
    room2.exits = {"west": room1, "south": room3}
    room3.exits = {"north": room2, "east": room4}
    room4.exits = {"west": room3}

    # Create player
    player_name = input("Enter your name: ")
    player = Player(player_name, room1)

    print("Welcome to the Text Adventure Game!")
    print("Type 'quit' to exit.")

    while True:
        print("\n" + player.current_room.name)
        print(player.current_room.description)
        command = input("What do you want to do? ").strip().lower()

        if command == "quit":
            print("Thanks for playing!")
            break
        elif command in ["north", "south", "east", "west"]:
            player.move(command)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()