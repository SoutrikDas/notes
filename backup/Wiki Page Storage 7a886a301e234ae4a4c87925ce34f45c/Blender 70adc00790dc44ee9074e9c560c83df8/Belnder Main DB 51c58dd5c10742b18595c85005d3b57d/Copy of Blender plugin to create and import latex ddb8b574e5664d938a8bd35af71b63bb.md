# Copy of Blender plugin to create and import latex

So the few commands that work are

Template 

```python
\documentclass[preview]{standalone}\usepackage[english]{babel}\usepackage{amsmath}\usepackage{amssymb}\usepackage{dsfont}\usepackage{setspace}\usepackage{tipa}\usepackage{relsize}\usepackage{textcomp}\usepackage{mathrsfs}\usepackage{calligra}\usepackage{wasysym}\usepackage{ragged2e}\usepackage{physics}\usepackage{xcolor}\usepackage{microtype}\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\linespread{1}
\DisableLigatures{encoding = *, family = *}

\begin{document}

\begin{align*}
Tex Here
\end{align*}

\end{document}
```

Then 

```python
latex -interaction=batchmode [filename].tex
```

This converts the .tex file to .dvi 

Then 

```python
dvisvgm **-n**  [filename].dvi 
```

This gives an output of type svg 

## Importing an SVG in blender

---

```python
import bpy 

a=bpy.ops.import_curve.svg(filepath=r"D:\Coding_Projects\manim\media\Tex\abc.svg",filter_glob=".svg")
```

The important part is that the path should be in raw format