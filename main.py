from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time
import random

class PortfolioApp:
    """Class representing the Portfolio Application."""
    def __init__(self, master):
        # Initialize the Tkinter window
        self.master = master
        # Set window size
        master.geometry("1500x800")
        # Disable window resizing
        master.resizable(0, 0)
        # Set window title
        master.title("Arsalan's Portfolio")  
        # Keep window on top
        master.attributes("-topmost", True)
        # Set window background color
        master.configure(background="#0a1013") 
        # Create and layout the widgets
        self.create_widgets()


    def create_widgets(self):
        """This method will contain the creation and layout of widgets"""
        

        # Create widgets (labels) and place them in the grid
        label1 = Label(self.master, text="Label 1")
        label1.grid(row=0, column=0)

        label2 = Label(self.master, text="Label 2")
        label2.grid(row=0, column=1)

        label3 = Label(self.master, text="Label 3")
        label3.grid(row=1, column=0, columnspan=2)  # Spanning two columns

        # Configure row and column weights for resizing
        self.master.grid_rowconfigure(0, weight=1)  # Make row 0 resizable
        self.master.grid_rowconfigure(1, weight=1)  # Make row 1 resizable
        
        self.master.grid_columnconfigure(0, weight=1)  # Make column 0 resizable
        self.master.grid_columnconfigure(1, weight=1)  # Make column 1 resizable


def main():
    """Initialize the Tkinter window and application."""
    window = Tk()  # Create Tkinter window
    app = PortfolioApp(window)  # Create instance of PortfolioApp
    window.mainloop()  # Run the Tkinter event loop


# Check if the script is executed directly
if __name__ == "__main__":
    # Call the main function to start the application
    main()
