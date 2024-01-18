import argparse, time
parser = argparse.ArgumentParser()
parser.add_argument("-debug", action='store_true', help='Debug mode')
parser.add_argument("-terminal", action='store_true', help='Disable windows and depends fully on terminal')
parser.add_argument("-version", action='store_true', help='Shows the version of the launcher.')
args = parser.parse_args()
if args.version:
    print("Version: 0.0.1")
    exit()
exec(compile(open('dependency_installer.py').read(), 'dependency_installer.py', 'exec'))
if not args.debug: 
    i=1
    while i<250:
        i=i+1
        print("")
print("Starting...")
exec(compile(open('starter.py').read(), 'starter.py', 'exec'))