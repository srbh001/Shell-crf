import os
import sys
import subprocess

COMMANDS_TYPE = {"exit": "shell", "echo": "shell", "type": "shell"}


def execute_exit(args):
    """Handles the exit command with an optional exit code."""
    try:
        code = int(args[0]) if args else 0
        sys.exit(code)
    except ValueError:
        print("exit: invalid exit code")
        sys.exit(1)


def execute_echo(args):
    """Handles the echo command by printing the given arguments."""
    print(" ".join(args))


def execute_type(args):
    """Handles the type command, checking if a command is a shell built-in."""
    if not args:
        print("type: missing argument")
        return

    command = args[0]
    if command in COMMANDS_TYPE:
        print(f"{command} is a {COMMANDS_TYPE[command]} builtin")
    else:
        paths = os.environ["PATH"].split(":")
        for directory in paths:
            if os.path.exists(f"{directory}/{command}"):
                print(f"{command} is {directory}/{command}")
                return
        print(f"{command}: not found")


def is_external_command(command):
    paths = os.environ["PATH"].split(":")
    for directory in paths:
        if os.path.exists(f"{directory}/{command}"):
            return True
    return False


def main():
    while True:
        try:
            sys.stdout.write("$ ")
            sys.stdout.flush()
            inp = input().strip().split()

            if not inp:
                continue

            command, *args = inp

            if command == "exit":
                execute_exit(args)
            elif command == "echo":
                execute_echo(args)
            elif command == "type":
                execute_type(args)

            elif is_external_command(command):
                args = " ".join(args)
                subprocess.run([command, args])

            else:
                print(f"{command}: command not found")

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except EOFError:
            print("\nExiting shell.")
            sys.exit(0)


if __name__ == "__main__":
    main()
