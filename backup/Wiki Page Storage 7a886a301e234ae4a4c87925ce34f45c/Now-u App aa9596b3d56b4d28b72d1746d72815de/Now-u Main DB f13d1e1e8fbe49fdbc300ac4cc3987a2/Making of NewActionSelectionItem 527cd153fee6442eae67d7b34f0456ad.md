# Making of NewActionSelectionItem

so Right now the old `ActionSelectioItem` used the class `LeadingSelectionItem` Which used `SelectionItem` , 

So the final Image should be something like this 

![Making%20of%20NewActionSelectionItem%20527cd153fee6442eae67d7b34f0456ad/Favourites.png](Making%20of%20NewActionSelectionItem%20527cd153fee6442eae67d7b34f0456ad/Favourites.png)

I am using the custom Tile Which gives me the border radius and shadow that now-u normally has 

which is great 

So the information about the icon , icon color and background color ,Can be taken from \

```dart
Map getActionIconMap() {
    if (campaignActionTypeData.containsKey(type)) {
      return {
        'icon': campaignActionSuperTypeData[campaignActionTypeData[type]['type']]['icon'],
        'iconColor': campaignActionSuperTypeData[campaignActionTypeData[type]['type']]['iconColor'],
        'iconBackgroundColor': campaignActionSuperTypeData[campaignActionTypeData[type]['type']]['iconBackgroundColor'],
      };
    }
```

This is a function of Every action 

The `Get Involved` Text is inside the Action Info Page 

![Making%20of%20NewActionSelectionItem%20527cd153fee6442eae67d7b34f0456ad/Untitled.png](Making%20of%20NewActionSelectionItem%20527cd153fee6442eae67d7b34f0456ad/Untitled.png)

![Making%20of%20NewActionSelectionItem%20527cd153fee6442eae67d7b34f0456ad/Screenshot_2020-11-06-20-27-56-218_com.nowu.app.jpg](Making%20of%20NewActionSelectionItem%20527cd153fee6442eae67d7b34f0456ad/Screenshot_2020-11-06-20-27-56-218_com.nowu.app.jpg)

And that text is gotten from 

```dart
_action.getSuperTypeName(),
```

The vertical Divider was not working until I wrapped my Row inside of `IntrinsicHeight()` Widget 

[Vertical Divider not showing](https://stackoverflow.com/questions/59960153/vertical-divider-not-showing)