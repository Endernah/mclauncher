import minecraft_launcher_lib, uuid

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

# Auth

if mode.lower() == "online":

    CLIENT_ID = "ce4970d7-153c-4730-86d0-761c3e8d5e81"
    REDIRECT_URL = "https://127.0.0.1/"

    login_url, state, code_verifier = minecraft_launcher_lib.microsoft_account.get_secure_login_data(CLIENT_ID, REDIRECT_URL)
    print(f"Please open {login_url} in your browser and copy the url you are redirected into the prompt below.")
    code_url=input("Url: ")

    try:
        auth_code = minecraft_launcher_lib.microsoft_account.parse_auth_code_url(code_url, state)
    except AssertionError:
        print("States do not match!")
        sys.exit(1)
    except KeyError:
        print("Url not valid")
        sys.exit(1)

    try:
        auth = minecraft_launcher_lib.microsoft_account.complete_login(CLIENT_ID, None, REDIRECT_URL, auth_code, code_verifier)
    except:
        print("Login failed!")
        sys.exit(1)
    print(auth)

# Username

try:
    if auth["name"]:
        username = auth["name"]
    else:
        try:
            if not username:
                while username == None or username == "":
                    username = input("Username: ")
        except:
            username = input("Username: ")
            while username == None or username == "":
                username = input("Username: ")
except:
    try:
        if not username:
            username = input("Username: ")
            while username == None or username == "":
                username = input("Username: ")
    except:
        username = input("Username: ")
        while username == None or username == "":
            username = input("Username: ")

# Uuid
try:
    if auth["id"]:
        uuid = auth["id"]
    else:
        uuid = str(uuid.uuid4())
except:
    uuid = str(uuid.uuid4())

# Token
try:
    if auth["access_token"]:
        token = auth["access_token"]
    else:
        token = ''
except:
    token = ''

options = {
    "username": username,
    "uuid": uuid,
    "token": token
}
mcpass = False
if not args.terminal:
    try:
        minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
    except:
        print("Failed to get version, Try again!")
else:
    while not mcpass == True:
        try:
            version = input("Version: ")
            minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)
            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
            mcpass = True
        except:
            print("Failed to get version, Try again!")
if 1==1:
    print(f"Starting Minecraft with options: {options}, Version: {version}")
else:
    print("Starting Minecraft")

subprocess.run(minecraft_command)