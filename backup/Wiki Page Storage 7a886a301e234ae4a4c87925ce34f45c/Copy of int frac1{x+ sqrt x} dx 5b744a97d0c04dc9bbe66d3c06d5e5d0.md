# Copy of \int \frac1{x+\sqrt x} \ dx

Column: Aug 26, 2020 12:53 PM
Last edited by: Soutrik das
Parent: 100%20Integrals%20BlackpenRedPen%20e8f460e07c904de0b02abe1066b64353.md
Tags: maths, question

$$\int \frac1{x+\sqrt x} \ dx$$

$t=\sqrt x$  $dt=\frac{dx}{2\sqrt x}$

$$\int \frac{2t}{t^2+t} \ dx$$

$$\int \frac{2t-1+1}{t^2+t} \ dx$$

$$\int \frac{2t+1}{t^2+t}+\frac{-1}{{t^2+t}} \ dx$$

For the left term we can just use substitution and get 
$\Large \log{t^2+t}$ but what about the other one ?

We probably have to do this 

$$\frac{1}{t^2+t}$$

$$\frac{1}{t^2+2\cdot \frac 12 \cdot t+\frac 14 -\frac 14}$$

$$\frac{1}{(t+\frac 12)^2-(\frac 12)^2}$$

something like $\frac1{x^2-a^2}$ $\to$ $\frac 1{2a} \log|\frac{x-a}{x+a}|$

$$ \log|\frac{t}{t+1}|$$

Final Answer 

$$\log{t^2+t} - \log|\frac{t}{t+1}|$$