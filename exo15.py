def check_vowels(user_input):
   
    vowels = ['a', 'e', 'o']
    
    for vowel in vowels:
        if vowel in user_input:
            print(f"The vowel '{vowel}' is present in the string.")
        else:
            print(f"The vowel '{vowel}' is not present in the string.")


user_input = input("Please enter a string in lowercase: ")
check_vowels(user_input)