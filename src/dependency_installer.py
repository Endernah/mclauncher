if args.debug:
    print("Debug mode enabled")
    debug = ""
else:
    debug = "> /dev/null 2>&1"
print("Installing dependencies")
import os, sys
if not "3" in f"{sys.version}":
    print("Python 3 not found")
    exit()
try:
    os.system(f"python3 -m pip install --upgrade pip {debug}")
    os.system(f"python3 -m pip install wget {debug}")
    os.system(f"python3 -m pip install requests {debug}")
except:
    print("Failed to install dependencies, Error: 202")
    exit()