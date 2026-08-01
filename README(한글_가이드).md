# 이 문서는 무엇인가

Claude(AI)가 자기 쪽 작업 디렉터리에서 `Videos_log` 저장소를 클론해서
팀원 실명을 역할명으로 바꾸고(`Final` 브랜치), `.bundle` 파일로 넘겨준 뒤,
사용자가 그 파일을 이용해 실제 GitHub에 `Final` 브랜치를 올린
전체 과정을 순서대로, 재현 가능하게 정리한 것입니다.

크게 두 부분으로 나뉩니다.

- **PART 1** — Claude가 자기 작업 디렉터리에서 한 일 (재현용)
- **PART 2** — 사용자가 자기 컴퓨터에서 한 일 (실제로 GitHub에 반영한 부분)

---

# PART 1. Claude 작업 디렉터리에서 한 일

[#part-1-claude-작업-디렉터리에서-한-일](#part-1-claude-작업-디렉터리에서-한-일)

## 1-1. 원본 저장소 클론

```
git clone https://github.com/seongbin45/Videos_log.git
cd Videos_log
```

## 1-2. 한글 파일명이 깨져 보이지 않도록 설정

기본 설정에서는 `git ls-files`, `git status` 등에서 한글 파일명이
`\354\230\201...` 같은 8진수 escape로 표시됩니다. 아래 설정으로 풀어줍니다.

```
git config core.quotepath false
```

## 1-3. 작업용 브랜치 생성

```
git checkout -b Final
```

## 1-4. 이름 → 역할명 치환 대상 사전 조사

바꾸기 전에, 실제로 어떤 이름이 어디에 몇 번 등장하는지 먼저 확인했습니다.

```
grep -rl "박다현\|조은선\|조용민\|정성훈\|최성빈" . --exclude-dir=.git
grep -rn "박다현" . --exclude-dir=.git          # 결과 없음 (실제로는 "김다현"으로 표기됨)
grep -rln "김다현" . --exclude-dir=.git
grep -rlnE "daehyun|eunsun|yongmin|seonghun|sungbin" . --exclude-dir=.git   # 로마자 anchor id
```

개인정보(전화번호/이메일/학번 등)가 더 있는지도 확인했습니다. (결과 없음)

```
grep -rnoE "01[0-9]-?[0-9]{3,4}-?[0-9]{4}" . --exclude-dir=.git
grep -rnoE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" . --exclude-dir=.git
```

## 1-5. 실제 치환 스크립트 실행

아래 파이썬 스크립트를 그대로 저장해서 실행했습니다.
(`rb`/`wb` 바이너리 모드로 읽고 쓴 이유: 파일이 Windows 방식 줄바꿈(`\r\n`)으로
되어 있어서, 일반 텍스트 모드로 읽고 쓰면 줄바꿈이 전부 `\n`으로 바뀌어
버려서 diff가 실제 변경보다 훨씬 크게 나오는 문제가 있었습니다.)

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

print("변경된 파일:")
for c in changed:
    print(" -", c)
```

실행 결과, 아래 5개 파일이 바뀌었습니다.

```
3조 팀원별 제작 업무 가이드_index.html
Docs/영상제작과정보고서_3조.html
files/초안_(또_다른_프로젝트)/(draft, 미사용)_scene1_flag_ceremony_team_guide.html
files/초안_(또_다른_프로젝트)/(draft, 미사용)_scene2_military_training_team_guide.html
차이나는_퀄리티_팀원_작업_분배표_index.html
```

## 1-6. 치환이 남김없이 됐는지 재검증

```
grep -rn "김다현\|조은선\|조용민\|정성훈\|최성빈\|daehyun\|eunsun\|yongmin\|seonghun\|sungbin" . --exclude-dir=.git
```
→ 아무것도 안 나오면 통과.

## 1-7. diff 육안 확인 + 어색한 중복 표현 수동 정리

스크립트가 단순 문자열 치환이다 보니, 원문에 이미 "팀장"이라는 단어가
있던 자리에 이름이 "팀장"으로 바뀌면서 `팀장 (팀장)`처럼 중복되는
곳이 몇 군데 생겼습니다. 이런 곳은 `git diff`로 하나하나 확인하면서
수동으로 정리했습니다.

```
git diff --stat
git diff "Docs/영상제작과정보고서_3조.html"
git diff "3조 팀원별 제작 업무 가이드_index.html"
git diff "차이나는_퀄리티_팀원_작업_분배표_index.html"
```

예: `<li><strong>팀장 (팀장)</strong>: ...` → `<li><strong>팀장</strong>: ...`
(에디터로 직접 문자열 치환, 파일마다 2곳)

## 1-8. 커밋

```
git add -A
git commit -m "팀원 실명을 역할명으로 대체 (개인정보 비식별화)

- 김다현 -> 팀장
- 조은선 -> 팀원1
- 조용민 -> 팀원2
- 정성훈 -> 팀원3
- 최성빈 -> 팀원4
- 로마자 anchor id(daehyun/eunsun/yongmin/seonghun/sungbin)도 leader/member1-4로 변경"
```

## 1-9. GitHub에 직접 push 시도 → 인증 정보 없어서 실패

```
git push origin Final
```
→ `fatal: could not read Username for 'https://github.com'`
(Claude 쪽 작업 환경에는 사용자의 GitHub 로그인 정보가 없기 때문에,
여기서는 직접 push가 불가능합니다. 그래서 아래 1-10처럼 `.bundle`
파일로 대신 전달했습니다.)

## 1-10. `.bundle` 파일 생성 및 검증

```
git bundle create videos_log_final.bundle Final
git bundle verify videos_log_final.bundle
```

이렇게 만들어진 `videos_log_final.bundle` 파일 하나를 사용자에게 전달했습니다.

---

# PART 2. 사용자가 자기 컴퓨터에서 한 일 (실제 GitHub 반영)

[#part-2-사용자가-자기-컴퓨터에서-한-일-실제-github-반영](#part-2-사용자가-자기-컴퓨터에서-한-일-실제-github-반영)

## 2-1. 저장소를 ZIP이 아니라 `git clone`으로 받기

GitHub "Download ZIP"으로 받은 폴더는 `.git`이 없어서 git 명령어가
전혀 먹히지 않습니다. 반드시 아래처럼 clone해야 합니다.

```
git clone https://github.com/seongbin45/Videos_log.git
cd Videos_log
```

## 2-2. 전달받은 bundle 파일을 클론한 폴더 안에 넣기

`videos_log_final.bundle` 파일을 방금 클론한 `Videos_log` 폴더
**안에** 복사해 넣습니다. (다른 폴더에 있으면 다음 명령어가 못 찾습니다.)

## 2-3. bundle 파일을 임시 원격 저장소로 등록

```
git remote add claude-bundle videos_log_final.bundle
```

## 2-4. bundle 안의 Final 브랜치를 내 로컬로 가져오기

```
git fetch claude-bundle Final:Final
```

## 2-5. 로컬의 Final 브랜치를 진짜 GitHub로 push

```
git push origin Final
```

## 2-6. 다 쓴 임시 원격 정리

```
git remote remove claude-bundle
```

---

# 참고 1: `.bundle` 파일을 다시 만들거나 수정하고 싶을 때

[#참고-1-bundle-파일을-다시-만들거나-수정하고-싶을-때](#참고-1-bundle-파일을-다시-만들거나-수정하고-싶을-때)

`.bundle`은 직접 편집하는 파일이 아니라 특정 시점 커밋들을 통째로
압축한 스냅샷입니다. 내용을 바꾸려면:

1. `Final` 브랜치에서 코드를 다시 수정하고 새로 커밋
2. `git bundle create [같은_파일명].bundle Final` 을 다시 실행
   → 기존 파일이 최신 커밋 내용으로 덮어써집니다.

# 참고 2: GitHub 저장소의 기본(default) 브랜치를 바꾸고 싶을 때

[#참고-2-github-저장소의-기본default-브랜치를-바꾸고-싶을-때](#참고-2-github-저장소의-기본default-브랜치를-바꾸고-싶을-때)

명령어가 아니라 GitHub 웹사이트에서 처리합니다.

1. 저장소 페이지 → **Settings**
2. 왼쪽 메뉴 **Branches**
3. "Default branch" 옆 연필 아이콘 클릭 → 원하는 브랜치 선택 → **Update**
4. 확인 문구가 뜨면 **I understand, update the default branch.** 클릭

---

# 👨‍💻 막히는 부분이 있다면 알려주세요:

[#‍-막히는-부분이-있다면-알려주세요](#‍-막히는-부분이-있다면-알려주세요)

Developed by

https://github.com/seongbin45
