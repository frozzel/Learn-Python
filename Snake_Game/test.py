with open("../test.txt") as file:
    content = file.read()
    print(content)
    
# with open("new_file.txt", mode="a") as file:## a = append w=write
#     file.write("\nSome new text")