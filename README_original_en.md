🌏 Languages: [한국어](README.md) | [English](README_original_en.md)

---

This is the process of creating a new repository on GitHub and uploading an entire folder.

<details>
<summary><b>Step 0: Set your Git user info (only once on this computer)</b></summary>

---

Git stores "who left this record" together with every commit. Without the user info setting, it stops at commit (step 3) with the error `Please tell me who you are.`
~~~
git config --global user.name 
~~~
~~~
git config --global user.email 
~~~

>ex)  
>git config --global user.name "your_english_name_or_github_username"  
>git config --global user.email "the_email_you_signed_up_to_github_with"  

<details>
<summary><b>How to check whether it is set</b></summary>
   
~~~
git config --global --list
~~~

</details>

<details>
<summary><b>Setting your user info is not an actual login process.</b></summary> 

```
* This step is not an actual login. GitHub account authentication is handled separately at step 6, git push.
* If the email you write here differs from your GitHub sign-up email, your commits will not be linked to your profile (GitHub account).  
* The email embedded in a commit remains in a public repository permanently.  
* To hide your personal email, use the 12345678+username@users.noreply.github.com address from GitHub Settings → Emails.  
* On a school or shared computer, drop --global and run the command inside that folder only.
```

</details>

</details>

---

# Step 1: Create a repository on the GitHub website

   1. Sign in to GitHub (Github.com).
   2. Click the + button in the top right and select `New repository`.
   3. Type whatever word comes to mind right now into `Repository name`.
   4. Leave the other settings (README, .gitignore, etc.) unchecked and empty, and click `Create repository` at the bottom.
   5. Copy the repository address in the https://github.com form shown in the address bar.

---

# Step 2: Enter the commands in your computer's terminal
Open a terminal (Git Bash or CMD) inside the folder you want to upload,    

and in the `"the_place_between_the_double_quotes"` part of the commands below, write whatever word comes to mind inside the quotation marks.  
(You may leave the content of "the_place_between_the_double_quotes" empty, as long as you keep the quotation marks.)    

And in `[paste_the_copied_github_repository_address_here]`, paste the address you copied yourself and run it.  
(We already copied the GitHub link back in 'Step 1: Create a repository on the GitHub website'.)  

## 0. Remove an existing, incorrectly linked command (linked address)
~~~
git remote remove origin
~~~

## 1. Initialize the current folder as a Git repository
~~~
git init
~~~

## 2. Add all files in the folder to the waiting state for upload

~~~
git add .
~~~

## 3. Create a save-point record

~~~
git commit -m
~~~

>ex)  
>git commit -m "in_the_place_between_the_double_quotes_you_may_write_anything_you_want_as_the_title."  

## 4. Change the default branch name to main

~~~
git branch -M main
~~~

## 5. Connect your computer to the GitHub repository

~~~
git remote add origin
~~~

>ex)  
>git remote add origin [paste_the_copied_github_repository_address_here]  

## 6. Send the final files to GitHub (log in if a login window appears)

~~~
git push -u origin main
~~~

------------------------------

# 👨‍💻 Let me know if there is anything you get stuck on:

Developed by

 [https://github.com/seongbin45](https://github.com/seongbin45)

------------------------------
