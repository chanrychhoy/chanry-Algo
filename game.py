import tkinter as tk

# Create an empty window
windows = tk.Tk() 
# Set TK window size to width 600 px and height 600px
windows.geometry("600x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello player")
canvas = tk.Canvas(frame)
# player
canvas.create_oval(250,600,300,550,fill="red")
# HERE YOU CAN START TO DRAW
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
windows.mainloop()      