import sys
import re


def countoccurances(file, regexp):
    print(file, " ", regexp)
    count = 0
    with open(file) as fhand:
        for line in fhand:
            line = line.rstrip()
            if re.search(regexp, line):
                # print(line)
                count += 1
    return f"{file} had {count} lines that matched {regexp}"


if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    """for i, arg in enumerate(sys.argv):
    #print(f"Argument {i:>6}: {arg}")"""
    if len(sys.argv) != 3:
        exit("Exited - invalid arguments")

    print(countoccurances(sys.argv[1], sys.argv[2]))


def test_countoccurances():
    assert (
        countoccurances("mbox-short.txt", "^Author")
        == "mbox-short.txt had 27 lines that matched ^Author"
    )
    assert (
        countoccurances("mbox.txt", "^X-")
        == "mbox.txt had 14368 lines that matched ^X-"
    )
    assert (
        countoccurances("mbox.txt", "java$")
        == "mbox.txt had 4218 lines that matched java$"
    )
    assert (
        countoccurances("mbox.txt", "^Author")
        == "mbox.txt had 1798 lines that matched ^Author"
    )
