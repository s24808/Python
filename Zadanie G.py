def isPalindrome(text):
    return text == text[::-1]


text = input("Podaj slowo: ")
ans = isPalindrome(text)

if ans:
    print("Slowo jest palindromem")
else:
    print("Slowo nie jest palindromem")
