import psutil

def list_processes(filter_name=None):
    """Lists running processes with optional filtering by name."""
    for proc in psutil.process_iter(attrs=["pid", "name", "cpu_percent", "memory_info"]):
        if not filter_name or filter_name.lower() in proc.info["name"].lower():
            mem_info = proc.info["memory_info"]
            print(f"PID: {proc.info['pid']} Name: {proc.info['name']} CPU: {proc.info['cpu_percent']}% Memory: {mem_info.rss // 1024} KB")
