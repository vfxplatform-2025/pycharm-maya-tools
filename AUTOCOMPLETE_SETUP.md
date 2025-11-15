# Maya 자동완성 설정 가이드

PyCharm에서 Maya Python API의 자동완성을 활성화하는 가이드입니다.

## 📋 목차

1. [개요](#1-개요)
2. [Stub 파일이란?](#2-stub-파일이란)
3. [설치](#3-설치)
4. [PyCharm 설정](#4-pycharm-설정)
5. [테스트](#5-테스트)
6. [트러블슈팅](#6-트러블슈팅)

---

## 1. 개요

Maya Python API는 동적으로 생성되는 모듈이 많아 PyCharm에서 자동완성이 제대로 작동하지 않습니다.

**문제점:**
```python
import maya.cmds as cmds
cmds.  # ← 자동완성이 안 나타남
```

**해결책:**
- `.pyi` stub 파일 사용
- PyCharm에게 Maya API의 타입 정보 제공
- 코드 작성 속도 향상 및 오타 방지

---

## 2. Stub 파일이란?

**Stub 파일 (.pyi)**:
- Python 모듈의 타입 정보만 담은 파일
- 실제 구현은 없고 함수/클래스 시그니처만 정의
- IDE가 자동완성에 사용

**예시:**
```python
# maya/cmds/__init__.pyi
def polySphere(
    name: str = ...,
    radius: float = ...,
    subdivisionsX: int = ...,
    subdivisionsY: int = ...
) -> list[str]: ...
```

---

## 3. 설치

### 3-1. 자동 설치 (권장)

`install.sh` 스크립트가 자동으로 stubs를 설치합니다:

```bash
bash install.sh
```

설치 위치:
```
~/.pycharm_tools/
└── stubs/
    └── maya/
        ├── __init__.pyi
        ├── cmds/__init__.pyi
        ├── api/__init__.pyi
        ├── OpenMaya.pyi
        └── ...
```

### 3-2. 수동 설치

```bash
# stubs 디렉토리 복사
cp -r stubs ~/.pycharm_tools/
```

---

## 4. PyCharm 설정

### 4-1. Settings 열기

**방법 1:** `Ctrl+Alt+S`
**방법 2:** `File > Settings`

### 4-2. Python Interpreter 설정

```
Settings
└── Project: [your_project]
    └── Python Interpreter
```

### 4-3. Show All 클릭

Python Interpreter 옆의 **톱니바퀴 아이콘** 클릭 → **Show All...**

### 4-4. Interpreter Paths 편집

1. 현재 사용 중인 인터프리터 선택
2. 하단의 **폴더 트리 아이콘** (Show paths for the selected interpreter) 클릭
3. **`+`** 버튼 클릭
4. 다음 경로 추가:
   ```
   /home/m83/.pycharm_tools/stubs
   ```
   ⚠️ **중요:** `m83`을 본인의 사용자명으로 변경

5. **OK** 클릭
6. **Apply** → **OK**

---

## 5. 테스트

### 5-1. 자동완성 테스트

PyCharm에서 새 Python 파일 생성:

```python
import maya.cmds as cmds

# cmds. 입력 후 Ctrl+Space
cmds.poly  # ← 자동완성 목록이 나타나야 함

# 함수 시그니처 확인 (Ctrl+P)
cmds.polySphere(  # ← 파라미터 힌트가 나타나야 함
```

**예상 결과:**
- `cmds.polySphere` 입력 시 자동완성 제안
- 파라미터 이름과 타입 힌트 표시
- 함수 docstring 표시 (Ctrl+Q)

### 5-2. OpenMaya API 테스트

```python
from maya import OpenMaya as om

# om. 입력 후 자동완성
om.MVector  # ← 자동완성되어야 함
om.MDagPath  # ← 자동완성되어야 함
```

### 5-3. Maya API 2.0 테스트

```python
from maya.api import OpenMaya as om2

# om2. 입력 후 자동완성
om2.MVector  # ← 자동완성되어야 함
om2.MFnMesh  # ← 자동완성되어야 함
```

---

## 6. 트러블슈팅

### 6-1. 자동완성이 여전히 안 나타남

**원인:** PyCharm 인덱싱이 완료되지 않음

**해결:**
1. `File > Invalidate Caches...`
2. **Invalidate and Restart** 클릭
3. PyCharm 재시작 대기
4. 인덱싱 완료 대기 (하단 상태바 확인)

---

### 6-2. "Cannot find reference" 경고

**증상:**
```python
import maya.cmds as cmds  # ← "No module named 'maya'" 경고
```

**원인:** 정상입니다. Stub 파일은 타입 정보만 제공합니다.

**설명:**
- 경고는 무시해도 됩니다
- 실행은 External Tools (F5)를 통해 Maya에서 하므로 문제없음
- 자동완성은 정상 작동합니다

**경고 숨기기 (선택):**
```python
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
```

---

### 6-3. Stub 경로가 추가되지 않음

**증상:** Interpreter Paths에서 경로 추가가 안 됨

**해결:**
1. 경로가 실제로 존재하는지 확인:
   ```bash
   ls -la ~/.pycharm_tools/stubs/
   ```

2. 절대 경로 사용:
   ```
   /home/m83/.pycharm_tools/stubs  (O)
   ~/.pycharm_tools/stubs          (X)
   ```

3. PyCharm 재시작

---

### 6-4. mayapy 실행 시 stub import 에러

**증상:**
```
ImportError: cannot import name 'cmds' from 'maya'
```

**원인:** mayapy가 stub 디렉토리를 실제 모듈로 인식

**해결:**

**방법 1: PYTHONPATH에서 제외 (권장)**
```bash
# ~/.bashrc 또는 ~/.zshrc
# PyCharm용 stubs는 PYTHONPATH에 추가하지 않음
```

**방법 2: run_with_mayapy.sh 수정**
```bash
#!/bin/bash
# stubs 경로 제외
export PYTHONPATH="${PYTHONPATH//:\/home\/m83\/.pycharm_tools\/stubs/}"
/usr/autodesk/maya2025/bin/mayapy "$@"
```

---

### 6-5. 일부 함수만 자동완성됨

**원인:** Stub 파일이 불완전함

**설명:**
- 제공된 stub은 가장 자주 사용되는 API만 포함
- Maya 전체 API를 커버하지는 않음

**해결:**
- 필요한 함수를 stub 파일에 직접 추가 가능
- 또는 공식 Maya stub 패키지 사용:
  ```bash
  pip install mayapy-stubs
  ```

---

## 7. Stub 파일 구조

```
~/.pycharm_tools/stubs/
└── maya/
    ├── __init__.pyi           # maya 모듈
    ├── standalone.pyi          # maya.standalone
    ├── utils.pyi               # maya.utils
    ├── cmds/
    │   └── __init__.pyi       # maya.cmds (가장 중요)
    ├── api/
    │   ├── __init__.pyi       # maya.api
    │   ├── OpenMaya.pyi       # Maya API 2.0
    │   ├── OpenMayaAnim.pyi
    │   ├── OpenMayaRender.pyi
    │   └── OpenMayaUI.pyi
    ├── OpenMaya.pyi           # Maya API 1.0
    ├── OpenMayaAnim.pyi
    ├── OpenMayaFX.pyi
    ├── OpenMayaMPx.pyi
    ├── OpenMayaRender.pyi
    └── OpenMayaUI.pyi
```

---

## 8. 추가 자동완성 개선

### 8-1. Type Hints 사용

```python
import maya.cmds as cmds
from typing import List, Optional

def create_spheres(count: int) -> List[str]:
    """Create multiple spheres"""
    result: List[str] = []
    for i in range(count):
        sphere = cmds.polySphere(name=f"sphere_{i}", radius=1.0)[0]
        result.append(sphere)
    return result
```

### 8-2. Docstring 작성

```python
def move_to_origin(obj: str) -> None:
    """Move object to world origin

    Args:
        obj: Maya object name
    """
    import maya.cmds as cmds
    cmds.move(0, 0, 0, obj, absolute=True)
```

---

## 9. 정리

### ✅ 완료 체크리스트

- [ ] stubs 디렉토리 설치 (`~/.pycharm_tools/stubs/`)
- [ ] PyCharm Interpreter Paths에 경로 추가
- [ ] PyCharm 재시작 및 인덱싱 대기
- [ ] `maya.cmds` 자동완성 테스트
- [ ] `maya.OpenMaya` 자동완성 테스트
- [ ] `maya.api` 자동완성 테스트

### 📖 추가 참고

- **README.md** - 전체 개요 및 사용법
- **PYCHARM_SETUP.md** - External Tools 설정
- **AUTOCOMPLETE_SETUP.md** - 이 문서

---

**설정 완료!** 🎉

이제 PyCharm에서 Maya API 자동완성이 작동합니다!
