
import os
from PIL import Image



#Takes tex input from user.
tex_equation = input("Type equation - ")

#Takes scale input from user.
scale = input("Type scaling factor - ")


#open files to write.
tex_file = open('tex_file.tex','w')
tex_file.write(r"""
\documentclass[tikz]{standalone}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{physics}
\begin{document}
\begin{tikzpicture}
\draw[line width=0mm] (0,0) rectangle (0,0) node [midway]
{$""")
tex_file.writelines(tex_equation)
tex_file.write(r"""
 $};
\end{tikzpicture}
\end{document}
""")
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

#determines the width and height of the png file.
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
os.system("rm -rf temporary")
os.system("mkdir temporary")
os.system("mv temp.png-1.png scale.py temp.svg tex_file.aux tex_file.log tex_file.tex tex_file.pdf temporary")
#remove temporary file.
#os.system('rm temp.png-1.png scale.py temp.svg tex_file.aux tex_file.log tex_file.tex')
os.system('exit')
print("Output is written in output.svg")
