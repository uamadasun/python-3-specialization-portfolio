"""This code takes in a CSV file of twitter data and analyzes it to see how positive or negative a particular tweet is. It creates a CSV file that will contain the "Number of retweets, number of replies, positive score (how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. This file can be uploaded to any spreadsheet program to create a visual graph or anything else the user wants to use it for."""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#gets the list of positive and negative  words that can be used
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#takes away punctuation marks from the tweet and leaves just the words
def strip_punctuation(st):
    for ch in st:
        if ch in punctuation_chars:
            st = st.replace(ch,"")
    return st 


#gets the count of how many positive and negative words are in the tweet
def get_pos(st):
    count = 0
    st = (strip_punctuation(st)).split()
    for wrd in st:
        if wrd.lower() in positive_words:
            count += 1
    return count

def get_neg(st):
    st = (strip_punctuation(st)).split()
    count = 0
    index = 0
    while index < len(st):
        if st[index] in negative_words:
            count += 1
        index += 1
    return count


#opens the file with the tweets and breaks up the text by lines and appends it to a new list
f = open('project_twitter_data.csv', 'r')
twitterFile = f.readlines()


newTwitterFile = []
for lin in twitterFile:
    lin = lin.strip().split(',')
    newTwitterFile.append(lin)
    

#creates a new file that will contain the Number of Retweets, Number of replies, Positive Score, Negative Score, and Net score info
newFile = open('resulting_data.csv', 'w')

#Header for newFile below:
newFile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
newFile.write('\n')
print(newFile)

#Rows below for newFile:
for item in newTwitterFile[1:]:
    retweets = item[1]
    replies = item[2]
    strip_punctuation(item[0])
    pos = get_pos(item[0])
    neg = get_neg(item[0])
    netScore = pos - neg
    rowString = ('{}, {}, {}, {}, {}'.format(retweets, replies, pos, neg, netScore))
    newFile.write(rowString)
    newFile.write('\n')
