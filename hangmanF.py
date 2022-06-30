# Problem Set 2, hangman.py
# Name: Cruz
# Time spent: 5/28  - 6/05

import random
import string
import re

WORDLIST_FILENAME = "words.txt"



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()
random_word = choose_word(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    c = 0 
    for char in secret_word:
      if char in letters_guessed:
        c += 1
    if c == len(secret_word):
      return True
    else:
      return False

#print(is_word_guessed( 'apple' , ['a','p','p','l','e']))




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s = []
    for char in secret_word:
      if char in letters_guessed:
        s.append(char)
    ans=''
    for char in secret_word:
        if char in s:
            ans += char
        else:
            ans += '_ '
    return ans

#print(get_guessed_word( 'apple', ['e', 'i', 'k', 'p', 'r', 's'] ))
      
        



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_alph = list(string.ascii_lowercase)
    for letter in letters_guessed:
        list_alph.remove(letter)
    return  ' '.join(list_alph)


    
#print(get_available_letters( ['e', 'i', 'k', 'p', 'r', 's'] ))

# def guessNotInWord(input_guess, s_word):
#   #not a letter in word?
#   if input_guess not in s_word:
#     return True

def valid_input(input_guess):
  pattern = re.compile(r"[a-z]+")
  if re.fullmatch(pattern , input_guess):
    return True
  else:
    print('invalid input')
    return False

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"


    print('--------------------------')
    print('Welcome to my game of hangman')
    print('I am thinking of a word that is', len(secret_word), 'letters long')

    global letters_guessed
    guesses_left = 6
    letters_guessed = []  
    
    while guesses_left > 0:

      if is_word_guessed( secret_word, letters_guessed):
        print('-----------------------')
        print('---congrats you won----')
        print('-----------------------')
        break
      else: 
        print('-----------------------')
        print('you have', guesses_left, 'guesses left')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = str(input('please enter you letter: ')).lower()

        if guess in letters_guessed:
          print('oops, you aleady entered that letter, try again', get_guessed_word(secret_word, letters_guessed))

        elif guess in secret_word and guess not in letters_guessed:
          letters_guessed.append(guess)
          print('good guess:', get_guessed_word(secret_word, letters_guessed))

        elif not valid_input(guess):
          print("")

        else: #the guess is not in letters guessed and not in secret word
          letters_guessed.append(guess)
          print(guess, 'is not in my word', get_guessed_word(secret_word,letters_guessed))
          guesses_left -= 1


      if guesses_left == 0:
          print("-------------")
          print("Sorry, you ran out of guesses. The word was else.", secret_word)
          break
      else: 
        continue



 
if __name__ == "__main__":

    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
