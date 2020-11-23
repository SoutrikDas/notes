# In the figure below, the switches S_1 and S_2 are closed simultaneously at t=0 and a current starts to flow in the circuit. Both the batteries have the same EMF. Ignore mutual inductance. The current I in the middle wire reaches its maximum magnitude I_{max} at time t=\tau

Column: Sep 26, 2020 5:21 PM
Last edited by: Soutrik das
Parent: JEE%20ADV%202018%20paper%201%20156baa1a568144639dd9e5b9a1b32e04.md

![In%20the%20figure%20below,%20the%20switches%20S_1%20and%20S_2%20are%20%20aa33d3e50a9e4613bb48996443aaf0aa/Untitled.png](In%20the%20figure%20below,%20the%20switches%20S_1%20and%20S_2%20are%20%20aa33d3e50a9e4613bb48996443aaf0aa/Untitled.png)

So first of all , the current is not maximum at steady state . its max somewhere in between . 

But how do we find the equation of current ? 

for one Inductor we know from [Charging Discharging Capacitor Inductor ( RC and LR ) ](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb.md) that the equation is 

$$i=i_0\left( 1-e^{-\frac{RT}{L}} \right)$$

But here it will probably be very different , maybe we need to derive again

Naming some points 

![In%20the%20figure%20below,%20the%20switches%20S_1%20and%20S_2%20are%20%20aa33d3e50a9e4613bb48996443aaf0aa/Untitled%201.png](In%20the%20figure%20below,%20the%20switches%20S_1%20and%20S_2%20are%20%20aa33d3e50a9e4613bb48996443aaf0aa/Untitled%201.png)

Starting from $B$ and going through $CDEA$

$$V-I_1R-L\frac{dI_1}{dt}=0$$

Starting from $H$ and going through $GFEA$

$$-V-2L\frac{dI_2}{dt}-I_2R=0$$

The equations so far , look , almost as if the loops were un attached , 

![In%20the%20figure%20below,%20the%20switches%20S_1%20and%20S_2%20are%20%20aa33d3e50a9e4613bb48996443aaf0aa/Untitled%202.png](In%20the%20figure%20below,%20the%20switches%20S_1%20and%20S_2%20are%20%20aa33d3e50a9e4613bb48996443aaf0aa/Untitled%202.png)

As if the action was happening like this , but in the question someone superimposed them 

If we write individual current equations , we get 

$$I_1=I_{1max}\left( 1-e^{-\frac{RT}{L}} \right)$$

$$I_2=\overbrace{-}^{\text{minus because in individual circuit current is opposite}}I_{2max}\left( 1-e^{-\frac{RT}{2L}} \right)$$

We can find $I_{max}$ by thinking of the inductor as conductor ( in steady state , it acts like a conductor , and current is max then and there ) 

But the if according to my logic , the maximum current should be when both the circuits have reached their individual steady state . Which is not true ? because the question specifies that $I=I_1+I_2$ reaches maximum at $t=\tau$ .

What am I missing?

There is nothing missing but the fact that $I_2$ opposes $I_1$ 

my nomenclature made it difficult to grasp .

![In%20the%20figure%20below,%20the%20switches%20S_1%20and%20S_2%20are%20%20aa33d3e50a9e4613bb48996443aaf0aa/Untitled%203.png](In%20the%20figure%20below,%20the%20switches%20S_1%20and%20S_2%20are%20%20aa33d3e50a9e4613bb48996443aaf0aa/Untitled%203.png)

Let $I_3=-I_2$

Now we can see that 

$$I=I_{1max}\left( 1-e^{-\frac{RT}{L}} \right)-I_{2max}\left( 1-e^{-\frac{RT}{2L}} \right)$$

$$I_{1max}=\frac V R$$

$$I_{2max}=\frac VR$$

$$I=\frac VR \left( e^{-\frac{RT}{2L}}-e^{-\frac{RT}{L}}\right)$$

It seems by mistake I have taken $t$ to be $T$ in the above equations

Differentiating with respect to $t$ 

$$\frac{ dI}{dt}=0=\frac VR\left(-\frac{R}{2L}\times  e^{-\frac{Rt}{2L}}+\frac{R}{L}\times e^{-\frac{Rt}{L}}\right)$$

we get 

$$0=-0.5 e^{-\frac{Rt}{2L}}+ e^{-\frac{Rt}{L}}$$

- we should also do the second derivative test to see if it really is maximum or not

    $$\dot f(t)=-0.5 e^{-\frac{Rt}{2L}}+ e^{-\frac{Rt}{L}}$$

    Differentiating again we get 

    but this looks so complex that I dont want to do it 

let $e^{-\frac{Rt}{2L}}=x$

$$0.5x=x^2$$

$$x=\frac 1{2}$$

taking $\ln$ on both sides

$$-\frac{Rt}{2L}=-\ln2$$

$$t=\frac {2L} R \ln 2$$

and I am sure we can just put this value to get the $I_{max}$ 

even better , we can actually use this 

$$e^{-\frac{Rt}{2L}}=\frac 1{2}$$

$$e^{-\frac{Rt}{L}}=\frac 1{4}$$

We can put these two into 

$$I=\frac VR \left( e^{-\frac{RT}{2L}}-e^{-\frac{RT}{L}}\right)$$

$$I_{max}=\frac V{4R}$$

But now the question arises , what happens at infinity ? 

$$I=\frac VR \left( e^{-\frac{RT}{2L}}-e^{-\frac{RT}{L}}\right)$$

From the above equation , its becoming ~~indeterminant~~ ( it was becoming 0 )  , but from the understanding that the two loops are ( acting like ) independent , we can think of their behaviour when they reach their own maximum current .

And the answer is 0, since each will have a full $V/R$ current