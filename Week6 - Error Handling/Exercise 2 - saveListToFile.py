def save_list2file(sentences, filename):
    for char in sentences:
        filename.write(char+"\n")
    pass

sentences = "Hello world"
file = open('filename.txt','w')
print(save_list2file(sentences,file))