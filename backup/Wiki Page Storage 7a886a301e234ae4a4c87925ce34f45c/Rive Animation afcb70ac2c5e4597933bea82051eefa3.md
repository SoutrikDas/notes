# Rive Animation

Column: Nov 5, 2020 8:21 AM
Last edited by: Soutrik das

For support of rive2 , the best place to ask question is not discord , its not reddit , its gmail 

![Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/Untitled.png](Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/Untitled.png)

So all of the question that you want to ask , ask it there 

# Basics

## Center something

![Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/center_something.gif](Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/center_something.gif)

## Make a Straight line with Pen Tool

![Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/make_a_straight_line_with_pen_tool.gif](Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/make_a_straight_line_with_pen_tool.gif)

## Change Stroke

![Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/increase_stroke_and_round_corner.gif](Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/increase_stroke_and_round_corner.gif)

## How to Duplicate ?

`Ctrl+J` 

## Trim Path

![Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/trim_path_sequential_vs_sync.gif](Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/trim_path_sequential_vs_sync.gif)

Sync v/s Sequential

# Putting Rive animation in flutter

## Export from Rive

![Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/export_from_rive.gif](Rive%20Animation%20afcb70ac2c5e4597933bea82051eefa3/export_from_rive.gif)

Now add this into the assets ( via `pubspec.yaml` )

![https://i.ibb.co/YXL4V27/adding-as-asset.gif](https://i.ibb.co/YXL4V27/adding-as-asset.gif)

you cannot add flr with the `rive` flutter package 

right now only  rive1 gives out `.flr` and rive2 gives out `.riv` , which means go the beta rive2 project 

So I have been having problems with the rive2 , but I finally got a hold of their [blogs](https://blog.rive.app/) , and [one of them](https://blog.rive.app/rives-flutter-runtime-part-1/) helped me finally do one succesful run of animation 

and the code goes like this 

 

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:rive/rive.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Rive Flutter Demo',
      home: Scaffold(
        body: MyRiveAnimation(),
      ),
    );
  }
}

class MyRiveAnimation extends StatefulWidget {
  @override
  _MyRiveAnimationState createState() => _MyRiveAnimationState();
}

class _MyRiveAnimationState extends State<MyRiveAnimation> {
  final riveFileName = '**lib/asset/off_road_car_blog_0_6.riv**';
  Artboard _artboard;

  @override
  void initState() {
    _loadRiveFile();
    super.initState();
  }

  // loads a Rive file
  void _loadRiveFile() async {
    final bytes = await rootBundle.load(riveFileName);
    final file = RiveFile();

    if (file.import(bytes)) {
      // Select an animation by its name
      setState(() => _artboard = file.mainArtboard
        ..addController(
          SimpleAnimation('idle'),
        ));
    }
  }

  /// Show the rive file, when loaded
  @override
  Widget build(BuildContext context) {
    return _artboard != null
        ? Rive(
            artboard: _artboard,
            fit: BoxFit.cover,
          )
        : Container();
  }
}
```

So there are a few parts to using rive 

```dart
void _loadRiveFile() async {
    final bytes = await rootBundle.load(riveFileName);
    final file = RiveFile();

    if (file.import(bytes)) {
      // Select an animation by its name
      setState(() => _artboard = file.mainArtboard
        ..addController(
          SimpleAnimation('idle'),
        ));
    }
  }
```

this function is used in the `initState` ( ie before the build function )