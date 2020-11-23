# Starting Developement of Belnder

Get to know [how to build blender](https://wiki.blender.org/wiki/Building_Blender/Linux/Ubuntu) from source code

### How to submit work

---

so two people said different things , 

- One said to go to [https://developer.blender.org/](https://developer.blender.org/) and Use `Submit Code`
- Another person said to work locally and commit often by submitting diffs to [git.github.io/git-reference/](http://git.github.io/git-reference/)

# Building Blender

So I got the git file for blender

Then I got the developement essentials 

# Sublime Problems

---

## Clang Format

---

First and small problem is how do I get the clang format ? 

so whenever you write something , and then press `Ctrl+S` meaning you save the file , it automatically reformats your code according to the clang format 

SO for that I installed a plugin for sublime known as `Clang Format` 

and in its `clan_format.sublime-settings` I added all these things 

```bash
{
	"binary": "/usr/bin/clang-format",
	"style": "LLVM",
	**"format_on_save": true,**
}
```

But the plugin is not the only thing that I had to download , instead I also had to download a binary file , maybe a bash or something file , about clang format , and gave my path to that binary in the first line of the settings 

## Searching through Files

---

- `Ctrl+P` gives you searching of files by file names
- `Ctrl+Shift+F` lets you search files by file content

## LSP to see common syntactical errors

---

So how does this work right ? 

so you need two things for this syntactical thing to work , 

- client - The LSP plugin for Sublime Text
- server - something else that you have to run , and it depends on language , if you want to debug C++ files , then you need a C++ server , if you want to debug a python file then you need a python server

so I have installed the client , now I need to install the server 

to install the server , the official guide is this 

[https://lsp.readthedocs.io/en/latest/cplusplus/](https://lsp.readthedocs.io/en/latest/cplusplus/)

so you have to install the clangd or clang tools 9 

when I write `sudo apt install clang-tools-9` I get this 

```bash
soutrik@soutrik-HP-Laptop-15-da3xxx:~$ sudo apt install clang-tools-9
[sudo] password for soutrik: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
clang-tools-9 is already the newest version (1:9.0.1-12).
The following package was automatically installed and is no longer required:
  libfprint-2-tod1
Use 'sudo apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 46 not upgraded.
soutrik@soutrik-HP-Laptop-15-da3xxx:~$ clang-tools-9 --version
clang-tools-9: command not found
```

[this message](https://discord.com/channels/280102180189634562/645268178397560865/770194988012404757)  on discord advises to do this 

> check that clangd is installed with which clangd on the command-line (perhaps alternatively, clangd-9). Then run "Preferences: LSP Settings" the command palette, and add something like this:
// Packages/User/LSP.sublime-settings
{
"clients": {
"clangd": {
"enabled": true,
// if your binary is called clangd-9, use this as well:
// "command": ["clangd-9"]
}
}
}

![Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/Untitled.png](Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/Untitled.png)

When I type `which clangd` I dont get anything 

when I type `clangd-9 --version` I get an error 

```bash
soutrik@soutrik-HP-Laptop-15-da3xxx:~$ which clangd
soutrik@soutrik-HP-Laptop-15-da3xxx:~$ clangd-9 --version

Command 'clangd-9' not found, but can be installed with:

sudo apt install clangd-9
```

now I have already installed a lot of clangd but I dont know their names , so , I should install one more right ? so I used `sudo apt install clangd-9` , then , 

so I added this piece of code to my preference - User Settings 

```bash
{
  "clients": {
    "clangd": {
      "enabled": true,
      // if your binary is called clangd-9, use this as well:
       "command": ["clangd-9"]
    }
  }
}
```

now , if I restart the sublime text , it should work in theory 

~~but it doesnt work, if I restart , there is no sublime text at the left bottom~~

I dont know why it didnt show it at the beginning , guess it was taking its own sweet time to start up , but now its working , and showing a lot of errors

![Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/Untitled%201.png](Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/Untitled%201.png)

## file not found errors in sublime

---

for example in the `main.c`  file in `source/blender/blenderkernel/intern/main.c`  , shows the 

- following errors

    ```bash
    ◌ source/blender/blenkernel/intern/main.c:
           28:10  	clang       	error     	'MEM_guardedalloc.h' file not found
           45:1   	clang       	error     	Unknown type name 'Main'
           47:3   	clang       	error     	Use of undeclared identifier 'Main'
           47:9   	clang       	error     	Use of undeclared identifier 'bmain'
           47:17  	clang       	error     	Implicit declaration of function 'MEM_callocN' is invalid in C99
           47:36  	clang       	error     	Use of undeclared identifier 'Main'
           48:3   	clang       	error     	Use of undeclared identifier 'bmain'
           48:17  	clang       	error     	Implicit declaration of function 'MEM_mallocN' is invalid in C99
           48:36  	clang       	error     	Use of undeclared identifier 'SpinLock'
           49:3   	clang       	error     	Implicit declaration of function 'BLI_spin_init' is invalid in C99
           49:28  	clang       	error     	Expected expression
           49:18  	clang       	error     	Use of undeclared identifier 'SpinLock'
           50:10  	clang       	error     	Use of undeclared identifier 'bmain'
           53:20  	clang       	error     	Unknown type name 'Main'
           56:3   	clang       	error     	Use of undeclared identifier 'ListBase'
           56:13  	clang       	error     	Use of undeclared identifier 'lbarray'
           56:21  	clang       	error     	Use of undeclared identifier 'MAX_LIBARRAY'
           61:26  	clang       	error     	Use of undeclared identifier 'LIB_ID_FREE_NO_MAIN'
           61:48  	clang       	error     	Use of undeclared identifier 'LIB_ID_FREE_NO_UI_USER'
           62:26  	clang       	error     	Use of undeclared identifier 'LIB_ID_FREE_NO_USER_REFCOUNT'
           62:57  	clang       	error     	Use of undeclared identifier 'LIB_ID_FREE_NO_DEG_TAG'
           64:3   	clang       	error     	Implicit declaration of function 'MEM_SAFE_FREE' is invalid in C99
           66:7   	clang       	error     	Implicit declaration of function 'set_listbasepointers' is invalid in C99
           66:37  	clang       	error     	Use of undeclared identifier 'lbarray'
           68:5   	clang       	error     	Use of undeclared identifier 'ListBase'
    ```

    ![Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/Untitled%202.png](Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/Untitled%202.png)

![Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/Untitled%203.png](Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/Untitled%203.png)

this is the main.c file

But , when I try to find the `MEM_guardedalloc.h` , I do find it , its just not in the same directory 

The main.c is in `/home/soutrik/coding_projects/blender-git/blender/source/blender/blenkernel/intern/main.c` 

Whereas the `MEM_guardedalloc.h` is in `/home/soutrik/coding_projects/blender-git/blender/intern/guardedalloc/MEM_guardedalloc.h`

so its not supposed to understand it right ? Then Why does it even work ?

~~I still dont understand how or why this works~~ 

> that is because the compiler knows where it can find the the header. This is specified in source/blender/blenkernel/CMakeLists.txt in line 45 currently. -JacquesLucke

So is there a way to make the clangd server recognise it ? and also maybe autocompletion , that would be sweet .

# Files and Architecture

---

![Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/codelayout.jpg](Starting%20Developement%20of%20Belnder%20cf46789b302f4307a4fb563f61c88e5b/codelayout.jpg)

Since building is something I am going to do a lot , it might be helpful to either 

- know the commands for a manual build
- set some kind of a system so I can build stuff using sublime text shortcut

right now its , go to  ~~build linux file ,~~  go to blender in blender-git , and do these commands 

```bash
make update 
make
```

# How to go from one version to another

currently I am trying to solve this bug [https://developer.blender.org/T80313](https://developer.blender.org/T80313)

but it was reported in 2.90 , whereas my current build version is of 2.91.0 

so I want to go back in time how do I do It ? 

so the answer was to use tags 

> You are looking for a `tag` not a `branch` 🙂 `git tag` to list all then tags and the check one out using `git checkout <tag>` 🙂

## What if the version isnt tagged yet ?

> They get tag when finally released

so if its not released what will you do ? 

There are some branch , with the name `remotes/origin/blender-v2.91-release` 

## How to check on which tag you are on

```bash
 git describe --tags
```

## Build lite blender

Go to the build file and then do this 

cmake only builds the recipe , and ninja install or make install things like that actually compile 

```bash
cmake -G "Sublime Text 2 - Ninja" ../blender -C ../blender/build_files/cmake/config/blender_lite.cmake
```

and then do 

```bash
ninja install -j 1
```

but the `-j 1` isnt needed because its only a lite version , it probably wont crash like the full version 

# How to pull / fetch changes done by other people

So I downloaded the source code , but it has been quite a while , what do I do now , since other people have added some files to almost all branches , and might have even added branches 

One fool proof way is to remove the entire source code and then re clone it from the repo 

but I may need to experiment with this 

The answer is probably to `git fetch origin`  ( [see here](https://www.notion.so/soutrik/Git-8a5be488f1db45b5a8031a961ddaba50#3dff6a4505944c08b9cd3ba6148c5626) )

# Finding Suitable bugs

---

the "Good First Issue" are hard to find ( reproduce) and are mostly assigned 

rather than that I thought issues in ui are more accessible ( as in reproducable easily ) , but according to Yevgeny Makarov , the following are often easy to fix but not important 

- "Low Priority Bugs"
- "Known Issues "

some more bug are 

- [https://developer.blender.org/T81374](https://developer.blender.org/T81374)
- [https://developer.blender.org/T73179](https://developer.blender.org/T73179)