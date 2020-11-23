# Linear Algebra

Child: Matrix%20Determinant%20(Cookbook)%20064e452271144bcd9eeb92b4668c0e2c.md
Column: Sep 30, 2020 1:10 PM
Last edited by: Soutrik das
Parent: Numerical%20Analysis%20d3653cd8f5d34935bd07cd197e0d9a8e.md
Tags: chapter

# Some Important Terms

---

## Matrices

---

### Special Matrices

---

- Row and Column Matrices

$$\left[\begin{array}{l}
2 \\
3 \\
5
\end{array}\right] \text{ and }
\left[\begin{array}{l}
2 &
3 &
5
\end{array}\right]$$

- Square matrix

$$M_{1}=\left[\begin{array}{lll}a_{1} & b_{1} & c_{1} \\a_{2} & b_{2} & c_{2} \\a_{3} & b_{3} & c_{3}\end{array}\right]$$

- Diagonal Matrix ( the matrix whose all diagonal elements are same is called Scalar Matrix )

$$\left[\begin{array}{rrr}3 & 0 & 0 \\0 & -2 & 0 \\0 & 0 & 6\end{array}\right] \text { and }\left[\begin{array}{lll}3 & 0 & 0 \\0 & 3 & 0 \\0 & 0 & 3\end{array}\right]$$

- Symmetric and Skew Symmetric

$$\left[\begin{array}{lll}a & h & g \\h & b & f \\g & f & c\end{array}\right] \text { and }\left[\begin{array}{ccc}0 & h & -g \\-h & 0 & f \\g & -f & 0\end{array}\right] \text { respectively. }$$

- Triangular Matrix ( Lower and Upper respectively )

$$\left[\begin{array}{lll}a & h & g \\0 & b & f \\0 & 0 & c\end{array}\right] \quad \text { and } \quad\left[\begin{array}{rrr}1 & 0 & 0 \\2 & 3 & 0 \\1 & -5 & 4\end{array}\right]$$

## Determinants

---

### Properties of Determinants

---

- The Determinant remains same even if the rows and columns are switched

$$|A |=|A^{T}|$$

- If Two parallel lines in a determinant is interchanged , the magnitude of determinant remains same but the sign alternates.
- The Determinant is $0$ if two parallel lines ( rows or columns ) are identical
- If a line in determinant is multiplied by a scalar , then the whole determinant is multiplied by that scalar

$$\left|\begin{array}{lll}a_{1} & p b_{1} & c_{1} \\a_{2} & p b_{2} & c_{2} \\a_{3} & p b_{3} & c_{3}\end{array}\right|=p\left|\begin{array}{lll}a_{1} & b_{1} & c_{1} \\a_{2} & b_{2} & c_{2} \\a_{3} & b_{3} & c_{3}\end{array}\right|$$

- We can break a determinant into two or more

$$\Delta=\left|\begin{array}{lll}a_{1} & b_{1} & c_{1}+d_{1}-e_{1} \\a_{2} & b_{2} & c_{2}+d_{2}-e_{2} \\a_{3} & b_{3} & c_{3}+d_{3}-e_{3}\end{array}\right|$$

We can write the above like below

$$\Delta=\begin{aligned}\left|\begin{array}{lll}a_{1} & b_{1} & c_{1} \\a_{2} & b_{2} & c_{2} \\a_{3} & b_{3} & c_{3}\end{array}\right|+\left|\begin{array}{lll}a_{1} & b_{1} & d_{1} \\a_{2} & b_{2} & d_{2} \\a_{3} & b_{3} & d_{3}\end{array}\right|-\left|\begin{array}{lll}a_{1} & b_{1} & e_{1} \\a_{2} & b_{2} & e_{2} \\a_{3} & b_{3} & e_{3}\end{array}\right|\end{aligned}$$

- Proof

    $$\begin{aligned}\Delta &=\left(c_{1}+d_{1}-e_{1}\right)\left(a_{2} b_{3}-a_{3} b_{2}\right)-\left(c_{2}+d_{2}-e_{2}\right)\left(a_{1} b_{3}-a_{3} b_{1}\right)+\left(c_{3}+d_{3}-e_{3}\right)\left(a_{1} b_{2}-a_{2} b_{1}\right) \\&=\left[c_{1}\left(a_{2} b_{3}-a_{3} b_{2}\right)-c_{2}\left(a_{1} b_{3}-a_{3} b_{1}\right)+c_{3}\left(a_{1} b_{2}-a_{2} b_{1}\right)\right]+\left[d_{1}\left(a_{2} b_{3}-a_{3} b_{2}\right)-d_{2}\left(a_{1} b_{3}-a_{3} b_{1}\right)\right.\\&\left.=d_{3}\left(a_{1} b_{2}-a_{2} b_{1}\right)\right]-\left[e_{1}\left(a_{2} b_{3}-a_{3} b_{2}\right)-e_{2}\left(a_{1} b_{3}-a_{3} b_{1}\right)+e_{3}\left(a_{1} b_{2}-a_{2} b_{1}\right)\right] \\&=\left|\begin{array}{lll}a_{1} & b_{1} & c_{1} \\a_{2} & b_{2} & c_{2} \\a_{3} & b_{3} & c_{3}\end{array}\right|+\left|\begin{array}{lll}a_{1} & b_{1} & d_{1} \\a_{2} & b_{2} & d_{2} \\a_{3} & b_{3} & d_{3}\end{array}\right|-\left|\begin{array}{lll}a_{1} & b_{1} & e_{1} \\a_{2} & b_{2} & e_{2} \\a_{3} & b_{3} & e_{3}\end{array}\right|\end{aligned}$$

- If each element of a line be added the *equi-multiples* of corresponding elements of parallel lines then determinant remains same

$$\begin{aligned}\Delta &=\left|\begin{array}{lll}a_{1} & b_{1} & c_{1} \\a_{2} & b_{2} & c_{2} \\a_{3} & b_{3} & c_{3}\end{array}\right| \\\Delta^{\prime}&=\left|\begin{array}{lll}a_{1} & +p b_{1}-q c_{1} & b_{1} & c_{1} \\a_{2} & +p b_{2}-q c_{2} & b_{2} & c_{2} \\a_{3} & +p b_{3}-q c_{3} & b_{3} & c_{3}\end{array}\right| \\ \Delta^{\prime}&=\left|\begin{array}{lll}a_{1} & b_{1} & c_{1} \\a_{2} & b_{2} & c_{2} \\a_{3} & b_{3} & c_{3}\end{array}\right|+\left|\begin{array}{lll}p b_{1} & b_{1} & c_{1} \\p b_{2} & b_{2} & c_{2} \\p b_{3} & b_{3} & c_{3}\end{array}\right|+\left|\begin{array}{llll}-q c_{1} & b_{1} & c_{1} \\-q c_{2} & b_{2} & c_{2} \\-q c_{3} & b_{3} & c_{3}\end{array}\right| \\ \Delta^{\prime}&=\Delta+0+0=\Delta\end{aligned}$$

- Determinant of Matrix Product

$$\det(A_1A_2A_3\cdots)=\det(A_1)\det(A_2)\cdots $$

- Multiplication of Determinants

$$\Delta_{1}=\left|\begin{array}{lll}a_{1} & b_{1} & c_{1} \\a_{2} & b_{2} & c_{2} \\a_{3} & b_{3} & c_{3}\end{array}\right| \text { and } \Delta_{2}=\left|\begin{array}{lll}l_{1} & m_{1} & n_{1} \\l_{2} & m_{2} & n_{2} \\l_{3} & m_{3} & n_{3}\end{array}\right|$$

$$\Delta_{1} \Delta_{2}=\begin{vmatrix} a_{1} l_{1}+b_{1} m_{1}+c_{1} n_{1}, & a_{1} l_{2}+b_{1} m_{2}+c_{1} n_{2},& a_1l_3+b_1m_3+c_1n_3 \\a_{2} l_{1}+b_{2} m_{1}+c_{2} n_{1}, & a_{2} l_{2}+b_{2} m_{2}+c_{2} n_{2},& a_{2} l_{3}+b_{1} m_{3}+c_{1} n_{3} \\a_{3} h_{1}+b_{3} m_{1}+c_{3} n_{1}, & a_{3} l_{2}+b_{3} m_{2}+c_{3} n_{2},& a_{3} b_{3}+b_{3} m_{3}+c_{3} n_{3}\end{vmatrix}$$

This I believe is because of Matrix multiplication . If we take two matrix 

$$M_{1}=\left(\begin{array}{lll}a_{1} & b_{1} & c_{1} \\a_{2} & b_{2} & c_{2} \\a_{3} & b_{3} & c_{3}\end{array}\right) \text { and } M_{2}=\left(\begin{array}{lll}l_{1} & m_{1} & n_{1} \\l_{2} & m_{2} & n_{2} \\l_{3} & m_{3} & n_{3}\end{array}\right)$$

$$M_{1} M_{2}^T=\left(\begin{matrix} a_{1} l_{1}+b_{1} m_{1}+c_{1} n_{1}, & a_{1} l_{2}+b_{1} m_{2}+c_{1} n_{2},& a_1l_3+b_1m_3+c_1n_3 \\a_{2} l_{1}+b_{2} m_{1}+c_{2} n_{1}, & a_{2} l_{2}+b_{2} m_{2}+c_{2} n_{2},& a_{2} l_{3}+b_{1} m_{3}+c_{1} n_{3} \\a_{3} h_{1}+b_{3} m_{1}+c_{3} n_{1}, & a_{3} l_{2}+b_{3} m_{2}+c_{3} n_{2},& a_{3} b_{3}+b_{3} m_{3}+c_{3} n_{3}\end{matrix}\right)$$

Then Taking Determinant on both side and using determinant product 

$$|M_1M_2^T|=|M_1|\times|M_2^T|=|M_1|\times|M_2|=\Delta_1\Delta_2$$

$$\Delta_{1} \Delta_{2}=\begin{vmatrix} a_{1} l_{1}+b_{1} m_{1}+c_{1} n_{1}, & a_{1} l_{2}+b_{1} m_{2}+c_{1} n_{2},& a_1l_3+b_1m_3+c_1n_3 \\a_{2} l_{1}+b_{2} m_{1}+c_{2} n_{1}, & a_{2} l_{2}+b_{2} m_{2}+c_{2} n_{2},& a_{2} l_{3}+b_{1} m_{3}+c_{1} n_{3} \\a_{3} h_{1}+b_{3} m_{1}+c_{3} n_{1}, & a_{3} l_{2}+b_{3} m_{2}+c_{3} n_{2},& a_{3} b_{3}+b_{3} m_{3}+c_{3} n_{3}\end{vmatrix}$$

## Cofactor

---

The cofactor of any element in a determinant is obtained by deleting the row and column in which that element is sitting in *with proper sign.* the sign of the $a_{ij}$ element is given by $-1^{(i+j)}$

$$\Delta =\begin{vmatrix}
a_1 &b_1&c_1 \\
a_2 & b_2 & c_2 \\
a_3 & b_3 & c_3 
\end{vmatrix}$$

Then the cofactor of $a_2$ will be 

$$A_2=-1^{(2+1)}\begin{vmatrix} 
b_1 & c_1 \\
b_3 & c_3
\end{vmatrix}$$

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

[Wiki Page Storage](Linear%20Algebra%2065ba3d6a197e4a3185978c1dcf3845be/Wiki%20Page%20Storage%2083b6cd1570c94b18a7f90826d114d418.csv)

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