import subprocess
import time
import sys
import requests

import os
import signal
from subprocess import Popen, PIPE
import psutil


def main():
    project_list = [
        {
            "name":"flask",
            "action": [
                "flask_ar",
                "y", 
                "flask_ar",
                "1",
                "3",
                "1",
                "2",
                "1" # Use 'y' to confirm the creation of the project
            ],
            "port":"5000"
        },
        {
            "name":"flask",
            "action": [
                "flask_ar1",
                "y", 
                "flask_ar1",
                "1",
                "3",
                "2",
                "2",
                "1" # Use 'y' to confirm the creation of the project
            ],
            "port":"5000"
        }
    ]
    for val in project_list:
        create_project(val["name"],val["action"])
        time.sleep(20)
        run_project(val["port"], val["action"][0]  )

def create_project(name,actions):

    inputs = "\n".join(actions) + "\n"
    process = subprocess.Popen(
        ["plutonkit", "create_project",f"source={name}"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=inputs)
    if process.returncode == 0:
        print("Output:")
        print(stdout)
    else:
        print("Error:")
        print(stderr)

def kill_process_on_port(port):
    process = Popen(["lsof", "-i", ":{0}".format(port)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    for process in str(stdout.decode("utf-8")).split("\n")[1:]:       
        data = [x for x in process.split(" ") if x != '']
        if (len(data) <= 1):
            continue

        os.kill(int(data[1]), signal.SIGKILL)
def run_project(port,dir):
    os.chdir(f"./{dir}")
    process = subprocess.Popen(['plkcmd', 'start'], stdout=subprocess.PIPE)
    time.sleep(10)
    x = requests.get(f"http://0.0.0.0:{port}")
    if x.status_code == 200:
        process.terminate()
        kill_process_on_port(port)
        print("project url was found")
        os.chdir(f"./")    
        #sys.exit(1)
    else:
        process.terminate()
        kill_process_on_port(port)
        print(f"project url was not found {x.status_code}")
        os.chdir(f"./")
        sys.exit(1)
        
    process.terminate()

    # Wait for the process to actually terminate and get the return code
    time.sleep(10)
    return_code = process.wait()
    print(f"Subprocess terminated with return code: {return_code}")    
if __name__ == "__main__":
    main()
