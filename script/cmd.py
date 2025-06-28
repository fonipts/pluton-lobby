import subprocess

def main():
    inputs = "Alice\n30\n"
    process = subprocess.Popen(
        ["python", "script.py"],
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

if __name__ == "__main__":
    main()
