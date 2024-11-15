import sys
from scope.dir_size import main as dir_size_main
from scope.port_checker import main as port_checker_main

def main():
    if len(sys.argv) < 2:
        print("Usage: scope [tree|port] [arguments]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "tree":
        sys.argv = [sys.argv[0]] + args
        dir_size_main()
    elif command == "port":
        sys.argv = [sys.argv[0]] + args
        port_checker_main()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: tree, port")
        sys.exit(1)
