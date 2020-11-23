# Numerical Analysis

Child: Gaussian%20Elimination%20db9a562b83654e55977775ee38580604.md, LU%20Decomposition%206d396b33d0354d1ea61513c005a86c73.md, Gauss-Jordan%20Elimination%209b380ad490914edd8970121fa886b69a.md, Linear%20Algebra%2065ba3d6a197e4a3185978c1dcf3845be.md
Column: Sep 30, 2020 11:59 AM
Last edited by: Soutrik das
Parent: Deep%20Learning%2075523c3ebbed4978aa999d16c0c00da0.md
Tags: aiml, data science, maths

> Numerical analysis is the study of algorithms that use numerical approximation (as opposed to symbolic manipulations) for the problems of mathematical analysis (as distinguished from discrete mathematics) -WIKIPedia

I am using the following book :

[Numerical Methods in Engineering With Python by Jaan Kiusalaas (z-lib.org).pdf](Numerical%20Analysis%20d3653cd8f5d34935bd07cd197e0d9a8e/Numerical_Methods_in_Engineering_With_Python_by_Jaan_Kiusalaas_(z-lib.org).pdf)

# System of Linear Algebra Equations

---

The question remains 

> **Solve the simultaneous equations Ax = b**

But as the matrix gets larger , the run time also gets larger 

> It usually possible to reduce the storage requirements and the run time by exploiting special properties of the coefficient matrix, such as sparseness (most elements of a sparse matrix are zero)

## Uniqueness of a solution

---

If the coefficient matrix is non singular , then there will be a unique solution $|A| \ne 0$

### Ill-Conditioning

---

We say a matrix is ill conditioned if its determinant is very close to zero . But how close . Well we actually compare it with ***norm*** of the matrix, which can have many definitions ( they are not same ) 

$$|A|<<\overbrace{||A||}^{\text{norm of the matrix }}$$

Different definitions of norms are the following 

$$||A||=\sqrt{\sum_{i=1}^n\sum_{j=1}^nA^2_{ij}}$$

$$||A||=\max_{1 \le i \le n}\sum_{j=1}^n|A_{ij}|$$

The formal measure of conditioning is the *matrix conditioning number* defined as 

$$\text{cond}(A)=||A||\phantom{a} ||A^{-1}||$$

If this number is close to unity, the matrix is well-conditioned. The condition number increases with the degree of ill-conditioning, reaching infinity for a singular matrix

So why does it matter ? 

It matters because when a matrix is ill conditioned , small changes in the coefficient matrix causes large changes in the solutions 

$$2x+y=3 \\
2x+1.001y=0 \\
\text{Solutions are}
\\
x=1501.5 \phantom{aa} y=-3000$$

$$2x+y=3 \\
2x+1.002y=0 \\
\text{Solutions are}
\\
x=751.5 \phantom{aa} y=-1500$$

Just a small change in the coefficient of $y$ causes such a massive change in the solutions , why ? $|A|=0.002$ is much smaller than the coefficients ( thats the informal way of measuring ill conditioned-ness) 

> Numerical solutions of ill-conditioned equations are not to be trusted. The reason is that the inevitable roundoff errors during the solution process are equivalent to introducing small changes into the coefficient matrix. This in turn introduces large errors into the solution, the magnitude of which depends on the severity of ill-conditioning

## Methods of Solution

---

There are two classes of methods for solving systems of linear, algebraic equations:

- direct  methods - they convert the original equations into *equivalent equation* that have the same solution but can be solved more easily . They use *elementary transformations* that we learned in JEE syllabus
- iterative methods - They start with a guess of the solution ***x***, and then they repeatedly refine the solution until a certain convergence  criterion is reached.

The following table has all the Direct  and Iterative methods ( I will ad them with time ) 

[Wiki Page Storage](Numerical%20Analysis%20d3653cd8f5d34935bd07cd197e0d9a8e/Wiki%20Page%20Storage%20d58bdab6014640c493b3f0b0586e30b8.csv)

![Numerical%20Analysis%20d3653cd8f5d34935bd07cd197e0d9a8e/Untitled.png](Numerical%20Analysis%20d3653cd8f5d34935bd07cd197e0d9a8e/Untitled.png)

Where 

- $U$ is upper triangular matrix

$$\mathbf{U}=\left[\begin{array}{ccc}U_{11} & U_{12} & U_{13} \\0 & U_{22} & U_{23} \\0 & 0 & U_{33}\end{array}\right]$$

- $LU$ ~~is lower triangular matrix~~

    $LU$ is something else . But the $L$ in the $LU$ stands for lower triangular matrix which is shown below 

    $$\mathbf{L}=\left[\begin{array}{ccc}L_{11} & 0 & 0 \\L_{21} & L_{22} &0 \\L_{31} & L_{32} & L_{33}\end{array}\right]$$

- $I$ is identity matrix

Triangular matrices play a very important role in solving , because they make solving very very easy 

Consider they following set of equations 

$$L_{11}x_1=c_1 \\
L_{21}x_1+L_{22}x_2=c_2\\
L_{31}x_1+L_{32}x_2+L_{33}x_3=c_3$$

At every point you solve for only one unknown , because you have already solved for the other before hand 

$$
\begin{array}{l}
x_1=c_1/L_{11}\\
x_{2}=\left(c_{2}-L_{21} x_{1}\right) / L_{22} \\
x_{3}=\left(c_{3}-L_{31} x_{1}-L_{32} x_{2}\right) / L_{33}
\end{array}$$

This procedure is known as *forward substitution.* Similarly in Gaussian Elimination we can easily solve for the unknowns using *backward substitution*.