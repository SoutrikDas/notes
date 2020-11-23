# Copy of \int x \sin^2 x \quad dx

Column: Aug 26, 2020 12:53 PM
Last edited by: Soutrik das
Parent: 100%20Integrals%20BlackpenRedPen%20e8f460e07c904de0b02abe1066b64353.md
Tags: maths, question

$$\begin {matrix}
&D&I \\
&x &\sin^2x  \\
-&1 &\frac12\cdot (x-\frac 12 \sin2x)  \\
+& 0& \frac12\cdot (\frac {x^2} 2+\frac 14 \cos2x) 
\end{matrix}$$

Too big , To make this slightly smaller to compute and not make errors here is a shortcut 

$$\begin{aligned}
\int x\sin^2x &=\ \int \frac12 \left[x-x\cos(2x) \right]\\
&= \frac {x^2}{4}+?
\left[
\begin{matrix}
&D&I \\
&-x&\cos(2x) \\
\hdashline \\
-&-1&\cfrac{\sin(2x)}{2} \\
+&0&\cfrac{-\cos(2x)}{4}\\
\end{matrix}
\right]
\\
&=\frac{x^2}4-\cfrac{x\sin(2x)}{2}-\cfrac{\cos(2x)}{4}
\end{aligned}$$