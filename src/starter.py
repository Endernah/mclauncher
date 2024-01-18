import main
args = main.args

if not args.terminal:
    import tkinter as tk
    def print_hello():
        print("Hello World")

    root = tk.Tk()
    button = tk.Button(root, text="Hello World", command=print_hello)
    button.pack()

    root.mainloop()
