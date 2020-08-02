#This program takes tex command as input and output svg files. You must have texlive, pdftocairo installed in our system, the program is written for linux os. Written by Sasanka Dowarah.
import os
from PIL import Image
#Takes input from user.
tex_equation = input("Type equation - ")
scale = input("Put scaling % factor - ")

#open files to write.
tex_file = open('tex_file.tex','w')
tex_file.writelines("\documentclass[tikz]{standalone}\n")
tex_file.writelines("\\begin{document}\n")
tex_file.writelines("\\begin{tikzpicture}\n")
tex_file.writelines("\draw[line width=0mm] (0,0) rectangle (0,0) node [midway]\n")
tex_file.writelines("{$")
tex_file.writelines(tex_equation)
tex_file.writelines("$};\n")
tex_file.writelines("\end{tikzpicture}\n")
tex_file.writelines("\end{document}\n")
tex_file.close()

#system command to compile the tex file.
os.system('pdflatex tex_file.tex')
os.system('pdftocairo -png tex_file.pdf temp.png')
im=Image.open('temp.png-1.png')
os.system('pdftocairo -svg tex_file.pdf temp.svg')
width=im.size[0]
height=im.size[1]
sw=str(width*int(scale))
sh=str(height*int(scale))
def str_cat(x):
	s = ''
	for i in range(len(x)):
		s+=x[i]
	return s
py_file=open('scale.py','w')
py_file.writelines("import os\n")
py_file.writelines("os.system('rsvg-convert temp.svg -w"+" "+str_cat(sw)+" -h"+" "+str_cat(sh)+" -f svg -o output.svg')\n")
py_file.close()
os.system("python3 scale.py")

os.system('rm temp.png-1.png scale.py temp.svg tex_file.aux tex_file.log tex_file.pdf tex_file.tex')
os.system('exit')
print("Output is written in output.svg")
