import sys


commands_type = {"exit": "shell", "echo": "shell", "type": "shell"}


def main():
    sys.stdout.write("$ ")

    while True:
        inp = input().strip().split(" ")

        command = inp[0]
        code = None
        if len(inp) > 1 and command == "exit":
            code = int(inp[1])

        if command == "exit":
            sys.exit(code)

        elif command == "echo":
            msg = " ".join(inp[1:])
            sys.stdout.write(f"{msg}\n")

        elif command == "type":
            command2 = inp[1]
            if command2 in commands_type:
                print(f"{command2} is a {commands_type[command2]} builtin")
            else:
                print(f"{command2}: not found")

        else:
            print(f"{command}: command not found")
        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
