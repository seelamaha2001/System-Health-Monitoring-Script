import psutil

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"CPU usage is high: {cpu_usage}%")

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"Memory usage is high: {memory_usage}%")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        print(f"Disk usage is high: {disk_usage}%")

def check_running_processes():
    # Get list of running processes
    running_processes = [p.name() for p in psutil.process_iter()]
    # Example process check
    if 'apache2' in running_processes:
        print("Apache server is running.")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
