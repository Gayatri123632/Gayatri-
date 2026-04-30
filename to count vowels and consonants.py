s = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)

