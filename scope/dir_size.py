import os

def get_size(path):
    if os.path.isfile(path) or os.path.islink(path):  # Check if it's a file or symlink
        return os.path.getsize(path)
    if os.path.isdir(path):  # Check if it's a directory
        return sum(get_size(os.path.join(path, f)) for f in os.listdir(path))
    return 0  # For other cases like sockets

def display_tree(path, indent=""):
    size = get_size(path)
    print(f"{indent}{os.path.basename(path)} ({size // 1024} KB)")
    if os.path.isdir(path):
        for item in os.listdir(path):
            display_tree(os.path.join(path, item), indent + "  ")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Visualize directory sizes in a tree format.")
    parser.add_argument("path", nargs="?", default=".", help="Path to the directory (default: current directory).")
    args = parser.parse_args()
    display_tree(args.path)
