import argparse


def main(inputString):
    # Write the code to reverse the string here
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    if len(inputString) == 0:
        return inputString
    else:
        return main(inputString[1:]) + inputString[0]


if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser("String Reverser")
    argumentParser.add_argument("--string", type=str, help="Input a string to reverse")
    parsed = argumentParser.parse_args()
    print(main(parsed.string))
