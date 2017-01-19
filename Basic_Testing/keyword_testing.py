

def main():

    fk = open('keywords.txt')
    keywords = []

    for word in fk:
        keywords.append(word)

    sFormat = ' '.join(keywords)
    keywords = sFormat.split('\n ')

    print(keywords)

if __name__ == '__main__':main()