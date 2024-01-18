def execute(file):
    with open(file) as f:
        code = compile(f.read(), file, 'exec')
        return exec(code)

import argparse, time
parser = argparse.ArgumentParser()
parser.add_argument("--debug", action='store_true', help='Debug mode')
parser.add_argument("--terminal", action='store_true', help='Disable windows and depends full on terminal')
args = parser.parse_args()
execute("dependency_installer.py")
if not args.debug: 
    i=1
    while i<250:
        i=i+1
        print("")
print("Starting...")
execute("starter.py")