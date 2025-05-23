String = input("Enter a Stirng: ")
is_vowel = "aeipuAEIOU"
print(len(String)) 

def check_first_vowel(x):
    if not x:
        print("String is empty.")
    elif x[0] in is_vowel:
        return f"The String start with a vowels {String[0]}"
    else:
        return f"The string doesn't start with a vowel letter.{String[0]}"


def revers_string(x):
    return x[::-1]

print(check_first_vowel(String))
print(revers_string(String))