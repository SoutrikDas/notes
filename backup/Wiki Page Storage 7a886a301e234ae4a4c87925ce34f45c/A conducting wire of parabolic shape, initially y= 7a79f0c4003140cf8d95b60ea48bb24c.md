# A conducting wire of parabolic shape, initially y=x^2 , is moving with velocity \vec V=V_0 \hat i in a non uniform magnetic field \vec B=B_0\left( 1+\left( \frac y L \right) ^\beta \right) \hat k. If V_0 , B_0, L and \beta are positive constants and \Delta \phi is the potential difference developed between the ends of the wire, then which statement is correct

Column: Sep 23, 2020 5:23 PM
Last edited by: Soutrik das
Parent: JEE%20ADV%202019%20paper%201%206e969e4fdf724b4eba045ad8c9ac0feb.md, EMI%20810a9cff73044ee68f1f88cb89f6f6ca.md
Tags: adv, physics, question

![A%20conducting%20wire%20of%20parabolic%20shape,%20initially%20y=%207a79f0c4003140cf8d95b60ea48bb24c/Untitled.png](A%20conducting%20wire%20of%20parabolic%20shape,%20initially%20y=%207a79f0c4003140cf8d95b60ea48bb24c/Untitled.png)

![A%20conducting%20wire%20of%20parabolic%20shape,%20initially%20y=%207a79f0c4003140cf8d95b60ea48bb24c/Untitled%201.png](A%20conducting%20wire%20of%20parabolic%20shape,%20initially%20y=%207a79f0c4003140cf8d95b60ea48bb24c/Untitled%201.png)

This is related to emotional EMF ( actually called "motional " , but our sir calls it emotional ) 

So how does that work ? We need to go to [EMI](EMI%20810a9cff73044ee68f1f88cb89f6f6ca.md) ( Specifically , go [here](EMI%20810a9cff73044ee68f1f88cb89f6f6ca.md) )

So the logic was that when moving Electrons may feel a force $F=q(\vec v \times \vec B )$ which will lead to their accumulation on one side of the wire , thus causing an EMF 

Before that lemme do some other motional emf questions  ( [Some easy EMI questions ](Some%20easy%20EMI%20questions%202397dc1e88fc4cad8627975e358224bf.md) 

But the problem here is that $(\vec v \times \vec B)$ is not constant here , its dependant on $y$ 

But still the if we break $d \vec l$ into $dy$ and $dx$ 

![A%20conducting%20wire%20of%20parabolic%20shape,%20initially%20y=%207a79f0c4003140cf8d95b60ea48bb24c/Untitled%202.png](A%20conducting%20wire%20of%20parabolic%20shape,%20initially%20y=%207a79f0c4003140cf8d95b60ea48bb24c/Untitled%202.png)

Blue is $-(\vec v \times \vec B)$ ( my intention was to draw + $(\vec v \times \vec B)$ but i did a mistake )  and red is $d \vec l$

- Even then , for that small element , $dx$ doesnt cause any change in potential

    Because Triple product of three vectors is $0$ when two of them are in the same plane ( because volume is zero ) 

    ![A%20conducting%20wire%20of%20parabolic%20shape,%20initially%20y=%207a79f0c4003140cf8d95b60ea48bb24c/Untitled%203.png](A%20conducting%20wire%20of%20parabolic%20shape,%20initially%20y=%207a79f0c4003140cf8d95b60ea48bb24c/Untitled%203.png)

So now lets integrate  ( representing potential with $\epsilon$ )

$$\epsilon =V_0B_0\int _0^L [1+\left ( \frac{y}{L}\right )^ \beta] (-\hat j)\cdot dy(\hat j)$$

$$\epsilon =-V_0B_0\int _0^L [1+\left ( \frac{y}{L}\right )^ \beta] dy$$

$$\epsilon =-V_0B_0\int _0^L [1+\frac 1{L^\beta} \left ( \frac{y}{1}\right )^ \beta] dy$$

$$\epsilon =-V_0B_0 (y+\frac{1}{L^\beta}\left ( \frac{y}{(\beta +1)}\right )^ {\beta +1}) \big |^L_0$$

$$\epsilon =V_0B_0 (y+\frac 1{L^\beta}\left ( \frac{y}{(\beta +1)}\right )^ {\beta +1}) \big |^0_L$$

$$\epsilon=0-V_0B_0(L+\frac{L}{(\beta +1)^{\beta +1}})$$

now we did get a negative potential ( because we were ging from 0 to L ) but we can understand that the Higher potential is at y=0 and lower potential is at y=L

Now putting different values of $\beta$

- $\beta=0$ then we get $|\epsilon|=2V_0B_0L$   ( Option A is correct)
- $\beta=2$ then we get $|\epsilon|=\frac{28}{27}V_0B_0L$

Since the only change has been done due to $dy$ component , hence if the length in $y$ direction remains same , then the potential will also be same . Hence option C is also correct 

And from this equation 

$$\epsilon=0-V_0B_0(L+\frac{L}{(\beta +1)^{\beta +1}})$$

We can take $L$ common , which means , the potential is indeed proportional to length along y axis , so option D is also correct