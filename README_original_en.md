This is the process for creating a new repository on GitHub and uploading an entire folder to it.

---

# Step 1: Create a Repository on the GitHub Website

   1. Log in to GitHub (Github.com).
   2. Click the **+** button in the top right corner and select **New repository**.
   3. Enter `CODYSSEY_2_ProJect` for the repository name.
   4. Leave the other settings (README, .gitignore, etc.) unchecked, and click **Create repository** at the bottom.
   5. Copy the repository address (in the form `https://github.com/...`) shown in the address bar.

---

# Step 2: Enter Commands in Your Computer's Terminal
Open a terminal (Git Bash or CMD) inside the folder you want to upload,
and in the command below, paste your own copied address into the part
that says "[paste_the_copied_github_repository_address_here]" before running it.
(We already copied the GitHub link back in "Step 1: Create a Repository on the GitHub Website".)

## 0. Remove any incorrectly linked remote from before
~~~
git remote remove origin
~~~

## 1. Initialize the current folder as a git repository
~~~
git init
~~~

## 2. Stage all files in the folder for upload

~~~
git add .
~~~

## 3. Create a save-point record

~~~
git commit -m "put_your_text_here_between_the_quotation_marks"
~~~

>git commit -m "you_can_write_whatever_you_want_as_the_title_between_the_quotation_marks"

## 4. Rename the default branch to main

~~~
git branch -M main
~~~

## 5. Connect your computer to the GitHub repository

~~~
git remote add origin
~~~

>git remote add origin [paste_the_copied_github_repository_address_here]

## 6. Send the final files to GitHub (log in if a login window appears)

~~~
git push -u origin main
~~~

------------------------------

# 👨‍💻 Let me know if you get stuck anywhere:

Developed by

 [https://github.com/seongbin45](https://github.com/seongbin45)

------------------------------
