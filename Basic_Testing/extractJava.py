
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

    print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

    # fh = open('dexter.java')
    #
    # for line in fh:
    #     print(line, end='')

    # keywords = []
    #
    # fk = open('keywords.txt')
    #
    # for word in fk:
    #     keywords.append(word)
    #
    # for line in keywords:
    #     print(line)

if __name__ == '__main__':main()