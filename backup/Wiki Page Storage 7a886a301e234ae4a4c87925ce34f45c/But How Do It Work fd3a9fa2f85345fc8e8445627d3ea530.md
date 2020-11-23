# But How Do It Work?

Column: Oct 31, 2020 9:29 AM
Last edited by: Soutrik das
Tags: book

This is a book about How Computers work , Cpu and ram and all that stuff

# One Bit of Memory and how four NAND Gate can `Remember`

This is supposedly , one bit of memeory 

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled.png](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled.png)

lets actually mathematically calculate that 

$$a=\overline{is} \\
b=\overline{as} \\
c=\overline{ob} \\
o=\overline{ca}$$

That is actually pretty complex, I mean look at the last part , the output of C is input of O and the output of O is input of C . But maybe , if we write it all down in terms of IS , we can make sense out of it 

$$a=\bar i + \bar s$$

$$b=\bar a+\bar s=is+\bar s \tag{since a=$\overline{is}$}$$

$$c=\overline o + \overline b=\overline o +as=\overline o +(\overline i+\overline s)s=\overline o +\overline i s$$

$$o=\overline {ca}=\overline c+\overline a=\overline c+is=\overline o +\overline is+is=\overline o+is$$

But we get this weird loop 

$$o=\overline o +is$$

why ? O depends on itself ? like how ?

Okay lets look at the books explanation of this 

## When s=1 , then Ou=I

when `s` is turned on , then output is same as Input 

when s=1 and i=0 

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/s1_i0.gif](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/s1_i0.gif)

if one input  is zero then the output is definately 1 without knowing the other input

when s=1 i=1

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/s1_i1.gif](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/s1_i1.gif)

## When s=0 we face a dillemma

the dillemma is this 

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/what_are_we_going_to_do_now.gif](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/what_are_we_going_to_do_now.gif)

I question marked `i` because either way , its kind of useless , but the others I question marked them because i dont know what to do 

Lets assume `o` is going to be `1`  and wow it works

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/omg.gif](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/omg.gif)

Let see what happens if we assume `o` to be  `0` , wut ? it also works !

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/wut.gif](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/wut.gif)

so if `o` can be either `0` or `1` then what does it do ?

So the answer to the question of what happens to '0' when 's' is turned off, is that
it stays the way it was, and it is no longer affected by 'i.

which means the current output depends on the previous output, if the previous output was 1 , then the new output will also be 1 , if the previous output was 0 , then the new output will also be 0 

## so how does this circuit help , what even is it ?

this circuit is `one bit of computer memory` 

This complicated memory is denoted like this 

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled%201.png](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled%201.png)

so `s` stands for `set` , when we want to set , we turn S on , then we pass the thing we want to store , ie I , then turn S off , this essentially locks the output to the thing we wanted , now after turning s off , even if we change I , its not going to change O . 

a little bit of research shows that this is called an SR latch and it stands for set and reset 

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled%202.png](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled%202.png)

And what we are doing is basically adding to these some more things 

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled%203.png](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled%203.png)

# A byte

why even use a byte ? Because with bits we only have two states , on or off , 1 or 0 , we cannot write letters with this can we ? 

Now why did we choose 8 bits = 1 byte , that even I dont know , but here is a diagram of a byte 

the `set` inputs of all the memory cells have been tied up so that when one `set` is on , all of the memory cells start capturing data , and you dont have to turn on 8 different `set` 's to do that.

![But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled%204.png](But%20How%20Do%20It%20Work%20fd3a9fa2f85345fc8e8445627d3ea530/Untitled%204.png)

Just to show you that computer
designers do have a sense of humor, when they use four bits as a unit, they call it
a nibble.
which means $\boxed {bits<nibble<Bytes}$