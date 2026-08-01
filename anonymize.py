#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
anonymize.py

폴더 안의 텍스트 파일들에서, 사용자가 지정한 이름/개인정보 문자열을
원하는 값으로 한 번에 치환해주는 간단한 도구입니다.

실행 방법:
    python anonymize.py

파이썬만 설치되어 있으면 별도 설치(pip install) 없이 바로 실행됩니다.
"""

import os
import sys

# 치환하지 않을 파일 확장자 (이미지/압축/문서 등 바이너리 파일)
BINARY_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".bmp",
    ".zip", ".rar", ".7z", ".pdf", ".exe", ".dll",
    ".mp3", ".mp4", ".mov", ".wav",
}

# 이 도구 자신, 그리고 git 관련 폴더는 건드리지 않음
SKIP_DIRS = {".git", "__pycache__", "node_modules"}


def ask_folder():
    """치환을 적용할 폴더 경로를 입력받는다."""
    while True:
        path = input("치환할 파일들이 들어있는 폴더 경로를 입력하세요: ").strip().strip('"')
        if not path:
            print("  -> 경로를 입력해주세요.\n")
            continue
        if not os.path.isdir(path):
            print(f"  -> '{path}' 폴더를 찾을 수 없습니다. 다시 입력해주세요.\n")
            continue
        return path


def ask_replacements():
    """
    '실제 값 -> 바꿀 값' 쌍을 반복해서 입력받는다.
    빈 값을 입력하면 입력을 종료한다.
    """
    print("\n이제 바꾸고 싶은 이름/개인정보를 입력하세요.")
    print("예: 실제 이름을 입력하면, 어떤 값으로 바꿀지 물어봅니다.")
    print("더 이상 추가할 게 없으면 아무것도 입력하지 않고 Enter를 누르세요.\n")

    pairs = {}
    count = 1
    while True:
        original = input(f"[{count}] 바꾸고 싶은 원래 값 (예: 홍길동, 010-1234-5678): ").strip()
        if original == "":
            break
        replacement = input(f"[{count}] 무엇으로 바꿀까요? (예: 팀원1, ***-****-****): ").strip()
        if replacement == "":
            print("  -> 바꿀 값이 비어 있어서 이 항목은 건너뜁니다.\n")
            continue
        pairs[original] = replacement
        count += 1
        print()

    return pairs


def collect_target_files(folder):
    """폴더 안의 (바이너리가 아닌) 모든 파일 경로를 모은다."""
    targets = []
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if ext in BINARY_EXTENSIONS:
                continue
            targets.append(os.path.join(root, name))
    return targets


def apply_replacements(filepath, pairs):
    """
    한 파일에 치환을 적용한다.
    - 바이너리 모드(rb/wb)로 읽고 써서 원래 줄바꿈(\\n / \\r\\n)을 그대로 보존한다.
    - UTF-8로 디코딩되지 않는 파일(진짜 바이너리)은 건너뛴다.
    - 실제로 뭔가 바뀐 경우에만 True를 반환한다.
    """
    try:
        with open(filepath, "rb") as f:
            raw = f.read()
        content = raw.decode("utf-8")
    except UnicodeDecodeError:
        return False

    original = content
    for old, new in pairs.items():
        content = content.replace(old, new)

    if content != original:
        with open(filepath, "wb") as f:
            f.write(content.encode("utf-8"))
        return True
    return False


def main():
    print("=" * 50)
    print(" 이름/개인정보 일괄 치환 도구")
    print("=" * 50)

    folder = ask_folder()
    pairs = ask_replacements()

    if not pairs:
        print("\n치환할 항목이 없어서 종료합니다.")
        return

    print("\n다음 내용으로 치환을 진행합니다:")
    for old, new in pairs.items():
        print(f"  '{old}'  ->  '{new}'")

    confirm = input("\n정말 진행할까요? (y/n): ").strip().lower()
    if confirm != "y":
        print("취소했습니다.")
        return

    files = collect_target_files(folder)
    changed_files = []

    for filepath in files:
        if apply_replacements(filepath, pairs):
            changed_files.append(filepath)

    print("\n" + "=" * 50)
    if changed_files:
        print(f"완료! 총 {len(changed_files)}개 파일이 바뀌었습니다:")
        for f in changed_files:
            print(f"  - {f}")
    else:
        print("바뀐 파일이 없습니다. 입력한 값이 파일 안에 없는지 확인해보세요.")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n중단되었습니다.")
        sys.exit(1)
