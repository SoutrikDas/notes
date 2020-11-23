# Complex Numbers

Child: Coordinate%20Geometry%206c24e8c54553431cbdb416a2da860633.md, Let%20s,t,r%20be%20non-zero%20complex%20numbers%20and%20L%20be%20the%204f76b81aceb34603a2a2f03500d69d5e.md
Column: Oct 9, 2020 9:44 PM
Last edited by: Soutrik das
Tags: chapter, maths

The Real Bulk of Complex Numbers Comes From The properties of **Conjugates, Modulus , Arguments** of a Complex Number, because they are used everywhere

- Algebraic Operations

    # Algebraic Operations

    ---

    ## Addition $(z_1+z_2)$

    ---

    $$(a+ib) +(c+id)=(a+c)+i(b+d)$$

    ## Substraction $(z_1-z_2)$

    ---

    $$(a+ib) -(c+id)=(a-c)+i(b-d)$$

    ## Multiplication $(z_1 \times z_2)$

    ---

    $$\frac{a+i b}{c+i d}=\frac{(a+i b)}{(c+i d)} \frac{(c-i d)}{(c-i d)}$$

- Finding the Square Root of a Complex Number

    # Finding the Square Root of a Complex Number

    ---

    > To be honest no one would need to find the square root of a complex number.

    ![Complex%20Numbers%2058520c2afe2a4be2a00a946e780d9af9/Untitled.png](Complex%20Numbers%2058520c2afe2a4be2a00a946e780d9af9/Untitled.png)

    Let $a+i b$ be a complex number such that $\sqrt{a+i b}=x+i y$, where $x$ and $y$ are real numbers.

    $$\begin{array}{ll}\sqrt{a+i b} & =x+i y \\\Rightarrow \quad(a+i b) & =(x+i y)^{2} \\\Rightarrow a+i b & =\left(x^{2}-y^{2}\right)+2 i x y\end{array}$$

    Then,On equating real and imaginary parts, we get

    $$x^{2}-y^{2}=a \\
    2 x y=b$$

    Now,

    $$\begin{aligned}&\left(x^{2}+y^{2}\right)^{2}=\left(x^{2}-y^{2}\right)^{2}+4 x^{2} y^{2} \\\Rightarrow &\left(x^{2}+y^{2}\right)^{2}=a^{2}+b^{2} \\\Rightarrow &\left(x^{2}+y^{2}\right)=\sqrt{a^{2}+b^{2}} \quad\left[\because x^{2}+y^{2} \geq 0\right]\end{aligned}$$

    $$$$

    Solving equations (i) and (ii), we get $x^{2}=\left(\frac{1}{2}\right)\left[\sqrt{a^{2}+b^{2}}+a\right] \text { and } y^{2}=\left(\frac{1}{2}\right)\left[\sqrt{a^{2}+b^{2}}-a\right]$ $\Rightarrow x=\pm \sqrt{\left(\frac{1}{2}\right)\left[\sqrt{a^{2}+b^{2}}+a\right]}$ and

     $y=\pm \sqrt{\left(\frac{1}{2}\right)\left[\sqrt{a^{2}+b^{2}}-a\right]}$ If $b$ is positive, then by the relation $2 x y=b, x$ and $y$ are of the same sign. Hence, $\sqrt{a+i b}=\pm\left\{\sqrt{\frac{1}{2}\left[\sqrt{a^{2}+b^{2}}+a\right]}+i \sqrt{\frac{1}{2}\left[\sqrt{a^{2}+b^{2}}-a\right]}\right\}$ If $b$ is negative, then by the relation $2 x y=b, x$ and $y$ are of different signs. Hence , $\sqrt{a+i b}=\pm\left\{\sqrt{\frac{1}{2}\left[\sqrt{a^{2}+b^{2}}+a\right]}-i \sqrt{\frac{1}{2}\left[\sqrt{a^{2}+b^{2}}-a\right]}\right\}$

- Properties of Conjugates

    # Properties of Conjugates

    ---

    1. $\overline{z_1+z_2}=\bar z_1+ \bar z_2$
    2. $\overline{z_1-z_2}=\bar z_1- \bar z_2$
    3. $\overline{z_1 \times z_2}=\bar z_1 \times \bar z_2$
    4. $\overline{\left( \cfrac{z_1}{z_2}\right)}=\left( \cfrac{\bar z_1}{\bar z_2}\right) , (z_2 \ne0)$
    5. $z+\overline z=2x=2Re(z)$
    6. $z_1 \overline z_2+\overline z_1 z_2 =2Re(z_1 \overline z_2)=2Re(\overline z_1 z_2)$
    7. If $z=f(z_1)$, then $\overline z=f( \overline z_1)$
    8. $( \overline z)^n= \overline {(z^n)}$
- Properties of Modulus of Complex Numbers

    # Properties of Modulus of Complex Numbers

    ---

    1. $Re(z) \le|z|$ and $Im(z) \le|z|$
    2. $z\times \overline z= |z|^2$
    3. $|z_1 z_2 z_3|=|z_1| |z_2||z_3|$
    4. ${\left| \cfrac{z_1}{z_2}\right|}=\cfrac{| z_1|}{| z_2|} , (z_2 \ne0)$
    5. $|z_1\pm z_2| \le |z_1|+|z_2|$ This is part of the triange inequality
    6. $|z_1 \pm z_2| \ge ||z_1|-|z_2||$
    7. $|z|^n=|z^n|$
    8. Triangle Ineguality
    9. $|z_1\pm z_2|^2=(z_1 \pm z_2)(\overline z_1 \pm \overline z_2)$ , From [this property](https://www.notion.so/Complex-Numbers-58520c2afe2a4be2a00a946e780d9af9#6bcf82ce87b94406af1b6b95f19a7c8f)
    $=|z_1|^2+|z_2|^2 \pm (z_1 \overline z_2+\overline z_1 z_2)$
    $=|z_1|^2+|z_2|^2 \pm 2Re(z_1 \overline z_2)$  From [this property](https://www.notion.so/Complex-Numbers-58520c2afe2a4be2a00a946e780d9af9#b4a8aee117e446f5b3cc44ff343348d1)
    10. If $|z_1+z_2|^2=|z_1|^2+|z_2|^2 \iff \frac {z_1}{z_2}$ is purely imaginary
    11. $|z_1+z_2|^2+|z_1-z_2|^2=2( |z_1|^2+|z_2|^2 )$
- Arguements of Complex Numbers

    # Arguements of Complex Numbers

    ---

    - What is arguement ?

        The angle of the complex Number made with the +ve x axis

    - What is a principle arguement ?

        That angle of a complex Number made with the +ve x axis , Which satisfies $\boxed{-\pi < \theta \le \pi}$

    1. $\arg \left(z_{1} z_{2}\right)=\arg \left(z_{1}\right)+\arg \left(z_{2}\right)+2 k \pi$   $(k$= $0$ or $1$ or $-1)$ 
    2. $\arg \left(\frac{z_{1}}{z_{2}}\right)=\arg \left(z_{1}\right)-\arg \left(z_{2}\right)+2 k \pi$
    3. $\arg \left(\cfrac{z}{\bar{z}}\right)=2 \arg (z)+2 k \pi$ 
    4. 

- What is De Moivre's Theorem

    # De Moivres Theorem

    ---

    The theorem states that 

    $$\left( e^{i\theta} \right)^n= e^{i (n\theta)} $$

    And why is this even useful ?

    Because we can do this 

    $$\left(\cos \theta  + i\sin \theta \right)^n = \cos n\theta + i \sin n\theta$$

- Properties of Roots of Unity
- Geometrical Applications of Complex Numbers
    - Distance formula

        Distance between two points $z_1$ and $z_2$ is $|z_1-z_2|$

    - Section Formula

        $$z=\frac{m_1z_1+m_2z_2}{m_1+m_2}$$

    - How would you write the equation of a Straight line ?

        In vectors we used to do $\vec v= \vec v_1+\lambda \vec v_2$

        So maybe we will do the same thing for complex numbers ? Because they are almost the same 

        $$z=z_1+\lambda z_2$$

- Loci
- Logarithm of Complex Numbers

# Loci

---

- What is a Loci ?

    It is the path of a point which is under geometric constraints ( some specified equations )

1. $|z -z_1|=|z-z_2|$  

    This is depicts a line that is the perpendicular bisector of the line joining $z_1$ and $z_2$ 

2. $|z-z_1|+|z-z_2|=k$

    This is as ellipse 

3. $|z-z_1|+|z-z_2|=|z_1-z_2|$
4.