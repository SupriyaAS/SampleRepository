# wap to print longest word
sentence1 = "this is a programming language & programming is fun"
word1 = sentence1.split()
for i in range (len(word1)-1):
    for i in range(len(word1) - 1):
        if len(word1[i]) < len(word1[i + 1]):
            word1[i], word1[i + 1] = word1[i + 1], word1[i]
print(word1)
###########################################################################################################
s13= "dad dad"
for char in reversed(s13):
    if s13==char:
        print("palindrome")
    else:
        print("not a palindrome")