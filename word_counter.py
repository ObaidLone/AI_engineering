sentence=input("enter the sentence: ")

words =sentence.split()
if words:
    print(len(words))
    
    print(max(words,key=len))
    
    # print(" ".join(words[::-1]))

    reverse_array = " ".join(words[::-1])

    print(reverse_array)
else:
    print(" please eneter words")