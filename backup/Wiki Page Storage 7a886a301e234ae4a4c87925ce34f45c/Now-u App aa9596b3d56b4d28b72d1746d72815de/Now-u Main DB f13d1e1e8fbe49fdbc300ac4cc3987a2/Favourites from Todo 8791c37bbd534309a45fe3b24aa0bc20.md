# Favourites from Todo

So the Todo Used to operate like this 

```dart
model.removeActionStatus(_action.getId()) //removing from todolist
 model.starAction(_action.getId()) //adding to todolist 
```

How do you know whether or not if an action is starred ?

```dart
bool isStarred = model.currentUser.getStarredActions().contains(_action.getId());
```

Where `_action` is an variable having an action

The final product is something like this 

![Favourites%20from%20Todo%208791c37bbd534309a45fe3b24aa0bc20/Favourites.png](Favourites%20from%20Todo%208791c37bbd534309a45fe3b24aa0bc20/Favourites.png)

The color information of the star is 

![Favourites%20from%20Todo%208791c37bbd534309a45fe3b24aa0bc20/Untitled.png](Favourites%20from%20Todo%208791c37bbd534309a45fe3b24aa0bc20/Untitled.png)

[Experimenting with the ActionSelectionItem](Favourites%20from%20Todo%208791c37bbd534309a45fe3b24aa0bc20/Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6.md)

so after a bit of tinkering , I have this 

```dart

```