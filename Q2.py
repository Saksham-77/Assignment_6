str = input("Enter a string: ")
rev_str = str[::-1]
if str.lower() == rev_str.lower():
    print("Yes the entered string is a palindrome")
else:
    print("No the entered string is not a palindrome")
