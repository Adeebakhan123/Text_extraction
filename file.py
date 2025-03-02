print(" welcome in game")
import random

def get_list_of_words(path):

    file=open(path, 'r')
    return file.read().splitlines()


words = get_list_of_words("D:\kik task\mit.edu_~ecprice_wordlist.10000.txt")
#print(words)

random_word = random.choice(words)
rm=list(random_word)
print(rm)
for i in rm:
    
print(rm)



