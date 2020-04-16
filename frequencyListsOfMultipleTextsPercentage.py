
'''
PREPARE TEXTS
- From PDF, use pdftotext
	pdftotext 'ESG traduzione completa Infurna Lagomarsini.pdf' ESG.txt
- From Word, save as .txt
'''

############# IMPORT PACKAGES AND DEFINE FUNCTIONS #############

import re

def percentage(part, whole):
  return round(100 * part/whole, 3) # calculate percentage and print only 3 decimals



############## PREPARE DATA #############

# load text files and lower case everything
lanc_AP = open('Lancelot/AP_Lancelot-traduz_APRILE2020_AP.txt', 'r').read().lower()
lanc_APF = open('Lancelot/APF_Lancelot_XXVIa_LIIa99_anatole.txt', 'r').read().lower()
lanc_ESp = open('Lancelot/ESp_LANCELOT_MichaLXIa_95-LXIII.txt', 'r').read().lower()
lanc_MI = open('Lancelot/MI_TrLanc_infurna.txt', 'r').read().lower()
lanc_NM = open('Lancelot/NM_LancillottoMichaVol.VII_NM_13.4.2020.txt', 'r').read().lower()

# replace apostrophe, remove punctuation and other characters, and split the text in words
apo = "\'|\’|\’"
regex = "\*|[0-9]|\(|\)|\.|,|;|-|:|\[|\]|\"|«|»|<|>|\/|§|\?|‒|–|“|―|!|—|‘|’|”"
wordlist1 = re.sub(regex, "", re.sub(apo, " ", lanc_AP)).split()					
wordlist2 = re.sub(regex, "", re.sub(apo, " ", lanc_APF)).split()					
wordlist3 = re.sub(regex, "", re.sub(apo, " ", lanc_ESp)).split()					
wordlist4 = re.sub(regex, "", re.sub(apo, " ", lanc_MI)).split()					
wordlist5 = re.sub(regex, "", re.sub(apo, " ", lanc_NM)).split()					



############# PROCESS DATA #############

# create a complete list of words from all texts
allwords = wordlist1 + wordlist2 + wordlist3 + wordlist4 + wordlist5

# this is only used to check if the word has been already included in the list
checkedWords = [] 

# list of results
wordfreq = [] 
wordfreqIfDiff = []

for w in allwords:  

	if (w not in checkedWords): # to avoid repating words already processed	
		checkedWords.append(w) 
		
		# percentage of occurrences in text
		w1perc = percentage(wordlist1.count(w),len(wordlist1))
		w2perc = percentage(wordlist2.count(w),len(wordlist2))
		w3perc = percentage(wordlist3.count(w),len(wordlist3))
		w4perc = percentage(wordlist4.count(w),len(wordlist4))
		w5perc = percentage(wordlist5.count(w),len(wordlist5))

		# just number of occurrences in text
		w1 = str(wordlist1.count(w))
		w2 = str(wordlist2.count(w))
		w3 = str(wordlist3.count(w))
		w4 = str(wordlist4.count(w))
		w5 = str(wordlist5.count(w))
		wordfreq.append(w + '\t' + str(w1perc) + '\t' + w1 + '\t' + str(w2perc) + '\t' + w2 + '\t' + str(w3perc) + '\t' + w3 + '\t' + str(w4perc) + '\t' + w4 + '\t' + str(w5perc) + '\t' + w5 + '\n')

		# if percentage values have a difference higher than $diff
		diff = 0.3
		if (
				abs(w1perc-w2perc)>diff or 
				abs(w2perc-w3perc)>diff or 
				abs(w1perc-w3perc)>diff or
				abs(w1perc-w4perc)>diff or
				abs(w1perc-w5perc)>diff or
				abs(w2perc-w4perc)>diff or
				abs(w2perc-w5perc)>diff or
				abs(w3perc-w4perc)>diff or
				abs(w3perc-w5perc)>diff or
				abs(w4perc-w5perc)>diff
			):
			wordfreqIfDiff.append(w + '\t' + str(w1perc) + '\t' + w1 + '\t' + str(w2perc) + '\t' + w2 + '\t' + str(w3perc) + '\t' + w3 + '\t' + str(w4perc) + '\t' + w4 + '\t' + str(w5perc) + '\t' + w5 + '\n')


alphabeticalWordfreq = sorted(wordfreq)   		# sort the list in alphabetical order
alphabeticalWordfreqIfDiff = sorted(wordfreqIfDiff)



############# PRINT RESULTS ON CSV FILE #############

o = open('frequencyListsOfMultipleTextsPercentage.csv', 'w')
o.write('' + '\t' + 'AP' + '\t \t' + 'APF' + '\t \t' + 'ESp' + '\t \t' + 'MI' + '\t \t' + 'NM' + '\t' + '\n')
for x in alphabeticalWordfreq:
	o.write(x)
o.close()



############# PRINT RESULTS WHEN VALUES ARE DIFFERENT ON CSV FILE #############

o = open('frequencyListsOfMultipleTextsPercentageIfDiff' + str(diff) + '.csv', 'w')
o.write('' + '\t' + 'AP' + '\t \t' + 'APF' + '\t \t' + 'ESp' + '\t \t' + 'MI' + '\t \t' + 'NM' + '\t' + '\n')
for x in alphabeticalWordfreqIfDiff:
	o.write(x)
o.close()


