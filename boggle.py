import random
import time

#set_time in seconds 
set_time=180
time_in_minutes=set_time/60

# text formatting 
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
grid = [# first row 
    {   "adjacentCells": [[0,1], [1,0], [1,1]],
        "id": [0,0],
        "active": False,
    },
    {   "adjacentCells": [[0,0], [0,2], [1,0], [1,1], [1,2]],
        "id": [0,1],
        "active": False,
    },
    {   "adjacentCells": [[0,1], [0,3], [1,1], [1,2], [1,3]],
        "id": [0,2],
        "active": False,
    },
    {   "adjacentCells": [[0,2], [1,2], [1,3]],
        "id": [0,3],
        "active": False,
    },  # second row 
    {   "adjacentCells": [[0,0], [0,1], [1,1], [2,0], [2,1]],
        "id": [1,0],
        "active": False,
    },
    {   "adjacentCells": [[0,0], [0,1], [0,2], [1,0], [1,2], [2,0], [2,1], [2,2]],
        "id": [1,1],
        "active": False,
    },
    {   "adjacentCells": [[0,1], [0,2], [0,3], [1,1], [1,3], [2,1], [2,2], [2,3]],
        "id": [1,2],
        "active": False,
    },
    {   "adjacentCells": [[0,2], [0,3], [1,2], [2,2], [2,3]],
        "id": [1,3],
        "active": False,
    },  # third row 
    {   "adjacentCells": [[1,0], [1,1], [2,1], [3,0], [3,1]],
        "id": [2,0],
        "active": False,
    },
    {   "adjacentCells": [[1,0], [1,1], [1,2], [2,0], [2,2], [3,0], [3,1], [3,2]],
        "id": [2,1],
        "active": False,
    },
    {   "adjacentCells": [[1,1], [1,2], [1,3], [2,1], [2,3], [3,1], [3,2], [3,3]],
        "id": [2,2],
        "active": False,
    },
    {   "adjacentCells": [[1,2], [1,3], [2,2], [3,2], [3,3]],
        "id": [2,3],
        "active": False,
    },  # fourth row 
    {   "adjacentCells": [[2,0], [2,1], [3,1]],
        "id": [3,0],
        "active": False,
    },
    {   "adjacentCells": [[2,0], [2,1], [2,2], [3,0], [3,2]],
        "id": [3,1],
        "active": False,
    },
    {   "adjacentCells": [[2,1], [2,2], [2,3], [3,1], [3,3]],
        "id": [3,2],
        "active": False,
    },
    {   "adjacentCells": [[2,2], [2,3], [3,2]],
        "id": [3,3],
        "active": False,
    },]

# frequency of letters occuring in main entries of Concicise Oxford Dict 1995
# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# len(letterFreak)=509
letterFreak=   ['E']*57 + ['J']*1  + ['O']*37 + ['T']*35 + ['Y']*9 + \
    ['A']*43 + ['F']*9  + ['K']*6  + ['P']*16 + ['U']*19 + ['Z']*1 + \
    ['B']*11 + ['G']*13 + ['L']*28 + ['Q']*10  + ['V']*5  + \
    ['C']*23 + ['H']*15 + ['M']*15 + ['R']*39 + ['W']*7  + \
    ['D']*17 + ['I']*38 + ['N']*34 + ['S']*29 + ['X']*1  
   
game_board = {
    0:['','','',''],
    1:['','','',''],
    2:['','','',''],
    3:['','','','']
    }

    # new_board places a random letter in each game_board location chosen from letterFreak
def new_board():
    for iii in range(4):
        for jjj in range(4):
            game_board[iii][jjj]=letterFreak[random.randrange(0,509,1)].upper()
 
 
def print_board(the_board):
    print(f"\n\t\t{color.RED}{color.BOLD}BOGGLE{color.END}\t\tTreat Q likes its QU.")
    print(f"-----------   \t\t\t{time_in_minutes} minutes, good luck!")
    for (iiiii) in the_board:
        print ("|",*the_board[iiiii],"|")
    print("-----------") 


def get_word(): 
    word = input(f"\t{color.PURPLE}Enter word:{color.END} ").upper()
    
    # spell check 
    if dictionary(word) == False:
        if len(word)>4: 
            print(f"{color.RED}{word}{color.END} not in dictionary:",end="")
        else:    
            print(f"{color.RED}{word}{color.END} not in dictionary:\t",end="")
        word = get_word()

    # length check 
    if len(word)<3:
        #print ("3 letters min: \t\t",end="")
        print(f"{color.RED}{word}{color.END} 3 letters min:\t",end="")
        word = get_word()
    
    # after word passes the spell check and length check, handle Qu
    word = word.replace("QU", "Q")

    # letter in grid check 
    letter_list=[]
        #create a list of the grid
        #loop through each letter in word variable 
    for a in game_board:
        for b in game_board[a]:
            letter_list.append(b)
    for c in word:
        if c in letter_list: 
            c=None
        else: 
            print (c, "not in list:\t\t",end="")
            word=get_word()

    return word


# pip3 install requests (in terminal before you can use it as an import)
import requests

# paste the following into browser window to see JSON
# https://www.dictionaryapi.com/api/v3/references/collegiate/json/voluminous?key=97c65a55-7309-481b-a5c6-72f2d66beb45

api_key = '97c65a55-7309-481b-a5c6-72f2d66beb45'

def dictionary(user_word):
    temp="no definition"
    try: 
        word_data = requests.get(
            f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{user_word}?key={api_key}")
        temp = word_data.json()[0]['shortdef']
        return True
        #print(f"\n {color.DARKCYAN}{user_word.upper()}{color.END} is spelled correctly.\n")
    except: 
        return False 
        #print(f"\n{color.RED}{user_word.upper()}{color.END} is not a word.\n")
    # print(word_data.status_code)
    # 200 = successful request 


def check_word(word):
    
    allLetters=[]  # a list of all the locations of letters in user's word
    allLettersList=[]
    for y in word:
        temp=[]
        for key in game_board:
            for z in range(4):
                if y == game_board[key][z]:
                    allLetters.append([game_board[key][z],key,z])
                    temp.append([game_board[key][z],key,z])
        if len(temp)>0:
            allLettersList.append(temp)


    # print("A list of letters in word list: \n")
    # for i in range(len(allLettersList)):
    #     print("\t",allLettersList[i])
    # Example print out - - - - - - - - - - - - - - - - 
    # 	 [['S', 2, 3], ['S', 3, 3]]
    # 	 [['A', 2, 1], ['A', 3, 0], ['A', 3, 2]]
    # 	 [['T', 1, 0], ['T', 1, 1], ['T', 2, 2]]

    # make allLettersList long enough to loop through 10 times
    # allows for up to 10 lettet word 
    for iiii in range(8):
        allLettersList.append([None])

    # create a list of all possile letter combinations 
    combos=[]
    eachCombo=[]
    for ii in allLettersList[0]:
        for jj in allLettersList[1]:
            for kk in allLettersList[2]:
                for ll in allLettersList[3]:
                    for mm in allLettersList[4]:
                        for nn in allLettersList[5]:
                            for oo in allLettersList[6]:
                                for pp in allLettersList[7]:
                                    for qq in allLettersList[8]:
                                        for rr in allLettersList[9]:
                                            eachCombo=ii,jj,kk,ll,mm,nn,oo,pp,qq,rr
                                            #print(eachCombo)
                                            combos.append(eachCombo)
                                            
    for h in range(len(word)-1):
        combo_temp=[]
        for i in combos:
            
            #print("combo action",i)
            for j in grid:
                # print("i:",i[0][1:3])
                # print("id",j['id'])
                if (i[h][1:3])==j['id'] and (i[h+1][1:3]) in j['adjacentCells']:
                    # verify if the current and next letter are adjacent 
                    # print ("legit", i[h][0],i[h+1][0])

                    #check if i (a valid word with valid adjacent letters) has used the same letter position twice 
                    #do this check before appending to combo_temp
                    newlist = [] # empty list to hold unique elements from the list
                    duplist = [] # empty list to hold the duplicate elements from the list
                    for xx in i:
                        # example of xx data:   [['N', 0, 3], ['O', 0, 2], ['N', 0, 3],None,None]
                        if xx != None:
                            if xx not in newlist:
                                newlist.append(xx)
                            else:
                                duplist.append(xx)

                    if len(duplist) == 0:
                        #print("here is i: ",i)
                        combo_temp.append(i)
                   

           
        combos=combo_temp      
    
    #print ("HELP",combos)

    return combos 
    


# combos variable is empty list if word is not found in game_board
# 
def score_word(word,combos,score,word_list): 
    if len(combos) > 0: 
        if 'Q' in word: 
            word = word.replace("Q", "QU")
        # check word_list for duplicates 
        if word in word_list: 
            print(f"{color.RED}{word}{color.END} duplicate",end="")

            # after this list check append word to word_list close to bottom of this function       

        elif len(word)==3 or len(word)==4:
            pts=1
            score+=pts
            
            print(f"{color.YELLOW}{word}{color.END} {pts}-pts",end="")
        elif len(word)==5:
            pts=2
            score+=2
            
            print(f"{color.YELLOW}{word}{color.END} {pts}-pts",end="")
        elif len(word)==6:
            pts=3
            score+=3
            
            print(f"{color.YELLOW}{word}{color.END} {pts}-pts",end="")
        elif len(word)==7:
            pts=5
            score+=5
            
            print(f"{color.YELLOW}{word}{color.END} {pts}-pts",end="")
        else:
            pts=11
            score+=11
            
            print(f"{color.YELLOW}{word}{color.END} {pts}-pts",end="") 

        word_list.append(word)
    else:
        #print(word,"not legit",end="")
        print(f"{color.RED}{word}{color.END} not legit",end="")
        #get_word()
    
    return score, word_list 


def main():
    # create a list of words and check for duplicates 
    word_list=[]

    import time    
    start_epoch_time = int(time.time())

    total=0
    new_board()  
    print_board(game_board)
    score=0
    # get_word returns word
    # check_word returns word,combos

    print("\t\t\t",end="")
   
    for aa in range(100):

        word=get_word()
        
        combos=check_word(word) # returns a list of legit letter sequences for word 
        score,word_list=score_word(word,combos,score,word_list)
        total = total + score
        print ("\tScore:",score,end="")
        current_epoch_time= int(time.time())
        if start_epoch_time + set_time < current_epoch_time:
            print ("\n\nGAME OVER")
            break

main()
