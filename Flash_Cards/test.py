import pandas

data = pandas.read_csv("./data/french_words.csv")
print(data)

print(data.to_dict())