num = [1,2,3]
new_lsit = [n+1 for n in num]
print(new_lsit)

name = "Dennis"
name_list = [letter for letter in name]
print(name_list)

range_new = range(1,5)
new_range = [range *2 for range in range_new]
new_range2 = [range *2 for range in range(1,5)]
print(new_range2)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie" ]

short_names = [name for name in names if len(name)< 5]
print(short_names)

longCap_names = [name.upper() for name in names if len(name)> 5]
print(longCap_names)