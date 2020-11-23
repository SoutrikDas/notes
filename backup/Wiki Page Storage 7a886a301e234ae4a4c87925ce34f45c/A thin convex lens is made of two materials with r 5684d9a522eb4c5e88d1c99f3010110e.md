# A thin convex lens is made of two materials with refractive indices n_1 and n_2, as shown. The radius of curvature of the left and right spherical surfaces are equal. f is the focal length of the lens when n_1=n_2=n. The fola length is f+\Delta f when n_1=n and n_2=n+\Delta n. Assuming \Delta n <<(n-1) and 1<n<2, what is correct

Column: Oct 9, 2020 9:40 PM
Last edited by: Soutrik das
Parent: JEE%20ADV%202019%20paper%201%206e969e4fdf724b4eba045ad8c9ac0feb.md, Optics%209bb9f3e50d454a969522b72343c81b20.md
Tags: adv, doubt cleared, physics, question

![A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled.png](A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled.png)

![A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled%201.png](A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled%201.png)

Alright , I believe I have to calculate the $f'$ ( since $f$ is already being used )  focal length as a function of $n_1$ and $n_2$ , and how do I do that ? Well I can use the formula of refraction at curved surfaces  ( Check [Optics](Optics%209bb9f3e50d454a969522b72343c81b20.md))

$$\frac{\mu_2}{v}-\frac{\mu_1}{u}=\frac{\mu_2-\mu_1}{R}$$

Now let the incoming rays be at an infinite distance ( so that we can call the final image to be the focal point ) 

Let the magnitude of radius be $R$ 

- Radius for the left Surface is $+R$
- Radius for the right surface is $-R$

- Failed attempt to calculate focal length by using Refraction on a curved surface formula $\frac{\mu_2}{v_1}-\frac{\mu_1}{u_1}=\frac{\mu_2-\mu_1}{R}$

    ## Refraction on Left curved surface

    ---

    $$\frac{\mu_2}{v_1}-\frac{\mu_1}{u_1}=\frac{\mu_2-\mu_1}{R}$$

    $$\frac{n_1}{v_1}-\frac{1}{-\infin}=\frac{n_1-1}{R}$$

    $$\frac{n_1R}{n_1-1}=v_1$$

    Now we will use $v_1$ as $u_2$ , ie we will use the image after refraction at first surface , as the object for refraction at second surface 

    But wait ! Before it reaches the second surface , Wont there be a refraction between the two lenses ? IDK

    ## Refraction on Right curved Surface

    ---

    $$\frac{\overbrace{1}^{air}}{\underbrace{v_2}_{f'}}-\frac{n_2}{u_1}=\frac{1-n_2}{-R}$$

    $$\frac 1 {v_2}-\frac{n_2(n_1-1)}{n_1R}=\frac{n_2-1}{R}$$

    $$\frac 1 {v_2}=\frac{n_2-1}{R}+\frac{n_2(n_1-1)}{n_1R}$$

    $$\frac 1 {v_2}=\frac{n_1n_2-n_1}{n_1R}+\frac{n_2n_1-n_2)}{n_1R}$$

    $$\frac 1 {v_2}=\frac{2n_1n_2-(n_1+n_2)}{n_1R}$$

    Since $v_2=f'$ ( since $f$ is a part of the question , general focal length is depicted using $f'$

    $$f'=\frac{n_1R}{2n_1n_2-(n_1+n_2)}$$

    Now the value of $f$ is  ( when $n_1=n_2=n$ )

    $$f=\frac{nR}{2n^2-2n}$$

    $$f=\frac{\cancel nR}{2\cancel n(n-1)}$$

    $$f=\frac{R}{2(n-1)}$$

    Now lets find the value of $f+\Delta f$ ( When $n_1=n$ and $n_2=n+\Delta n$ )

    $$f'=\frac{n_1R}{2n_1n_2-(n_1+n_2)}$$

    $$f+\Delta f=\frac{nR}{2n(n+\Delta n)-(n+n+\Delta n)}$$

    $$f+\Delta f=\frac{nR}{2n^2+2n\Delta n-n-n-\Delta n}$$

    How do we find $\frac{\Delta f}{f}$ and $\frac{\Delta n}{n}$ ? Do we put in the value of $f$ in this ? man that would be too long . But i dont have any other way 

    $$\Delta f=\frac{nR}{2n(n-1)+\Delta n(2n-1)}-\frac{R}{2(n-1)}$$

    $$\Delta f=\frac{[2(n-1)]nR}{[2n(n-1)+\Delta n(2n-1)][2(n-1)]}-\frac{R[2n(n-1)+\Delta n(2n-1)]}{2(n-1)[2n(n-1)+\Delta n(2n-1)]}$$

    $$\Delta f=\frac{[2(n-1)]nR-R[2n^2+2n\Delta n-2n-\Delta n]}{[2n(n-1)+\Delta n(2n-1)][2(n-1)]}$$

    $$\Delta f=\frac{2n^2R-2nR-2n^2R-2n\Delta nR+2nR+R\Delta n}{[2n(n-1)+\Delta n(2n-1)][2(n-1)]}$$

    $$\Delta f=\frac{\cancel{2n^2R}-\bcancel{2nR}-\cancel{2n^2R}-2n\Delta nR+\bcancel{2nR}+R\Delta n}{[2n(n-1)+\Delta n(2n-1)][2(n-1)]}$$

    $$\Delta f=\frac{R\Delta n(1-2n)}{[2n(n-1)+\Delta n(2n-1)][2(n-1)]}$$

    $$\frac{\Delta f}{f}=\frac{\Delta n(1-2n)}{2n(n-1)+\Delta n(2n-1)}$$

# Using Lens maker formula for each individual lens , then using Thin lenses in contact concept

---

Before getting into calculation , remember the lens maker formula assumes that the material of the lens be same everywhere , and that the outside material is also the same 

But you might think that here if we take left lens as a system , the materials outside the lens isnt the same 

![A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled%202.png](A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled%202.png)

But we can assume there to be a very thin layer of air between the two lenses 

![A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled%203.png](A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled%203.png)

Hence we can use the lens maker formula again !

## Left lens

$$f_1=\frac{R}{n_1-1}$$

## Right Lens

$$\frac 1{f_2}=(n_2-1)\left(\overbrace0^{\text{infinite radius bcuz flat}}- \frac 1 {\underbrace{-R}_{\text{sign convention}}}\right)$$

$$f_2=\frac{R}{n_2-1}$$

That was much smoother

Now we know that when in contact 

$$\frac 1{f_{eq}}=\frac 1 {f_1}+\frac 1 {f_2}+\cdots$$

$$\frac 1{f_{eq}}=\frac{n_1-1}{R}+\frac{n_2-1}{R}$$

$$f_{eq}(n_1,n_2)=\frac{R}{n_1+n_2-2}$$

From question , we know that when $n_1=n_2=n$ then the equivalent focal length is termed as $f$ 

$$f=\frac{R}{2(n-1)}$$

When $n_1=n$ and $n_2=n+\Delta n$ , equivalent focal length is going to be $f+\Delta f$ 

$$f+\Delta f=\frac{R}{2n+\Delta n-2}$$

$$\Delta f=\frac{R}{2n+\Delta n-2}-\overbrace{\frac{R}{2(n-1)}}^{f}$$

$$\Delta f=R\times \frac{2n-2-2n+2-\Delta n}{(2n+\Delta n-2)(2n-2)}$$

$$\frac{\Delta f }f=\frac{-\Delta n}{(2n+\Delta n-2)} \tag 1$$

Using the assumption that 

$$(n-1)>>\Delta n$$

$$\frac{\Delta f }f=\frac{-\Delta n}{2(n-1)} \tag 1$$

# Nekoma's Solution

---

![https://cdn.discordapp.com/attachments/702561907961233459/758664423651934278/IMG_20200924_174938.jpg](https://cdn.discordapp.com/attachments/702561907961233459/758664423651934278/IMG_20200924_174938.jpg)

According to me $\Delta f$ was 

$$\Delta f=\frac{-R\Delta n}{(2n+\Delta n-2)(2n-2)}$$

Acc to Nekoma , he neglected the $\Delta n$ in the denominator part 

![A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled%204.png](A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/Untitled%204.png)

$$\Delta f=\frac{-R\Delta n}{4(n-1)^2}$$

Now he finds 

$$\left |\frac{\Delta f}{f} \right|=\left| \frac{-\Delta n}{2(n-1)} \right|$$

This is the more rigourously correct version

![A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/WhatsApp_Image_2020-09-24_at_18.11.03.jpeg](A%20thin%20convex%20lens%20is%20made%20of%20two%20materials%20with%20r%205684d9a522eb4c5e88d1c99f3010110e/WhatsApp_Image_2020-09-24_at_18.11.03.jpeg)

Actually that negative also explains why option C is correct 

Option A is prooved , and option D , is true probably because $R$ does not even enter this equation ( ie $\frac{\Delta f}{f}$ is independant of $R$ ) 

[]()