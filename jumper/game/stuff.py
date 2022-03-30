'''
Authors:
Logan Crossley
John Pischke
Seth Whetten
Dawson Packer 

Description:
This is our stuff class. It scans for repeats of letters in the guessed word.
'''
word = 'puppy'
guess = 'p'

times_letter_is_in_word = 0
return_value = []
for i in range(len(word)):
    letter = word[i]
    letter_index = i
    if guess == letter: 
        return_value.append(letter_index)
        times_letter_is_in_word += 1

if times_letter_is_in_word == 0:
    return_value.append(-1)
print(return_value)