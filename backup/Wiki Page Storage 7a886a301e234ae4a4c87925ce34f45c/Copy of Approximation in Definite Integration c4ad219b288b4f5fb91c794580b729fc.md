# Copy of Approximation  in Definite Integration

Column: Oct 9, 2020 9:20 PM
Last edited by: Soutrik das
Parent: Integration%201312c408a8a94e6ab99b42c3b72c371c.md
Tags: maths

[Concepts](Copy%20of%20Approximation%20in%20Definite%20Integration%20c4ad219b288b4f5fb91c794580b729fc/Concepts%20215858433f8b4ac5be6db614adc1d1c0.csv)

# Here is a list of Formulas

$$\text{if $f(x) \ge g(x)$ then}\quad \int_a^bf(x)dx \ge \int_a^bg(x)dx $$

$\text{if $f_1(x),f(x),f_2(x)$ are continuous functions in [a,b] such that $f_1(x) \le f(x) \le f_2(x) \forall x \in[a,b]$ }$then 

$$\int_a^bf_1(x)dx \le \int_a^bf(x)dx \le\int_a^bf_2(x)dx$$

---

# Examples

1] The value of $\int_0^1e^{x^2} dx$ is less than or greater than what ?

We know that 

$$e^0 <e^{x^2} <e^1 \quad  \forall x\in (0,1)$$

$$\int_0^1e^0 dx <\int_0^1e^{x^2}dx <\int_0^1e^1 dx\quad  \forall x\in (0,1)$$

$$1<\int_0^1e^{x^2}dx <e\quad  \forall x\in (0,1)$$

Hence the given integral is greater than 1 and les than $e$ 

2]  Which one of the following is correct?

(a) $\int_{0}^{1} \frac{d x}{\sqrt{4-x^{2}-x^{3}}} \leq \frac{\pi}{4 \sqrt{2}}$
(b) $\int_{0}^{1} \frac{d x}{\sqrt{4-x^{2}-x^{3}}}<\frac{\pi}{4 \sqrt{2}}$
(c) $\int_{0}^{1} \frac{d x}{\sqrt{4-x^{2}-x^{3}}}=0$
(d) None of the above

![Copy%20of%20Approximation%20in%20Definite%20Integration%20c4ad219b288b4f5fb91c794580b729fc/Untitled.png](Copy%20of%20Approximation%20in%20Definite%20Integration%20c4ad219b288b4f5fb91c794580b729fc/Untitled.png)

Sol. (a) $\because 0 \leq x \leq 1 \Rightarrow 0 \leq x^{3} \leq x^{2} \leq 1$
$\Rightarrow \quad-x^{2} \leq-x^{3} \leq 0$
$\Rightarrow \quad 4-x^{2}-x^{2} \leq 4-x^{2}-x^{3} \leq 4-x^{2}$
$\Rightarrow \quad \frac{1}{\sqrt{4-x^{2}}} \leq \frac{1}{\sqrt{4-x^{2}-x^{3}}} \leq \frac{1}{\sqrt{4-2 x^{2}}}$
$\therefore \int_{0}^{1} \frac{d x}{\sqrt{4-x^{2}}} \leq \int_{0}^{1} \frac{d x}{\sqrt{4-x^{2}-x^{3}}} \leq \int_{0}^{1} \frac{d x}{\sqrt{4-2 x^{2}}}$
$\Rightarrow \quad \frac{\pi}{6} \leq \int_{0}^{1} \frac{d x}{\sqrt{4-x^{2}-x^{3}}} \leq \frac{\pi}{4 \sqrt{2}}$

---

Example 55
If $\quad I_{1}=\int_{0}^{\pi / 2} \cos (\sin x) d x$
$$I_{2}=\int_{0}^{\pi / 2} \sin (\cos x) d x$$ and $I_{3}=\int_{0}^{\pi / 2} \cos x d x,$ then
(a) $I_{1}>I_{3}>I_{2}$
(b) $I_{3}>I_{1}>I_{2}$
$(c) I_{1}>I_{2}>I_{3}$
(d) $I_{3}>I_{2}>I_{1}$

![https://cdn.mathpix.com/snip/images/6sWvwjS5ErAfVVHexdhrYvPRmTc2pcB45v4Z_3t2z8s.original.fullsize.png](https://cdn.mathpix.com/snip/images/6sWvwjS5ErAfVVHexdhrYvPRmTc2pcB45v4Z_3t2z8s.original.fullsize.png)

---