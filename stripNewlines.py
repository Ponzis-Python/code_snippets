#strip newlines
#https://stackoverflow.com/questions/11664443/how-do-i-read-multiple-lines-of-raw-input-in-python
print("Paste string here")
sentinel = ''

for line in iter(input, sentinel):
    pass

daString = '\n'.join(iter(input, sentinel))
#daString = daString.replace('\n', ' ').replace('\r', '')
print(daString)