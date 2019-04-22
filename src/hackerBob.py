hashed_password = "qbt"
unhashed_password = "dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"
rotate_by = 13
hashed_guess = ""
i = 0

password_guess = input("Take a guess at the password you hacker you ")

while i < len(password_guess):
    letter = password_guess[i]
    i = i + 1

    if letter not in alphabet:
        hashed_guess = hashed_guess + letter
    else:
        index_in_alphabet = alphabet.index(letter)
        new_index = index_in_alphabet + rotate_by
        if new_index >= len(alphabet):
            new_index = new_index - len(alphabet)
        hashed_guess = hashed_guess + alphabet[new_index]
        print(hashed_guess)
        break

while hashed_guess.index(0) != hashed_password.index(0):
    print("You do not have the first character correct, keep guessing")
    elif hashed_guess.index(0) == hashed_password.index(0):
        print("You have guessed the first character correctly")
        while hashed_guess.index(1) != hashed_password.index(1):
            print ("You do not have the second chracter correct, keep guessing ")
            elif hashed_guess.index(1) == hashed_password.index(1):
                print ("You have guessed the second character correctly ")
                    while hashed_guess.index(2) != hashed_password.index(2):
                        print ("You have guessed the final letter incorrectly")
                        elif hashed_guess.index(3) == hashed_password.index(3):
                            print ("You have guessed the final letter correct")

                    
        

# def crack_password(password):
#     passwd = list(thePassword)
#     for i in range(0, 10):
#         for j in range(0,10):
#             for k in range(0,10):
#                 for l in range(0,10):
#                     if str(i) == passwd[0] and str(j) == passwd[1] and str(k) == passwd[2] and str(l) == passwd[3]:
#                         mylist=[str(i),str(j),str(k),str(l)]
#                         code = "".join(mylist)
#                         #print mylist
#                         #print code
#     print("Four Digit Password: {}".format(code))






# print("You have guessed the password correctly")
# print("You have got the first character correct")
# print("You have got the second character correct")
# print("You have got the third character correct")

# #calling function with correct password
# crack_password(dog)
# # USER INPUTS PASSWORD GUESS
# # PASSWORD GUESS GETS HASHED
# #HASHED GUESS GETS COMPARED TO STORED PASSWORD (WILL ADD HASHED PASSWORD EXTRA LAYER)