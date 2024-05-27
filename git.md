Repository
    similar to project
    `git init`

remote
    location where the repository is present
    example github/LearnPython
    https://github.com/YogeshwaranThiru/LearnPython.git
    origin is the name of the remote
    git remote add <remote name> <remote url>
    git remote add origin https://github.com/YogeshwaranThiru/LearnPython.git

to view the commit the branch
git log 

to view the files that are changed
git status

to add changes for commiting
git add <file name>

to commit files
git commit -m '<commit messsage>'

to set upstream
git push --set-upstream origin master

to pull from Github
git pull remote_name Branch_name

remote: origin
Branch: git_hub -- master(default)

<<<<<<< HEAD
to pull-request
=======
to check all braches 
git branch

to create a new branch
>>>>>>> stash workaround
git branch <branch_name>
git checkout <branch_name>

to push branch to git hub
git push --set-upstream origin <Branch_name>

from github clone the repository
git clone git@url

to merge master and branch
git merge <branch_name>
--> feature_brach create
--> goto feature_branch
--> commit create
--> goto master
--> merge with feature_branch

to delte Branch in local
git branch -D <branch_name>

to delete branch in github
git push --delete origin <branch_name>

to delete last commit
git reset --hard HEAD~1 // latest commit will delete

confict --> editor --> needed code select in options 
need to commit the file


stash -->to move uncommited change into the tray.
git stash
move from  tray to current branch
git stash pop

to get online chages to local
git fetch origin
to allign in sequnce 
git rebase origin/branch

git rebase --continue // if confilict happens needs to clear and continue with this command
--> add confict file.

to add latest changes to last commit
git commit --amend


