import random

with open("english_words.txt", encoding="utf8") as f:
    words_perma = f.read().splitlines() 
#filter out all words that are different length from the answers length
#find the most common letter in remaining words
#check if the most common letter is in the answer
#   if true remove all words from list that dont have the letter
#   if false remove all words that do have the letter
#check if the length of the list is 1
#   if true then the remaining word is the answer
#   if false its messed up somewhere

def filter_length(answer_len, words):
    remove = []
    for word in words:
        if len(str(word)) != answer_len:
            remove.append(word)
    for word in remove:
        words.remove(word)
    return words

def find_letter(words):
    alphabet_count = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0,
    }
    for word in words:
        for letter in word:
            alphabet_count[letter.lower()] += 1
    return({k: v for k, v in sorted(alphabet_count.items(), key=lambda item: item[1])})

def check_letter(words, word, letter, word_pos, answer, remove):
    answer_pos = [pos for pos, char in enumerate(answer) if char == letter]
    if word_pos != answer_pos:
        remove.append(word)
        print(remove)

used_letter = []
def filter_if_letter_in(words, answer):
    global used_letter, wrong_turns

    alphabet_count = find_letter(words)
    letter_found = False
    index = 1
    while not letter_found:
        letter = list(alphabet_count)[len(alphabet_count)-index]
        if letter in used_letter:
            index += 1
        elif letter not in used_letter:
            used_letter.append(letter)
            letter_found = True
    #removes the words that have the letter in it
    #wrong turn += 1 because the letter is not in the word
    if letter not in answer:
        wrong_turns += 1
        remove = []
        for word in words:
            if letter in word:
                remove.append(word)
        for word in remove:
            words.remove(word)
        return(words)
    #removes the words that dont have the letter in it
    remove = []
    for word in words:
        if letter not in word:
            remove.append(word)
        else: # removes word that the places of letters dont match
            word_pos = [pos for pos, char in enumerate(word) if char == letter]
            answer_pos = [pos for pos, char in enumerate(answer) if char == letter]
            if word_pos != answer_pos:
                remove.append(word)
    for word in remove:
        words.remove(word)
    return(words)

wrong_turns = 0
def run(answer, answer_len, words):
    global wrong_turns
    
    
    print("THE RANDOM WORD IS:", answer)
    words = filter_length(answer_len, words)
    i = True
    while i:
        words = filter_if_letter_in(words, answer)
        if len(words) == 1:
            i = False

    print("THE WORD I FOUND IS", words[0])
    print("AMOUNT OF WRONG GUESSES", wrong_turns)
    input("Enter to exit")
    return wrong_turns



answer = str(input("input the word > "))
answer_len = len(answer)

run(answer, answer_len, words_perma)
