from Tkinter import *

r = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print v.get()

Label(r, 
      text="""Choose your favourite 
programming language:""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(r, 
                text=txt,
                padx = 20, 
                variable=val, 
                command=ShowChoice,
                value=val).pack(anchor=W)

mainloop()
