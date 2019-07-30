


## ATTENTION! Put the name of the source txt file at line 17
## Size of the chuncks can be replace at line 45




import re, statistics

###########################
##
## OPEN AND READ THE FILE
##
###########################
txtfile = open('MYFILE.txt', 'r', encoding='utf-8')
txt = txtfile.read()


###########################
##
## PREPARE THE TEXT
##
###########################
# everything that is not a letter is replaced by a space and all to lowercase
txt_pre = re.sub('[^A-Za-z]+', ' ', txt).lower()

# create a list of tokens
list_tokens = []
for tkn in txt_pre.split():
	list_tokens.append(tkn)

# count the number of total tokens
tot_tokens = len(list_tokens)
print("Number of total tokens: " + str(tot_tokens))


###########################
##
## CALCULATE TTRs AND THEIR STATISTICAL MEAN
##
###########################
# Divide text into chuncks of 1000 tokens
chuncks = [list_tokens[i:i+1000] for i in range(0, len(list_tokens), 1000)]
print("Number of chuncks of 1000 tokens, for control: " + str(len(chuncks)))

# Calculate the TTR for each chunck and add it to the list TTRs
TTRs = []
for chunck in chuncks:
	tokens = len(chunck)
	types = len(set(chunck))  # from list to set = from many to unique
	TTR = types / tokens * 100
	TTRs.append(TTR)
# print(TTRs)

# calculate the statistical mean of all TTRs
STTR = statistics.mean(TTRs)
print("STTR is: " + str(STTR))

