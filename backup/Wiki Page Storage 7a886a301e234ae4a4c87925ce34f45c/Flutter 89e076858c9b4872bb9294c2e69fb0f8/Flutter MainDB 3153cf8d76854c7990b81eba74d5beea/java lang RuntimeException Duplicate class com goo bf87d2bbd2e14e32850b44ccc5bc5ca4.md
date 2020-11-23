# java.lang.RuntimeException: Duplicate class com.google.common.util.concurrent.ListenableFuture found in modules jetified-guava-20.0.jar (com.google.guava:guava:20.0) and jetified-listenablefuture-1.0.jar (com.google.guava:listenablefuture:1.0)

Answer over [here](https://stackoverflow.com/questions/56639529/duplicate-class-com-google-common-util-concurrent-listenablefuture-found-in-modu)

The answer is to add something to the build gradle file 

 

```python
implementation 'com.google.guava:listenablefuture:9999.0-empty-to-avoid-conflict-with-guava'
```

But where is the build.gradle and shouldnt there be two of them ? Which one should I put this in ?

![java%20lang%20RuntimeException%20Duplicate%20class%20com%20goo%20bf87d2bbd2e14e32850b44ccc5bc5ca4/add_to_build_gradle.gif](java%20lang%20RuntimeException%20Duplicate%20class%20com%20goo%20bf87d2bbd2e14e32850b44ccc5bc5ca4/add_to_build_gradle.gif)