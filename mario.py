# Input from user
while True:
    try:
        height = int(input("Height: "))
        if (height >= 1) and (height <= 8):
            break
    except:
        print("", end="")

# Brick Matrix
for i in range(height):

    for j in range(height):

        if (int(i) + int(j)) > (int(height) - 1) or (int(i) + int(j)) == (int(height) - 1):
            print("#", end="")
        else:
            print(" ", end="")
    print("")
