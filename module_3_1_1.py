sting = 'Urban'
list_to_search = ('ban', 'BaNaN', 'urBan')
sting = sting.lower()
for i in list_to_search:
    i = i.lower()
    if i == sting:
        a = True
if a == True:
    print(True)
else:
    print(False)
