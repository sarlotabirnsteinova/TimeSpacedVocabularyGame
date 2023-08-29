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
        vocabTest_current = VocabTest(fname_all)
        update_hint_fn(f"Current file \n {fname_all}")
    else:
        new_no_name = Path(__file__).with_name(f"VocabUnits{datetime.date.today()}")
        vocabTest_current = VocabTest(new_no_name)
        update_hint_fn(f"Newly created file \n {new_no_name}.")
    # start testing with fistr expression
    # nextVocabUnit()

def save_VocabTest():
    """ 
    save (pickle) changes made in VocabTest 
    """
    global vocabTest_current
    if vocabTest_current is not None:
        vocabTest_current.save_VocabUnitsList()
    else:
        update_hint_fn("Nothing to save yet!")

def submit_answer():
    """
    submitt answer to VocabTest class
    """
    global vocabTest_current
    if vocabTest_current.currentVocabUnit is not None:
        answer_str = str(entryWin_answer.get())   # read answer from window
        hint_str = str(vocabTest_current.give_correct_answer())   
        update_hint_result(hint_str)  # print right answers
        # check answer in VocabTest instance
        transl_status = vocabTest_current.process_test(answer_str)
        # clear entrz window for another expression
        entryWin_answer.delete(0,len(answer_str))
        print(f"Your answer was: {transl_status}")
    else:
        update_hint_result("Test is empty.")


def nextVocabUnit():
    """
    test nextVocabUnit from VocabTest class
    """
    global vocabTest_current
    # clean result hint
    update_hint_result("")
    # change hint_prompt
    if vocabTest_current.currentVocabUnit is not None:
        native_str = vocabTest_current.currentVocabUnit.native
        native_long_str = vocabTest_current.currentVocabUnit.native_long
        if native_long_str is not None:
            update_hint_next(f"{native_str}\n{native_long_str}")
        else:
            update_hint_next(f"{native_str}")
    else:
        update_hint_result("Out of expression for this VocabTest. \n  Save or reload this test or load a new one.   :)")
    
    
# updating hint texts
def update_hint_fn(text):
    """
    Update hint under filename for vocab test entry.
    """
    hint0.configure(text=text)

def update_hint_result(text):
    """
    Update hints after submitting answer.
    """
    hint_result.configure(text=text)
    pass

def update_hint_next(text):
    """
    Update hints after new VocabUnit is loaded.
    """
    hint_prompt.configure(text=text)
    pass

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

window.title('Vocab Test Game')

exit_button = tk.Button(window,text="Exit Game",font=("Arial",11), fg="White", bg="#465362", command=exit)
exit_button.place(x=505,y=5)
save_button = tk.Button(window,text="Save Game",font=("Arial",11,"bold"), fg=c_green_darker, bg=c_darkblue,command=save_VocabTest)
save_button.place(x=505,y=35)

#..  Labels   ........
title = tk.Label(window,text="Vocab Test Game",font=("Arial",26,"bold"),fg="#011936",bg=c_bg)
title.place(x=170, y=30)
title2 = tk.Label(window,text="Test Words",font=("Arial",26),fg="#011936",bg=c_bg)
title2.place(x=ww/3, y=wh*1/4+50)

fs_hint = 12
hint0 = tk.Label(window, text="Click Load VocabTest", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint0.place(x=ww/5, y=wh*1/5+30)
#
hint1 = tk.Label(window, text="Word or expression to translate", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint1.place(x=ww/4-20, y=wh*2/5+20) 
hint3 = tk.Label(window, text="Your answer:", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint3.place(x=ww/3-20, y=wh/3*2-20) 
hint4 = tk.Label(window, text="Result:", font=("Arial", fs_hint, "normal", "italic"),fg = "White", bg=c_bg, justify=tk.LEFT)
hint4.place(x=ww/3-20, y=wh/5*4-10) 
# changing hints
hint_prompt = tk.Label(window, text="", font=("Arial", fs_hint+2, "normal", "bold"),fg = c_darkblue, bg="White", justify=tk.LEFT)
hint_prompt.place(x=ww/3-20, y=wh/2)
hint_result = tk.Label(window, text="", font=("Arial", fs_hint+2, "normal"),fg = c_darkblue, bg="White", justify=tk.LEFT)
hint_result.place(x=ww/3-20, y=wh/5*4+20)

#..  buttons  ..........
find_test_button = tk.Button(window, text="Load VocabTest", font=("Arial", 14), fg = "White", bg="#011936",command=load_VocabTest)
find_test_button.place(x=ww/4*3-60, y=wh/5-3) 

submit_answer_button = tk.Button(window,text="Submit answer",font=("Arial",14, "bold"), fg="White",bg="#011936",command=submit_answer)
submit_answer_button.place(x=ww/2+50, y=wh/4*3-35)

nextUnit_button = tk.Button(window,text="Next",font=("Arial",14, "bold"), fg=c_green_darker,bg="#011936",command=nextVocabUnit)
nextUnit_button.place(x=ww/2-20, y=wh-40)

#..  input windows  .....
# filename of VocabTest
fn_VocabTest = tk.StringVar()
name_VocabTest = tk.Entry(window,font=("Arial",14),textvariable=fn_VocabTest)
name_VocabTest.place(x=ww/4, y=wh/5)
# answer input
input_answer = tk.StringVar()
entryWin_answer = tk.Entry(window,font=("Arial",14),textvariable=input_answer)
entryWin_answer.place(x=ww/4-20, y=wh/4*3-30)

# Start the window
window.mainloop()