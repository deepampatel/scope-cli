import os

def get_size(path):
    if os.path.isfile(path) or os.path.islink(path):
        return os.path.getsize(path)
    if os.path.isdir(path):
        return sum(get_size(os.path.join(path, f)) for f in os.listdir(path))
    return 0

def display_tree(path, indent=""):
    size = get_size(path)
    print(f"{indent}{os.path.basename(path)} ({size // 1024} KB)")
    if os.path.isdir(path):
        for item in os.listdir(path):
            display_tree(os.path.join(path, item), indent + "  ")
