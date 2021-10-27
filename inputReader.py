
#!/usr/bin/env python

import argparse


def prepareFiles(inputPath: str, graphemePath: str, phonemePath: str) -> None:
    # open input file
    with open(inputPath, "r", encoding='utf-8') as fInput:
        # open grapheme file
        with open(graphemePath, "w", encoding='utf-8') as gOutput:
            # open phoneme file
            with open(phonemePath, "w", encoding='utf-8') as pOutput:
                # for each line in the input, split the first word into the grapheme file (with spaces) and the rest to the phoneme file
                for line in fInput:

                    word = line.split()[0]
                    trans = line[len(word):]
                    wordWithSpace = ""

                    for c in word:

                        wordWithSpace += c.casefold() + " "

                    # so I can see on the console
                    print("-----------------")
                    print(wordWithSpace.strip())
                    print(trans.strip())
                    print("-----------------")
                    # for the file output
                    print(wordWithSpace.strip(), file=gOutput)
                    print(trans.strip(), file=pOutput)


def main(args: argparse.Namespace) -> None:

    prepareFiles(args.inputFile, args.graphemeFile, args.phonemeFile)
    print("Finished!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", type=str,
                        help="file for our program to read/tokenize")
    parser.add_argument("graphemeFile", type=str,
                        help="output file for grapheme")
    parser.add_argument("phonemeFile", type=str,
                        help="output file for phoneme")
    args = parser.parse_args()
    main(args)
