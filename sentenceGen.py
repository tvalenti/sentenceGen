import random
"""
Program: sentenceGen.py
Author: Tom
generates a user defined amount of sentences based on the items in the tuples
"""
# vocab: wors in 4 different parts of speech
articles    = ("A", "THE")
nouns       = ("BOY", "GIRL", "BAT", "BALL")
verbs       = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():
    """Builds and returns a sentence"""
    return nounPhrase() + " " + verbPhrase() + "."

def nounPhrase():
    """Builds and returns a noun Phrase"""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase"""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase"""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input a number of sentences to generate"""
    number = int(input("Enter the number of sentences >> "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()