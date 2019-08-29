from nltk.corpus import words
import time

letters = list("abcdefghijklmnopqrstuvwxyz")
to_decrypt = input("Enter a string to decrypt: ").lower()


start_time = time.time()
processes = []

# Variables to keep track of the result - the most likely decrypted string
most_likely_num = 0
most_likely = to_decrypt
most_likely_string = ""
shifted = 0

# Decrypt a word inside the string
def decrypt_word(word, shift):
    decrypted = ""

    for letter in word:
        # If the letter is not in the letters list, keep it as it is
        if letter not in letters:
            decrypted += letter
            continue
        
        # If the index is too high, re-start from the beginning
        index = letters.index(letter)
        if index + shift > len(letter):
            index -= len(letters)

        # Add the decrypted letter to the decrypted string
        decrypted += letters[index + shift]

    return decrypted

# Decrypt the string
def decrypt_string(string, shift):
    global most_likely_num
    global most_likely
    global shifted

    likely = 0
    decrypted = decrypt_word(to_decrypt, shift).split(" ")

    # Calculate the likelihood of the words being actual english words
    for word in decrypted:
        if word in words.words():
            likely += 1

    # If this word has higher likelihood than the most likely word,
    # set this word as the new most likely word
    if likely > most_likely_num:
        most_likely_num = likely
        most_likely = decrypted
        shifted = i

if __name__ == "__main__":
    # Loop through all the possible shift according to the size of the letters array
    for i in range(1, len(letters)):
        decrypt_string(to_decrypt, i)

    # Turn the most likely array into a string
    for word in most_likely:
        most_likely_string = "{} {}".format(most_likely_string, word)
    most_likely_string = most_likely_string.strip()

    # Print the most likely decrypted string
    print("The decrypted string is most likely:")
    print(most_likely_string)
    print("Shifted {} times".format(shifted))
    print("The program took {0:.3f} seconds to finish.".format(time.time() - start_time))