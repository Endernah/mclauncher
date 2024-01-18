mode = 'offline' # Limit to cracked accounts

if not args.terminal:
    print("Loading GUI.")

    def minecraft():
        root.withdraw()
        global version, username
        version = version_entry.get()
        username = name_entry.get()
        exec(compile(open('minecraft.py').read(), 'minecraft.py', 'exec'))
        root.destroy()

    root = tk.Tk()
    root.title("Endernah/mclauncher")
    root.geometry("500x300")

    play_button = tk.Button(root, text="Play", command=minecraft)
    play_button.pack()

    name_label = tk.Label(root, text="Username:")
    name_label.pack()

    name_entry = tk.Entry(root)
    name_entry.pack()

    version_label = tk.Label(root, text="Version:")
    version_label.pack()

    version_entry = tk.Entry(root)
    version_entry.pack()

    print("Opening GUI.")
    root.mainloop()
else:
    print("Terminal mode.")
    exec(compile(open('minecraft.py').read(), 'minecraft.py', 'exec'))