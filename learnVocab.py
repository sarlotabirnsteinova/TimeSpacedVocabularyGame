import tkinter as tk
from vocabTest import VocabTest 
from pathlib import Path
import datetime

vocabTest_current = None

# the fun stuff
def load_VocabTest():
    """
    tries to load VocabTest named from input window, makes new if does not exist
    """
    global vocabTest_current
    fname = str(name_VocabTest.get())
    if len(fname)>0:
        fname_all = Path(__file__).with_name(fname)
        # print(f"File name inputed {fname_all}")  # , type{type(fname)} not sure if it won't make problems later
        # 
        vocabTest_current = VocabTest(fname_all)
        upate_hint_fn(f"Current file {fname_all}")
    else:
        new_no_name = Path(__file__).with_name(f"VocabUnits{datetime.date.today()}")
        vocabTest_current = VocabTest(new_no_name)
        upate_hint_fn(f"Newly created file \n {new_no_name}.")

def add_VocabUnit():
    """
    add new VocabUnit to VocabTest class
    """
    global vocabTest_current
    if vocabTest_current is None:
        upate_hint_add(f"Nowhere to add!")
        return
    native = str(entryWin_native.get())
    target = str(entryWin_target.get())
    native_long, target_long = None, None
    if len(entryWin_native_long.get())>0 and len(entryWin_target_long.get())>0:
        native_long, target_long = str(entryWin_native_long.get()), str(entryWin_target_long.get())
    # add new VocabUnit to current active VocabTest
    if len(native)>0:
        vocabTest_current.add_VocabUnit(native=native,target=target,native_long=native_long,target_long=target_long)
        entryWin_native.delete(0,len(native))
        entryWin_target.delete(0,len(target))
        if len(entryWin_native_long.get())>0 and len(entryWin_target_long.get())>0:
            entryWin_native_long.delete(0,len(native_long))
            entryWin_target_long.delete(0,len(target_long))
        upate_hint_add(f"Word '{native}' added.")
    else:
        upate_hint_add(f"Empty word '{native}' not added.")


def save_VocabTest():
    """
    save (pickle) changes made in VocabTest 
    """
    global vocabTest_current
    if vocabTest_current is not None:
        vocabTest_current.save_VocabUnitsList()
        upate_hint_fn(f"VocabTest saved as: \n {vocabTest_current.fname}!")
    else:
        upate_hint_fn("Nothing to save yet!")


def upate_hint_add(text):
    """
    Update hint under Add button.
    """
    hint5.configure(text=text)

def upate_hint_fn(text):
    """
    Update hint under filename for vocab test entry.
    """
    hint0.configure(text=text)

#..  Main Window   .......
window = tk.Tk()

ww, wh  = 600, 600
window.geometry(f"{ww}x{wh}")
window.config(bg="#82a3a1")
window.resizable(width=False,height=False)

#..  Main Titles & Main Buttons  .....
c_bg = "#82a3a1"
c_bluegray = "#465362"
c_darkblue = "#011936"
c_green_darker = "#9fc490"
c_green = "#c0dfa1"

window.title('Vocab Learning Game')

exit_button = tk.Button(window,text="Exit Game",font=("Arial",11), fg="White", bg="#465362", command=exit)
exit_button.place(x=505,y=5)
save_button = tk.Button(window,text="Save Game",font=("Arial",11,"bold"), fg=c_green_darker, bg=c_darkblue,command=save_VocabTest)
save_button.place(x=505,y=35)

#..  Labels   ........
title = tk.Label(window,text="Vocab Learning Game",font=("Arial",26,"bold"),fg="#011936",bg=c_bg)
title.place(x=80, y=30)
title2 = tk.Label(window,text="New words to learn!",font=("Arial",26),fg="#011936",bg=c_bg)
title2.place(x=170, y=250)

fs_hint = 12
hint0 = tk.Label(window, text="Click Start VocabInput to load VocabTest Library", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint0.place(x=40, y=190)
hint1 = tk.Label(window, text="native", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint1.place(x=90+30, y=wh/5*3-20)
hint2 = tk.Label(window, text="target", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint2.place(x=320+30, y=wh/5*3-20)
hint3 = tk.Label(window, text="native: an example sentence", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint3.place(x=90-20, y=wh/4*3-20)
hint4 = tk.Label(window, text="target: an example sentence", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint4.place(x=320-10, y=wh/4*3-20)
hint5 = tk.Label(window, text="", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint5.place(x=ww*2/5+20, y=wh*6/7+40)


#..  buttons  ..........
find_test_button = tk.Button(window, text="Load VocabTest", font=("Arial", 14), fg = "White", bg="#011936",command=load_VocabTest)
find_test_button.place(x=370, y=147) 

add_newVocab_button = tk.Button(window,text="Add new!",font=("Arial",14, "bold"), fg="White",bg="#011936",command=add_VocabUnit)
add_newVocab_button.place(x=ww*2/5, y=wh*6/7)

#..  input windows  .....
# filename of VocabTest
fn_VocabTest = tk.StringVar()
name_VocabTest = tk.Entry(window,font=("Arial",12),textvariable=fn_VocabTest)
name_VocabTest.place(x=180, y=150)
# new VocabUnit input
input_native, input_target = tk.StringVar(), tk.StringVar()
input_native_long, input_target_long = tk.StringVar(), tk.StringVar()
entryWin_native = tk.Entry(window,font=("Arial",14),textvariable=input_native)
entryWin_native.place(x=40, y=wh/5*3)
entryWin_target = tk.Entry(window,font=("Arial",14),textvariable=input_target)
entryWin_target.place(x=300, y=wh/5*3)
entryWin_native_long = tk.Entry(window,font=("Arial",14),textvariable=input_native_long)
entryWin_native_long.place(x=40, y=wh/4*3)
entryWin_target_long = tk.Entry(window,font=("Arial",14),textvariable=input_target_long)
entryWin_target_long.place(x=300, y=wh/4*3)


# Start the window
window.mainloop()