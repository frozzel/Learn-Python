#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("./Input/Names/invited_names.txt") as names:
#     name_list = names.readlines()
    
# with open("./Input/Letters/starting_letter.txt") as letter:
#     new_letter = letter.readlines()
    
# for x in range(0, len(name_list)):   
#     with open(f"./Output/ReadyToSend/{name_list[x]}.txt", mode="w") as file:
#      name = name_list[x].replace("\n", ",\n")
#      new_letter[0] = f"Dear {name}"
#      for y in range(len(new_letter)):
#         file.write(new_letter[y])
        


#Tutorial method:

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    new_letter = letter.read()
    for name in name_list:
        stp_name = name.strip()
        n_let = new_letter.replace(PLACEHOLDER, stp_name)
        with open(f"./Output/ReadyToSend/letter_for_{stp_name}.txt", mode="w") as file:
           file.write(n_let)
