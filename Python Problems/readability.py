#User Input
text = str(input("Text: "))

#Initialisation
Letters = 0
Words = 1
Sentences = 0

#Linear search for Words,Letters,Sentences
for i in range(len(text)):
    if text[i].isalpha():
        Letters += 1
    elif text[i].isspace():
        Words += 1
    elif text[i] == '.' or text[i] == '!' or text[i] == '?':
        Sentences += 1

#Index Calculation
l = Letters / Words * 100
s = Sentences / Words * 100
index = round(0.0588 * l - 0.29 * s - 15.8)

#Index Conditions
if index > 16:
    print("Grade 16+")
elif index > 1 and index < 17:
    print(f"Grade {index}")
else:
    print("Before Grade 1")
