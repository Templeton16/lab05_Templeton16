# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true")

    args = parser.parse_args()

    pattern = args.pattern.lower() if args.ignore_case else args.pattern
    with open(args.filename) as lines:
        for number, line in enumerate(lines, start=1):
            text = line.rstrip("\n")
            candidate = text.lower() if args.ignore_case else text
            if pattern in candidate:
                print(f"{number}: {text}")


if __name__ == "__main__":
    main()
