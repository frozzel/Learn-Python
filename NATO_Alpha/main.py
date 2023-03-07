import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a Word:  ").upper()

ans = [alpha[letter] for letter in word]

print(ans)