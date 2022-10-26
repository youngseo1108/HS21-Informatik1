alphabet = "a b c d e f g"
data = alphabet.split() #split string into a list
print(data)

lst = []
dataset = ["Hello world", "This is the WORLD", "hello again"]
for i in range(len(dataset)):
    lst.append(dataset[i].lower().split())
print(lst)