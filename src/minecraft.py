import minecraft_launcher_lib, subprocess

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
latest_version = minecraft_launcher_lib.utils.get_latest_version()["release"]
options = {
    "username": "endernah_",
    # This is a random uuid to bypass
    "uuid": 'bf77b78b-c6a5-48ef-a538-9c76c45cdafb',
    "token": ''
}
minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)

# Start Minecraft
subprocess.run(minecraft_command)