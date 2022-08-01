from tkinter import *
import tkinter.messagebox
 
def gpa_calculator(grades):
    points = 0
    i = 0
    crds = 0
    credit = {"1":1, "2":2, "3":3, "4":4}
    grade_c = {"A":4,"A-":3.75,"B+":3.5,"B":3.0,"B-":2.75, "C+":2.5,"C":2.0,"C-":1.5,"D":1.0,"F":0}
    if grades != []:
        for grade in grades:
            if grade not in grade_c:
                return "Invalid"
        points += grade_c[grade]
        gpa = (points * len(crds)) / len(grades)
        return gpa
    else:
        return None
 
class App:
    def __init__(self, parent):
        self.parent = parent
        self.frame_1 = Frame(parent)
        self.frame_1.pack()
        self.sub_count = 1
        self.subs = []
        Label(self.frame_1, text="Enter Grade :").grid(row=self.sub_count-1, column=0)
        self.subs.append(Entry(self.frame_1))
        self.subs[self.sub_count-1].grid(row=self.sub_count-1, column=1)
        Label(self.frame_1, text="Enter credit hour :").grid(row=self.sub_count-1, column=0)
        self.subs.append(Entry(self.frame_1))
        self.subs[self.sub_count-1].grid(row=self.sub_count-1, column=1)

 
        self.btn_1 = Button(parent, text="Add Courses !",
                            command=self.add_courses)
        self.btn_1.pack(pady=8)
        
        self.btn_3 = Button(parent, text="Add credit hour of the consequetive course !",
                            command=self.add_credit)
        self.btn_3.pack(pady=8)

        self.btn_2 = Button(parent, text="Calculate GPA",
                            command=self.calc_CG)
        self.btn_2.pack(pady=8)
 
    def add_courses(self):
        self.sub_count += 1
        Label(self.frame_1, text="Enter Grade :").grid(row=self.sub_count-1, column=0)
        self.subs.append(Entry(self.frame_1))
        self.subs[self.sub_count-1].grid(row=self.sub_count-1, column=1)
    
    def add_credit(self):
        self.sub_count += 1
        Label(self.frame_1, text="Enter credit hour :").grid(row=self.sub_count-1, column=0)
        self.subs.append(Entry(self.frame_1))
        self.subs[self.sub_count-1].grid(row=self.sub_count-1, column=1)
 
    def calc_CG(self):
        grades = []
        for sub in self.subs:
            if sub.get() != "":
                grades.append(sub.get())
        tkinter.messagebox.showinfo("Predicted CGPA ", str(gpa_calculator(grades)))
 
 
root = Tk()
app = App(root)
root.mainloop()
