if not args.terminal:
    import tkinter as tk
    def print_hello():
        print("Hello World")

    root = tk.Tk()
    button = tk.Button(root, text="Hello World", command=print_hello)
    button.pack()

    root.mainloop()
else:
    print("Terminal mode.")
    mode = 'offline'
    exec(compile(open('minecraft.py').read(), 'minecraft.py', 'exec'))