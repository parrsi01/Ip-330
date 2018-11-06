from flask import Flask
from flask import redirect, url_for
from flask import request, make_response
from flask import render_template
from itertools import permutations as p
#scrabble word dictionary

app = Flask(__name__)

file = open('/usr/share/dict/american-english', 'r')
file = open('/usr/share/dict/british-english','r')

american = set(line.strip() for line in open('/usr/share/dict/american-english', 'r'))
british = set(line.strip() for line in open('/usr/share/dict/british-english', 'r'))

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    

@app.route('/', methods=['GET','POST'])
def scrabble():
    #input should be 7 individual id characters from user
    return render_template('scrabble.html')

@app.route('/permutation', methods=['GET','POST'])
def permutation():
    #List to store letters from the user
    permutation = []
    for letter in ["letter1", "letter2", "letter3", "letter4", "letter5", "letter6", "letter7"]:
        if request.form.get(letter) != '':
            permutation.append(request.form.get(letter))
    wordlist = list(p(permutation)) #list of tuples
    newlist = []
    length = len(permutation)
    for word in wordlist:
        newlist.append(''.join(word))
    #sets
    wordset = set(newlist)
    american_list = []
    british_list = []
    #Check if string in wordset is a word in american/british dictionary. Then return it. For loop + if-statement
    for word in wordset:
        if word in american:
            american_list.append(word)
    #then return the word to the html page scrabble.html. --> Almost Done
    #Use scrabble dictionary to score points from word and return the score and length.
    return render_template('scrabble.html', sum = total, result1 = american_list, myset = wordset , words = newlist, lengthword = length)
        



if __name__ == '__main__':
    app.run()