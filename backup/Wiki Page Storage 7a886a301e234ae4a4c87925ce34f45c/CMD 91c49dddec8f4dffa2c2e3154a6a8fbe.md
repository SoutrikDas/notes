# CMD

Column: Nov 17, 2020 3:27 PM
Last edited by: Soutrik das

Tutorials are [here](http://steve-jansen.github.io/guides/windows-batch-scripting/part-1-getting-started.html) 

# Batch Files

---

A batch file is a script file in DOS or OS/2 and microsoft windows

File extensions 

- `.dat` - old and causes some problems
- `.cmd` - modern

Try to avoid spaces in file names as spaces create headaches in scripting 

Pascal casing your filenames is an easy way to avoid spaces (e.g., `HelloWorld.cmd` instead of `Hello World.cmd`)

Things to ocnsider with names 

- Avoid ames of built in commands , system binaries or popular programs

## Running your Batch Files

---

Ways to run a batch file 

- Double click open - But this is used for batch files that are tested and finished
- Drag and drop into already open cmd prompt - Used to debug and edit

## Add Comments

---

The official way is to use `REM` at the beginning of the comment 

```bash
REM this is a comment 
```

A workaround or hack is to use `::`  ( the power operator `:` twice ) because its almost always ignored ( `FOR` loops error out )

```bash
:: this is almost always a comment 
```

So the ways to write a comment is 

- `REM`
- `::`

## Debugging your Script

---

- There is no debugger
- make custom error statements using `echo`

# Scripting

---

THe first line is usually to turn ECHO OFF 

`@ECHO OFF` 

After execution of batch files , the system turns on the ECHo by default 

You can turn on the ECHO by `ECHO ON` 

It basically stops the cmd , to print (echo)  every line of our batch file 

## Variables

---

### Variable Declaration

---

DOS does not require declaration of variables. The value of undeclared/uninitialized variables is an empty string, or "". Most people like this, as it reduces the amount of code to write. 

### Variable Assignment

---

The `SET` command assigns a value to a variable 

```bash
SET foo=bar
:: the above works 
SET foo = bar 
:: this doesnt work
```

Do not use whitespace between the name and value; `SET foo = bar` will not work but `SET foo=bar` will work.

If you want to do arithmatic operations during assignments like `SET foo=2+2` then you have use `/A` switch 

```bash
SET /A foo=2+2
```

### Variable Naming Conventions

---

- use lowercase name for script variables (Camel for the batch file name ) as environmental variables have all upper case
- DOS is case insensitive
- to check if you are not overwriting a variable , use `ECHO %foo%` if the print statement has something , then its an environmental variable

### Reading the value of a variable

---

```bash
C:\> SET foo=bar
C:\> ECHO %foo%
bar
```

- prefixing and postfixing variable with `%` ( in some cases it doesnt work )

### List Existing Variables

---

- `SET` without anything else will give the list of all variables

```bash
C:\Users\Soutrik>SET
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\Soutrik\AppData\Roaming
CommonProgramFiles=C:\Program Files\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=DESKTOP-3M2SSRC
ComSpec=C:\Windows\system32\cmd.exe
DriverData=C:\Windows\System32\Drivers\DriverData
foo=hello
fooo=hell
FPS_BROWSER_APP_PROFILE_STRING=Internet Explorer
FPS_BROWSER_USER_PROFILE_STRING=Default
GIT_LFS_PATH=C:\Program Files\Git LFS
HOMEDRIVE=C:
HOMEPATH=\Users\Soutrik
LOCALAPPDATA=C:\Users\Soutrik\AppData\Local
LOGONSERVER=\\DESKTOP-3M2SSRC
MOZ_PLUGIN_PATH=C:\Program Files (x86)\Foxit Software\Foxit Reader\plugins\
NUMBER_OF_PROCESSORS=8
OneDrive=C:\Users\Soutrik\OneDrive
OS=Windows_NT
Path=C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;
C:\Windows\system32;C:\Windows;
C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;
C:\Windows\System32\OpenSSH\;C:\Program Files\Git\cmd;
C:\src\flutter\bin;C:\Program Files (x86)\Avogadro\bin;
D:\Videos;C:\Program Files\nodejs\;C:\Program Files\Git LFS;
C:\Users\Soutrik\AppData\Local\Programs\Python\Python38-32\Scripts\;
C:\Users\Soutrik\AppData\Local\Programs\Python\Python38-32\;
C:\Users\Soutrik\AppData\Local\Microsoft\WindowsApps;
C:\Users\Soutrik\AppData\Local\Programs\MiKTeX 2.9\miktex\bin\x64\;
C:\Users\Soutrik\AppData\Local\Programs\Microsoft VS Code\bin;
C:\Users\Soutrik\AppData\Roaming\npm;C:\Users\Soutrik\AppData\Local\GitHubDesktop\bin
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
PROCESSOR_ARCHITECTURE=AMD64
PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 126 Stepping 5, GenuineIntel
PROCESSOR_LEVEL=6
PROCESSOR_REVISION=7e05
ProgramData=C:\ProgramData
ProgramFiles=C:\Program Files
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
PROMPT=$P$G
PSModulePath=C:\Program Files\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules
PUBLIC=C:\Users\Public
SESSIONNAME=Console
SystemDrive=C:
SystemRoot=C:\Windows
TEMP=C:\Users\Soutrik\AppData\Local\Temp
TMP=C:\Users\Soutrik\AppData\Local\Temp
USERDOMAIN=DESKTOP-3M2SSRC
USERDOMAIN_ROAMINGPROFILE=DESKTOP-3M2SSRC
USERNAME=Soutrik
USERPROFILE=C:\Users\Soutrik
windir=C:\Windows
```

# Make Directory with cmd

---

```python
mkdir <dir name>
```

```python

```

Run `dir /a` to view a list of all files in the directory and their attributes.

The `dir /a`  command gives an output like this 

```python
Volume in drive D is DATA
 Volume Serial Number is 18CE-95C9

 Directory of D:\

29-09-2020  17:43    <DIR>          $RECYCLE.BIN
17-07-2020  20:56    <DIR>          .freedownloadmanager
02-10-2020  11:28    <DIR>          Coding_Projects
03-10-2020  22:34    <DIR>          Documents
03-10-2020  19:11    <DIR>          Downloads
26-06-2020  14:57        64,756,120 Godot_v3.2.2-stable_win64.exe
06-09-2020  07:31    <DIR>          Heavy Softwares
08-09-2020  20:44    <DIR>          Heavy Softwares [Rar]
16-07-2020  23:38    <DIR>          hp 16 gb Dads Pendrive
21-09-2020  11:51    <DIR>          msdownld.tmp
25-09-2020  07:59    <DIR>          Music
25-08-2020  19:13    <DIR>          Notion Export
09-08-2020  18:58    <DIR>          Phone Download Dump[9.8.20]
03-10-2020  06:12    <DIR>          Pictures
04-10-2020  17:49    <DIR>          portable applications
21-09-2020  11:42    <DIR>          ProgramFiles(temp)
17-07-2020  21:45    <DIR>          Sync Folder
17-07-2020  13:33    <DIR>          System Volume Information
03-09-2020  14:33    <DIR>          Textures
02-10-2020  11:55    <DIR>          Videos
               1 File(s)     64,756,120 bytes
              19 Dir(s)  789,414,477,824 bytes free
```

## Remove a folder using `rmdir /s <folder name>`

---

If your folder has a space , its best to use 

```python
rmdir /s "My Folder"
```

## Make a file without any text

---

```python
type nul > hello.txt
```

Delete it with 

```python
del hello.txt
```

![CMD%2091c49dddec8f4dffa2c2e3154a6a8fbe/createanddeleteafile.gif](CMD%2091c49dddec8f4dffa2c2e3154a6a8fbe/createanddeleteafile.gif)

### Create file with a little bit of text

---

```python
echo typetexthere > helloworld.txt
```

![CMD%2091c49dddec8f4dffa2c2e3154a6a8fbe/createfilewithtext.gif](CMD%2091c49dddec8f4dffa2c2e3154a6a8fbe/createfilewithtext.gif)

# For Looping in cmd

---

```python
for /l %i in (1,1,100) do (type nul>h%i.txt) 
REM will create 100 files "h1.txt" "h2.txt" .... "h3.txt"
```

The `/l` is used to increment i everytime 

![CMD%2091c49dddec8f4dffa2c2e3154a6a8fbe/Untitled.png](CMD%2091c49dddec8f4dffa2c2e3154a6a8fbe/Untitled.png)

and the `(1,1,100)` is like `(start, increment , end )`

When referencing For loop variable within a batch file you need to double up the percent signs (ie: `%%a`), but if you do this when just running the command straight at the prompt it won't work. You need to change them to a single percent sign (`%a`).

![CMD%2091c49dddec8f4dffa2c2e3154a6a8fbe/createanddeletemutliplefiles.gif](CMD%2091c49dddec8f4dffa2c2e3154a6a8fbe/createanddeletemutliplefiles.gif)

# cd

- Go back one directory using `cd ..`
- Go back two directory using `cd ../..`
- Go back $n$ directory using $\boxed{\text{cd } {..}/../../.. \dots \text{n times}}$
- Go to `D` drive by using `D:` or `d:`

## open file explorer from cmd

---

Instead of primarily using file explorer and then typing out cmd to access cmd of that path , I thought of primarily using cmd to navigate and only when I need to use the file explorer of that path I will open the file explorer

and to do that the command is `start <path>` 

## open video file from cmd

---

`vlc <path to video file>`