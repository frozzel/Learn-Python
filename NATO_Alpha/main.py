import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha = {row.letter:row.code for (index, row) in data.iterrows()}

def gen_alpha():
    word = input("Enter a Word:  ").upper()
    try:
        ans = [alpha[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        gen_alpha()
    else:
        print(ans)
        continue_on = input("Do you want to continue? Y/N:  ").upper()
        if continue_on == "Y":
            gen_alpha()
            
gen_alpha()