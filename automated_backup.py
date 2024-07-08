import os
import logging
import subprocess
from datetime import datetime

# Set up logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Backup source and destination
SOURCE_DIR = '/path/to/source/directory'
DESTINATION_DIR = 'user@remote_host:/path/to/remote/directory'

def backup_directory():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_cmd = f'rsync -avz {SOURCE_DIR} {DESTINATION_DIR}'

    try:
        subprocess.check_call(backup_cmd, shell=True)
        logging.info(f'Backup succeeded at {timestamp}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Backup failed at {timestamp} with error: {e}')

if _name_ == "_main_":
    backup_directory()
