my_family = {}

def add_family_member(role, name):
    if role in my_family.keys():
        my_family[role].append(name)

    else:
        names = []
        names.append(name)
        my_family[role] = names

    return my_family

add_family_member('brother', 'Arne')
add_family_member('mother', 'Anne')
add_family_member('brother', 'Geir')
print(my_family)

for key, value in my_family.items():
    for name in value:
        print(name, 'is my', key)







