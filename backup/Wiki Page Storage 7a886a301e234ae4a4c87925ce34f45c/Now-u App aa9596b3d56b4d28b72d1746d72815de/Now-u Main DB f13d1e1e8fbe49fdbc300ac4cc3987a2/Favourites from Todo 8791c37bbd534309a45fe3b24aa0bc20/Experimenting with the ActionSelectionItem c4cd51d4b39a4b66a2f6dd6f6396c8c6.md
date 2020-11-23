# Experimenting with the ActionSelectionItem

so right now its something like this 

ActionSelectionItem

LeadingSelectionItem 

- leading widget
- and lot more stuff

For now until James approves  , I just want to add the animation of the star 

This is the full code of  the LeadingSelectionItem

```dart
**Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Padding(
          padding: EdgeInsets.symmetric(vertical: 5, horizontal: outerHpadding ?? defaultOuterHpadding),
          child: CustomTile(
              child: Stack(children: [
            Padding(
              padding: EdgeInsets.symmetric(vertical: 10, horizontal: innerHpadding ?? defaultInnerHpadding),
              child: Row(children: <Widget>[
                leading,
                SizedBox(width: 10),
                Expanded(
                  child: SelectionItem(
                      onClick: onTap,
                      child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.max, mainAxisAlignment: MainAxisAlignment.start, children: <Widget>[
                        Container(
                          height: 45,
                          width: MediaQuery.of(context).size.width -
                                  (outerHpadding ?? defaultOuterHpadding) * 2 -
                                  (innerHpadding ?? defaultInnerHpadding) * 2 -
                                  (iconWidth ?? defaultIconWidth) -
                                  10 -
                                  extraOverflow ??
                              40,
                          child: Align(
                            alignment: Alignment.centerLeft,
                            child: Text(
                              text,
                              style: textStyleFrom(
                                Theme.of(context).primaryTextTheme.bodyText1,
                                fontSize: 16,
                              ),
                              maxLines: 2,
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                        ),
                        time != null
                            ? Row(
                                mainAxisSize: MainAxisSize.max,
                                mainAxisAlignment: MainAxisAlignment.start,
                                children: <Widget>[
                                  Icon(
                                    Icons.access_time,
                                    size: 15,
                                    color: Theme.of(context).primaryColor,
                                  ),
                                  SizedBox(
                                    width: 2,
                                  ),
                                  Text(time,
                                      style: textStyleFrom(
                                        Theme.of(context).primaryTextTheme.bodyText1,
                                        fontWeight: FontWeight.w600,
                                        color: Theme.of(context).primaryColor,
                                        fontSize: 11,
                                      )),
                                ],
                              )
                            : secondaryText == null
                                ? Container()
                                : Text(secondaryText,
                                    style: textStyleFrom(
                                      Theme.of(context).primaryTextTheme.bodyText1,
                                      fontWeight: FontWeight.w600,
                                      color: Theme.of(context).primaryColor,
                                      fontSize: 11,
                                    )),
                      ])),
                )
              ]),
            ),
            // Im checking here because the value could be null
            isNew == true || isCompleted == true
                ? Positioned(
                    top: 0,
                    right: 0,
                    child: Container(
                      decoration: BoxDecoration(color: isNew ? Theme.of(context).errorColor : Color.fromRGBO(89, 152, 26, 1), borderRadius: BorderRadius.only(bottomLeft: Radius.circular(8))),
                      child: Padding(
                          padding: EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                          child: isNew
                              ? Text("New",
                                  style: textStyleFrom(
                                    Theme.of(context).primaryTextTheme.bodyText1,
                                    color: Colors.white,
                                    fontSize: 12,
                                  ))
                              // Otherwise is completed
                              : Icon(
                                  Icons.check,
                                  color: Colors.white,
                                  size: 12,
                                )),
                    ),
                  )
                : Container(),
          ]))),
    );
  }**
```

```dart
Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Padding(
          padding: EdgeInsets.symmetric(vertical: 5, horizontal: outerHpadding ?? defaultOuterHpadding),
          child: CustomTile(
              child: Stack(children: [
            Text("firstchild"),
            Padding(
						...
						)
```

![Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6/Screenshot_2020-11-03-20-52-01-455_com.nowu.app.jpg](Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6/Screenshot_2020-11-03-20-52-01-455_com.nowu.app.jpg)

This is with the first child 

![Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6/Screenshot_2020-11-03-20-54-29-269_com.nowu.app.jpg](Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6/Screenshot_2020-11-03-20-54-29-269_com.nowu.app.jpg)

This is without the first child

The leading widget inside of the `ActionSelectionItem` goes somewhere into `LeadingSelectionItem`

If I pass only a text inside the leading , I get this 

![Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6/Screenshot_2020-11-03-21-02-48-189_com.nowu.app.jpg](Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6/Screenshot_2020-11-03-21-02-48-189_com.nowu.app.jpg)

Passing a Text in the leading widget

Passing this widget inside leading widget 

```dart
Padding(
                  padding: EdgeInsets.all(5),
                  child: Container(
                    width: 60,
                    height: 60,
                    decoration:
                        BoxDecoration(borderRadius: BorderRadius.all(Radius.circular(8)), color: completed ? action.getActionIconMap()['iconColor'] : action.getActionIconMap()['iconBackgroundColor']),
                    child: Center(
                      child: Icon(
                        completed ? Icons.check : action.getActionIconMap()['icon'],
                        color: completed ? Colors.white : action.getActionIconMap()['iconColor'],
                        size: 30,
                      ),
                    ),
                  ),
                )
```

I get this 

![Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6/Screenshot_2020-11-03-21-09-28-929_com.nowu.app.jpg](Experimenting%20with%20the%20ActionSelectionItem%20c4cd51d4b39a4b66a2f6dd6f6396c8c6/Screenshot_2020-11-03-21-09-28-929_com.nowu.app.jpg)

# Conclusion 1: leading takes the icon widget ( on the left most side ) with a background