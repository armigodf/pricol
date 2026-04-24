import sys


def main(argv: list):
    move = ""
    input_data = list()
    imput = "" if "--input" not in argv else "input.txt"
    output = "" if "--output" not in argv else "output.txt"
    for i in range(len(argv)):
        if argv[i] == "--input" and argv[i + 1] != "--output":
            imput = argv[i + 1]
        elif argv[i] == "--output" and "-" not in argv[i + 1]:
            output = argv[i + 1]
        elif "--input" not in argv:
            input_data = list(map(int, input().split()))
        if "-sum" in argv: move = "+"
        if "-mul" in argv: move = "*"
        if "-avg" in argv: move = "avg"


if __name__ == "__main__":
    main(sys.argv)
