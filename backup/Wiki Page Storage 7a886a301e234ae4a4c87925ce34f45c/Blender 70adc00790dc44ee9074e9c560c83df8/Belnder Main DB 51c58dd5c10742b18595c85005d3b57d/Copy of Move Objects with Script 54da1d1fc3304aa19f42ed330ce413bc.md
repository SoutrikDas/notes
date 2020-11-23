# Copy of Move Objects with Script ?

There are really two parts to this question 

How do I get an object in context , and then how do I move it , rotate it , scale it ? 

You can get a object in many ways 

the easiest is to either know its name or to select it 

## getting object with name

```jsx
ob=bpy.data.objects['Sphere']
```

## Getting selected object

```jsx
ob=bpy.context.object
objects=bpy.context.selected_objects
```

## Getting position of an object

```jsx

```

## Setting position of an object

```jsx
ob.position = (1,3,4) 
```