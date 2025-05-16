import tkinter as tk
root = tk.Tk()

art = '''

 ____        _ _              
/ ___| _   _| | |_ __ _ _ __  
\___ \| | | | | __/ _` | '_ \ 
 ___) | |_| | | || (_| | | | |
|____/ \__,_|_|\__\__,_|_| |_|
                              
Enter Text you want to convert to ASCII art : Sultan
+-+-+-+-+-+-+
|S|u|l|t|a|n|
+-+-+-+-+-+-+


'''

print(art)

label = tk.Label(text=art)
label.pack()

root.mainloop()
