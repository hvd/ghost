import sys
import random

wordbuffer = ''

#Flag to indicate if there is a game winner.
gamewinner = False

#These are actually words with odd number of letters so optimal for computer
optimalwords = {}
evenwords =  {}
wordset = set()
player1 = 'human'
player2 = 'computer'


def isloser(word):
    if word in wordset and len(word)%2==0:
        print player1 + "  wins."
        sys.exit()
    elif word in wordset and len(word)%2!=0:
        print player2 + " wins."
        sys.exit()
    else:
        print "gameplay continues:"

def playermove(currentword):
    humanletter = raw_input('Enter your letter human:')
    currentword = currentword + str(humanletter).strip()
    currentword = currentword.lower()
    print "human plays " + currentword
    isloser(currentword)
    if not gamewinner:
        computermove(currentword)

def optimalmove(currentword):
    firstletter=currentword[0]
    listofwords = optimalwords.get(firstletter)
    listofopponentwords = evenwords.get(firstletter)
    subsetopponent = [w for w in listofopponentwords if currentword in w]
    #subset of winning words.
    subset = [s for s in listofwords if currentword in s]
    # Remove all losing plays
    for i in subsetopponent:
        for j in subset:
            if i in j:
                    subset.remove(j)
    
    #strategy to lengthen gameplay in case no winning word exists
    if not subset:
            max_length,longest_element = max([(len(x),x) for x in subsetopponent])
            wordtoplay=longest_element
            partword = currentword + wordtoplay[len(currentword)] 
            return partword
    index = random.randint(0,len(subset)-1)
    wordtoplay = subset[index]
    partword = currentword + wordtoplay[len(currentword)]    
    print "Computer Plays " + currentword + wordtoplay[len(currentword)]
    return partword
    

def computermove(currentword):
    partword = optimalmove(currentword)
    isloser(partword)
    if not gamewinner:
        playermove(partword)

    

def letsplayghost():
    print "Spooky Times human, lets play ghost"
    currentword = ''
    playermove(currentword)


#Read the words and store them in a dict for later comprehension
def init():
    f = open('WORD.LST', 'r')
    for line in f:
        word = str(line)
        word = word.strip()
        wordlength = len(word)
        
        letter = word[0]
#    print(wordlength)
        if wordlength%2!=0 and wordlength>4:
            wordset.add(word)
            if letter in optimalwords:
                wordlist = optimalwords[letter]
                wordlist.append(word)
                optimalwords[letter] = wordlist
            else:
                optimalwords[letter] = [word]
        elif wordlength%2==0 and wordlength>4:
            wordset.add(word)
            if letter in evenwords:
                wordlist = evenwords[letter]
                wordlist.append(word)
                evenwords[letter] = wordlist
            else:
                evenwords[letter] = [word]
    letsplayghost()





init()
#for k,v in optimalwords.items():
#    print(k,v)
#    print('\n')

#for k,v in evenwords.items():
#    print(k,v)
#    print('\n')