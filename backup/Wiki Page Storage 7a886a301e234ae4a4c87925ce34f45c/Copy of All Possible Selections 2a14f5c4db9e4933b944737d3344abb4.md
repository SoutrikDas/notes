# Copy of All Possible Selections

Column: Aug 26, 2020 12:53 PM
Last edited by: Soutrik das
Tags: maths

[Concepts](Copy%20of%20All%20Possible%20Selections%202a14f5c4db9e4933b944737d3344abb4/Concepts%205afc6f77bdb249cdb19856af09371a5e.csv)

# All Possible Selections

## ex: No. of ways n diff things taken **one or More** at a time

Ans : $^nC_1+^nC_2+^nC_3+\cdots ^nC_n=2^n-1$

## Total Number of Selections of One or More Things
from p Identical Things of One Type, q Identical
Things of Another Type, r Identical Things of the
Third Type and n Different Things

Since, the number of ways of selecting $r$ things out of n identical things is 1 for all $r \le n$
Hence, the number of ways of selecting zero or more things
out of p identical things is \a{1}{Choosing 0}{1}{Choosing 1}

$$\newcommand{\a}[4]{\overbrace{#1}^{\text{#2}}+\underbrace{#3}_{\text{#4}}} \a{1}{choose 0 out of p}{1}{choosing 1 out of p}+\cdots=p+1$$

Similarly, the number of ways of selecting zero or more things
out of q and r identical things is q + 1 and r + I, respectively

Also the number of ways of selecting zero or more things out
of n different things is 2 x 2 x 2 x ··· n times = 2".

So No. of ways to choose **0 or more** from p,q,r identical and n diff is 

$$(p+1)\times(q+1)\times(r+1)\times 2^n$$

No of ways to choose zero things = $1\times1\times1\times1$=1 

So no. of ways to Choose **1 or more** = 0 or more - choosing 0 

$$(p+1)\times(q+1)\times(r+1)\times 2^n-1$$

If $p=0$ , $q=0$ and $r=0$ we get the formula as $2^n-1$ which is same as [N diff things taken one or more at a time](https://www.notion.so/Combinatoric-39f52117392b498793bbc111a9a3475d#364e6f6686f44912b2cfe0465b010709)