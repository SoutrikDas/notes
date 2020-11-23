# Matrix Determinant (Cookbook)

Column: Oct 2, 2020 3:22 PM
Last edited by: Soutrik das
Parent: Linear%20Algebra%2065ba3d6a197e4a3185978c1dcf3845be.md
Tags: chapter, maths

Notes primarily from [matrixcookbook.com](http://matrixcookbook.com) 

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

# Basics

---

$$\begin{aligned}(\mathbf{A B})^{-1} &=\mathbf{B}^{-1} \mathbf{A}^{-1} \\(\mathbf{A B C} \ldots)^{-1} &=\ldots \mathbf{C}^{-1} \mathbf{B}^{-1} \mathbf{A}^{-1} \\\left(\mathbf{A}^{T}\right)^{-1} &=\left(\mathbf{A}^{-1}\right)^{T} \\(\mathbf{A}+\mathbf{B})^{T} &=\mathbf{A}^{T}+\mathbf{B}^{T} \\(\mathbf{A B})^{T} &=\mathbf{B}^{T} \mathbf{A}^{T} \\(\mathbf{A} \mathbf{B C} \ldots)^{T} &=\ldots \mathbf{C}^{T} \mathbf{B}^{T} \mathbf{A}^{T} \\\left(\mathbf{A}^{H}\right)^{-1} &=\left(\mathbf{A}^{-1}\right)^{H} \\(\mathbf{A}+\mathbf{B})^{H} &=\mathbf{A}^{H}+\mathbf{B}^{H} \\(\mathbf{A} \mathbf{B})^{H} &=\mathbf{B}^{H} \mathbf{A}^{H} \\(\mathbf{A} \mathbf{B} \mathbf{C} \ldots)^{H} &=\ldots \mathbf{C}^{H} \mathbf{B}^{H} \mathbf{A}^{H}\end{aligned}$$

Here the only thing New is the Hermitian Transpose .

## What is Hermitian Transpose ?

---

A hermitian transpose has value only for matrix containing complex numbers 

For a real numbered Matrix , its just Transpose 

$$A^T=A^H \tag{if A is real}$$

But for a Complex matrix , the definition follows 

> Transpose of a Matrix followed by conjugates of each entries of the matrix is called a Hermitian Transpose

Lets take an example 

$$A=\left[ 
\begin{matrix}
1+i &2-3i \\
-i&2\\
\end{matrix}
\right]$$

Then 

$$A^T=\left[ 
\begin{matrix}
1+i &-i \\
2-3i&2\\
\end{matrix}
\right]$$

$$A^H=\left[ 
\begin{matrix}
1-i &+i \\
2+3i&2\\
\end{matrix}
\right]$$

## Trace

---

$$\begin{aligned}\operatorname{Tr}(\mathbf{A}) &=\sum_{i} A_{i i} \\\operatorname{Tr}(\mathbf{A}) &=\sum_{i} \lambda_{i}, \quad \lambda_{i}=\operatorname{eig}(\mathbf{A}) \\\operatorname{Tr}(\mathbf{A}) &=\operatorname{Tr}\left(\mathbf{A}^{T}\right) \\\operatorname{Tr}(\mathbf{A} \mathbf{B}) &=\operatorname{Tr}(\mathbf{B} \mathbf{A}) \\\operatorname{Tr}(\mathbf{A}+\mathbf{B}) &=\operatorname{Tr}(\mathbf{A})+\operatorname{Tr}(\mathbf{B}) \\\operatorname{Tr}(\mathbf{A} \mathbf{B} \mathbf{C}) &=\operatorname{Tr}(\mathbf{B} \mathbf{C A})=\operatorname{Tr}(\mathbf{C A B}) \\\mathbf{a}^{T} \mathbf{a} &=\operatorname{Tr}\left(\mathbf{a} \mathbf{a}^{T}\right)\end{aligned}$$

![Matrix%20Determinant%20(Cookbook)%20064e452271144bcd9eeb92b4668c0e2c/TraceofMatrix2.gif](Matrix%20Determinant%20(Cookbook)%20064e452271144bcd9eeb92b4668c0e2c/TraceofMatrix2.gif)