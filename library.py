names = []
for _ in range(2):
    name = input("please enter the name of someone you know ")
    names.append(name)
lowercased = [name.lower()for name in names]
titlecased = [name.title() for name in lowercased]
invitations = [f"dear{name}, please come to the wedding this saturday!"for name in titlecased]

for item in invitations:
    print(item)



































