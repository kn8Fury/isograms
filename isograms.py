#! /usr/bin/python3
''' Searches for isograms in source file and writes them to the
corresponding 'isograms_xx.txt' file.
'''

def IsIsogram(Word):
	if(not Word.isalpha()): return False
	LettersSeen = set()
	for Letter in Word:
		if(Letter in LettersSeen): return False
		else: LettersSeen.add(Letter)
	return True

def OpenFiles():
	global Isograms
	Isograms = {}
	# map length to file objects
	for i in range(3,14):
		Isograms[i] = open('isograms_{:02}.txt'.format(i),'a+')

def CloseFiles():
	for key in Isograms:
		Isograms[key].close()

def main():
	OpenFiles()
	#src = 'words_webster.txt'
	src = 'words_git.txt'
	with open(src,'r') as WordFile:
		WordLen = 0
		for Line in WordFile.readlines():
			Word = Line.rstrip()
			if(IsIsogram(Word)):
				WordLen = len(Word)
				if( WordLen > 2 and WordLen < 14 ):
					Isograms[WordLen].write(Word + '\n')
	CloseFiles()

if __name__ == "__main__":
	main()