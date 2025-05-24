print("Which topic want to learen.")
print("1. String-methods")
print("2. List-Methods")
print("3. Tuple-Methods")

def string_method():
    print('''Python has a set of built-in methods that you can use on strings.

        Note: All string methods returns new values. They do not change the original string.

        Method	        Description
        capitalize()	Converts the first character to upper case
        casefold()	Converts string into lower case
        center()	Returns a centered string
        count()	    Returns the number of times a specified value occurs in a string
        encode()	Returns an encoded version of the string
        endswith()	Returns true if the string ends with the specified value
        expandtabs()    Sets the tab size of the string
        find()	Searches the string for a specified value and returns the position of where it was found
        format()	Formats specified values in a string
        format_map()	Formats specified values in a string
        index()	Searches the string for a specified value and returns the position of where it was found
        isalnum()	Returns True if all characters in the string are alphanumeric
        isalpha()	Returns True if all characters in the string are in the alphabet
        isascii()	Returns True if all characters in the string are ascii characters
        isdecimal()	Returns True if all characters in the string are decimals
        isdigit()	Returns True if all characters in the string are digits
        isidentifier()	Returns True if the string is an identifier
        islower()	Returns True if all characters in the string are lower case
        isnumeric()	Returns True if all characters in the string are numeric
        isprintable()	Returns True if all characters in the string are printable
        isspace()	Returns True if all characters in the string are whitespaces
        istitle()	Returns True if the string follows the rules of a title
        isupper()	Returns True if all characters in the string are upper case
        join()	Converts the elements of an iterable into a string
        ljust()	Returns a left justified version of the string
        lower()	Converts a string into lower case
        lstrip()	Returns a left trim version of the string
        maketrans()	Returns a translation table to be used in translations
        partition()	Returns a tuple where the string is parted into three parts
        replace()	Returns a string where a specified value is replaced with a specified value
        rfind()	Searches the string for a specified value and returns the last position of where it was found
        rindex()	Searches the string for a specified value and returns the last position of where it was found
        rjust()	Returns a right justified version of the string
        rpartition()	Returns a tuple where the string is parted into three parts
        rsplit()	Splits the string at the specified separator, and returns a list
        rstrip()	Returns a right trim version of the string
        split()	Splits the string at the specified separator, and returns a list
        splitlines()	Splits the string at line breaks and returns a list
        startswith()	Returns true if the string starts with the specified value
        strip()	Returns a trimmed version of the string
        swapcase()	Swaps cases, lower case becomes upper case and vice versa
        title()	Converts the first character of each word to upper case
        translate()	Returns a translated string
        upper()	Converts a string into upper case
        zfill()	Fills the string with a specified number of 0 values at the beginning
        Note: All string methods returns new values. They do not change the original string.''')

def List_Methods():
    print('''List Methods
                Python has a set of built-in methods that you can use on lists.

            Method	Description
            append()	Adds an element at the end of the list
            clear()	Removes all the elements from the list
            copy()	Returns a copy of the list
            count()	Returns the number of elements with the specified value
            extend()	Add the elements of a list (or any iterable), to the end of the current list
            index()	Returns the index of the first element with the specified value
            insert()	Adds an element at the specified position
            pop()	Removes the element at the specified position
            remove()	Removes the item with the specified value
            reverse()	Reverses the order of the list
            sort()	Sorts the list''')

def Tuple_Methods():
    print('''Python has two built-in methods that you can use on tuples.

            Method	Description
            count()	Returns the number of times a specified value occurs in a tuple
            index()	Searches the tuple for a specified value and returns the position of where it was found
''')

choice = int(input("Enter a choice: "))

if choice == 1:
    string_method()
elif choice == 2:
    List_Methods()
elif choice == 3:
    Tuple_Methods()
else:
    print("Enter a valid choice!!")