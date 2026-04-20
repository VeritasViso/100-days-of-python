## Made by @VeritasViso on 20/04/2026 at 20:39pm.

# Treasure Island project (Day 3 of 100)

## the big chameleon thing at the start
print("                     _.....---..._")
print("      _..-'-.   _.--'             '--.._")
print("  _.-' (  0) Y''                        ''-.._")
print(" (---.._,                                     '-._")
print("  `---.,___.-/  /----......./  /..------...____   '-.")
print("     _/  /  _/  /         __/  /   __/  /      `-.   ")
print("    (((-'  (((-'         (((---'  (((---`         )  /")
print("                                               .-'.-'")
print("                                     Veritas  (__`-,")
print("                                      (+jgs)     ``"")")


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

first_Decision = input("Type (left) or (right): ").casefold()

if first_Decision == "left": ## "==" means EQUAL TO.
    print("You've come to a lake. There is an island in the middle of the lake.")
    second_Decision = input("Type (wait) to wait for a boat. Type (swim) to swim across. ").casefold()
    if second_Decision == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        third_Decision = input("One red, one yellow and one blue. Which colour do you choose? ").casefold()
        if third_Decision == "red":
            print("It's a room full of fire. Game over.")
        elif third_Decision == "yellow":
            print("You found the treasure! You Win! Bluddy Brilliant mate!")
        elif third_Decision == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You didnt type the correct options. Retry with the exact words provided.")
    elif second_Decision == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You didnt type the correct options. Retry with the exact words provided.")
elif first_Decision == "right": ## printing what happens if the user types "right".
    print("You fell into a hole. Game Over.")
else:
    print("You didnt type the correct options. Retry with the exact words provided.")
