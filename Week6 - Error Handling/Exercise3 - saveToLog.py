def save_to_log(entry, logfile):
    open('logfile.txt','a')
    logfile.write(entry)
    logfile.close()
def read_log(file):
    file = open('logfile.txt','r')
    upper = str(file.read()).upper()
    return upper
entry = "My name is"
log = open('logfile.txt','w')
log.write("Hello world ")
print(save_to_log(entry,log))
print(read_log(log))