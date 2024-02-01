def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def count_characters(s):
    return len(s)

def concatenate_strings(s1, s2):
    return s1 + s2

def repeat_string(s, n):
    return s * n

def search_substring(s, substring):
    return s.find(substring)

def find_character_index(s, char):
    return s.find(char)

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def is_alphanumeric(s):
    return s.isalnum()

def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

def replace_substring(s, old_substring, new_substring):
    return s.replace(old_substring, new_substring)

def remove_whitespaces(s):
    return ''.join(s.split())

def main():
    user_string = input("Enter a string: ")

    while True:
        print("\nMenu:")
        print("1. Reverse String")
        print("2. Capitalize String")
        print("3. Count Characters")
        print("4. Concatenate Strings")
        print("5. Repeat String")
        print("6. Search Substring")
        print("7. Find Character Index")
        print("8. Convert to Uppercase")
        print("9. Convert to Lowercase")
        print("10. Check Alphanumeric")
        print("11. Check Palindrome")
        print("12. Replace Substring")
        print("13. Remove Whitespaces")
        print("14. Exit")

        choice = input("Enter your choice (1-14): ")

        if choice == '1':
            result = reverse_string(user_string)
            print("Reversed String:", result)
        elif choice == '2':
            result = capitalize_string(user_string)
            print("Capitalized String:", result)
        elif choice == '3':
            result = count_characters(user_string)
            print("Number of Characters:", result)
        elif choice == '4':
            second_string = input("Enter another string to concatenate: ")
            result = concatenate_strings(user_string, second_string)
            print("Concatenated String:", result)
        elif choice == '5':
            repetition_count = int(input("Enter the repetition count: "))
            result = repeat_string(user_string, repetition_count)
            print("Repeated String:", result)
        elif choice == '6':
            substring = input("Enter the substring to search for: ")
            index = search_substring(user_string, substring)
            if index != -1:
                print(f"Substring found at index {index}.")
            else:
                print("Substring not found.")
        elif choice == '7':
            char_to_find = input("Enter the character to find: ")
            index = find_character_index(user_string, char_to_find)
            if index != -1:
                print(f"Character '{char_to_find}' found at index {index}.")
            else:
                print(f"Character '{char_to_find}' not found.")
        elif choice == '8':
            result = convert_to_uppercase(user_string)
            print("Uppercase String:", result)
        elif choice == '9':
            result = convert_to_lowercase(user_string)
            print("Lowercase String:", result)
        elif choice == '10':
            result = is_alphanumeric(user_string)
            if result:
                print("The string is alphanumeric.")
            else:
                print("The string is not alphanumeric.")
        elif choice == '11':
            result = is_palindrome(user_string)
            if result:
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        elif choice == '12':
            old_substring = input("Enter the substring to replace: ")
            new_substring = input("Enter the new substring: ")
            result = replace_substring(user_string, old_substring, new_substring)
            print("Modified String:", result)
        elif choice == '13':
            result = remove_whitespaces(user_string)
            print("String without Whitespaces:", result)
        elif choice == '14':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
