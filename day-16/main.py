from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle") 
timmy.color("green")
timmy.resizemode("auto")

my_screen = Screen()
print(my_screen.canvheight)

timmy.forward(100)
my_screen.exitonclick()


# from prettytable import PrettyTable

# table = PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric", ])
# table.add_row(["Squirtle", "Water"])
# table.add_row([ "Charmander", "Fire"])

# table.align = "c"

# print(table)