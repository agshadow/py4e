import urllib.request, urllib.parse, urllib.error

import pprint
import re


def inputUrl():
    url = input("Enter Website to retrieve: ")
    return url


def splitUrl(url):
    try:
        # print(f"{url=}")
        split = url.split("/")[2]
        # print(f"{split=}")
    except IndexError:
        print("IndexError occured - invalid format")
        exit()
    return (split, url)


def getUrl(url):
    target = url[1]

    fhand = urllib.request.urlopen(target)
    count = 0
    for line in fhand:
        if re.search("<[pP]>", line.decode()):
            foundre = re.findall("<[pP]>", line.decode())
            count += len(foundre)
        # break
    return f"{count} paragraph tags"


if __name__ == "__main__":
    splitUrl = splitUrl(inputUrl())
    print(f"{splitUrl=}")
    print(getUrl(splitUrl))


def test_splitUrl():
    assert splitUrl("http://data.pr4e.org/romeo.txt") == (
        "data.pr4e.org",
        "http://data.pr4e.org/romeo.txt",
    )
    assert splitUrl("http://www.google.com/") == (
        "www.google.com",
        "http://www.google.com/",
    )
