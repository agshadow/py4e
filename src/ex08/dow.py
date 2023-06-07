import string
from collections import Counter


def countdays(fname):
    counts = dict()
    with open(fname) as han:
        for line in han:
            line = line.rstrip()
            # print('Line:', line)
            wds = line.split()
            # print('Words:',wds)

            if len(wds) < 3 or wds[0] != "From":
                # print ("ignore")
                continue
            # print(wds[1])
            if wds[1] not in counts:
                counts[wds[1]] = 1
            else:
                counts[wds[1]] += 1
    return counts


def findmax(fname):
    """templist = list()
    for key, val in countdays(fname).items():
        templist.append((val,key))
    max = sorted(templist, reverse=True)"""
    b, a = sorted([(v, k) for k, v in countdays(fname).items()], reverse=True)[0]
    return f"{a} {b}"
    return "cwen@iupui.edu"


def domaincount(fname):
    counts = dict()
    with open(fname) as han:
        for line in han:
            if line[:4] != "From":
                continue
            if len(line.split()) < 3:
                continue
            print(" stripped line: ", line.rsplit("@")[1].split()[0])
            domain = line.rsplit("@")[1].split()[0]
            counts[domain] = counts.get(domain, 0) + 1

    return counts


def timeofday(fname):
    counts = dict()
    with open(fname) as file:
        for line in file:
            line = line.rstrip()
            wds = line.split()

            if len(wds) < 3 or wds[0] != "From":
                continue
            hour = wds[5].split(":")[0]
            counts[hour] = counts.get(hour, 0) + 1

    result = sorted([(k, v) for k, v in counts.items()])

    print(" result: ", result)
    resultstr = ""
    for i in result:
        a, b = i
        resultstr = resultstr + str(a) + " " + str(b) + "\n"
    print(" resultstr: ", resultstr.rstrip())
    return resultstr.rstrip()
    return "04 3\n06 1\n07 1\n09 2\n10 3\n11 6\n14 1\n15 2\n16 4\n17 2\n18 1\n19 1"


def lettercount(fname):
    counts = dict()
    with open(fname) as file:
        for line in file:
            line = line.rstrip().lower().replace(" ", "")
            linelist = list(line.translate(str.maketrans("", "", string.punctuation)))
            print(linelist)
            for i in linelist:
                counts[i] = counts.get(i, 0) + 1

    # print (counts)
    result = sorted([(v, k) for k, v in counts.items()], reverse=True)
    # print (result)
    resultstr = ""
    for i in result:
        b, a = i
        resultstr = resultstr + str(a) + " " + str(b) + "\n"

    return resultstr.rstrip()
    return "n 4\na 3\nc 2\nd 1\nb 1"


# uses Counter()
def letterscounter(fname):
    counts = Counter()
    with open(fname) as file:
        for line in file:
            line = (
                line.rstrip()
                .lower()
                .replace(" ", "")
                .translate(str.maketrans("", "", string.punctuation))
            )
            counts.update(line)
            # counts.update(line.translate(str.maketrans('', '', string.punctuation)))
    resultstr = ""
    resultstr = resultstr.join(
        resultstr + i + " " + str(counts[i]) + "\n" for i in counts
    )
    return resultstr.rstrip()


if __name__ == "__main__":
    # print(countdays())
    print(letterscounter("clown-short.txt"))


def test_countdays():
    result = countdays("mbox-short.txt")
    expected = {
        "stephen.marquard@uct.ac.za": 2,
        "louis@media.berkeley.edu": 3,
        "zqian@umich.edu": 4,
        "rjlowe@iupui.edu": 2,
        "cwen@iupui.edu": 5,
        "gsilver@umich.edu": 3,
        "wagnermr@iupui.edu": 1,
        "antranig@caret.cam.ac.uk": 1,
        "gopal.ramasammycook@gmail.com": 1,
        "david.horwitz@uct.ac.za": 4,
        "ray@media.berkeley.edu": 1,
    }
    assert result == expected


def test_findmax(monkeypatch):
    assert findmax("mbox-short.txt") == "cwen@iupui.edu 5"


def test_domaincount():
    result = {
        "media.berkeley.edu": 4,
        "uct.ac.za": 6,
        "umich.edu": 7,
        "gmail.com": 1,
        "caret.cam.ac.uk": 1,
        "iupui.edu": 8,
    }
    assert domaincount("mbox-short.txt") == result


def test_timeofday():
    expected = "04 3\n06 1\n07 1\n09 2\n10 3\n11 6\n14 1\n15 2\n16 4\n17 2\n18 1\n19 1"


def test_lettercount():
    expected = "n 4\na 3\nc 2\nd 1\nb 1"
    assert lettercount("clown-short.txt") == expected


def test_letterscounter():
    expected = "n 4\na 3\nc 2\nd 1\nb 1"
    assert letterscounter("clown-short.txt") == expected
