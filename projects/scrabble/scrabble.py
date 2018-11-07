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
    wordlist = []
    for i in range(7):
        wordlist+= list(p(permutation,i+1))
    print(wordlist)
    newlist = []
    for word in wordlist:
        newlist.append(''.join(word))
    #sets
    wordset = set(newlist)
   
    return_list = []
    #Check if string in wordset is a word in american/british dictionary. Then return it. For loop + if-statement
    total = 0
    mydictionary = request.form.get('dictionary')
    print(mydictionary)
    if mydictionary == 'british':
        #if requests.args.get == british :
        for word in wordset:
            if word in british:
                return_list.append(word)
    else:
        if mydictionary == 'american':
            for word in wordset:
                if word in american:
                    return_list.append(word)

    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

    return_total = []
    for word in return_list:
        for i in word:
            total = total+score[i]
        return_total.append(str(total))
    

    #Iterate through permutations to  find smaller words in 7 letters
    #then return the word to the html page scrabble.html. --> Almost Done
    #Use scrabble dictionary to score points from word and return the score and length.
    return render_template('scrabble.html', count = return_total, result = return_list, myset = wordset , words = newlist)
        



if __name__ == '__main__':
    app.run() 