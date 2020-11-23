# Shading

Tags: chapter

# Basics  and Shortcut

---

![Shading%200c0ec0fe9abe41bbb9a793c44659ace1/knife_.gif](Shading%200c0ec0fe9abe41bbb9a793c44659ace1/knife_.gif)

Cut multiple connections with the knife tool , the shortcut is `Ctrl+Right Click` then draw 

To join quickly , use `Alt + Right Click`

![Shading%200c0ec0fe9abe41bbb9a793c44659ace1/join_with_alt_right_click_.gif](Shading%200c0ec0fe9abe41bbb9a793c44659ace1/join_with_alt_right_click_.gif)

If you want to switch between two nodes alternatively , ie you want to try one , and then try another , and then try the previous one again , like so 

![Shading%200c0ec0fe9abe41bbb9a793c44659ace1/swap.gif](Shading%200c0ec0fe9abe41bbb9a793c44659ace1/swap.gif)

But this manual joining is a bit tedious , Instead we can use `Ctrl + Shift + Left Click`

![Shading%200c0ec0fe9abe41bbb9a793c44659ace1/control_shift_click.gif](Shading%200c0ec0fe9abe41bbb9a793c44659ace1/control_shift_click.gif)

which makes a buffer kind of node 

## How blender shades ,

So the way it shades is that , it stores a bunch of points and faces and each face can have their own material , yes , each face one material is a Possibility , But thats not what we generally do , generally Blender assigns all faces with one material , but we can still assign different material , heres how 

So how to do it ? 

- Go to Edit Mode
- Select a Face
- And then Assign like shown

![https://i.ibb.co/YBJ1RW7/different-materials-on-the-same-model.gif](https://i.ibb.co/YBJ1RW7/different-materials-on-the-same-model.gif)

## Use Values to form Color

---

You can use the `Combine RGB` Node to mix values into color , where 1 means its fully red, 0 means no red ( ie the  values dont go from 0-255  , they go from 0-1 )

![Shading%200c0ec0fe9abe41bbb9a793c44659ace1/Untitled.png](Shading%200c0ec0fe9abe41bbb9a793c44659ace1/Untitled.png)

## Make your own Node In Blender

---

## Drivers : Use LocRotScale to Shade

---

So drivers basically allow you to shade depending on the Loc Rot Scale of the object 

![Shading%200c0ec0fe9abe41bbb9a793c44659ace1/driver.gif](Shading%200c0ec0fe9abe41bbb9a793c44659ace1/driver.gif)

## Maths with 3D coordinates

---