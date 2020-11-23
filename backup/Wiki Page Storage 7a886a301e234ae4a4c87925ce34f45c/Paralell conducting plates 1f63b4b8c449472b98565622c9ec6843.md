# Paralell conducting plates

Child: Capacitance%20caeded92469e47e098a21d1ef36e2d0c.md, Redistributing%20Charges%20Grounding%20(%20Connecting%20char%20629b314ecb0341b380fa2ecb23d86d71.md
Column: Oct 9, 2020 9:40 PM
Last edited by: Soutrik das
Tags: doubt, doubt cleared, physics

# Helpful guidelines for parallel plate questions :

---

1. Charges appearing on the outer surfces should be equal in magnitude as well as sign  ( otherwise  $\vec E=0$ inside the conductors wouldnt be true )
2. Charges appearing on the facing surfaces should be equal in magnitude but opposite in sign  ( Gauss Law )
3. If we connect any plate ( innermost or outermost ) then the charge appearing on the outermost surfaces will become 0  ( Go [here](https://www.notion.so/Paralell-conducting-plates-1f63b4b8c449472b98565622c9ec6843#5784052d2ab0466f9d7d9c9069a6b45a) or [here](https://physics.stackexchange.com/questions/256562/grounding-system-of-conducting-plates))
4. The charges on the plates other than the ones connected to the earth shoud be conserved ( because charge can flow in/out through the connection with earth)

# Charge distribution on conductors without any connection ( equal or unequal gaps doesnt matter )

---

![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled.png](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled.png)

For these cases we will use two pieces of information 

1. The charge on the outermost surfaces ( left surface of leftmost bar , and right surface of rightmost bar ) is going to be $\cfrac{\sum Q_i}{2}$
2. After movement of charges , $\vec E=0$ inside a conductor 
3. Gauss law , which when we apply in two conductors , we know that these faces will have opposite charges 

    ![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%201.png](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%201.png)

Now we can use this fact to distribute charges , for example :

![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates1.gif](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates1.gif)

Two parallel plate 

![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates2.gif](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates2.gif)

3 parallel plates 

## Charge distribution on conductors with unequal gaps

---

There will be no difference , because the fact that the outer most surfaces have $\sum Q_i /2$  derives from the fact that Electric field inside a conductor is 0 

- Derivation of  $\sum Q_i /2$

    ![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates3.gif](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates3.gif)

    now if equate the electric field due to the charges on the left side to the electric field due to the charges on the right side ( because elec field in second plate has to be 0 , and thats only possible when the left and right elec fields are same )

    $$\frac{10}{2A\epsilon} +\frac{q-10}{2A\epsilon} =\frac{15-q}{2A\epsilon} +\frac{q-15}{2A\epsilon} +\frac{12-q}{2A\epsilon} $$

    $$q=12-q
    \\q=6$$

    Which is what we were getting from $\sum Q_i/2$

![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates32.gif](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates32.gif)

# Connecting outermost two plates with wires ( equal or unequal gaps DOES matter )

---

So the concept is that the outermost surface will have the same charge distribution , with or without wires 

- But why does the charges on the outer most surfaces remain the same even when you connect them through a wire ?

    To understand that , lets see the whole story without assuming that w=they will remain same before and after connecting the wire 

    ![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates32.gif](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates32.gif)

    Charge distribution before connecting the wire

    Okay , now lets connect the wire ,without the assumption that the outermost surfaces will have same charges 

    ![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%202.png](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%202.png)

    The probelm is for electric field at $A$ to be $0$ , $Q_1$ has to be equal to $Q_2$ 

    ![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%203.png](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%203.png)

    Now lets use charge conservation for conductor 1 and conductor 3 together

    Before connecting the wire , the total charge of conductor 1 and 2 was  = $7$

    After connecting the wire , total charge = $(Q+q)+(-5-q+Q)=2Q-5$

    Now using charge conversion , ( ie before = after ) , we get 

    $$2Q-5=7 \\
    Q=6$$

    Hence the charge on the outermost surface remains same before and after ( because before connecting the wire $\sum Q_i/2=6$ )

- Can we use the fact that charge of first plate + charge of second plate is conserved to find $q$ ?

    No . Why ? 
    Initial charge = $10-3=7$

    Final charge = $6+q-5-q+6=7$

    It means that : charge is INDEED constant , but it doesnt give us some new information about $q$ , so its useless 

![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates32.gif](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplates32.gif)

Charge distribution before connecting the wire

![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%204.png](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%204.png)

Charge distribution after connecting the wire , $q$ is unknown 

Now use the fact that the potential of the first and third plates are same ( since they are connected , hence potential has to be same , otherwise current will flow and make the potential same )

$$\overbrace{\frac{(6+q)*3d}{A\epsilon}+\frac{5*2d}{A\epsilon}}^
{\text{Potential of
 3 due to 1 and 2}}=\overbrace{
\frac{5*1d}{A\epsilon}+\frac{(1-q)*3d}{A\epsilon}
}^{\text{Potential of 1 due to 2 and 3}}$$

Unequal or equal gaps will **make a difference here** , if the gaps were equal then you would have to adjust the distance between them in [this step](https://www.notion.so/Paralell-conducting-plates-1f63b4b8c449472b98565622c9ec6843#f64c4be3a60c43eea2c207e0c2925ba9)

$$18+3q+10=5+3-3q$$

$$6q=5+3-10-18$$

$$6q=-20$$

$$q=-\frac{10}{3}$$

Note : $q$ is not the amount of charge tranferred by the wire , it is simply the charge on the right face of the left most plate . To find the charge transferred by the wire Check the initial and final charge of the left most plate .
Initial Charge = $10$ 
Final Charge = $6-\frac {10}3=\frac 83$
From this you can get the charge that flowed through the wire 

# Connecting two middle plates with wire

---

# Two plates , one grounded

---

What happens ? 

1. The outermost charges become 0 
- Why does outermost become 0 ?

     Go [here](https://physics.stackexchange.com/questions/256562/grounding-system-of-conducting-plates) to see the actual answer . The reason is that when grounded , charges redistribute in such a way that the total energy of the electric field is minimum . Since the electric field inside is insignificant , the electric field outside is the biggest contributing factor to the energy of electric field. **The minimum of this energy is achieved when the total charge of the system of plates is zero**. This state is reachable: any charge can come to/from the grounded plate. And we know it is minimum because it is zero!

    So, the result is: whenever you ground one of the plates (any of them!), the total charge of all the plates becomes zero. The interlocking faces already amount to 0 , so to make the toal charge 0 , the outermost charge becomes 0 and it moves inside 

    What if we dont assume them to be zero , but instead take them as a variable ? 

    ![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%205.png](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%205.png)

    This is what will happen if we dont just assume the outermost charges will become 0 

    So now we can see that $Q_1$ has to be equal to $Q_2$ otherwise the electric field inside of first conductor becomes non zero.
    So now we have this picture 

    ![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%206.png](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/Untitled%206.png)

    One more condition can be that the second plate has 0 potential , so there shouldnt be any potential because of the first plate ? but then its more like the first plate is high in potential , it doesnt cast potential on the second plate , does it now ?

![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplatesgroundingtwoplates.gif](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplatesgroundingtwoplates.gif)

The chrage that flows through the ground to the plate is $-14$ , because before it was $4$ and after, it became $-10$

- When we ground one plate , the other plate still has charge, so the grounded plate is at a non zero potential , but after grounding , we should have a 0 potential plate , right ?

    In reality the plate **becomes zero potential** , but if you do NOT include **Self Potential** in your calculation you will find that the earthed plate has non zero potential

# 4 plates , outermost two grounded ( unequal or equal gaps will matter here)

---

![Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplatesgroundingoutermostoffourplates.gif](Paralell%20conducting%20plates%201f63b4b8c449472b98565622c9ec6843/parallelplatesgroundingoutermostoffourplates.gif)

Now we have to solve for $q$ , how will we do that ? We can Find out the potential of any grounded plates and equate it to $0$

But before that lets define some terms 

$$E_1=\frac{q}{2A\epsilon} $$

$$E_2=\frac{5}{2A\epsilon} $$

$$E_3=\frac{-2}{2A\epsilon} $$

$$E_4=\frac{-(3+q)}{2A\epsilon} $$

Now lets find the Potential for the last plate ( because its electric field looks a bit bad ) 

$$(-E_1*3d)+(-E_2*2d)+(-E_3*d)=\overbrace 0^{\text{4 th plate is grounded}}$$

Equal or unequal gaps **make a difference** here ,If the gaps were unequal then you would have to use that information here ( [in this step](https://www.notion.so/Paralell-conducting-plates-1f63b4b8c449472b98565622c9ec6843#6350b3b11a124f949d071633274be8cd))

Eliminating the $d$ and $\frac{1}{2A\epsilon}$ we get 

$$3q+10-2=0$$

$$q=-\frac 83$$

# Electric Field and Potential of Infinite Conducting Sheets

---