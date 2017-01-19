
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():

    # print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

    fk = open('keywords.txt')
    keywords = []

    for word in fk:
        keywords.append(word)

    sFormat = ' '.join(keywords)
    keywords = sFormat.split('\n ')

    fh = open('dexter.java')
    statement = []

    # temp = 'I love bananas'
    # statement = temp.split(' ')
    # print(statement)

    for line in fh:
        # print(line, end='')
        statement = line.split(' ')

        for word in statement:

            if word in keywords:
                print(bcolors.WARNING + word + bcolors.ENDC, end=' ')
            else:
                print(word, end=' ')

    # for line in keywords:
    #     print(line)

if __name__ == '__main__':main()