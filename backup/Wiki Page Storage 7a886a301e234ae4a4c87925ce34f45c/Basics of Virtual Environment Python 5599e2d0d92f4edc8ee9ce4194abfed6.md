# Basics of Virtual Environment Python

Column: Oct 9, 2020 9:33 PM
Last edited by: Soutrik das
Parent: Python%20py%2037f8f5b26a314016a6c73e8e8340af98.md

Use `pip install virtualenv` to install the package

![Basics%20of%20Virtual%20Environment%20Python%205599e2d0d92f4edc8ee9ce4194abfed6/Untitled.png](Basics%20of%20Virtual%20Environment%20Python%205599e2d0d92f4edc8ee9ce4194abfed6/Untitled.png)

To test if it has been installed , use `virtualenv --version` 

`virtualenv venv` will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, it was `venv`) can be anything; omitting the name will place the files in the current directory instead.

So go to your project Directory and type `virtualenv <name>` 

- if you put the name , it will make a folder with that name
- if you dont put the name , it will not make any folder , but put the files in that directory

# How to use a virtual env

---

To use it You must activate it 

```bash
venv\Scripts\activate
```

On running this command you will see some changes 

![Basics%20of%20Virtual%20Environment%20Python%205599e2d0d92f4edc8ee9ce4194abfed6/Untitled%201.png](Basics%20of%20Virtual%20Environment%20Python%205599e2d0d92f4edc8ee9ce4194abfed6/Untitled%201.png)