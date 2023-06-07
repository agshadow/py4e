import socket
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
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url[0], 80))
    addr = "GET " + url[1] + " HTTP/1.0\r\n\r\n"
    cmd = addr.encode()

    mysock.send(cmd)
    dataRecievedCounter = 0
    while True:
        data = mysock.recv(512)
        dataRecievedCounter += len(data)
        if len(data) < 1:
            break
        print(data.decode(), end="")
    print("Length of Document: ", dataRecievedCounter)
    mysock.close()


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
