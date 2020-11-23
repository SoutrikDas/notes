# Copy of  In a radioactive sample, ^{40} _{19}K nuclei either decay into stable ^{40}_{20} Ca nuclei with decay
constant

Column: Sep 23, 2020 2:32 PM
Last edited by: Soutrik das
Parent: JEE%20ADV%202019%20paper%201%206e969e4fdf724b4eba045ad8c9ac0feb.md
Tags: adv, physics, question

![Copy%20of%20In%20a%20radioactive%20sample,%20%5E%7B40%7D%20_%7B19%7DK%20nucl%20745a354fff4d445b842e1d3baa92b045/Untitled.png](Copy%20of%20In%20a%20radioactive%20sample,%20%5E%7B40%7D%20_%7B19%7DK%20nucl%20745a354fff4d445b842e1d3baa92b045/Untitled.png)

What is Given ?

- Parallel Reaction

$$^{40} _{19}K\to \begin{cases}
^{40}_{20} Ca \quad k_1=4.5 \times 10^{-10}  \\
^{40}_{18}Ar \quad k_2=0.5 \times 10^{-10}
\end{cases}$$

- Initial no. of nuclei of $K$ not given so have to assume $n$

Now what do we know about a parallel reaction is that 

$$\newcommand{\a}[1]{\frac{d[#1]}{dt}} 
-\a K=[K]\times(k_1+k_2)$$

~~Mostly its graph wrt time is like this~~ 

Lets SOlve it Using DE

$$-\int _n^{n-a}\frac{dK}{K}=(k_1+k_2)t$$

$$-\ln K| _n^{n-a}=(k_1+k_2)t$$

$$\ln \left( \frac{n}{n-a}\right)=(k_1+k_2)t$$

But how do we find How much $Ca$ or $Ar$ has been produced ?

~~From the reactions~~ 

$$K \to Ca$$

$$K \to Ar$$

~~So $a$ nuclei of $K$ will give $a$ nuclei of ...NONONONO , then obviously the ratio will be 1 , so that cannot happen .~~

Instead there must be a relation. Because within that $a$ nuclei some is given to $Ca$ and Some is given to $Ar$  . And  that ratio is **probably** the ratio of their individual rate constants .

ie 

$$a=\begin{cases}
a\times \cfrac{k_1}{k_2+k_1} \text{ for Ca} \\
a\times \cfrac{k_2}{k_1+k_2} \text{ for Ar}
\end{cases}$$

~~Therefore the ratio of these two $\cfrac{Ca}{Ar}$become 99 then the equation is this~~

$$\frac{k_1}{k_2}=99$$

~~But how can this be as they are both constants?~~

The answer to this can be found [here](https://www.notion.so/Parallel-Reactions-7b508ec084044c3db087595f6ba0f70a#7cbbc67396a94653b2e3ea88a38f85a2) 

$$Ca=+\frac{k_1}{k_1+k_2}  \times K_0 
  \left(1- e^{-(k_1+k_2)t} \right)$$

~~Even with this its a bit unsolvable~~ 

$$Ar=+\frac{k_2}{k_1+k_2}  \times K_0 
  \left(1- e^{-(k_1+k_2)t} \right)$$

~~ie the ratio becomes~~ 

$$\frac{k_1}{k_2}=constant$$

---

🤦🏼 I have been taking the ratio of $\frac{Ca}{Ar}$ when i should have been taking the ratio of $\frac{Ca+Ar}{K}$

$$Ca+Ar=K_0 
  \left(1- e^{-(k_1+k_2)t} \right)\\
K=K_0  \left(e^{-(k_1+k_2)t} \right)$$

According to the question we have 

$$\cfrac{K_0 
  \left(1- e^{-(k_1+k_2)t} \right)}{K_0  \left(e^{-(k_1+k_2)t} \right)}$$

$$\cfrac{ 
  \left(1- e^{-(k_1+k_2)t} \right)}{ \left(e^{-(k_1+k_2)t} \right)}=\frac{1-x}{x}=99$$

Where $x=e^{-(k_1+k_2)t}$ then we get 

$$x=0.01$$

$$ \ln{x }=-(k_1+k_2)t \\
2.302 \log x=-(k_1+k_2)t\\
2.303 (-2)=-(5)\times 10^{-10} t$$

/fra