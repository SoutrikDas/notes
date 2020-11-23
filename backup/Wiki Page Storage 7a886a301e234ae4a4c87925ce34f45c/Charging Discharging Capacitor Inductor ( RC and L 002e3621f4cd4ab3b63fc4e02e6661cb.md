# Charging Discharging Capacitor Inductor ( RC and LR )

Column: Sep 26, 2020 3:10 PM
Last edited by: Soutrik das
Parent: Capacitance%20caeded92469e47e098a21d1ef36e2d0c.md
Tags: physics

# C-R Circuits

---

## Charging

---

Normally when there is no resistance , the capacitor charges crazy fast , almost no time  ( because of infinite current ) 

But with a resistance limits the current at every point , so it cannot charge that fast 

![Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled.png](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled.png)

Using Kirchoff voltage Law 

$$+E-\frac qC-iR=0$$

we know 

$$i=\frac{dq}{dt}$$

$$+E-\frac qC-\frac{dq}{dt}R=0$$

We have got a [linear differential equation](https://www.notion.so/soutrik/Differential-Equation-140b16dfa0854772803fa71633eb3ff2#a3d1c39a5ff1469ebbec0d770f3c09be) If I am not wrong , Lets arrange it in a way we can solve it 

The first thing is to make the coefficient of $\frac{dq}{dt}$ to $1$

$$\frac{dq}{dt}+\frac{q}{RC}= \frac E R$$

$$\large IF=e^{\int \frac{1}{RC}dt}=e^{\frac{t}{RC}}$$

$$d(q\times e^{\frac{t}{RC}})=\frac E Re^{\frac{t}{RC}} dt$$

Integrating we get 

$$q\times e^{\frac{t}{RC}}=ECe^{\frac{t}{RC}}+c \tag 1$$

Now putting $t=0$ we get that 

$$q=EC+c$$

But clearly at the beginning , there was no charge  on the plates, which means 

$$c=-EC$$

We can also write $EC$ and $q_0$ because that is the maximum charge that we can put on 

$$c=-q_0$$

So equation 1 becomes 

$$q\times e^{\frac{t}{RC}}=q_0(e^{\frac{t}{RC}}-1)$$

Now if we divide 

$$q=q_0(1-e^{-\frac{t}{RC}})$$

This is the general Equation of charging a capacitor 

### $\tau$ in Charging

---

We define $\tau =RC$ such that when $t=\tau$ we get 

$$q=q_0\left(1-\frac 1 e \right)$$

$$q=q_0\left(\frac {e-1}e \right)$$

The Eulers number is $e=2.718 \dots$

$$q=q_0\left(\frac {1.718}{2.718} \right)$$

Remember $\boxed{\cfrac{1.718}{2.718}=0.632}$

$$q=(0.632)\times q_0$$

This fact is used not only in physics for RC and LR , but also in Chemistry in first order kinetics , which is also used in Radioactivity and decay ( since all radioactivity is first order ) 

![Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%201.png](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%201.png)

We write this equation as 

$$\large q=q_0(1-e^{-\frac{t}{\tau}})$$

## Discharging or RC circuit

---

The formula can be derived in the same fashion , it will be 

 

$$q=q_0\left( e^{-\frac t{RC}} \right)$$

### $\tau$ in Discharging RC

---

when $t=\tau$ 

$$q=q_0\left( \frac 1 e \right)$$

Remember $\boxed{\cfrac{1.718}{2.718}=0.632}$ and $0.632=\frac{e-1}{e}=1-\frac 1 e$ , from here you can get the value of $\frac 1 e=0.36$ 

![Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%202.png](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%202.png)

# Growth of Current in LR circuit

---

![Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%203.png](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%203.png)

Writing kirchoff Loop Law equation we get 

$$V-iR-L\frac{di}{dt}=0$$

Keep in mind that initially the current is almost 0 , but slowly it rises and attains its final value $i_0$ , its almost like a capacitor being charged ( initially no charge , slowly comes to $q_0$ ) 

Again a  [linear differential equation](https://www.notion.so/soutrik/Differential-Equation-140b16dfa0854772803fa71633eb3ff2#a3d1c39a5ff1469ebbec0d770f3c09be)  which if we solve we will get 

the only difference that we see here is that the  exponential term has changed $\boxed{e^{-\frac t{RC}}}$ in Capacitor and $\boxed{e^{-\frac {RT}L}}$ in Inductor .

Therefore the value of $\tau$ will also change from $\frac 1 {RC}$ to $\frac {L}{R}$

So the final equation for growth of current is 

$$i=i_0\left(     
1-e^{-\frac{t}{\tau}}
\right)$$

# Questions

---

![Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%204.png](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%204.png)

If you think that in this question ( max charge is $CV/2$ ) the equation of $q$ will be 

$$q=q_0(1-e^{-\frac{t}{RC}})$$

Then you are wrong , why ? Because here $R$ is only the resistance in the branch of capcitors 

So do we need to account for the other branche's resistance also ? 

Yes , when we derived the formula , there wasnt any other resistance , so we oviously didnt include it in our formula , but in reality there is a procedure we must follow , to find out what our time constant is going to be .

We can find that out via basic method ( integration ) Physics wallah [derived it here](https://youtu.be/zyZDmc-j_C0?t=2063) , but there is also a shortcut method 

The basic method requires you to use KNL 

[Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/vlc-record-2020-09-26-13h46m25s-NA-Electrostatic_Capacitance_19__-_RC_Circuit_-_How_to_Solve_Circuit_with_Resistor__Capacitor_both.mp4-.mp4](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/vlc-record-2020-09-26-13h46m25s-NA-Electrostatic_Capacitance_19__-_RC_Circuit_-_How_to_Solve_Circuit_with_Resistor__Capacitor_both.mp4-.mp4)

Shortcut is to 

- Find $q_0$ ( charge at steady stete )
- Find $R_i$ such that it is the eq Resistance across capacitor ( with battery shorted )

[Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/vlc-record-2020-09-26-14h10m48s-NA-Electrostatic_Capacitance_19__-_RC_Circuit_-_How_to_Solve_Circuit_with_Resistor__Capacitor_both.mp4-.mp4](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/vlc-record-2020-09-26-14h10m48s-NA-Electrostatic_Capacitance_19__-_RC_Circuit_-_How_to_Solve_Circuit_with_Resistor__Capacitor_both.mp4-.mp4)

we get 

![Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%205.png](Charging%20Discharging%20Capacitor%20Inductor%20(%20RC%20and%20L%20002e3621f4cd4ab3b63fc4e02e6661cb/Untitled%205.png)

and on finding R eq we get 

$$R_i=\frac 32 R$$

therefore 

$$\large q=q_0(1-e^{-\frac{t}{(\frac 32 R)C}})$$

Now this was due to extra resistors , what if we add extra capacitors  ( we will probably have to follow the basic method )