list = {}
search_words = ["Python", "C", "OOP", "Hello", "Java"]
with open("input.txt", "r") as file:
    contents = file.read().split()
    for txt in contents:
        for word in search_words:
            if word.casefold() == txt.casefold():
                if word in list:
                    list[word] = list[word] + 1
                else:
                    list[word] = 1
        
for item in list:
    print("{}->{}".format(item, list[item]))


 

