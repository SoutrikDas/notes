# A cycle wheel contains 24 spokes of 0.5 m length , It is rotated in horizontal plane with 120 revolution /min in the effect of earth magnetic field. If total magnetic field of earth is 10^4 G, then dynamic emf accross center and rim of the wheel ( angle of dip is 30\degree)

![A%20cycle%20wheel%20contains%2024%20spokes%20of%200%205%20m%20length%20,%20b26eb14f93104a89b00daa70cc912bf3/Untitled.png](A%20cycle%20wheel%20contains%2024%20spokes%20of%200%205%20m%20length%20,%20b26eb14f93104a89b00daa70cc912bf3/Untitled.png)

Why is there even an emf ? Because when we rotate a rod like this 

![A%20cycle%20wheel%20contains%2024%20spokes%20of%200%205%20m%20length%20,%20b26eb14f93104a89b00daa70cc912bf3/rotating_rod.gif](A%20cycle%20wheel%20contains%2024%20spokes%20of%200%205%20m%20length%20,%20b26eb14f93104a89b00daa70cc912bf3/rotating_rod.gif)

Especially in a magnetic Field , then an emf is produced , which is 

$$E=\frac{\omega Bl^2}{2}$$

For how this formula comes about , check [EMI](../../EMI%20810a9cff73044ee68f1f88cb89f6f6ca.md) 

So what is the $\omega$ of The cycle wheel ?

$$\omega=\frac{120 \text{ revolution}}{min}=\frac{120 \times 2\pi}{60 s}=4\pi$$

But since there are many spokes (24 ) this effect will also be imminent for all of the spokes

So 

$$E=24\times \frac{\overbrace{\omega l^2}^{\text{we know}}B}{2}$$

To find the Magnetic field We take the component of Magnetic field along with angle of dip ( [check here](https://www.notion.so/soutrik/Magnetism-44758a8789a747ddb56b2e42e99d3a7f#ba72f79119f6472eb55ea05ed6698fb9) )

$$B_H=B \cos (\theta _{dip})\\
B_V=B\sin (\theta _{dip})$$

$$B_v=1000G\times 0.5 =1T\times 0.5=\frac 12$$

Where 

- $B$ is the net magnetic field of earth
- $\theta_{dip}$ is the angle of dip
- $B_H$ is the magnetic field in horizontal plane at that position ( we dont need this )
- $B_V$ is the magnetic field in vertical plane ( we need this )

$$\newcommand{\a}[2]{\overbrace{#1}^{\text{#2}}}
E=12\times \a{4\pi}{$\omega$}\times \a{0.25}{$l^2$}\times \a{\frac 12}{Magnetic field in vertical plane}$$

$$E=6\pi$$