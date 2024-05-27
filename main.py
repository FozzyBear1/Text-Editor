import tkinter as tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)

    window.title(f"Open File: (filepath)")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: (filepath)")

def change_font_size(text_edit, font, delta):
    size = font['size']
    new_size = size + delta
    if new_size > 0:  # Prevent the font size from becoming zero or negative
        font.configure(size=new_size)



def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=40)  # Adjust minsize as needed for the buttons to fit
    window.rowconfigure(1, minsize=400)  # Adjust remaining space for the text widget
    window.columnconfigure(0, minsize=600)

    # Font
    font = Font(family="Arial", size=14)

    # Creates the actual text interface
    text_edit = tk.Text(window, font=font)
    text_edit.grid(row=1, column=0, sticky="nsew")

    # Frame
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    frame.grid(row=0, column=0, sticky="ew")  # Set frame at the top row spanning entire width


    # Scrollbar
    scrollbar = tk.Scrollbar(window, orient="vertical", command=text_edit.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    text_edit['yscrollcommand'] = scrollbar.set

    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    increase_font_button = tk.Button(frame, text="+", command=lambda: change_font_size(text_edit, font, 1))
    decrease_font_button = tk.Button(frame, text="-", command=lambda: change_font_size(text_edit, font, -1))

    save_button.pack(side=tk.LEFT, padx=5, pady=5)
    open_button.pack(side=tk.LEFT, padx=5)
    increase_font_button.pack(side=tk.LEFT, padx=5)
    decrease_font_button.pack(side=tk.LEFT, padx=5)

    window.bind("<Control-s>", lambda event: save_file(window, text_edit))
    window.bind("<Control-o>", lambda event: open_file(window, text_edit))
    
    window.mainloop()

main()
