"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Valeria Paiz.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------

    # root = tkinter.Tk()
    # frame = ttk.Frame(root, padding=20)
    # frame.grid()
    # button = ttk.Button(frame, text='Button 1')
    # button.grid()
    # root.mainloop()

    root2 = tkinter.Tk()

    frame2 = ttk.Frame(root2, padding=20)
    frame2.grid()

    hello_button = ttk.Button(frame2, text='Print Hello')
    hello_button['command'] = lambda: print('Hello')
    hello_button.grid(row=0, column=0)

    entry_box = ttk.Entry(frame2)
    entry_box.grid(row=1, column=0)

    hg_button = ttk.Button(frame2, text='Print Hello/Goodbye')
    hg_button.grid(row=3, column=0)
    hg_button['command'] = lambda: hello_goodbye(entry_box)

    integer_entry = ttk.Entry(frame2)
    integer_entry.grid(row=4, column=0)

    repeat_button = ttk.Button(frame2, text='Repeat Text')
    repeat_button.grid(row=5, column=0)
    repeat_button['command'] = lambda: print_repeat(entry_box, integer_entry)

    root2.mainloop()


def hello_goodbye(entry_box):
    if entry_box.get() == 'ok':
        print('Hello')
    else:
        print('Goodbye')


def print_repeat(entry_box, integer_box):
    num = int(integer_box.get())
    for k in range(num):
        print(entry_box.get())


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
