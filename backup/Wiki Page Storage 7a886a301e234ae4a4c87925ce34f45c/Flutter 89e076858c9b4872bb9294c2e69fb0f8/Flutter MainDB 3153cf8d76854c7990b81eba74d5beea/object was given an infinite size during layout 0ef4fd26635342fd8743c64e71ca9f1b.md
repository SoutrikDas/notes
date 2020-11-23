# object was given an infinite size during layout.

Tags: problem, solved

So I have been having problems with layout of the rive animation 

on its own its just fine 

but when I nest it in a column or container or both , theres the problem 

This website is probably relevant 

[Understanding constraints](https://flutter.dev/docs/development/ui/layout/constraints)

So what I was able to understand from this website is that if you want to constrain a widget , then constraint the parent first 

so I did constrain the `Container` , heck I even tried to constrain the `Column` with the `MainAxisSize.min` but its still overflowing the bottom by infinite pixels

Here is a relevant section of the code 

```dart
@override
  Widget build(BuildContext context) {
    return _artboard != null //checking if the rive animation has loaded or not
        ? Center(
            child: Container(
              width: 80,
              height: 90,
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text("First"),
                  Rive(
                    artboard: _artboard,
                    fit: BoxFit.cover,
                  ),
                  Text("Second"),
                ],
              ),
            ),
          )
        : Container(
            child: Text("Not yet loaded"),
          );
  }
}
```

Okay solved it 

the problem was that you couldnt specifiy the height of column , and column always try to expand , so the rive was also trying to expand 

what I did to fix it was to just wrap the rive inside a container and give it a definite height