mode = 'offline' # Limit to cracked accounts

if not args.terminal:
    print("Loading GUI.")

    import tkinter.scrolledtext as st

    class TextHandler(logging.Handler):
        def __init__(self, text):
            logging.Handler.__init__(self)
            self.text = text

        def emit(self, record):
            msg = self.format(record)
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            self.text.yview(tk.END)

    root = tk.Tk()
    root.title("Endernah/mclauncher")
    root.geometry("500x300")

    console = st.ScrolledText(root, height=6, width=300)
    console.pack()

    logging.basicConfig(level=logging.INFO)
    handler = TextHandler(console)
    logging.getLogger().addHandler(handler)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    def minecraft():
        play_button.config(state=tk.DISABLED)
        global version, username
        version = version_entry.get()
        username = name_entry.get()
        if username == "" or username == None:
            logging.info("Username not specified!")
            play_button.config(state=tk.NORMAL)
            return
        if version == "" or version == None:
            logging.info("Version not specified!")
            play_button.config(state=tk.NORMAL)
            return
        threading.Thread(target=start_minecraft).start()
    
    def start_minecraft():
        class StreamToLogger(object):
            def __init__(self, logger, log_level=logging.INFO):
                self.logger = logger
                self.log_level = log_level

            def write(self, message):
                if message.rstrip() != "":
                    self.logger.log(self.log_level, message.rstrip())

            def flush(self):
                pass

        stdout_logger = logging.getLogger('STDOUT')
        sl = StreamToLogger(stdout_logger, logging.INFO)
        sys.stdout = sl

        stderr_logger = logging.getLogger('STDERR')
        sl = StreamToLogger(stderr_logger, logging.ERROR)
        sys.stderr = sl
        exec(compile(open('minecraft.py').read(), 'minecraft.py', 'exec'))

    play_button = tk.Button(root, text="Play", command=minecraft, height=3, width=20, bg='gray')
    play_button.pack(side=tk.BOTTOM)

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