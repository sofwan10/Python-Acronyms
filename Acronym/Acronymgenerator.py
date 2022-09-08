user_input = str(input("Enter a Phrase: "))     #put any phrase in the input field e.g "Ahmad Sofwan"
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)