# Input from user
while True:
    try:
        change = float(input("Change: "))
        if (change >= float(0.01)):
            break
    except:
        print("", end="")

count = int(0)

coins = round(change * 100)

#Calculations

while coins > 0:
    if coins >= 25:
        coins -= 25
        count += 1
    elif coins >= 10:
        coins -= 10
        count += 1
    elif coins >= 5:
        coins -= 5
        count += 1
    else:
        coins -= 1
        count += 1

print(count)
