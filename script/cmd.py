import subprocess
import time
import sys
import requests
import select
import gc
import os
import signal
import socket
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


project_list["django1"]={
            "name":"django",
            "action": [
                "django_ar1",
                "y", 
                "django_ar1",
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
    time.sleep(10)

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

def wait_for_port(port, host='127.0.0.1', timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=2):
                return True
        except OSError:
            time.sleep(2)
    return False

def kill_process_on_port(port):
    process = Popen(["lsof", "-i", f":{port}"], stdout=PIPE, stderr=PIPE)
    stdout, _ = process.communicate()
    for line in str(stdout).split("\\n")[1:]:
        parts = [x for x in line.split(" ") if x]
        if len(parts) > 1:
            try:
                os.kill(int(parts[1]), signal.SIGKILL)
                print(f"Killed process {parts[1]} on port {port}")
            except Exception as e:
                print(f"Error killing process: {e}")

def run_project(port, dir):
    print(dir, ":dir")
    os.chdir(f"./{dir}")
    #kill_process_on_port(port)
    print(":port kill")
    try:
        process = subprocess.Popen(
            ['plkcmd', 'start'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Wait for the server to start
        if not wait_for_port(int(port)):
            print(f"Server on port {port} did not start in time.")
            process.terminate()
            sys.exit(1)

        # Optionally, read a few lines of output (non-blocking)
        for _ in range(5):
            ready, _, _ = select.select([process.stdout], [], [], 1)  # 1 second timeout
            if ready:
                line = process.stdout.readline()
                if not line:
                    break
                print("Server output:", line.strip())
            else:
                print("No server output (timeout)")
                break

        x = requests.get(f"http://127.0.0.1:{port}/")
        print(f"http://127.0.0.1:{port}/", ":accessing")
        print(x.status_code, ":sd")
        if x.status_code == 200:
            print("project url was found")
            os.chdir("../")
            sys.exit(0)
        else:
            print(f"project url was not found {x.status_code}")
            process.terminate()
            sys.exit(1)

       # kill_process_on_port(port)
        os.chdir("../")
        #process.terminate()
        #sys.stdout.flush()
    except BrokenPipeError:
        print("Broken pipe detected (output truncated)", file=sys.stderr)
        sys.stderr.close()
        sys.exit(1)
    finally:
        kill_process_on_port(port)
        #if process are killed, or call :
        process.terminate()
        sys.stdout.flush()
        gc.collect()
        #osgc.collect()` to force garbage collection.

#### 3. Split.chdir("../")
        sys.stdout.flush()    
     
if __name__ == "__main__":
    main()
