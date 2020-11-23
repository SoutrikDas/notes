# Copy of The greatest term in the expansion of (1+x)^{10}
when x=\frac{2}{3} is

Column: Aug 26, 2020 12:55 PM
Last edited by: Soutrik das
Tags: maths, question

my approach was 

$$ \begin{aligned}
(1+x)^{10} &= t_0+t_1+t_2+\cdots t_{10}
\end{aligned}$$

now for $t_r$ to be the highest we have to have the following 

$$\newcommand{\a}[1]{^{10}C_{#1}\frac{2^{#1}}{3^{#1}}}
\a{r-1} \le \a{r} \ge \a{r+1}$$

![Copy%20of%20The%20greatest%20term%20in%20the%20expansion%20of%20(1+x%201977a4d7bc6c471a9a22c812538bd55a/Untitled.png](Copy%20of%20The%20greatest%20term%20in%20the%20expansion%20of%20(1+x%201977a4d7bc6c471a9a22c812538bd55a/Untitled.png)

But obviously solution of r will be all those numbers after maximum term , because they are also greater than the next term .so from all the solutions of r , we only want the smallest term 

$$\newcommand{\a}[1]{^{10}C_{#1}\frac{2^{#1}}{3^{#1}}} \begin{aligned}

&=\a{r} \ge \a{r+1} \\&=\frac{\cancel{10!}(r+1)!(10-r-1)!}{r!(10-r)!\cancel{(10!)}}\ge \frac{2}{3}
\\&=\frac{(r+1)}{(10-r)} \ge \frac{2}{3} \\
&=3r+3 \ge 20-2r \\
&=5r \ge 17
\\ &r=\{ 4,5,6,7,8,9,10\} \\
& \text{term number}=\{ 5,6,7,8,9,10,11\}
\end{aligned}$$

hence maximum term is 5th term