Claude(AI)가 로컬에서 작업한 브랜치를 bundle 파일로 넘겨주고,
그걸 내 컴퓨터의 진짜 git 저장소로 가져와서 GitHub에 올리는 과정입니다.

---

# -1단계: (참고) .bundle 파일은 어떻게 만드는가

[#-1단계-참고-bundle-파일은-어떻게-만드는가](#-1단계-참고-bundle-파일은-어떻게-만드는가)

이번 작업에서는 Claude(AI)가 자기 쪽 작업 폴더에서 `Final` 브랜치를
만들고 커밋한 뒤, 아래 명령어로 `.bundle` 파일을 뽑아서 전달했습니다.
직접 만들 일이 없어도, 원리를 알아두면 나중에 다른 사람과
git 원격 저장소 없이 브랜치를 주고받을 때 쓸 수 있습니다.

**생성 (커밋이 이미 끝난 상태에서 실행)**

```
git bundle create [저장할_파일명].bundle [브랜치명]
```

> git bundle create videos_log_final.bundle Final

**검증 (파일이 제대로 만들어졌는지 확인)**

```
git bundle verify [파일명].bundle
```

> git bundle verify videos_log_final.bundle

**수정하고 싶을 때**

`.bundle` 파일은 직접 편집하는 파일이 아니라, 특정 시점의 커밋들을
통째로 압축해놓은 스냅샷입니다. 내용을 바꾸려면:

1. 원본 브랜치(`Final`)에서 코드를 다시 수정하고 새로 커밋
2. 위 `git bundle create` 명령어를 **같은 파일명으로 다시 실행** →
   기존 파일이 최신 커밋 내용으로 덮어써집니다.

---

# 0단계: 폴더가 진짜 git 저장소인지 확인하기

[#0단계-폴더가-진짜-git-저장소인지-확인하기](#0단계-폴더가-진짜-git-저장소인지-확인하기)

GitHub에서 "Download ZIP"으로 받은 폴더는 `.git` 폴더가 없어서
git 명령어가 전혀 먹히지 않습니다. 반드시 `git clone`으로 받은 폴더에서 작업해야 합니다.

```
git clone [깃허브_저장소_주소]
```

> git clone https://github.com/seongbin45/Videos_log.git

클론이 끝나면 그 폴더 안으로 이동합니다.

```
cd [클론된_폴더명]
```

---

# 1단계: 받은 bundle 파일을 원격 저장소처럼 등록하기

[#1단계-받은-bundle-파일을-원격-저장소처럼-등록하기](#1단계-받은-bundle-파일을-원격-저장소처럼-등록하기)

`.bundle` 파일은 git 커밋 기록이 통째로 들어있는 파일입니다.
이 파일을 "원격 저장소"인 것처럼 내 로컬 git에 등록합니다.

**중요:** 이 명령어는 `.bundle` 파일이 실제로 들어있는 폴더(클론한 저장소 폴더 안)에서 실행해야 합니다.

```
git remote add claude-bundle [bundle_파일명]
```

> git remote add claude-bundle videos_log_final.bundle

---

# 2단계: bundle 안에 있는 브랜치를 내 로컬로 가져오기

[#2단계-bundle-안에-있는-브랜치를-내-로컬로-가져오기](#2단계-bundle-안에-있는-브랜치를-내-로컬로-가져오기)

`claude-bundle`이라는 원격에서 `Final`이라는 브랜치를 가져와서,
내 로컬에도 `Final`이라는 이름으로 만듭니다.

```
git fetch claude-bundle [원격_브랜치명]:[로컬_브랜치명]
```

> git fetch claude-bundle Final:Final

---

# 3단계: 가져온 브랜치를 진짜 GitHub로 올리기

[#3단계-가져온-브랜치를-진짜-github로-올리기](#3단계-가져온-브랜치를-진짜-github로-올리기)

```
git push origin [브랜치명]
```

> git push origin Final

이 명령어를 실행하면 GitHub 저장소에 `Final`이라는 새 브랜치가 생깁니다.

---

# 4단계: 임시로 등록했던 bundle 원격 정리하기

[#4단계-임시로-등록했던-bundle-원격-정리하기](#4단계-임시로-등록했던-bundle-원격-정리하기)

더 이상 필요 없는 `claude-bundle` 원격 연결을 삭제해서 깔끔하게 정리합니다.
(GitHub에 올라간 `Final` 브랜치는 그대로 남아있습니다.)

```
git remote remove claude-bundle
```

---

# 참고: GitHub 저장소의 기본(default) 브랜치를 바꾸고 싶을 때

[#참고-github-저장소의-기본default-브랜치를-바꾸고-싶을-때](#참고-github-저장소의-기본default-브랜치를-바꾸고-싶을-때)

방문했을 때 기본으로 보여지는 브랜치만 바꾸고 싶다면 (main은 그대로 남음),
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
