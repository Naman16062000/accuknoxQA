import psutil
import logging
import time

logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    if cpu_usage > CPU_THRESHOLD:
        logging.info(f'High CPU usage detected: {cpu_usage}%')

    if memory_info.percent > MEMORY_THRESHOLD:
        logging.info(f'High memory usage detected: {memory_info.percent}%')

    if disk_info.percent > DISK_THRESHOLD:
        logging.info(f'High disk usage detected: {disk_info.percent}%')

    # Log running processes
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        logging.info(f'Process {proc.info["name"]} (PID {proc.info["pid"]}) is using {proc.info["cpu_percent"]}% CPU')

if _name_ == "_main_":
    while True:
        check_system_health()
        time.sleep(60)  # Check every 60 seconds
