import argparse
import sys

from titanic_utils.str_utils import extract_titles


def main():
    parser = argparse.ArgumentParser(description="Extract the title from a name")
    parser.add_argument(
        "-n", "--name", required=False, help="Name to extract title from"
    )
    parser.add_argument("-nl", "--names-list", help="List of names separated by ;")
    args = parser.parse_args()

    # print(extract_titles(args.name))
    list_of_names = args.names_list.split(";")
    for name in list_of_names:
        print(extract_titles(name))


if __name__ == "__main__":
    # This part will be executed
    # when calling the script from the terminal
    main()
