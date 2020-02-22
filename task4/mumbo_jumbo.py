
first, second = set(), set()

sent1 = input()
while (not sent1 == ""):
    for x in sent1:
        first.add(x)
        
    sent2 = input()
    for x in sent2:
        second.add(x)

    sent1 = input()

print("Mumbo" if len(first) > len(second) else "Jumbo")
