import urllib.request, urllib.parse, urllib.error

import pprint


def inputUrl():
    url = input("Enter Website to retrieve: ")
    return url


def splitUrl(url):
    try:
        print(f"{url=}")
        split = url.split("/")[2]
        print(f"{split=}")
    except IndexError:
        print("IndexError occured - invalid format")
        exit()
    return (split, url)


def getUrl(url):
    target = url[1]

    fhand = urllib.request.urlopen(target)
    dataRecievedCounter = 0
    for line in fhand:
        print("💥", len(line))
        dataRecievedCounter += len(line)
        print(line.decode().strip())

    print("Length of Document: ", dataRecievedCounter)


if __name__ == "__main__":
    splitUrl = splitUrl(inputUrl())
    print(f"{splitUrl=}")
    getUrl(splitUrl)


def test_splitUrl():
    assert splitUrl("http://data.pr4e.org/romeo.txt") == (
        "data.pr4e.org",
        "http://data.pr4e.org/romeo.txt",
    )
    assert splitUrl("http://www.google.com/") == (
        "www.google.com",
        "http://www.google.com/",
    )
