
# Scope-CLI

**Scope-CLI** is a lightweight command-line tool that helps with:
- **Directory Size Visualization**: Displays the sizes of directories and files in a tree-like structure.
- **Port Checker**: Checks if a specific port is in use, provides detailed process information, and allows you to manage (e.g., kill) processes.

---

## Installation

Install directly from PyPI:

```bash
pip install scope-cli
```

---

## Usage

### 1. Directory Size Visualization
Display a directory's structure along with the size of each folder and file.

```bash
scope tree /path/to/directory
```

**Example Output**:
```text
project (120 MB)
  src (40 MB)
    main.py (15 KB)
    utils.py (25 KB)
  assets (50 MB)
    image1.png (25 MB)
    image2.png (25 MB)
```

---

### 2. Port Checker
Check if a specific port is in use, see detailed information about the process, and optionally kill it.

#### Important Note for Ports
On some systems, accessing detailed port information may require elevated permissions. Use `sudo` if necessary to avoid permission issues.

#### Check Port Usage
```bash
sudo scope port 8080
```

**Example Output**:
```text
Port 8080 is in use by process:
  - PID: 1234
  - Name: python
  - Command: python manage.py runserver
  - Working Directory: /Users/yourname/project
  - Status: running
  - User: yourname
```

#### Kill Process Using Port
```bash
sudo scope port 8080 --kill
```

**Interactive Prompt**:
```text
Do you want to kill process python (PID 1234)? (y/n): y
Process python (PID 1234) terminated.
```

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests on the [GitHub repository](https://github.com/deepampatel/scope-cli).

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/deepampatel/scope-cli/blob/main/LICENSE) file for details.
