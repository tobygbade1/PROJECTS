# Exercise to loop though a list of names and output the lenght of each name

name_list =["Raymond", "Karen", "Justified", "Adekunle"]

for name in name_list:
    if len(name) > 5 and ("n" in name or "N" in name):
        print("The length of the name is: ", str(len(name)),  "; ",  name)

    continue


while len(name_list) >= 1:
        poped_name = name_list.pop()
        print("The last removed name is: ", poped_name)


