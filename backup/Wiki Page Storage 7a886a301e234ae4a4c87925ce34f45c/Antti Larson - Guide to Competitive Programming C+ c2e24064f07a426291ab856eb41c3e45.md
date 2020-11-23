# Antti Larson - Guide to Competitive Programming C++

Child: Grokking%20Algorithm%20-%20Aditya%20Bhargava%20755f6e92ceb240ec99d0139e91d9682f.md
Column: Nov 5, 2020 2:03 PM
Last edited by: Soutrik das
Parent: C++%20af78ebe91d7e4bd78a6245cc8bc0e666.md, Algorithm%209cd60dea97f742dba4e01aa71877da77.md, Books%20c09fa9d40bfa499ba9545c5017dd2010.md
Tags: book, cs

The problem set used for this page is the following:

[CSES Problem Set](https://cses.fi/problemset/)

 

# 2. Programming Techniques

---

Use `#include<bits/stdc++.h>` to include the standard library like 

- `iostream`
- `algorithm`
- `vector`

And this works on codeforces on GNU G++ 17 ! But only if you include the `.h` 

Ie , if you use 

```cpp
#include <bits/stdc++> //not going to work
```

Its not going to work. But If you use the following :

```cpp
#include <bits/stdc++.h> //going to work
```

Its going to work

However , If you want to individually include `iostream` , Then `#include<iostream.h>` would give a compilation error. The correct code is `#include<iostream>`

## Input and Output

---

Get the whole line using 

```cpp
string s;
getline(cin,s)
```

## Vectors

---

Vectors are a template class. What is a template class ? They are the class that cant be initialised normally ( `dtype a;` ) Rather you have to specify another datatype 

```cpp
vector<dtype> a;
vector<int> a;
```

Basically a vector is an array with some extra functionalities like dynamic length ( it can change length and the system will take care of it) 

### Size of a vector ? using `v.size()`

---

To get the size of a vector use the function `v.size()` where v is a vector 

![Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/vector_size.gif](Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/vector_size.gif)

### How to add or remove things to a vector ?

---

Use the `push_back()` function 

Heres code to push three things

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i];
    }
}
```

![Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/looping_iver_in_a_vector.gif](Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/looping_iver_in_a_vector.gif)

But you can also loop in a different way ( a bit more pythonisque way )

```cpp
for (int i:v)
    {
        cout << i;
    }
```

![Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/another_way_to_loop_over.gif](Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/another_way_to_loop_over.gif)

The above code will copy each element of `v` into `i` , which means if you are in a loop and change the value of `i` , it will not reflect the change in that element of vector `v` . To resolve this you can instead use a reference `for(int& i:v)`

To set the array size back to zero ( and clear everything ) use the `clear()` function 

```cpp
v.clear();
```

To Remove , you can use two things 

- `v.pop_back()` This works just like the `push_back`  meaning , it always removes stuff from the back ( just like a que ( that we learned in class xii ))
- `v.erase(some complex stuff)`

# Recursion

---

> When you write a recursive function, you have to tell it when to stop
recursing. that’s why every recursive function has two parts: the **base
case**, and the **recursive case**.

The recursive case is when the function calls itself , the recursive case is when the function doesnt call itself

## ( Call ) Stack

---

If you have a function like 

```cpp
def greet(name):
	print "hello"+name
	greet2(name)
	bye(name)

//Where greet2 and bye are other functions 
```

A box in the image represents a block of memory 

![Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/Untitled.png](Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/Untitled.png)

Then when you just enter the first function ( with the name `maggie` ) , your stack will be like this 

![Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/Untitled%201.png](Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/Untitled%201.png)

Now as it executes the first line , `greet2(name)` The stack becomes this.

![Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/Untitled%202.png](Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/Untitled%202.png)

Then as the `greet2(name)` function is over , The stack changes again 

![Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/Untitled%203.png](Antti%20Larson%20-%20Guide%20to%20Competitive%20Programming%20C+%20c2e24064f07a426291ab856eb41c3e45/Untitled%203.png)

> This is the big idea behind this section: when you call a function from another
function, the calling function is paused in a partially completed state. All the values of the variables for that function are still stored in memory

# Divide and Conquer (DC)

---

This problem solving method relies on recursion