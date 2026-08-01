🌏 Languages: [English](README.md) | [한국어](README(한글_가이드).md)

---

# What This Document Is

This is a reproducible, step-by-step writeup of the whole process:
Claude (AI) cloned the `Videos_log` repository in its own working
directory, replaced team members' real names with role labels
(on a `Final` branch), handed the branch over as a `.bundle` file,
and then the user used that file to actually push the `Final`
branch to GitHub.

It's split into two parts:

- **PART 1** — What Claude did in its own working directory (reproducible)
- **PART 2** — What the user did on their own computer (what actually landed on GitHub)

---

# PART 1. What Claude Did in Its Working Directory

[#part-1-what-claude-did-in-its-working-directory](#part-1-what-claude-did-in-its-working-directory)

## 1-1. Clone the original repository

```
git clone https://github.com/seongbin45/Videos_log.git
cd Videos_log
```

## 1-2. Make Korean filenames display correctly

By default, `git ls-files`, `git status`, etc. show Korean filenames
as octal escapes like `\354\230\201...`. This setting turns that off.

```
git config core.quotepath false
```

## 1-3. Create a working branch

```
git checkout -b Final
```

## 1-4. Survey what needs to be replaced (name → role label)

Before changing anything, I first checked exactly which names
appeared where, and how many times.

```
grep -rl "박다현\|조은선\|조용민\|정성훈\|최성빈" . --exclude-dir=.git
grep -rn "박다현" . --exclude-dir=.git          # no results (actually written as "김다현" in the repo)
grep -rln "김다현" . --exclude-dir=.git
grep -rlnE "daehyun|eunsun|yongmin|seonghun|sungbin" . --exclude-dir=.git   # romanized anchor ids
```

I also checked for any other personal information (phone numbers,
emails, student IDs, etc.). None found.

```
grep -rnoE "01[0-9]-?[0-9]{3,4}-?[0-9]{4}" . --exclude-dir=.git
grep -rnoE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" . --exclude-dir=.git
```

## 1-5. Run the actual replacement script

I saved and ran the following Python script exactly as-is.
(Why binary mode `rb`/`wb`: the files used Windows-style line
endings (`\r\n`). Reading/writing in plain text mode would have
silently converted every line ending to `\n`, which made the diff
look far bigger than the actual change.)

```python
import subprocess, os

files = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.splitlines()
binary_ext = {'.png', '.jpg', '.jpeg', '.webp', '.zip', '.pdf', '.gif', '.ico'}

name_map = {
    "김다현": "팀장",
    "조은선": "팀원1",
    "조용민": "팀원2",
    "정성훈": "팀원3",
    "최성빈": "팀원4",
}
id_map = {
    "daehyun": "leader",
    "eunsun": "member1",
    "yongmin": "member2",
    "seonghun": "member3",
    "sungbin": "member4",
}

changed = []
for f in files:
    ext = os.path.splitext(f)[1].lower()
    if ext in binary_ext:
        continue
    if not os.path.isfile(f):
        continue
    with open(f, "rb") as fh:
        raw = fh.read()
    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError:
        continue
    orig = content
    for k, v in name_map.items():
        content = content.replace(k, v)
    for k, v in id_map.items():
        content = content.replace(k, v)
    if content != orig:
        with open(f, "wb") as fh:
            fh.write(content.encode("utf-8"))
        changed.append(f)

print("Changed files:")
for c in changed:
    print(" -", c)
```

The following 5 files were changed as a result:

```
3조 팀원별 제작 업무 가이드_index.html
Docs/영상제작과정보고서_3조.html
files/초안_(또_다른_프로젝트)/(draft, 미사용)_scene1_flag_ceremony_team_guide.html
files/초안_(또_다른_프로젝트)/(draft, 미사용)_scene2_military_training_team_guide.html
차이나는_퀄리티_팀원_작업_분배표_index.html
```

## 1-6. Re-verify nothing was left over

```
grep -rn "김다현\|조은선\|조용민\|정성훈\|최성빈\|daehyun\|eunsun\|yongmin\|seonghun\|sungbin" . --exclude-dir=.git
```
→ If nothing prints, it passed.

## 1-7. Visually check the diff + manually clean up awkward duplication

Since the script does plain string replacement, in a few spots
the word "팀장" (team lead) was already sitting right next to where
a name got replaced with "팀장," producing a duplicate like
`팀장 (팀장)`. I checked these one by one with `git diff` and
cleaned them up manually.

```
git diff --stat
git diff "Docs/영상제작과정보고서_3조.html"
git diff "3조 팀원별 제작 업무 가이드_index.html"
git diff "차이나는_퀄리티_팀원_작업_분배표_index.html"
```

Example: `<li><strong>팀장 (팀장)</strong>: ...` → `<li><strong>팀장</strong>: ...`
(direct string edits, two spots per file)

## 1-8. Commit

```
git add -A
git commit -m "Replace team members' real names with role labels (de-identification)

- 김다현 -> 팀장 (Team Lead)
- 조은선 -> 팀원1 (Member 1)
- 조용민 -> 팀원2 (Member 2)
- 정성훈 -> 팀원3 (Member 3)
- 최성빈 -> 팀원4 (Member 4)
- Also changed romanized anchor ids (daehyun/eunsun/yongmin/seonghun/sungbin) to leader/member1-4"
```

## 1-9. Tried to push directly to GitHub → failed, no credentials

```
git push origin Final
```
→ `fatal: could not read Username for 'https://github.com'`
(Claude's working environment has no access to the user's GitHub
login credentials, so a direct push isn't possible from here.
That's why I handed the branch over as a `.bundle` file instead —
see step 1-10.)

## 1-10. Create and verify the `.bundle` file

```
git bundle create videos_log_final.bundle Final
git bundle verify videos_log_final.bundle
```

The resulting `videos_log_final.bundle` file was the single file
handed over to the user.

---

# PART 2. What the User Did on Their Own Computer (Actual GitHub Push)

[#part-2-what-the-user-did-on-their-own-computer](#part-2-what-the-user-did-on-their-own-computer)

## 2-1. Get the repo via `git clone`, not a ZIP download

A folder downloaded via GitHub's "Download ZIP" has no `.git`
folder, so git commands won't work at all in it. It must be
cloned properly, like this:

```
git clone https://github.com/seongbin45/Videos_log.git
cd Videos_log
```

## 2-2. Put the received bundle file inside the cloned folder

Copy `videos_log_final.bundle` **into** the `Videos_log` folder you
just cloned. (If it's in a different folder, the next command
won't be able to find it.)

## 2-3. Register the bundle file as a temporary remote

```
git remote add claude-bundle videos_log_final.bundle
```

## 2-4. Fetch the Final branch out of the bundle into your local repo

```
git fetch claude-bundle Final:Final
```

## 2-5. Push the local Final branch to the real GitHub repo

```
git push origin Final
```

## 2-6. Clean up the temporary remote when done

```
git remote remove claude-bundle
```

---

# Note 1: Recreating or updating the `.bundle` file

[#note-1-recreating-or-updating-the-bundle-file](#note-1-recreating-or-updating-the-bundle-file)

A `.bundle` file isn't something you edit directly — it's a
snapshot of a set of commits at a given point in time. To change
its contents:

1. Make more changes on the `Final` branch and commit them
2. Re-run `git bundle create [same_filename].bundle Final`
   → this overwrites the existing file with the latest commits.

# Note 2: Changing the default branch of a GitHub repository

[#note-2-changing-the-default-branch-of-a-github-repository](#note-2-changing-the-default-branch-of-a-github-repository)

This isn't done with a command — it's done on the GitHub website.

1. Go to the repository page → **Settings**
2. In the left sidebar, click **Branches**
3. Next to "Default branch," click the pencil icon → select the
   branch you want → **Update**
4. When the confirmation prompt appears, click
   **I understand, update the default branch.**

---

# 👨‍💻 Let me know if you get stuck anywhere:

[#let-me-know-if-you-get-stuck-anywhere](#let-me-know-if-you-get-stuck-anywhere)

Developed by

https://github.com/seongbin45
