import signal
import subprocess
import os


start_process = subprocess.Popen("python3 main.py", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
start_process1 = subprocess.Popen("python3 control_ads.py", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

while True:
    command = input()
    if command == 'stop':
        os.killpg(os.getpgid(start_process.pid), signal.SIGTERM)
        os.killpg(os.getpgid(start_process1.pid), signal.SIGTERM)
        break