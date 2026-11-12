# # def greet(name):
# #     return "Hello ," + name 
# # message =greet("lone")
# # print(message)


# def is_even(number):
#     return number %2== 0



# def describe_number(number):
#     if number< 0:
#         return "negative"
#     elif is_even(number):
#         return "even"
#     else:
#         return "odd"

# check= describe_number(9)
# # print(check) 

# sentence=input("enter the sentence")

# def word_count(sentence):
#     words=sentence.split()
#     return len(words)
# result = word_count(sentence)
# # print(result)
# def longest_word(sentence):
#     words=sentence.split()
#     return max(words,key=len)
# long = longest_word(sentence)
# # print(long)

# def reverse_word(sentence):
#     words=sentence.split()
#     return  " ".join(words[::-1])
# rev = reverse_word(sentence)
# # print(rev)

# def word_fre(sentence):
#     sentence=sentence.lower()
#     words=sentence.split()
#     frequency={}
#     for word in words:
#         if word in frequency:
#             frequency[word] +=1
#         else:
#             frequency[word] =1
#     return frequency
# frequency_word = word_fre(sentence)
# print(frequency_word)


# Function 1: Check whether a number is even
def is_even(number):
    return number % 2 == 0


# Function 2: Describe a number
def describe_number(number):
    if number < 0:
        return "negative"
    elif is_even(number):
        return "even"
    else:
        return "odd"


# Function 3: Count words
def word_count(sentence):
    words = sentence.split()
    return len(words)


# Function 4: Find the longest word
def longest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    return max(words, key=len)


# Function 5: Reverse words
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


# Function 6: Count word frequency
def word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# Main function
def main():
    # Ask the user for input
    sentence = input("Enter a sentence: ")
    number = int(input("Enter a number: "))

    # Call sentence functions
    print("\n--- Sentence Results ---")
    print("Word count:", word_count(sentence))
    print("Longest word:", longest_word(sentence))
    print("Reversed words:", reverse_words(sentence))
    print("Word frequency:", word_frequency(sentence))

    # Call number functions
    print("\n--- Number Results ---")
    print("Is even:", is_even(number))
    print("Number description:", describe_number(number))


# Program entry point
if __name__ == "__main__":
    main()
