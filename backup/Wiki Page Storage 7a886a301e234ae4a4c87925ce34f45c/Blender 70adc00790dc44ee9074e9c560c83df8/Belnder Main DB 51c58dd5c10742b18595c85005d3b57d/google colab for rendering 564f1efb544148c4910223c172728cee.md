# google colab for rendering

so , I wanted to render the animation of the golden sphere procedural texture that I saw from polyfordj , youtube channel , but my laptop took so much time to even render just one animation 

so I thout if I can leverage the google gpus and cpus 

So I want to test a few things 

- how fast is their cpu compared to mine for rendering image
- how fast is their gpu compared to their cpu and my cpu for rendering image ,
- how fast is their gpu compared to nothing for rendering an animation
- the limitations of this method

so I have saved my blender file with correct things 

- camera is ok
- render output is 1920 x 1080
- ~~render output is a ffmpeg video  of encoding MP4~~  render output is PNG
- **blend file has gpu enabled**

so the concept  is to install blender on the virtual machine and then use those machines to render out stuff , 

for this we need to somehow give that virtual machine our blend file ,

and we can do so by putting our blend file in our drive , and then using an api to get it into the VM

![google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/create_a_folder_for_blender_files.gif](google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/create_a_folder_for_blender_files.gif)

then upload the file in there

Execute the [codelab](https://colab.research.google.com/drive/1-2bO65rxXYRzvcmWv20OLDByBr5u4OP9#scrollTo=QRzNmiHN8Xr0) cells sequentially ( first install blender ) 

Then mount your gdrive ( google drive , using the authentication code ) 

Then choose the file path 

![google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/add_the_correct_path.gif](google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/add_the_correct_path.gif)

you caN BROWSE   the VM's files using this 

![google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/browse_files_and_even_copy_path.gif](google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/browse_files_and_even_copy_path.gif)

But now my problem is with the final command for rendering multiple frames 

```dart
!sudo ./blender/blender -P setgpu.py 
-b '/gdrive/My Drive/BlenderFolder/proceduralfirst.blend' 
-o '/gdrive/My Drive/BlenderFolder/proceduralfirst/V.png'
 **-s 1 -e 10** -a
```

first of all , this is one command , I just broke it into pieces to make myself understand 

- so the code in blue is to set the start and ending frames ,

this page has almost all commands 

[Command Line Arguments - Blender Manual](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)

- The `-a` is for rendering animations

![google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled.png](google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled.png)

- the `-P` is to run a python script

![google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled%201.png](google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled%201.png)

- `-b` is used for UI less rendering

![google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled%202.png](google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled%202.png)

now the idea of the `V.png` name of the output is that when the first notebook renders the first filename ,it will give that file a name of `v0001.png` probably , so doing this , you will get all the pngs in  one folder , then maybe use ffmpeg to create a video from png [using ffmpeg](https://stackoverflow.com/questions/24961127/how-to-create-a-video-from-images-with-ffmpeg)

## Problem: cant find blender command

![google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled%203.png](google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled%203.png)

it cant find `./blender/blender` path or binary , what do i do 

so finally it works , but there were a lot of other problems , but I got the animation 
after you get all the images , select all of them and download them , Then Use ffmpeg command to join them 

```dart
ffmpeg -framerate 24 -i secondtry%04d.png output.mp4
```

where %04d means how many digits of variable numbers are there 

![google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled%204.png](google%20colab%20for%20rendering%20564f1efb544148c4910223c172728cee/Untitled%204.png)

for my case there were 4 digits of variable numbers , 

remember to set the output to `<path>/<filename without png>` ie `<path>/secondtry`

then it will generate `secondtry0001.png` by itself depending on the blendfile probably