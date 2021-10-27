#!/usr/bin/env python

import argparse


def readFile(inputPath: str) -> None:
    # open input file
    with open(inputPath, "r", encoding='utf-8') as fInput:
        target = ""  # our target string
        hyp = ""  # our hypothesis string
        totalCount = 0
        incorrectCount = 0
        for line in fInput:

            if "T" in line.split()[0]:
                target = line.split()[1:]
                print(target)
            if "H" in line.split()[0]:
                hyp = line.split()[2:]
                print(hyp)
                if hyp != target:
                    print("Not a match!")
                    incorrectCount += 1
            totalCount += 1
        print("WER: ", round((incorrectCount/totalCount)*100))


def main(args: argparse.Namespace) -> None:

    readFile(args.inputFile)
    print("Finished!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", type=str,
                        help="predictions file for our program to read")
    args = parser.parse_args()
    main(args)
