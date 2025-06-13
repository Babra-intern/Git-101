# Exercise 1 
Linus Torvalds created  github in 2005 
Git is a version control system designed to help keep track of changes in software development. It also allows developers  to work on a project simultaneously with interfering each other's work

# Exercise 2
Git is the version control system and a source code management system.It is installed and maintained in the cloud.

GitHub is a Cloud based hosting platform that incorporates git's version control features  allowing  users to manage various Git repositories

GitLab is a DevOps platform that integrates various tools(version control,issue tracking , continuous integration/deployment) and functionalities to streamline software developmennt 


# Exercise 3
 - Mercurial
 - Jenkens
 - Apache Subversion
 - Helix Core 

# Exercise 4 
- Git init creates a new git repository. It  creates a hidden directory named `(. git)` in the the project root

- Git status displays the state of the working directory. It provides the staged commit , files that are untracked and files that have changes but are not staged.

# Exercise 5 
Git commit saves the state of the project. It saves a new commit object in the local git repository.It basically takes a snapshot of your project at a specific point in time.

- "Refer to the commit image in the 'images' folder, specifically the screenshot named 'Exercise 5.'"
-![Alt text](images/Exercise5.png)



# Excersise 6 
You use the command `touch .gitignore`
edit the git ignore folder with the file you want to ignore 

# Exercise 7  
Git log is used to display the list of commit in reversed chronological order

- "Refer to the Git log image in the 'images' folder, specifically the screenshot named 'git-log'"

-![Alt text](images/git-log.PNG)

# Execise 8 
`Git add .`  - is used to add changes from the working area to the staging area 

# Exercise 9 
The staging area in Git which is also known as the index, is an intermediate area where changes are gathered before they are committed to the repository. It allows for reviews and correction to be made before final commit.

- "Refer to the commit image in the 'images' folder, specifically the screenshot named 'Staging '"
-![Alt text](images/staging.png)

# Exercise 10

`git commit -m "message" `

# Excersise 11 
`Git fetch` retrieves all changes from the remote repository to the local repository without merging them into the current branch. 
`Git pull`, fetches and automatically integrates the changes into the current working directory. Git push sends local commits to the remote repository.

# Exercise 12

`git remote show origin`

- "Refer to the image in the 'images' folder, specifically the screenshot named 'remote-show'"
-![Alt text](images/remote-show.PNG)

# Exercise 13 
rebase rewrites the commit history by taking changes from one branch and applying them onto another, creating a new base commit.

Merge combines changes from one branch into another, preserving the commit history.

# Exercise 14 
git checkout allows you to switch between branches , create new branches and even revert changes in the working directory

the alias of git checkout is git switch 

- "Refer to the image in the 'images' folder, specifically the screenshot named 'checkout'"
-![Alt text](images/Checkout.PNG)

# Exercise 15 
Git tags are references used to label specific points in the git history.

- Types of git tags 
    1. Lightweight 
    2. Annotated 


# Exercise 16

`git branch -d` , deletes a merged branch.

`git branch -D`, deletes a branch, even if unmerged

# Exercise 17 

- "Refer to the image in the 'images' folder, specifically the screenshot named 'Exercise 17'"

-![Alt text](images/rename_branch.PNG)

# Exercise 18

`git revert` creates a new commit that undoes changes made in a previous commit without removing history.
`git reset` moves the repository back to a previous commit, discarding changes if used with --hard.

# Exercise 19

(Refer to Exercise 19 in the 'images' folder that shows the branches, as well as the Git-101 folder for the  calculator.py)

-![Alt text](images/branches.PNG)

# Exercise 20

(Refer to Exercise 20 in the 'images' folder that show the results from the how to collaborate activity)

here is the link to the repo
https://github.com/Babra-intern/how-we-collaborate
