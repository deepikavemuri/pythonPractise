no_words = int(input("Enter the number of words you want to sort:\n"))
word_list = []
for i in range(no_words):
    x = input()
    word_list.append(x)
word_list.sort()
print(word_list)
