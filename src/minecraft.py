import minecraft_launcher_lib, subprocess, uuid

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

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
latest_version = minecraft_launcher_lib.utils.get_latest_version()["release"]
minecraft_launcher_lib.install.install_minecraft_version(latest_version, minecraft_directory)

# Username

try:
    if auth["name"]:
        username = auth["name"]
    else:
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
if 1==1:
    print(f"Starting Minecraft with options: {options}")
else:
    print("Starting Minecraft")
minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)

# Start Minecraft
subprocess.run(minecraft_command)