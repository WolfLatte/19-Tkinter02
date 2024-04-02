import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()

frm_1 = tk.Frame()
frm_1.pack()

label_1 = tk.Label(
    master = frm_1, 
    text = "Would you like some coffee?"
)
label_1.pack()

button_1 = tk.Button(
    window, 
    text = "Click!"
)
button_1.pack()

entry_1 = tk.Entry(
    window
)
entry_1.pack()

entry_1.insert(0, "Enter Order Here!")

frm_2 = tk.Frame()
frm_2.pack()

label_2 = tk.Label(
    master = frm_2, 
    text = "My personal thoughts on your order :)"
)
label_2.pack()

text_box = tk.Text()
text_box.pack()

text_box.insert("1.0", "HOT REGULARLY-BREWED COFFEE WITH CREAM.")
text_box.insert("2.0", "\nYou’re probably an older person.")
text_box.insert("3.0", "\nHOT, BLACK, REGULAR-BREWED COFFEE")
text_box.insert("4.0", "\nYou may not have emotions. Enjoy the bitter taste of dead coffee bean souls.You also might be a dad.")
text_box.insert("5.0", "\nICED COFFEE.")
text_box.insert("6.0", "\nI never understood iced coffee until I tried it, and now I love it.")
text_box.insert("7.0", "\nDOUBLE SHOT.")
text_box.insert("8.0", "\nYou are a student or a middle-aged person maybe in their 30’s")

window.mainloop()