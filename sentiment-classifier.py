
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
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

def strip_punctuation(st):
    for ch in st:
        if ch in punctuation_chars:
            st = st.replace(ch,"")
    return st 

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
            count = count + 1
        index = index + 1
    return count

f = open('project_twitter_data.csv', 'r')
twitterFile = f.readlines()
#print(twitterFile)

newTwitterFile = []
for lin in twitterFile:
    lin = lin.strip().split(',')
    newTwitterFile.append(lin)
    
#print (newTwitterFile)

newFile = open('resulting_data.csv', 'w')

#Header below:
newFile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
newFile.write('\n')
print(newFile)

#Rows below:
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
