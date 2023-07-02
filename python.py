from tkinter import *

root = Tk()
root.maxsize(800, 600)
root.minsize(800, 600)
root.title("Percentage Application")

# Class - 03

maths_03 = Label(root, text="Maths: ")
maths_03.place(relx=0.45, rely=0.02, anchor=CENTER)
ent_maths03 = Entry(root)
ent_maths03.place(relx=0.55, rely=0.025, anchor=CENTER)

eng_03 = Label(root, text="English: ")
eng_03.place(relx=0.45, rely=0.055, anchor=CENTER)
ent_eng03 = Entry(root)
ent_eng03.place(relx=0.552, rely=0.055, anchor=CENTER)

sci_03 = Label(root, text="Science: ")
sci_03.place(relx=0.45, rely=0.085, anchor=CENTER)
ent_sci03 = Entry(root)
ent_sci03.place(relx=0.553, rely=0.085, anchor=CENTER)

# social03 = Label(root, text="Social Science: ")
# social03.place(relx=0.4, rely=0.105, anchor=CENTER)
# ent_social03 = Entry(root)
# ent_social03.place(relx=0.6, rely=0.105, anchor=CENTER)

# hindi03 = Label(root, text="Hindi: ")
# hindi03.place(relx=0.5, rely=0.135, anchor=CENTER)
# ent_hindi03 = Entry(root)
# ent_hindi03.place(relx=)

lbl_outof = Label(root, text="Each subject out of: ")
lbl_outof.place(relx=0.428, rely=0.115, anchor=CENTER)
ent_outof = Entry(root)
ent_outof.place(relx=0.572, rely=0.115, anchor=CENTER)



lbl_output3 = Label(root)
lbl_output3.place(relx=0.5, rely=0.2, anchor=CENTER)

# Class - 04


maths_04 = Label(root, text="Maths: ")
maths_04.place(relx=0.45, rely=0.25, anchor=CENTER)
ent_maths04 = Entry(root)
ent_maths04.place(relx=0.55, rely=0.25, anchor=CENTER)

eng_04 = Label(root, text="English: ")
eng_04.place(relx=0.45, rely=0.28, anchor=CENTER)
ent_eng04 = Entry(root)
ent_eng04.place(relx=0.552, rely=0.28, anchor=CENTER)

sci_04 = Label(root, text="Science: ")
sci_04.place(relx=0.45, rely=0.31, anchor=CENTER)
ent_sci04 = Entry(root)
ent_sci04.place(relx=0.553, rely=0.31, anchor=CENTER)

lbl_outof1 = Label(root, text="Each subject out of: ")
lbl_outof1.place(relx=0.428, rely=0.34, anchor=CENTER)
ent_outof1 = Entry(root)
ent_outof1.place(relx=0.572, rely=0.34, anchor=CENTER)


lbl_output4 = Label(root)
lbl_output4.place(relx=0.5, rely=0.42, anchor=CENTER)

# Class - 06


maths_06 = Label(root, text="Maths: ")
maths_06.place(relx=0.45, rely=0.47, anchor=CENTER)
ent_maths06 = Entry(root)
ent_maths06.place(relx=0.55, rely=0.47, anchor=CENTER)

eng_06 = Label(root, text="English: ")
eng_06.place(relx=0.45, rely=0.5, anchor=CENTER)
ent_eng06 = Entry(root)
ent_eng06.place(relx=0.552, rely=0.5, anchor=CENTER)

sci_06 = Label(root, text="Science: ")
sci_06.place(relx=0.45, rely=0.53, anchor=CENTER)
ent_sci06 = Entry(root)
ent_sci06.place(relx=0.553, rely=0.53, anchor=CENTER)

lbl_outof2 = Label(root, text="Each subject Total Mark: ")
lbl_outof2.place(relx=0.428, rely=0.56, anchor=CENTER)
ent_outof2 = Entry(root)
ent_outof2.place(relx=0.572, rely=0.56, anchor=CENTER)

lbl_outof2sci = Label(root, text=",  Science Total Marks: ")
lbl_outof2sci.place(relx=0.71, rely=0.56, anchor=CENTER)
ent_outof2sci = Entry(root)
ent_outof2sci.place(relx=0.84, rely=0.56, anchor=CENTER)


lbl_output6 = Label(root)
lbl_output6.place(relx=0.5, rely=0.66, anchor=CENTER)

class class_03():
    def __init__(self):
        pass
        # self.mathmatics = int(mathmatics)
        # self.english = int(english)
        # self.science = int(science)
        # self.outof = outof
        
    def percentage(self):
        math = ent_maths03.get()
        eng = ent_eng03.get()
        sci = ent_sci03.get()
        totalMarks = ent_outof.get()
        
        totalmarks = int(math)+int(eng)+int(sci)
        percent = totalMarks*100/(outof*3)
        lbl_output3['text'] = str(percent)
       

obj_class03 = class_03(math, eng, sci, totalMarks)
obj_class03.percentage()

class class_04():
    def __init__(self, mathmatics, english, science, outof):
        self.mathmatics = mathmatics
        self.english = english
        self.science = science
        self.outof = outof
        
        totalmarks = int(self.mathmatics+self.english+self.science)
        
        self.percent = totalmarks*100/(self.outof*3)
        
    def percentage(self):
        lbl_output4['text'] = int(self.percent)
        
btn_class6 = Button(root, text="Class 06")
btn_class6.place(relx=0.5, rely=0.61, anchor=CENTER)

btn_class3 = Button(root, text="Class 03", command=obj_class03.percentage)
btn_class3.place(relx=0.5, rely=0.15, anchor=CENTER)

btn_class4 = Button(root, text="Class 04")
btn_class4.place(relx=0.5, rely=0.37, anchor=CENTER)

root.mainloop()