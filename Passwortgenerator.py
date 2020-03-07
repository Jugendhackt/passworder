import random
def wordlistget():
    file = open('Wordlist.txt', 'r', encoding='UTF-8')
    wordlist = file.readlines()
    return wordlist

def create(length = 20, space = "", replacerule = []):
    
    wordlist = wordlistget()
    password=random.choice(wordlist)
    password = password.replace('\n','')
    while length > len(password):
        password=password + space
        password=password + random.choice(wordlist)
        for x in replacerule:
            if len(x)>1:
                password=password.replace(x[0], x[1])
        password = password.replace('\n','')
    return password
if __name__ == "__main__":
    password=create()
    print(password)