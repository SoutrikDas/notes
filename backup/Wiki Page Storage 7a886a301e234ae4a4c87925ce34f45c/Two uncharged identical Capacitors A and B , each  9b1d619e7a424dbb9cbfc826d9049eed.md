# Two uncharged identical Capacitors A and B , each of Capacitance C, and an inductor of inductance L are arranged as shown in the adjacent figure. At t=0, the switch S1 (left) is closed while the switch S2 (right) remains open. At time t= t_0=\sqrt{LC\pi /2} ,  switch S_2 is closed hwile S_1 is opened

Column: Oct 9, 2020 9:24 PM
Last edited by: Soutrik das
Parent: Capacitance%20caeded92469e47e098a21d1ef36e2d0c.md
Tags: question

![Two%20uncharged%20identical%20Capacitors%20A%20and%20B%20,%20each%20%209b1d619e7a424dbb9cbfc826d9049eed/Untitled.png](Two%20uncharged%20identical%20Capacitors%20A%20and%20B%20,%20each%20%209b1d619e7a424dbb9cbfc826d9049eed/Untitled.png)

Normally when we connect DC across a capacitor it charges very fast , almost no time , charging takes time when a resistor is connected with the capacitor , but I have never seen a case of Capacitor and an Inductor. 

So when the left Circuit is completed what happens ? 

The Batteryx starts giving Charge to Capacitor , but this is not AC , But does LC oscillations happen in AC or DC ?

Anyway at t=t the KVL will give us 

$$E -\frac{q}{C} \overbrace{-L\frac{di}{dt}}^{\text{I am a bit unsure about this part}}=0$$

Because it really depends if the current is increasing or decreasing , But in an ideal condition after $t=\infin$ the capacitor will be fully charged . But then we dont have that much of time . So now what ?

we can write $i=\frac{dq}{dt}$ maybe to find something

$$E-\frac{q}{C}-L\frac{d^2q}{dt^2}=0$$

OH ! this is almost like SHM  Maybe a bit different but a lot same 

In SHM we had 

$$F=-kx$$

Or 

$$\frac{d^2x}{dt^2}=-kx$$

And Solution of this equation was ... 

$$x=A\sin( \omega t+\phi)$$

Here we have 

$$\frac{d^2q}{dt^2}=\frac EL-\frac q {CL}$$

So solution will be 

$$q=A\sin{(\omega t+\phi)}$$

putting t=0 we get that $q=0$ so $\phi =0$ , What is the maximum value of Q ? It will be $q=CE$ 

What about Omega ? We find it out by using $\omega = 2\pi /T$ but then what is Time period ?

OK we dont need the time period , we can find it by using $\omega^2= k/m$ , for this case 

$$\omega^2=\frac{1}{CL} \\
\omega=\frac{1}{\sqrt{CL}}$$

Hence the final equation is 

$$q=CE\sin{\left(\frac{1}{\sqrt{CL}}t \right)}$$

But then its a bit weird because I never heard about oscillations when Source is connected .