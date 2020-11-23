# series.value_counts()

Description: Counts and displays the values 
Tags: function

For example , in the stack overflow database , we have a column named `Hobbyist` and the answers to that is `yes` or `no` , so how do we get the answer to this question : How many people said yes to that Hobbyist question ?

![series%20value_counts()%20f7ab95ede40d427d833105c2ce9b40a3/Untitled.png](series%20value_counts()%20f7ab95ede40d427d833105c2ce9b40a3/Untitled.png)

So for that we can just use the value_count() function on that series ( remember `df["Hobbyist"]` is a series )

![series%20value_counts()%20f7ab95ede40d427d833105c2ce9b40a3/Untitled%201.png](series%20value_counts()%20f7ab95ede40d427d833105c2ce9b40a3/Untitled%201.png)

And the return type is also a Series 

![series%20value_counts()%20f7ab95ede40d427d833105c2ce9b40a3/Untitled%202.png](series%20value_counts()%20f7ab95ede40d427d833105c2ce9b40a3/Untitled%202.png)

Also , if you use the code `df["Hobbyist"].value_counts("Yes")` then it will return the percentage of that value

![series%20value_counts()%20f7ab95ede40d427d833105c2ce9b40a3/Untitled%203.png](series%20value_counts()%20f7ab95ede40d427d833105c2ce9b40a3/Untitled%203.png)

in the second line , I basically did 

$$\frac{\text{Yes}}{(\text{Yes + No})}=\text{Yes}/(\text{ Yes + No )}$$