import sys


def main():
    print("Podaj end by wyjść")
    user_input = None
    while user_input == None:
        user_input = input(": ")
        if user_input == "end":
            pass
        else:
            user_input = None


if __name__ == "__main__":
    main()
sys.exit(0)
