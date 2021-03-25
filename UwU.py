print('Right so at last I got rid of those goddamn C syntax.')
print("Let's try something new. \n")
print("What would you like to do?")
print("Please input: \n 1 - Waifu Calculator \n 2 - Husbando Calculator")

iwantthis = input(">")

def waifucalculator():
    print("\n Welcome to Waifu Calculator! \n")
    print("Who's you wifey waifu wifey?")

    WaifuInput = input("My Waifu is: \n >")
    WaifuInput = WaifuInput.capitalize()
    waifu = WaifuInput.lower()

    print(f"So your waifu is {WaifuInput}")
    print("Let me think about that...")
    if waifu == "ganyu":
        return print(f"Solid choice.")
    elif waifu == "cocogoat":
        return print(f" Y E S ")
    else: return print(f'{WaifuInput} is not a valid choice. \n Please try again.')

def husbandocalculator():
    print("\n Welcome to Husbando Calculator! \n")
    print("Who's your husbandy husbando?")

    HusbandoInput = input("My husbando is: \n >")
    HusbandoInput = HusbandoInput.capitalize()
    Husbando = HusbandoInput.lower()

    print(f"So your husbando is {HusbandoInput}")
    print("Let me see....")
    if Husbando == "zhongli":
        return print(f"Yes.")
    else: return print(f"No.")

if iwantthis == "1":
    print("You have chosen:\n Waifu Calculator!")
    waifucalculator()

elif iwantthis == "2":
    print("You have chosen:\n Husbando Calculator!")
    husbandocalculator()

else: print("Please enter a valid response.")