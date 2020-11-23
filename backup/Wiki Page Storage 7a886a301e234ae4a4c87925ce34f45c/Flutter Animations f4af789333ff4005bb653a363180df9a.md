# Flutter Animations

Column: Nov 8, 2020 12:47 PM
Last edited by: Soutrik das
Parent: Flutter%2089e076858c9b4872bb9294c2e69fb0f8.md

Using AnimatedContainer for implicit animation , but it doesnt work out 

[https://dartpad.dev/embed-flutter.html?id=65bf1fefc2a88698a60f188a1d9a4f9f](https://dartpad.dev/embed-flutter.html?id=65bf1fefc2a88698a60f188a1d9a4f9f)

I thought that this might be some problem happening only on dartpad , but it seems it happens even on my phone 

# Net Ninja Animation Series

---

## BiolerPlate Code

---

So there is already a base 

## Implicit v/s Explicit ?

---

In General , we can do an animation in both way , but explicit gives us more control ( therefore is harder to set up ) ( because it has an animation controller 

Implicit is mostly easy 

Generally :

If the animation is an endless loop → Explicit Animation

If the animation requires granular control → Implicit Animation 

So Here is the results when I animated the width , color , margin of an AnimatedContainer 

[https://dartpad.dev/d22432b7586d642ae82fa186a383e33e](https://dartpad.dev/d22432b7586d642ae82fa186a383e33e)

So this was a built in implicit animation 

## Custom Implicit animation using `Tween` Animation Builder

---

- Define our custom start and end points

What does a `tween` do ? It maps between the start and end values ,

So if the start and end values are $0$ and $3$ Then 

$$0,\overbrace{0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7}^{\text{made by the tween}},3$$