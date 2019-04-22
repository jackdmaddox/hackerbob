HASHED_PASSWORD = "ubefr"

def encrypt(the_input):
    i = 0
    hashed_guess = ""
    rotate_by = 13
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while i < len(the_input):
        letter = the_input[i]
        i = i + 1
        if letter not in alphabet:
            hashed_guess = hashed_guess + letter
        else:
            index_in_alphabet = alphabet.index(letter)
            new_index = index_in_alphabet + rotate_by
            if new_index >= len(alphabet):
                new_index = new_index - len(alphabet)
            hashed_guess = hashed_guess + alphabet[new_index]
    return hashed_guess

def crack_password(password):
    password_guess = input("guess my password: ")
    i = 0
    for char in password_guess:
        coded = encrypt(char)

        if coded == password[i]:
            print(f"you guessed {char} correctly!")
            i += 1
        else: 
            print(f"{char} is not correct")
            i += 1

    coded_guess = encrypt(password_guess)
    if coded_guess == password:
        print("You win")
    else:
        print("loser)")

crack_password(HASHED_PASSWORD)

