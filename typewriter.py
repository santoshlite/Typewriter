from tkinter import *
from tkinter import filedialog
from tkinter import font
import tkinter as tk

root = Tk()
root.title('Writer')
root.geometry("630x1200")
root.configure(bg='#e6e6e6')

def open_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	name = text_file
	name = name.replace("C:/gui/", "")
	name = name.replace(".txt", "")
	
	text_file = open(text_file, 'r')
	stuff = text_file.read()

	my_text.insert(END, stuff)
	text_file.close()

	root.title(f'{name} - Textpad')

def open_pic():
	pic_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Pic File", filetypes=(("Pic Files", "*.jpg"), ))
	name = pic_file
	name = name.replace("C:/gui/", "")
	name = name.replace(".jpg", "")
	
	pic_file = open(pic_file, 'r')
	stuff = pic_file.read()

	my_text.insert(END, stuff)
	pic_file.close()

	root.title(f'{name} - Textpad')

def save_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	text_file = open(text_file, 'w')
	text_file.write(my_text.get(1.0, END))

def add_image():
	# Add image
	global my_image
	my_image = PhotoImage(file="images/profile.png")
	position = my_text.index(INSERT)
	my_text.image_create(position, image=my_image)

	

def select():
	selected = my_text.selection_get()
	my_label.config(text=selected)

def bolder():
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	my_text.tag_configure("bold", font=bold_font)

	current_tags = my_text.tag_names("sel.first")

	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last" )
	else:
		my_text.tag_add("bold", "sel.first", "sel.last" )


def italics_it():
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	my_text.tag_configure("italic", font=italics_font)
	current_tags = my_text.tag_names("sel.first")

	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last" )
	else:
		my_text.tag_add("italic", "sel.first", "sel.last" )

def Arial():
	arial_font = font.Font(my_text, my_text.cget("font"))
	arial_font.configure(family=("Arial"))

	my_text.tag_configure("arial", font=arial_font)

	current_tags = my_text.tag_names("sel.first")

	if "arial" in current_tags:
		my_text.tag_remove("arial", "sel.first", "sel.last" )
	else:
		my_text.tag_add("arial", "sel.first", "sel.last" )

def Calibri():
	arial_font = font.Font(my_text, my_text.cget("font"))
	arial_font.configure(family=("Calibri"))

	my_text.tag_configure("calibri", font=arial_font)

	current_tags = my_text.tag_names("sel.first")

	if "calibri" in current_tags:
		my_text.tag_remove("calibri", "sel.first", "sel.last" )
	else:
		my_text.tag_add("calibri", "sel.first", "sel.last" )

def Times_New_Roman():
	time_font = font.Font(my_text, my_text.cget("font"))
	time_font.configure(family=('Times New Roman'))

	my_text.tag_configure("time", font=time_font)

	current_tags = my_text.tag_names("sel.first")

	if "time" in current_tags:
		my_text.tag_remove("time", "sel.first", "sel.last" )
	else:
		my_text.tag_add("time", "sel.first", "sel.last" )

def SegoeUI():
	segoe_font = font.Font(my_text, my_text.cget("font"))
	segoe_font.configure(family=("Segoe UI"))

	my_text.tag_configure("segoe", font=segoe_font)

	current_tags = my_text.tag_names("sel.first")

	if "segoe" in current_tags:
		my_text.tag_remove("segoe", "sel.first", "sel.last" )
	else:
		my_text.tag_add("segoe", "sel.first", "sel.last" )

def ComicMS():
	comic_font = font.Font(my_text, my_text.cget("font"))
	comic_font.configure(family=("Comic Sans MS"))

	my_text.tag_configure("comic", font=comic_font)

	current_tags = my_text.tag_names("sel.first")

	if "comic" in current_tags:
		my_text.tag_remove("comic", "sel.first", "sel.last" )
	else:
		my_text.tag_add("comic", "sel.first", "sel.last" )

def Georgia():
	georgia_font = font.Font(my_text, my_text.cget("font"))
	georgia_font.configure(family=("Georgia"))

	my_text.tag_configure("georgia", font=georgia_font)

	current_tags = my_text.tag_names("sel.first")

	if "georgia" in current_tags:
		my_text.tag_remove("georgia", "sel.first", "sel.last" )
	else:
		my_text.tag_add("georgia", "sel.first", "sel.last" )

def Verdana():
	verdana_font = font.Font(my_text, my_text.cget("font"))
	verdana_font.configure(family=("Verdana"))

	my_text.tag_configure("verdana", font=verdana_font)

	current_tags = my_text.tag_names("sel.first")

	if "verdana" in current_tags:
		my_text.tag_remove("verdana", "sel.first", "sel.last" )
	else:
		my_text.tag_add("verdana", "sel.first", "sel.last" )

def fifteen():
	fif_font = font.Font(my_text, my_text.cget("font"))
	fif_font.configure(size="15")

	my_text.tag_configure("fif", font=fif_font)

	current_tags = my_text.tag_names("sel.first")

	if "fif" in current_tags:
		my_text.tag_remove("fif", "sel.first", "sel.last" )
	else:
		my_text.tag_add("fif", "sel.first", "sel.last" )

def twelve():
	tw_font = font.Font(my_text, my_text.cget("font"))
	tw_font.configure(size="12")

	my_text.tag_configure("tw", font=tw_font)

	current_tags = my_text.tag_names("sel.first")

	if "tw" in current_tags:
		my_text.tag_remove("tw", "sel.first", "sel.last" )
	else:
		my_text.tag_add("tw", "sel.first", "sel.last" )

def seven():
	seven_font = font.Font(my_text, my_text.cget("font"))
	seven_font.configure(size="17")

	my_text.tag_configure("seven", font=seven_font)

	current_tags = my_text.tag_names("sel.first")

	if "seven" in current_tags:
		my_text.tag_remove("seven", "sel.first", "sel.last" )
	else:
		my_text.tag_add("seven", "sel.first", "sel.last" )

def twen():
	twen_font = font.Font(my_text, my_text.cget("font"))
	twen_font.configure(size="20")

	my_text.tag_configure("twen", font=twen_font)

	current_tags = my_text.tag_names("sel.first")

	if "twen" in current_tags:
		my_text.tag_remove("twwen", "sel.first", "sel.last" )
	else:
		my_text.tag_add("twen", "sel.first", "sel.last" )

def twotwo():
	two_font = font.Font(my_text, my_text.cget("font"))
	two_font.configure(size="22")

	my_text.tag_configure("two", font=two_font)

	current_tags = my_text.tag_names("sel.first")

	if "two" in current_tags:
		my_text.tag_remove("two", "sel.first", "sel.last" )
	else:
		my_text.tag_add("two", "sel.first", "sel.last" )

def underline():
	un_font = font.Font(my_text, my_text.cget("font"))
	un_font.configure(underline = True)

	my_text.tag_configure("un", font=un_font)

	current_tags = my_text.tag_names("sel.first")

	if "un" in current_tags:
		my_text.tag_remove("un", "sel.first", "sel.last" )
	else:
		my_text.tag_add("un", "sel.first", "sel.last" )

def Red():
	over_font = font.Font(my_text, my_text.cget("font"))
	over_font.configure(overstrike=True)

	my_text.tag_configure("over", font=over_font)

	current_tags = my_text.tag_names("sel.first")

	if "over" in current_tags:
		my_text.tag_remove("over", "sel.first", "sel.last" )
	else:
		my_text.tag_add("over", "sel.first", "sel.last" )

def Blue():
	blue_font = font.Font(my_text, my_text.cget("font"))
	blue_font = text.tag_config("start", background="black", foreground="yellow")

	my_text.tag_configure("blue", font=blue_font)

	current_tags = my_text.tag_names("sel.first")

	if "blue" in current_tags:
		my_text.tag_remove("blue", "sel.first", "sel.last" )
	else:
		my_text.tag_add("blue", "sel.first", "sel.last" )

my_frame = Frame(root)
text_scroll = Scrollbar(my_frame)
my_text = Text(my_frame, width=70, height=80, font=("Arial",14), selectbackground="#75afff", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)


open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(side=LEFT, anchor=NW)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(side=LEFT, anchor=NW)


bold_button = Button(root, text="Bold", command=bolder)
bold_button.pack(side=LEFT, anchor=NW)

italics_button = Button(root, text="Italics", command=italics_it)
italics_button.pack(side=LEFT, anchor=NW)

red_button = Button(root, text="Overstrike", command=Red)
red_button.pack(side=LEFT, anchor=NW)

underline_button = Button(root, text="Underline", command=underline)
underline_button.pack(side=LEFT, anchor=NW)

arial_button = Button(root, text="Arial", command=Arial)
arial_button.pack(side=LEFT, anchor=NW)

calibri_button = Button(root, text="Calibri", command=Calibri)
calibri_button.pack(side=LEFT, anchor=NW)

time_button = Button(root, text="Times New Roman", command=Times_New_Roman)
time_button.pack(side=LEFT, anchor=NW)

segoe_button = Button(root, text="Segoe UI", command=SegoeUI)
segoe_button.pack(side=LEFT, anchor=NW)

comic_button = Button(root, text="Comic sans MS", command=ComicMS)
comic_button.pack(side=LEFT, anchor=NW)

georgia_button = Button(root, text="Georgia", command=Georgia)
georgia_button.pack(side=LEFT, anchor=NW)

verdana_button = Button(root, text="Verdana", command=Verdana)
verdana_button.pack(side=LEFT, anchor=NW)

tw_button = Button(root, text="12", command=twelve)
tw_button.pack(side=LEFT, anchor=NW)

fif_button = Button(root, text="15", command=fifteen)
fif_button.pack(side=LEFT, anchor=NW)

seven_button = Button(root, text="17", command=seven)
seven_button.pack(side=LEFT, anchor=NW)

twen_button = Button(root, text="20", command=twen)
twen_button.pack(side=LEFT, anchor=NW)

two_button = Button(root, text="22", command=twotwo)
two_button.pack(side=LEFT, anchor=NW)

undo_button = Button(root, text="Undo", command=my_text.edit_undo)
undo_button.pack(side=LEFT, anchor=NW)

redo_button = Button(root, text="Redo", command=my_text.edit_redo)
redo_button.pack(side=LEFT, anchor=NW)

my_frame.pack(pady=10)
# Create scrollbar
text_scroll.pack(side=RIGHT, fill=Y)
my_text.pack()
# Configure our scrollbar
text_scroll.config(command=my_text.yview)

root.mainloop()
