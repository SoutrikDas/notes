# Grokking Algorithm - Aditya Bhargava

Column: Nov 5, 2020 3:19 PM
Last edited by: Soutrik das
Parent: Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45.md

# 5. Hash Tables

---

implementation of hash tables in python is dictionaries , basically , theres a function called hash function , when you give it a key , it instantly spits out a unique number , then you check the that index of another array ( which stores the values ) , and there you go , you put in a key , got the value instantly , no searching , instantly

# 6. Breadth First Search

---

> Breadth-first search allows you to find the shortest distance
between two things

You can

- write a checkers AI that calculates the fewest move to victory
- Write a spell checker for fewest edit to a real word ( Readed -> Reader is one edit )
- Finding the doctor closest to you in the network

## What is a graph ?

---

a graph is just a way to model information
Graphs are made up of nodes and edges
There are two types of graphs

- Undirected graphs ( Scalar)
- Directed graphs ( Vector)

so an example of directed graphs is , if A has to give a gift to B , but B doesnt have to give a gift to A , in this case you would want to use a directed graph

![Grokking%20Algorithm%20-%20Aditya%20Bhargava%20755f6e92ceb240ec99d0139e91d9682f/Untitled.png](Grokking%20Algorithm%20-%20Aditya%20Bhargava%20755f6e92ceb240ec99d0139e91d9682f/Untitled.png)

![Grokking%20Algorithm%20-%20Aditya%20Bhargava%20755f6e92ceb240ec99d0139e91d9682f/Untitled%201.png](Grokking%20Algorithm%20-%20Aditya%20Bhargava%20755f6e92ceb240ec99d0139e91d9682f/Untitled%201.png)

both of the following graphs are equal 

![Grokking%20Algorithm%20-%20Aditya%20Bhargava%20755f6e92ceb240ec99d0139e91d9682f/Untitled%202.png](Grokking%20Algorithm%20-%20Aditya%20Bhargava%20755f6e92ceb240ec99d0139e91d9682f/Untitled%202.png)