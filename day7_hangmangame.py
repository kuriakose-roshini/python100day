import random
#instead you can add a file with word list and import it from there - from file_name import wordlist 
world_list = ["hello","hi","bonjour","namaste"]
chosen_word = random.choice(word_list)
#print chosen word

guess = input("Guess a letter:").lower()
print guess
