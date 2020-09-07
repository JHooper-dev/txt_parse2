from percenter import percenter
from student import student
import os

punc = "!()-[]{};:\,<>./?@#$%^&*_~"
common_words = ["is", "a", "then", "that", "there", "to", "if", "this", "it", "it's", "but", "are", "these", "and", "of", "i", ""]

student_list = []

wanted_common_words_removed = True
wanted_caps_filter = True

Path = "C:\\Users\\royal\\source\\repos\\txt_parse2\\txt_parse2\\Responses\\"
filelist = os.listdir(Path)
for x in filelist:
	if x.endswith(".txt"):
########## store student's name
		student_name = str(x).replace(".txt", "").replace("_", " ")
########## open and read file
		temp = open(Path + x, "r")
		temp2 = temp.read()
########## remove punctuation
		for i in temp2:
			if i in punc:
				temp2 = temp2.replace(i, "")
########## remove new lines
		temp2 = temp2.replace('\n', " ")
########## caps filter
		if wanted_caps_filter:
			temp2 = temp2.lower()
########## split into list
		doc = temp2.split(" ")
########## sort list
		doc = sorted(doc)
########## common word remover
		doc2 = []
		i = 1
		j = 1
		if wanted_common_words_removed:
			com_count = 0
			while i <= len(doc):
				if doc[i-1] not in common_words:
					doc2.append(doc[i-1])
				else:
					if doc[i-1] != "":
						com_count += 1
				i += 1
		else:
			doc2 = doc
########## word counter
		i = 1
		j = 1
		words = []
		while i <= len(doc2):
			if (i-1) == 0:
					words.append(percenter(doc2[i-1], doc2.count(doc2[i-1]))) # always adds first word
			if words[j-1].word != doc2[i-1]: # checks if current word = previous word
				words.append(percenter(doc2[i-1], doc2.count(doc2[i-1])))
				j += 1
			i += 1
########## bubble sorts counted words from greatest to least
		swapped = True
		while swapped:
			swapped = False
			for i in range(1, len(words)):
				if words[i-1].count > words[i].count:
					tp = words[i - 1]
					words.remove(tp)
					words.insert(i, tp)
					swapped = True
		words.reverse()
########## creates student object with above data		
		student_list.append(student(student_name, temp, doc2, words, com_count, wanted_common_words_removed))

print(student_list[0].name +"\n"+ student_list[1].name + "\n\n")
		

for i in range(0, len(student_list)):
	print("This is " + student_list[i].name + "'s list of words: \n-")
	print(str(student_list[i].commons) + " common words were removed!\n-")

	for j in range(0, len(student_list[i].freq)):
		print("The word \"" + student_list[i].freq[j].word + "\" is used " + str(student_list[i].freq[j].count) + " times.")

	print("\n\n")

temp.close()
