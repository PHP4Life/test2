# Task 2 - Where should I look?
room = input("Where should I look? (bedroom, bathroom or living)")

if room = "bedroom":
    bedroomWhere = input("Where in the bedroom should i look? (under the bed, in the wardrobe)")
    if bedroomWhere = "under the bed":
        print("Found some mess but no phone")
    else:
        print("Found some mess but no phone")
elif room = "bathroom":
    bathroomWhere = input("Where in the bathroom should I look? (bathtub, sink)")
    if bathroomWhere = "bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")
elif room = "living":
    livingRoomWhere = input("Where in the living room should I look? (on the table, in the couch)")
    if livingRoomWhere = "on the table":
        print("Yes! i found my phone!")
    else:
        print("Found some stuff but no phone")
else:
    print("I do not know where that is but I will keep looking")