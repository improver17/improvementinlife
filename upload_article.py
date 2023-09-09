import subprocess
import time


def upload(cmd):
    subprocess.call(f"git {cmd}", shell=True)

try:
    upload('add .')
    time.sleep(1)
    upload('status')
    time.sleep(1)
    msg = input('Enter commit message: ')
    upload(f'commit -m "{msg}"' if msg else 'commit -m "file created/ modified"')
    time.sleep(1)
    upload('push -u origin main')

except Exception as e:
    print(e)

