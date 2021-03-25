print("\nOkay, so Kim said he wanted more of this shit \nbut now with lists and arrays.")
print("PS. Fuck C and C++ syntax. They are driving me mad.")

print("\nWelcome to this thingy!")
print("What would you like to do?")
print("Please select the following:\n 1 - for Waifu Calculator\n 2 - for Husbando Calculator")
print("To exit, please type 'exit'")

while True:
    megahomo = input(">")
    if megahomo.lower() not in ('1', '2', 'exit'):
        print(f'Invalid reponse, please try again.')
        print("Please select the following:\n 1 - for Waifu Calculator\n 2 - for Husbando Calculator")
        print("To exit, please type 'exit'")
        continue
    else: 
        break

femchar = ['amber', 'barbara', 'beidou', 'diona', 'fishcl', 'ganyu', 'jean', 'keqing', 'klee', 'lisa', 
'mona', 'ningguang', 'noelle', 'qiqi', 'sucrose', 'xiangling', 'xinyan', 'lumine']

malechar = ['albedo', 'bennett', 'chongyun', 'diluc', 'kaeya', 'razor', 'tartaglia', 'venti', 
'xiao', 'xingqiu', 'zhongli', 'aether']

def waifucalculator():
    print('Welcome to Waifu Calculator!')
    print("Note: This calculator only supports waifu from Genshin Impact only!")
    
    while True:
        waifu = input("Please enter your waifu name: \n >")
        if waifu.lower() not in femchar:
            print("!!!That is not a valid waifu name!!!")
            print("----Please try again.----")
            continue
        else: break
    print(f"So your waifu is: {waifu.capitalize()}")
    print("Let me think about that for a sec;")
    if waifu.lower() == 'ganyu':
        print('\nThat is one fine choice my good sir!\n Glory to Cocogoat, the Legendary Adeptibeast!')
    elif waifu.lower() == 'mona':
        print('Fuck you. No matter how hard I try, I would never get her. ;-;')
    else: print("Okay, that's kind lame.")

def husbandocalculator():
    print('Welcome to Husbando Calculator!')
    print("Note: This calculator only supports husbando from Genshin Impact only!")

    while True:
        husbando = input("Please enter your husbando name: \n >")
        if husbando.lower() not in malechar:
            print("!!!That is not a valid husbando name!!!")
            print("----Please try again.----")
            continue
        else: break
    print(f"So your husbando is: {husbando.capitalize()}")
    print(f"Let me think about that....")
    if husbando.lower() == 'zhongli':
        print("Well, well. If it ain't the Geodaddy. All hail Rex Lapis and his cheap fake death!")
        print("I bet Ganyu is going to be pissed about you faking your death.")
    elif husbando.lower() == 'venti':
        print('EHE TE NANDAYO')
    else: print('Meh, lame.')

choice = megahomo.lower()

if choice == '1':
    print('\nYou have selected: Waifu Calculator!\n')
    waifucalculator()
elif choice == '2':
    print('\nYou have selected: Husbando Calculator!\n')
    husbandocalculator()
else: exit()