# TOOLS *********************************************************************
# content = assignment
#
# deliver = Upload the files to your git repository
#           and share it in the assignment submission form.
#
# date    = 2024-03-13
# email   = contact@alexanderrichtertd.com
#***************************************************************************
"""



NOTE: Give yourself the time to play around with the tools,
      make sure everything works properly and note down your questions for our Q&A.




#******************************************************************************
# 11. ADVANCED SCRIPT EDITOR
#******************************************************************************
Let's explore and advance in our use of the script editor:

    a) Install and try one unfamiliar but promising script editor
       that you will use through out the masterclass:

        * Sublime Text 3
        * Visual Studio Code
        * PyCharm
        * ATOM
        * VIM
        * ...


    b) Check out the settings and plugins and add these or more:
        * user settings
        * git
        * spell check
        * color theme
        * ...


    c) USE a few new shortcuts


    d) ADD one helpful snippet and use it through out the masterclass


    e) SHARE in the Discord/python-advanced group:

        * Which script editor did you use previously and what was your experience?
        * Which script editor you try for this masterclass?



NOTE: Nothing to upload in this task.









#******************************************************************************
# 12. SHELL
#******************************************************************************
1) Do the following steps only using a shell:

    a) Create the directory "shell_test"

md E:\Users\Zakkyo\Desktop\class\advanced\1\shell_test

    b) Create the file "test_print.py" with a simple print into the directory

md E:\Users\Zakkyo\Desktop\class\advanced\1\shell_test\test_print.py

    c) Rename the file to "new_test_print.py"

ren E:\Users\Zakkyo\Desktop\class\advanced\1\shell_test\test_print.py E:\Users\Zakkyo\Desktop\class\advanced\1\shell_test\new_test_print.py


    d) List what is in the directory "shell_test" including their file permissions
cd E:\Users\Zakkyo\Desktop\class\advanced\1\shell_test
dir

    e) Execute the Python file and call the simple print
type E:\Users\Zakkyo\Desktop\class\advanced\1\shell_test\new_test_print.py

    f) Remove the directory "shell_test" with its content
del E:\Users\Zakkyo\Desktop\class\advanced\1\shell_test

    BONUS: Solve the tasks without looking them up.












2) CREATE a custom .bat or .sh that does the following:

    a) STARTS a DCC of your choice (Maya, 3ds Max, Nuke, Houdini, ...)
start "C:\ProgramFiles\Autodesk\Maya2024\bin\maya.exe"

    b) ADDS custom script paths
set "C:\ProgramFiles\Autodesk\Maya2024\scripts\"

    c) ADDITIONAL overwrites (paths, menus, ...)


    d) Make sure everything works as intended










#******************************************************************************
# 13. GIT
#******************************************************************************

1) STUDY git example
-----------------------------------------------------------
Before we start to work with git let's make sure to get familiar with the workflow
and how a git project should look like.
Browse through the folders and Wiki of my Open Source Pipeline Plex
which also serves as a code and documentation example throughout this masterclass:

    a) EXPLORE the Plex git repository and look into the code:
    https://github.com/alexanderrichtertd/plex


    b) READ the Wiki to understand the basics of the pipeline:
    https://github.com/alexanderrichtertd/plex/wiki












2) CREATE an assignment repository
-----------------------------------------------------------
All the upcoming assignments must be uploaded to your git repository.
Use the git shell for the following tasks:

    a) Create a new repository for the assignments on GitHub/GitLab/... with the sub folders:
        * 0_app (for your application)
        * 1_tools
        * 2_style
        * 3_advanced
        * 4_ui

       NOTE: If you use sensitive (company) data make your repository private.
             Invite me using alexanderrichtertd@gmail.com (GitHub)
             (Keep the resources out of your repository.)


    b) ADD a README.mb file describing your application.


    c) ADD and fill out a .ignore file (must ignore all .pyc files)


    d) ADD, commit and push your first application script(s) remote into "01_app" directory.

    IMPORTANT: In future assignments make sure to commit and push the original version
               before starting with the assignment so we have a before and after.
               The commit message must be: INIT 1_tools / 2_style / 3_advanced / 4_UI
               And: DONE 1_tools / 2_style / 3_advanced / 4_UI.


    e) MAKE changes, commit and push again


    f) CREATE a branch "develop", make small changes and push it remote


    g) MERGE your develop changes into master


    h) TEST and clone your remote repository into another directory (as if you are a user).




3) SUBMIT ASSIGNMENT your git link here:
https://www.alexanderrichtertd.com/pa-tools
"""
