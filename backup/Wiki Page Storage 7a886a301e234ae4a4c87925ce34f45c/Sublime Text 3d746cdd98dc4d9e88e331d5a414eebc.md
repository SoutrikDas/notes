# Sublime Text

Column: Oct 31, 2020 4:50 PM
Last edited by: Soutrik das

# LSP for Python

How to set up a LSP for python ? It seems LSP is a server  , so you have to install a server 

, the problem was that LSP for python doesnt work unless you have opened a folder , 

that is , if you just have  a file open, then its not going to work 

---

You can customise a lot of the settings by going to LSP Preferences 

For example this piece of code 

```python
"diagnostics_highlight_style": "box",
```

makes the LSP box your errors or warnings

![Sublime%20Text%203d746cdd98dc4d9e88e331d5a414eebc/Untitled.png](Sublime%20Text%203d746cdd98dc4d9e88e331d5a414eebc/Untitled.png)

Which is something I do not want , but currently the only two options are `underline` and `box` , there is no disable function 

I was able to remove most of the squiggly lines , as they were warnings using the following code 

```python
"show_diagnostics_severity_level": 1,
```

This means when the diagnostic window is open , it will only show messages of level 1 

- 1 - errors
- 2 - warnings
- 3 - info
- 4 - hint

# Interactive build

---

 You can go to an external terminal and do 

```python
python -i <filename>.py
```

or if you want to do it inside the sublime Text then check this 

[[CQ32] Make any build system interactive with Terminus!](https://youtu.be/etIJMVIvVgg)

# Searching in Sublime

---

- `Ctrl+P` gives you searching of files by file names
- `Ctrl+Shift+F` lets you search files by file content
-