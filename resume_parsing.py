import nltk
import os

resume_folder = '/home/anantharam/Deepika/Resumes_text'
resumes = os.listdir(resume_folder)

for resume_path in resumes:
	document = open(resume_folder + "/" + resume_path)

	x = document.read()

	x = x.replace("\n", " ")
	print(x)

	job_keyWords = ['Python', 'C', 'Finance']

#lines = x.split('\n')
#words = []
	
	s = ""
    
#	temp = open(keyword_content, 'a+')
	words = nltk.word_tokenize(x)
	print(words)

	for word in words:
		if word in job_keyWords:
			f = open(word+'.txt', 'a+')
			#print(s)
			if word not in temp:
				s += word
				f.write(resume_path + ",")
			f.close()