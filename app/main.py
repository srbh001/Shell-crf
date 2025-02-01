import sys


def main():
    sys.stdout.write("$ ")

    while True:
        inp = input().strip().split(" ")

        command = inp[0]
        code = None
        if len(inp) > 1:
            code = int(inp[1])

        if command == "exit":
            sys.exit(code)

        print(f"{command}: command not found")
        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
