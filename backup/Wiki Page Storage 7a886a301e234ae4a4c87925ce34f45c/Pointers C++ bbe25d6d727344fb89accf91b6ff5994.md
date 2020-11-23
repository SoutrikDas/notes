# Pointers C++

Column: Oct 11, 2020 9:15 PM
Last edited by: Soutrik das
Parent: C++%20af78ebe91d7e4bd78a6245cc8bc0e666.md

A pointer is a variable that holds a memory address, usually the location of another variable in the memory 

The concept of pointers is a very strong yet most dangerous and vulnerable feature of C++ , if used incorrectly , they cause minute bugs that are hard to figure out 

Every byte in the computers memory has an adress ( just numbers ) A pointer stores these adresses

After compiling a program , c++ has four distinct regions of memory for four specific functions 

![Pointers%20C++%20bbe25d6d727344fb89accf91b6ff5994/WhatsApp_Image_2020-09-19_at_12.51.01_PM.jpeg](Pointers%20C++%20bbe25d6d727344fb89accf91b6ff5994/WhatsApp_Image_2020-09-19_at_12.51.01_PM.jpeg)

- The program code holds the compiled c++ program code
- The next region (2) holds global variables , Global Variables remain in memory for as long as the program runs

# Compilation

In simple words we can say compilation is just converting our source code ( human readable ) to machine readable code ( assembly code I believe ) 

But its not that simple 

## Step 1: Preprocessing

When you write a source code file in C++, you include header files with extensions .h, .hxx, or .hpp, and sometimes with no extensions. You use the directive #include to mark a header file. The source file usually has the extension .cc, .cxx or .cpp.

The preprocessor directives are just ways of telling the compiler that 

> hey before you work on compiling the serious stuff , there are some small stuff , like if you find a #define macro a*b then please replace "macro" with a*b everywhere in the program 
Or 
If you find #include , then please put all the header file source code inside the main .cpp file ( maybe this is not correct )

Before Pre processing : 

```cpp
#include <iostream>

using namespace std;

#define PI 3.14159

int main()

{
    cout << "Value of PI:" << PI << endl;
    return0;
}
```

After Pre processing 

```cpp
int main()

{
    cout << "Value of PI:" << 3.14159 << endl;
    return 0;
}
```

So the preprocessing is just find and replace ( sometimes ) 

> Overall, in the preprocessor stage, the source code file is temporarily expanded to prepare for compilation. This file has a greater number of lines that your simple source code. You can print this preprocessed file on stdout. Header files add bulk to the code. The more header files you include, the longer the preprocessed file will be.

So yeah , header files get added to the main.cpp file 

> The preprocessor also adds some markers on the code to tell the compiler where each line came from. This helps to produce error messages that make sense to you.

# Static v/s Dynamic Allocation

### The golden rule of computer

> Anything and Everything ( data or instruction ) that needs to be processed must be loaded into internal memory before its processing takes place.

The memory is allocated to data or instructions in two ways 

- Statically
- Dynamically

## Static Allocation

When the memory to be allocated is known before hand ( you know you need 4KB for a variable ) , and is allocated during compilation itself , it is static memory allocation

## Dynamic Allocation

When the amount of memory to be allocated is not known rather it is required to allocate main memory as and when required during runtime ( when the program is actually executing ) itself, then the allocation of memory at run time is referred to as dynamic memory allocation 

C++ offers two operators for dynamic memory allocation 

- new - allocates memory dynamically and returns a pointer storing the memory address
- delete - deallocates memory pointed by the given pointer

Global variables have a static extent ( lifetime of the program ) 

Local variables have local extent 

Dynamically allocated objects on heap memory ( free store memory ) have dynamic extent (means they do not have any pre defined extent ( they remain in memory until explicitly removed using delete ) 

### Declaration and Initialization of Pointers

```cpp
type * var ;
int * iptr; //initializes a integer pointer iptr
char * cptr; //initializes a char pointer cptr
float * fptr ;//initializes a float pointer fptr
```

When we say iptr is an integer pointer we really mean that the memory it points to , has int value 

![Pointers%20C++%20bbe25d6d727344fb89accf91b6ff5994/Untitled.png](Pointers%20C++%20bbe25d6d727344fb89accf91b6ff5994/Untitled.png)

```cpp
int i =5;
int * iptr ; //declaration
iptr = & i ;  //initialisation //stores the memory address of i in the iptr 
```

if `i` is a variable then `&i` returns a pointer to that variable 

### Dereferencing ( accessing the values in a pointer )

Using the `*` operator to change/access the values of a pointer is called dereferencing 

```cpp
cout<<(*iptr)
```

$$cout<<\overbrace{*iptr}^{\text{the value inside the address iptr is pointing}}$$

# Dot v/s →

Basically they are the same 

a dot operator is applied to the actual object , to get access to its members 

whereas the arrow is applied to a pointer to that object , to reference the object's members 

Explained in depth over [here](https://www.tutorialspoint.com/cplusplus/cpp_member_operators.htm) 

# Use pointer for Array initialisation ?