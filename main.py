# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
print("please enter first word")
word = input("string1:")
print("please enter second word")
anagram = input("string2:")
word2 = sorted(word)
print(word2)
anagram2 = sorted(anagram)
print(anagram2)
if word2 == anagram2:
    print(True)
else:
    print(False)
