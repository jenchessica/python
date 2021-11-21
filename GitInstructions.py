# The absolute path is: C:\Users\Jessica\AppData\Local\Programs\Git

Jessica@SarahV MINGW64 /
$ cd python/

Jessica@SarahV MINGW64 /python (master)
$ pwd
/python

Jessica@SarahV MINGW64 /python (master)
$ git add NumberGuessing.py

Jessica@SarahV MINGW64 /python (master)
$ git add GitInstructions.py

Jessica@SarahV MINGW64 /python (master)

$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   GitInstructions.py
        new file:   NumberGuessing.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/

Jessica@SarahV MINGW64 /python (master)
$ git commit
[master 8f0bd58] Wow my coding skills are pretty weird ahahaha
 2 files changed, 21 insertions(+)
 create mode 100644 GitInstructions.py
 create mode 100644 NumberGuessing.py

Jessica@SarahV MINGW64 /python (master)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 589 bytes | 589.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jenchessica/python.git
   474b363..8f0bd58  master -> master

Jessica@SarahV MINGW64 /python (master)
