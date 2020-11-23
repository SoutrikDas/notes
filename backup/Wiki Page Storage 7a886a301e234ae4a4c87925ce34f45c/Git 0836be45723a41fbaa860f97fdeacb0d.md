# Git

Column: Nov 2, 2020 10:04 PM
Last edited by: Soutrik das
Tags: book

There are two types of VCS

- Centralised VCS
- Decentralised VCS

Now Git is a DVCS

```cpp
git pull origin master
```

updates your master branch from remote repo 

So how to update all branch from local repo?

# Branches

---

How to make one ?

```bash
git branch <branch name>
```

How to go to that branch 

```bash
git checkout <branch name>
```

How to do that together 

```bash
git checkout <branch name> -b 
```

What this does is basically make a branch first and then checkout to it .

Basically checking out means switching the head 

How to merge ?

```bash
git merge <branch name 2> 
```

What this will do is basically merge `<branch name 2>` to `<branch name 1>` where the latter is the active branch 

So the full code is 

```bash
git checkout <branch name 1>
git merge <branch name 2>
```

This basically merges `<branch name 2>` to `<branch name 1>` 

Now if the code is such , that an automatic merge is possible , thats great . But if its not , you have to solve the merge conflicts 

```bash
D:\Coding_Projects\Git rough\corvo>git merge rough
Auto-merging rough.txt
CONFLICT (content): Merge conflict in rough.txt
Automatic merge failed; fix conflicts and then commit the result.
```

![Git%200836be45723a41fbaa860f97fdeacb0d/solved_the_conflict.gif](Git%200836be45723a41fbaa860f97fdeacb0d/solved_the_conflict.gif)

## Delete a branch

```bash
git branch <branch name> -d
```

The `-d` tag is for delete 

# So what to do to download all the branches ?

# Stash basically reverts your branch to the factory state ( when you created it)

and then later on if you want you can pop those changes back

# what to do if you want to push a branch thats not in remote

So you just do `git push` and git will tell you to make some changes to make that branch 

Suppose this is the condition , You have two branches in remote repo , and three in local 

![Git%200836be45723a41fbaa860f97fdeacb0d/branches_.gif](Git%200836be45723a41fbaa860f97fdeacb0d/branches_.gif)

Then what do you do ?

You use `--set-upstream` short `-u` 

```dart
git push -u origin <branch>
```

Where origin is not a branch , but your remote repo 

![Git%200836be45723a41fbaa860f97fdeacb0d/make_a_new_branch.gif](Git%200836be45723a41fbaa860f97fdeacb0d/make_a_new_branch.gif)

# How to clone and put the git file in the current directory

---

so whenever you clone , suppose in Dir `A` , git makes a new folder inside `A`  with the name `<repo-name>` and all the cool stuff is inside it . But what if we wanted all the cool stuff inside `A` ?

This is the most general command

```dart
git clone <repository> <path>
```

So the repo is basically the link , and the path is where you want the clone to be , but normally we dont give anything .

```dart
git clone <repo> .
```

The dot represents the current path

But it somehow gives me this error 

```dart
fatal: destination path '.' already exists and is not an empty directory.
```

That my current directory is not empty ,Can I bypass it ?

One answer was to git clone into an empty directory and then copy stuff from the old directory 

Another answer was to git init , and then link it up with remote 

I am going to link it up with remote 

```dart
git init .
git remote add -t \* -f origin <repository-url>
git checkout master
```

But the second line is almost same as 

```dart
git remote add origin <repo-link.git>
```

But its giving me this error 

```dart
fatal: invalid refspec '+refs/heads/\*:refs/remotes/origin/\*'
```

To solve it I went to [this](https://stackoverflow.com/questions/32064360/git-remote-command-returns-fatal-invalid-refspec-refs-heads-refs-remotes-or)

And the solution was to change 

```dart
fatal: invalid refspec '+refs/heads/\*:refs/remotes/origin/\*'
```

To 

```dart
fatal: invalid refspec '+refs/heads/*:refs/remotes/origin/*'
```

That was all 

# src refspec master does not match any

---

Check the [second answer](https://stackoverflow.com/questions/4181861/message-src-refspec-master-does-not-match-any-when-pushing-commits-in-git) , it is to use 

```dart
git push origin HEAD:master
```

# How to download new branch and tags from remote ?

so `git pull` helps you to update the current branch to the latest work done in remote repo , but `git fetch origin` helps you get all new branches 

[Learn Git from Scratch - Fetch and Pull from Origin](https://www.youtube.com/watch?v=q6rYglziOjM)