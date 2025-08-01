### Detailed videos on working with Git and GitHub:
1. [Git Tutorial for Beginners by Telusko](https://www.youtube.com/playlist?list=PLsyeobzWxl7q2eaUkorLZExfd7qko9sZC)
2. [Tutorials by Simplilearn](https://youtube.com/playlist?list=PLEiEAq2VkUUJs7lyLgSsRlnd9syrFBzSM)

### git commands to setup in your local pc:
```
git config --global user.name "<github_username>"
git config --global user.email "<github_email>"
```

### useful and needed git commands:
```
git clone https://github.com/saikrishnavadali05/SSSSO-RR-District-Basic-Python-Training-June-2022.git
git config --get remote.origin.url
git config –global user.name "[name]"
git config –global user.email "[email address]"
git add [file]
git add *
git commit -m "[ Type in the commit message]"
git commit -a
git diff
git diff –staged
git diff [first branch] [second branch]
git reset [file]
git reset [commit]
git reset –hard [commit]
git status
git rm [file]
git log
git push origin develop
```

### Folders to be created with id_name 
1. folder_name : ```vadali_sai_krishna```.
2. Everyday learning progress to be pushed onto github.
3. ```initial_full_name``` folder for each contributor should be visible in the repo.
4. Every folder should contain :
   * Code files with Outputs (in Comments)
   * special notes prepared for yourself
   * Problem Solving (new folder to be created).
   * Python learning (new folder to be created).
   * Improved and practice python files

> In the intial stages you can do your work on the master branch and a pull request can be put to merge your work into the python training repo.

### Steps to push your entire work onto develop branch (not master) as you gain some knowledge in git
1. First clone the repo into your local system with the command in step 2
2. ```git clone <repo link>```
3. create a branch called develop in local with the command in step 4
4. ```git branch develop```
5. checkout to the new branch that you created with the command in step 6
6. ```git checkout develop```
7. make code changes and then add the new folder with command in point 8
8. ```git add foldername```
9. commit your changes locally first with the command in point 10
10. ```git commit -m "commit_message"```
11. push the entire code onto develop branch with the command in point 12
12. ```git push origin develop```
