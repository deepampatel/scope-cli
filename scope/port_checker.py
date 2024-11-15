import psutil
import os
import signal

def check_port(port, kill=False):
    try:
        for conn in psutil.net_connections(kind="inet"):
            if conn.laddr.port == port:
                proc = psutil.Process(conn.pid)
                print(f"Port {port} is in use by process:")
                print(f"  - PID: {proc.pid}")
                print(f"  - Name: {proc.name()}")
                print(f"  - Command: {' '.join(proc.cmdline())}")
                print(f"  - Working Directory: {proc.cwd()}")
                print(f"  - Status: {proc.status()}")
                print(f"  - User: {proc.username()}")
                
                if kill:
                    confirm = input(f"Do you want to kill process {proc.name()} (PID {proc.pid})? (y/n): ")
                    if confirm.lower() == 'y':
                        proc.terminate()
                        proc.wait(timeout=5)  # Wait for the process to terminate
                        print(f"Process {proc.name()} (PID {proc.pid}) terminated.")
                    else:
                        print("Operation aborted.")
                return

        print(f"Port {port} is free.")
    except psutil.AccessDenied:
        print(f"Access denied: Cannot retrieve process information for port {port}.")
    except psutil.NoSuchProcess:
        print("The process associated with this port no longer exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Check if a port is in use and manage processes.")
    parser.add_argument("port", type=int, help="Port number to check.")
    parser.add_argument("--kill", action="store_true", help="Kill the process using the specified port.")
    args = parser.parse_args()
    check_port(args.port, kill=args.kill)
