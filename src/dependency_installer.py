if args.debug:
    print("Debug mode enabled")
    debug = ""
else:
    debug = "> /dev/null 2>&1"
import os, sys, subprocess
print("Checking for Python3")
try:
    version = subprocess.check_output(['python3', '--version'], text=True)
    python = "python3"
except:
    try:
        version = subprocess.check_output(['python', '--version'], text=True)
        python = "python"
    except:
        print("Failed to check for Python3, Exiting!")
        sys.exit(1)
    if not python:
        print("Failed to check for Python3, Exiting!")
        sys.exit(1)
if not "3" in f"{version}":
    print("Python3 not found")
    exit()
else:
    if args.debug:
        print(f"Python3 found: {version}")
    else:
        print("Python3 found")
print("Installing dependencies")
try:
    os.system(f"{python} -m pip install --upgrade pip {debug}")
    os.system(f"{python} -m pip install wget {debug}")
    os.system(f"{python} -m pip install requests {debug}")
    os.system(f"{python} -m pip install minecraft-launcher-lib {debug}")
except:
    print("Failed to install dependencies, Exiting!")
    exit()