#! /usr/bin/python3
''' Extracts definition words from 'webster.txt'. Only non-repeating words
with all alphabets are considered, i.e., no word endings or beginnings.
'''

def main():
	# open webster file, create and open 'words_webster.txt'
	with open('webster.txt',encoding='ISO-8859-1') as Webster, \
			open('words_webster.txt','a+') as Words:
		Temp = ""
		for Line in Webster.readlines():	# for each line in file
			Word = Line.rstrip('\n')	# rstrip line
			if Word:	# if not empty
				if Word.isalpha():	# words with all alphabets
					if Word.isupper():	# words in all uppercase
						if Word != Temp:	# unrepeating words
							# update temp and add line.to 'words_webster.txt' in lower case
							Temp = Word
							Words.write(Word.lower() + '\n')

if __name__ == "__main__":
	main()