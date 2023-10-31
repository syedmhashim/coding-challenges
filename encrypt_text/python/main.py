def encrypt_text(s, k):
    number_of_letters = 26
    lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alphabets = lowercase_alphabets.upper()
    
    char_arr = [*s]
    for i in range(len(char_arr)):
        if char_arr[i] in lowercase_alphabets:
            position = lowercase_alphabets.index(char_arr[i])
            char_arr[i] = lowercase_alphabets[(position+k)%number_of_letters]
        
        if char_arr[i] in uppercase_alphabets:
            position = uppercase_alphabets.index(char_arr[i])
            char_arr[i] = uppercase_alphabets[(position+k)%number_of_letters]
    return ''.join(char_arr)

if __name__ == "__main__":
    k = 3
    test_cases = [
        "There's-a-starman-waiting-in-the-sky",
    ]
    print(f"K: {k}")
    for i in range(len(test_cases)):
        print("Test case:")
        print(test_cases[i])
        
        print("Result:")
        print(encrypt_text(test_cases[i], k))