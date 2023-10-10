import pandas
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

dataframe = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in dataframe.iterrows()}
#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_alphabet():
    word = input("Insert the word: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in word]
    except:
        print("Sorry, only letters in the alphabet please.")
        generate_alphabet()
    else:
        print(phonetic_list)

generate_alphabet()