import urllib2

response = urllib2.urlopen('http://www.gutenberg.org/files/135/135-h/135-h.htm')
html = response.read()
sentence = "this is a pretty sad sentence"


sad = 0
words =0

listofwords = sentence.split(' ')
for word in listofwords:
    print word
    words=words+1
    if word == 'sad':
        break
    



