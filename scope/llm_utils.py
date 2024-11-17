import os
from openai import OpenAI, AuthenticationError, RateLimitError
import subprocess
from colorama import Fore, Style, init
import subprocess
from colorama import Fore, Style
import traceback
import json

init(autoreset=True)


cli_prompt = (
    "You are a highly knowledgeable CLI assistant"
    "Your goal is to provide safe, precise, and actionable command-line suggestions.\n\n"
    "Guidelines:\n"
    "1. Only suggest commands that align with the 'scope' tool's capabilities or safe, standard CLI utilities.\n"
    "2. Avoid commands that involve destructive actions such as deleting files, modifying configurations, or accessing sensitive data.\n"
    "3. Ensure every command is clearly explained, including its purpose and expected output.\n"
    "4. If the query is ambiguous, ask for clarification instead of guessing.\n"
    "5. Emphasize safety and best practices in all suggestions.\n"
    "6. If a command could impact the system state, warn the user and recommend verification steps.\n\n"
    
    "Always reply in a JSON format like the following example:\n"
    '''
    {
        "command": "ls -l",
        "is_safe": "safe",
        "explanation": {
            "purpose": "Lists all files in the current directory in long format.",
            "parameters": {
                "-l": "Use a long listing format to display detailed information about files."
            }
        },
        "alternatives": [
            {
                "command": "ls -lh",
                "description": "Displays file sizes in a human-readable format."
            },
            {
                "command": "ls -a",
                "description": "Lists all files, including hidden files."
            }
        ],
        "warnings": [],
        "expected_output": "A detailed list of files with permissions, size, owner, and timestamps.",
        "command_found": true,
        "clarification_needed": false
    }

    all fields are required. If a field is not applicable, provide an null or empty value.
    '''
)

class LLMIntegrationError(Exception):
    """Custom exception for LLM errors."""

    pass


def get_llm_response(query):
    """Fetch a safe and precise CLI command suggestion from the LLM."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise LLMIntegrationError(
            "Missing API key. Set the OPENAI_API_KEY environment variable."
        )

    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": cli_prompt},
                {"role": "user", "content": query},
            ]
        )
        return response.choices[0].message.content
    except AuthenticationError:
        raise LLMIntegrationError("Invalid API key. Please check your OPENAI_API_KEY.")
    except RateLimitError:
        raise LLMIntegrationError("Rate limit exceeded. Please try again later.")
    except Exception as e:
        traceback.print_exc()
        raise LLMIntegrationError(f"An unexpected error occurred: {e}")


def safe_load_json(json_str):
    """Safely load a JSON string."""
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return {}

def handle_llm_command(query, execute):
    """
    Process the LLM command and optionally execute the suggested command
    based on the structured contract response.
    """
    try:
        # Get the structured response from the LLM
        response = get_llm_response(query)
        response = safe_load_json(response)
        # Parse the response
        command = response.get("command")
        is_safe = response.get("is_safe")
        explanation = response.get("explanation", {}).get(
            "purpose", "No explanation provided."
        )
        alternatives = response.get("alternatives", [])
        warnings = response.get("warnings", [])
        command_found = response.get("command_found", False)
        clarification_needed = response.get("clarification_needed", False)

        if clarification_needed:
            print(
                f"{Fore.YELLOW}Clarification Needed: {response.get('message', 'Could you clarify your query?')}{Style.RESET_ALL}"
            )
            return

        if not command_found:
            print(f"{Fore.RED}No valid command found for the query.{Style.RESET_ALL}")
            return

        print(f"\n{Fore.CYAN}Suggested Command:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{command}{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}Explanation:{Style.RESET_ALL}")
        print(explanation)

        if warnings:
            print(f"\n{Fore.RED}Warnings:{Style.RESET_ALL}")
            for warning in warnings:
                print(f"- {warning}")

        if alternatives:
            print(f"\n{Fore.MAGENTA}Alternative Commands:{Style.RESET_ALL}")
            for alt in alternatives:
                print(
                    f"- {Fore.GREEN}{alt['command']}{Style.RESET_ALL}: {alt['description']}"
                )

        if is_safe == "destructive":
            print(
                f"\n{Fore.RED}⚠️ This command is potentially destructive! Proceed with caution.{Style.RESET_ALL}"
            )

        if execute:
            confirm = input(
                f"\n{Fore.MAGENTA}Do you want to execute this command? (y/n): {Style.RESET_ALL}"
            ).lower()
            if confirm == "y":
                print(f"{Fore.BLUE}Executing command...{Style.RESET_ALL}")
                result = subprocess.run(
                    command, shell=True, text=True, capture_output=True
                )
                print(f"{Fore.CYAN}Command Output:{Style.RESET_ALL}")
                print(result.stdout)
                if result.stderr:
                    print(f"{Fore.RED}Command Error:{Style.RESET_ALL}")
                    print(result.stderr)
            else:
                print(f"{Fore.YELLOW}Execution aborted.{Style.RESET_ALL}")
    except LLMIntegrationError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
