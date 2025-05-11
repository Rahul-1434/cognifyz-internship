f=open('words.txt','r')
sentense=f.readlines()
words=''.join(sentense).split()
for word in sorted(list(set(words))):
    print(word,':',words.count(word))