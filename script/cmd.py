import subprocess
import time
import sys
import requests

import os
import signal
from subprocess import Popen, PIPE

project_list = {}
project_list["flask1"]={
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
        }
project_list["flask2"]={
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
project_list["bottle1"]={
            "name":"bottle",
            "action": [
                "bottle_ar1",
                "y", 
                "bottle_ar1",
                "1",
                "3",
                "2",
                "1" # Use 'y' to confirm the creation of the project
            ],
            "port":"5000"
        }
project_list["fastapi1"]={
            "name":"fastapi",
            "action": [
                "fastapi_ar",
                "y", 
                "fastapi_ar",
                "1",
                "3",
                "2",
                "2",
                "1" # Use 'y' to confirm the creation of the project
            ],
            "port":"8000"
        }
project_list["fastapi2"]={
            "name":"fastapi",
            "action": [
                "fastapi_ar1",
                "y", 
                "fastapi_ar1",
                "1",
                "3",
                "2",
                "1",
                "1" # Use 'y' to confirm the creation of the project
            ],
            "port":"8000"
        }



def main():
    
    sys_arg = sys.argv[1]
    val = project_list[sys_arg]
    #for val in project_list:
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
        process.terminate()
        sys.stdout.flush()
        sys.stderr.close()
    else:
        print("Error:")
        print(stderr)
        process.terminate()
        sys.stdout.flush()
        #sys.stderr.close()

def kill_process_on_port(port):
    process = Popen(["lsof", "-i", ":{0}".format(port)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    for process in str(stdout.decode("utf-8")).split("\n")[1:]:       
        data = [x for x in process.split(" ") if x != '']
        if (len(data) <= 1):
            continue

        os.kill(int(data[1]), signal.SIGKILL)
def run_project(port,dir):
    print(dir,":dir")
    os.chdir(f"./{dir}")
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    #kill_process_on_port(port)
    try:
        process: Popen[str] = subprocess.Popen(['plkcmd', 'start'], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        time.sleep(20)
        print(str(stdout.decode("utf-8")),"::stdout.decode")
        print(process.returncode,"::process.returncode")
        x = requests.get(f"http://127.0.0.1:{port}/")
        print(f"http://127.0.0.1:{port}/",":accessing")
        print(x.status_code,":sd")
        if x.status_code == 200:
            
            print("project url was found")
        #?    kill_process_on_port(port)
        #?    os.chdir(f"../")
        #?    process.terminate()
            
            
            #sys.exit(0)
        else:
            
            print(f"project url was not found {x.status_code}")
        #?    kill_process_on_port(port)
        #?    os.chdir(f"../")    
        #?    process.terminate()
            
            
            sys.exit(1)
        #for i in range(1000):
        #    print(f"Line {i}")
        time.sleep(10)
        kill_process_on_port(port)
        os.chdir(f"../")
        
        print("Some output")
        #process.terminate()
        
        #time.sleep(3)
        #os.kill(os.getpid(), signal.SIGTERM)
        #time.sleep(15)
        #sys.stdout.flush()  # Ensure output is flushed
    except BrokenPipeError:
        # Exit gracefully when the pipe is closed
        print("Broken pipe detected (output truncated)", file=sys.stderr)
        #sys.stderr.close()  # Avoid "Exception ignored" messages
        #sys.exit(1)  # Optional: Exit with a non-zero status
    
if __name__ == "__main__":
    main()
