import psutil
import socket


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
                    confirm = input(
                        f"Do you want to kill process {proc.name()} (PID {proc.pid})? (y/n): "
                    )
                    if confirm.lower() == "y":
                        proc.terminate()
                        proc.wait(timeout=5)
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
