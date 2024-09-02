from tkinter import*
from tkinter.messagebox import*
import math 

root = Tk()
root.title("ANGLE CONVERTOR")
root.geometry("600x600+100+100")
root.configure(bg = "lightblue")
f = ("Arial", 30, "bold",)

def d_to_r():
	try:
		d = float(ent_degree.get())
		if (d < 0.0) or (d> 360) :
			showerror("issue", "Value should be min 1 or max 360")
			return
		r = math.radians(d)
		ent_degree.delete(0,END)
		ent_degree.focus()
		showinfo("Radian ", round(r,2))
	except ValueError:
		showerror("issue", "Degree Cannot be empty or Alphabet")
	except Exception as e:
		showerror("issue", e)


def r_to_d():
	try:
		r = float(ent_radian.get())
		if (r < 0.0) or (r> 360) :
			showerror("issue", "Value should be min 1 or max 360")
			return
		d = math.degrees(r)
		ent_radian.delete(0,END)
		ent_radian.focus()
		showinfo("Degree ", round(d,2))
	except ValueError:
		showerror("issue", "Radian Cannot be empty or Alphabet")
	except Exception as e:
		showerror("issue", e)
		

lab_header = Label(root, text= "ANGLE CONVERTOR", font=f, bg = "lightblue")
lab_header.pack(pady=20)
	
lab_degree = Label(root, text = "DEGREES", font=f, bg = "lightblue" )
ent_degree = Entry(root, font=f)
lab_degree.pack(pady=10)
ent_degree.pack(pady=10)

btn_degree = Button(root, text="CONVERT", font=f, command = d_to_r)
btn_degree.pack(pady = 10)

lab_radian = Label(root, text = "RADIANS", font=f, bg = "lightblue")
ent_radian = Entry(root, font=f)
lab_radian.pack(pady=10)
ent_radian.pack(pady=10)

btn_radian = Button(root, text="CONVERT", font=f, command = r_to_d)
btn_radian.pack(pady = 10)

root.mainloop()