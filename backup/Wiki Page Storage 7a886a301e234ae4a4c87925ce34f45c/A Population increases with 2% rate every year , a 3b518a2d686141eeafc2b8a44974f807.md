# A Population increases with 2% rate every year , at the end of n years the final population was 40% more than the initial population , what is the value of n?

Column: Sep 11, 2020 6:00 PM
Last edited by: Soutrik das

- Failed try

    Let the initial population be $P$ 

According to the binomial theorem

$$(1+x)^n=1+^nC_1x+^nC_2x^2+^nC_3x^3+\cdots $$

Where $^nC_r$ is $\boxed {\cfrac{n!}{(n-r)!\times r!}}$  and the exclamation marks means Factorial 

 $\boxed{n! = n\times (n-1) \times (n-2)\times \cdots \times 1}$

Taking 

$$(1+0.02)^n=1+n(0.02)+\frac{(n)(n-1)}{2}\times (0.02)^2+..$$

For approximation we will only take the first term 

$$(1+0.02)^n=1+n(0.02)$$

we know the result should come as $1.4$

$$1.4=1+n(0.02)$$

$$0.4=n\times 0.02$$

$$n=\frac{0.4}{0.02}$$

$$n=\frac{40}{2}$$

approximately its coming 20 , but n should be lower 

---

According to the binomial theorem

$$(1+x)^n=1+^nC_1x+^nC_2x^2+^nC_3x^3+\cdots $$

Where $^nC_r$ is $\boxed {\cfrac{n!}{(n-r)!\times r!}}$  and the exclamation marks means Factorial 

 $\boxed{n! = n\times (n-1) \times (n-2)\times \cdots \times 1}$

Taking 

$$(1+0.02)^n=1+n(0.02)+\frac{(n)(n-1)}{2}\times (0.02)^2+..$$

For approximation we will only take the first term 

$$(1+0.02)^n=1+n(0.02)$$

we know the result should come as $1.4$

$$1.4=1+n(0.02)$$

$$0.4=n\times 0.02$$

$$n=\frac{0.4}{0.02}$$

$$n=\frac{40}{2}$$

approximately its coming 20 , but n should be lower 

- Failed try

    $$(1.4)\times P=P\left[1+(0.02)^1+(0.02)^2+(0.02)^3+\cdots (0.02)^n \right] $$

    $$(1.4)\times \cancel P=\cancel P\left[1+(0.02)^1+(0.02)^2+(0.02)^3+\cdots (0.02)^n \right] $$

    $$(1.4)=\left[1+(0.02)^1+(0.02)^2+(0.02)^3+\cdots (0.02)^n \right]  \tag 2$$

    Now lets try to find RHS of this equation 

    We know for a GP that 

    $$a \left( \frac{1-r^{n+1}}{1-r} \right)=\overbrace{a+ar+ar^2+ar^3+\cdots ar^n}^{\text{there are n+1 terms}}$$

    Using this in equation $2$ we get

    $$1.4=1\left(\frac{ 1-(0.02)^{n+1}}{1-0.02} \right)$$

    $$1.4=\left(\frac{ 1-(0.02)^{n+1}}{0.98} \right)$$

    $$1.4 \times 0.98=1-(0.02)^{n+1}$$

    $$(0.02)^{n+1}=1-1.4 \times 0.98$$

    $$(0.02)^{n+1}=1-1.372$$

    # Retry

    Initially there was $P$ people 

    after the end of first year there was $(1.02)\times P$ , and the addition was $(0.02)\times P$- 

    After the second year there was $(1.02)^2\times P$ and the addition was $(1.02)^2P-(1.02)P$

    After third year there was $(1.02)^3P$ and the addition was $(1.02)^3P-(1.02)^2P$

     

    $$\begin{matrix}
    & P+&\\
    &(1.02)P& -P \\
    &(1.02)^2P&-(1.02)P \\
    &\cdots& \\
    &(1.02)^nP &-(1.02)^{n-1}P
    \end{matrix}$$

    Sum is coming to be $(1.02)$ which is obvious , but how do i get that power ?

    $$1.4=(1.02)^n$$