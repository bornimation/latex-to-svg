#This program takes tex command as input and output svg files. You must have texlive, pdftocairo installed in our system, the program is written for linux os. Written by Sasanka Dowarah.
import os
from PIL import Image
print("Runs on linux only. This program takes tex equation as input and produces svg file of the equation using LaTeX. Type your equation below as you type in a LaTeX compiler. The scale factor (non zero integer) scales your svg file by the input given. Typical values for scale input are 1(no scaling),10,100. Output will be written in output.svg file. Check the program for more info.\n")

#if you want to use the svg files in blender, you should use scaling.
#install texlive : sudo apt install texlive --full.
#install pdftocairo : sudo apt install poppler-utils.
#install PIL : pip install Pillow.
#pillow is not required if you do not want scaling.
#install rsvg convert : apt-get install librsvg2-bin.
#rsvg package is not required if you do not want scaling.

#Takes tex input from user.
tex_equation = input("Type equation - ")

#Takes scale input from user.
scale = input("Type scaling factor - ")

#open files to write.
tex_file = open('tex_file.tex','w')
tex_file.writelines("\documentclass[tikz]{standalone}\n")
tex_file.writelines("\\usepackage[utf8]{inputenc}\n")
tex_file.writelines("\\usepackage{amsmath}\n")
tex_file.writelines("\\usepackage{amssymb}\n")
tex_file.writelines("\\usepackage{physics}\n")
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

#we want to do scaling by keeping the aspect ratio same. For that we need the dimension of the image. We will first convert the pdf output of LaTeX to a png file to estimate the dimension, then we will use the dimensions to scale the svg file.
#pdf to png conversion.
os.system('pdftocairo -png tex_file.pdf temp.png')

#opens the png file.
im=Image.open('temp.png-1.png')

#pdf to svg conversion.
os.system('pdftocairo -svg tex_file.pdf temp.svg')

#deermines the width and height of the png file.
width=im.size[0]
height=im.size[1]

#height and width are scaled.
sw=str(width*int(scale))
sh=str(height*int(scale))

def str_cat(x):
	s = ''
	for i in range(len(x)):
		s+=x[i]
	return s

#python file to scale.
py_file=open('scale.py','w')
py_file.writelines("import os\n")
py_file.writelines("os.system('rsvg-convert temp.svg -w"+" "+str_cat(sw)+" -h"+" "+str_cat(sh)+" -f svg -o output.svg')\n")
py_file.close()

#runs python file.
os.system("python3 scale.py")

#remove temporary file.
os.system('rm temp.png-1.png scale.py temp.svg tex_file.aux tex_file.log tex_file.pdf tex_file.tex')
os.system('exit')
print("Output is written in output.svg")
