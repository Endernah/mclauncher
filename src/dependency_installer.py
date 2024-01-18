if args.debug:
    print("Debug mode enabled")
    debug = None
else:
    debug = subprocess.DEVNULL
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
    sys.exit(1)
else:
    if args.debug:
        print(f"Python3 found: {version}")
    else:
        print("Python3 found")
print("Installing dependencies")
try:
    subprocess.run([python, "-m", "pip", "install", "--upgrade", "pip"], stdout=debug, stderr=debug)
    subprocess.run([python, "-m", "pip", "install", "wget"], stdout=debug, stderr=debug)
    subprocess.run([python, "-m", "pip", "install", "requests"], stdout=debug, stderr=debug)
    subprocess.run([python, "-m", "pip", "install", "minecraft-launcher-lib"], stdout=debug, stderr=debug)
except:
    print("Failed to install dependencies, Exiting!")
    sys.exit(1)