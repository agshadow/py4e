import re
import sys


def newrevision(filename):
    occurancesList = list()
    with open(filename) as fhand:
        for line in fhand:
            line = line.rstrip()
            occurancesList += re.findall("^New Revision: ([0-9]*)", line)
    # print(occurancesList)
    avg = sum(int(x) for x in occurancesList) / len(occurancesList)
    print("average: ", (avg))

    return round(avg)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Exited - invalid arguments")

    print(newrevision(sys.argv[1]))


def test_newrevision():
    assert newrevision("mbox-short.txt") == 39757
