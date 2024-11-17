
# Scope-CLI: The AI-Powered Command Line Tool

**Scope-CLI** is a versatile, AI-powered command-line tool designed for developers. It combines traditional CLI utilities with the power of an LLM assistant to provide precise, safe, and actionable command-line suggestions. Whether you need intelligent command-line recommendations, check ports, or visualize directory sizes, Scope-CLI has you covered.

---

## Installation

### Core Features
Install the lightweight version with basic functionality:
```bash
pip install scope-cli
```

### LLM Add-On
Enable the AI-powered assistant by installing the optional LLM module:
```bash
pip install scope-cli[llm]
```
#### On Linux/MacOS:
Add the following line to your shell configuration file (e.g., `.bashrc`, `.zshrc`):
```bash
export OPENAI_API_KEY="your-openai-api-key"
```
Then reload your shell:
```bash
source ~/.zshrc  # Or source ~/.bashrc
```

---

## Features and Usage

### 1. LLM-Powered Command Line Assistant
Leverage an LLM to suggest safe and actionable CLI commands, explain commands, or execute tasks.

![example](https://cache.sigaba.in/Screenshot%202024-11-17%20at%203.12.57%E2%80%AFPM.png)


#### Suggest a Command
Ask the assistant to suggest a command for your query:
```bash
scope llm "List all Python files in the current directory"
```

**Example Output**:
```text
Suggested Command:
ls *.py
```

#### Explain a Command
Get detailed information about a specific command:
```bash
scope llm "Explain the port command"
```

**Example Output**:
```text
The 'port' command checks if a specific port is in use. It provides details about the process using the port and optionally allows you to terminate the process.
Example:
scope port 8080 --kill
```

#### Execute a Suggested Command
Use the `--execute` flag to directly run the suggested command:
```bash
scope llm "List all Python files in the current directory" --execute
```

**Interactive Prompt**:
```text
Suggested Command:
ls *.py

Do you want to execute this command? (y/n): y
Executing command...
Command Output:
script1.py
script2.py
```

---

### 2. Port Checker
Check if a specific port is in use, get detailed process information, and optionally kill the process.

#### Important Note
On some systems, accessing detailed port information may require elevated permissions. Use `sudo` if necessary.

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

### 3. Directory Size Visualization
Quickly display a directory's structure and the size of each folder and file.

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

## Why Scope-CLI?

- **AI-Powered Recommendations**: Get intelligent, context-aware command-line suggestions.
- **Safe and Developer-Focused**: Designed to prioritize safety and precision, ensuring no accidental data loss.
- **Modular Design**: Lightweight by default, with optional AI-powered functionality.
- **Ease of Use**: Simple commands for common developer tasks like visualizing directories or checking ports.

---

## Contributing

We welcome contributions from the community! Whether it’s a bug fix, feature suggestion, or documentation improvement, feel free to open an issue or pull request on the [GitHub repository](https://github.com/deepampatel/scope-cli).

---

## License

Scope-CLI is licensed under the MIT License. See the [LICENSE](https://github.com/deepampatel/scope-cli/blob/main/LICENSE) file for more details.
