# PyCharm 설정 가이드

PyCharm에서 Maya Tools를 사용하기 위한 완전한 설정 가이드입니다.

## 📋 목차

1. [External Tools 등록](#1-external-tools-등록)
2. [단축키 설정](#2-단축키-설정)
3. [테스트](#3-테스트)
4. [트러블슈팅](#4-트러블슈팅)

---

## 1. External Tools 등록

### 1-1. Settings 열기

**방법 1:** `Ctrl+Alt+S`
**방법 2:** `File > Settings`

### 1-2. External Tools 메뉴로 이동

```
Settings
└── Tools
    └── External Tools  ← 여기로 이동
```

### 1-3. Tool 추가

오른쪽 상단의 **`+`** 버튼 클릭

---

### Tool 1: Run in Maya (Maya GUI 연동)

**Edit Tool 창에서 다음과 같이 입력:**

#### 기본 정보
- **Name:** `Run in Maya`
- **Description:** `Send code to running Maya GUI (port 7002)`
- **Group:** `External Tools` (기본값)

#### Tool Settings
- **Program:**
  ```
  /usr/bin/python3
  ```

- **Arguments:**
  ```
  /home/$USER/.pycharm_tools/run_in_maya.py $FilePath$
  ```

  ⚠️ **중요:** `$USER`를 실제 사용자명으로 변경
  예: `/home/m83/.pycharm_tools/run_in_maya.py $FilePath$`

- **Working directory:**
  ```
  $FileDir$
  ```

#### Advanced Options (펼치기)
- ☑ **Synchronize files after execution**
- ☑ **Open console for tool output**
- ☑ **Make console active on message in stdout**
- ☑ **Make console active on message in stderr**

**하단 `OK` 클릭**

---

### Tool 2: Run with mayapy (Standalone)

**다시 `+` 버튼 클릭**

#### 기본 정보
- **Name:** `Run with mayapy`
- **Description:** `Execute script with mayapy standalone`
- **Group:** `External Tools`

#### Tool Settings
- **Program:**
  ```
  /home/$USER/.pycharm_tools/run_with_mayapy.sh
  ```

  ⚠️ **중요:** `$USER`를 실제 사용자명으로 변경
  예: `/home/m83/.pycharm_tools/run_with_mayapy.sh`

- **Arguments:**
  ```
  $FilePath$
  ```

- **Working directory:**
  ```
  $FileDir$
  ```

#### Advanced Options
- ☑ **Synchronize files after execution**
- ☑ **Open console for tool output**
- ☑ **Make console active on message in stdout**
- ☑ **Make console active on message in stderr**

**하단 `OK` 클릭**

---

### 1-4. 설정 저장

- **Apply** 클릭
- **OK** 클릭

---

## 2. 단축키 설정

### 2-1. Keymap 설정 열기

**Settings (`Ctrl+Alt+S`) > Keymap**

### 2-2. External Tools 검색

검색창에 입력:
```
External Tools
```

### 2-3. Run in Maya 단축키 설정

1. `Run in Maya` 항목을 **한 번 클릭** (선택)
2. **우클릭** 또는 오른쪽 **`+`** 아이콘 클릭
3. **`Add Keyboard Shortcut`** 선택
4. 팝업창에서 키 입력:
   ```
   F5
   ```
5. 충돌 경고가 나올 경우:
   - **`Remove`** 선택 (기존 F5 기능 제거)
   - F5는 원래 파일 복사 기능이지만 거의 사용하지 않음
6. **OK** 클릭

### 2-4. Run with mayapy 단축키 설정

1. `Run with mayapy` 항목 **한 번 클릭**
2. **우클릭** > `Add Keyboard Shortcut`
3. 키 입력:
   ```
   Shift+F5
   ```
4. **OK** 클릭

### 2-5. 저장

- **Apply** 클릭
- **OK** 클릭

---

## 3. 테스트

### 3-1. mayapy Standalone 테스트 (Maya 실행 불필요)

1. PyCharm에서 `test_mayapy_standalone.py` 파일 열기
   경로: `~/.pycharm_tools/test_mayapy_standalone.py`

2. **실행 방법 3가지:**
   - **우클릭** > `External Tools` > `Run with mayapy`
   - 단축키: `Shift+F5`
   - 상단 메뉴: `Tools > External Tools > Run with mayapy`

3. **예상 결과 (PyCharm 콘솔):**
   ```
   ==================================================
   mayapy Standalone Test
   ==================================================
   ✓ Maya standalone initialized
   Maya Version: 2025
   ✓ Created cube: test_cube
   ✓ Created sphere: test_sphere
   ✓ Scene saved to: /tmp/pycharm_maya_test.ma
   ==================================================
   ```

---

### 3-2. Maya GUI 연결 테스트 (Maya 실행 필요)

#### 준비 단계

**1. Maya 실행:**
```bash
m25_v  # 또는 Maya GUI 직접 실행
```

**2. Maya Script Editor에서 Command Port 열기:**

`Windows > General Editors > Script Editor`

Python 탭에서 다음 코드 실행:
```python
import maya.cmds as cmds
cmds.commandPort(name=':7002', sourceType='python')
print("✓ Command port opened on :7002")
```

**확인:**
```python
# 포트가 열렸는지 확인
cmds.commandPort(':7002', query=True)  # True 나와야 함
```

#### 테스트 실행

1. PyCharm에서 `test_maya_connection.py` 열기
   경로: `~/.pycharm_tools/test_maya_connection.py`

2. **실행:**
   - 우클릭 > `External Tools` > `Run in Maya`
   - 또는 단축키: `F5`

3. **예상 결과:**

   **PyCharm 콘솔:**
   ```
   Sending test_maya_connection.py to Maya...
   ✓ Code sent to Maya on port 7002
   ```

   **Maya Script Editor:**
   ```
   ==================================================
   Maya Connection Test
   ==================================================
   Maya Version: 2025
   Current Scene: Untitled
   Total Objects in Scene: 8
   ✓ Created sphere: pycharm_test_sphere
   ✓ Moved sphere to (0, 5, 0)
   ✓ Applied red shader
   ==================================================
   Test Complete!
   ==================================================
   ```

   **Maya Viewport:**
   - 빨간색 구체가 Y축 5 위치에 생성됨

---

## 4. 트러블슈팅

### 4-1. External Tools 메뉴에 항목이 안 보임

**원인:** 설정이 저장되지 않음

**해결:**
1. `Settings > Tools > External Tools` 재확인
2. Tool 이름이 정확한지 확인
3. PyCharm 재시작

---

### 4-2. 단축키가 작동하지 않음

**원인 1:** Keymap 설정이 저장되지 않음

**해결:**
1. `Settings > Keymap` 확인
2. `External Tools` 검색
3. `Run in Maya`에 F5가 등록되어 있는지 확인
4. PyCharm 재시작

**원인 2:** 다른 플러그인과 충돌

**해결:**
1. `Settings > Keymap`
2. 검색창에 `F5` 입력
3. 다른 기능에 F5가 할당되어 있는지 확인
4. 충돌하는 기능의 단축키 제거

---

### 4-3. "can't open file" 에러

**증상:**
```
/usr/bin/python3: can't open file '$UserHome$/.pycharm_tools/run_in_maya.py'
```

**원인:** PyCharm 변수가 치환되지 않음

**해결:**
1. `Settings > Tools > External Tools > Run in Maya > Edit`
2. Arguments를 절대 경로로 변경:
   ```
   /home/m83/.pycharm_tools/run_in_maya.py $FilePath$
   ```
3. `$USER`나 `$UserHome$` 같은 변수 대신 실제 경로 사용

---

### 4-4. "Connection refused" 에러

**증상:**
```
✗ Error: Maya is not running or command port is not open.
```

**원인:** Maya command port가 열리지 않음

**해결:**

**1. Maya가 실행 중인지 확인**

**2. Command Port 다시 열기:**
```python
# Maya Script Editor에서
import maya.cmds as cmds
cmds.commandPort(name=':7002', sourceType='python')
```

**3. 포트 확인:**
```python
# True가 나와야 함
cmds.commandPort(':7002', query=True)
```

**4. 다른 포트가 열려있는지 확인:**
```python
# 7001이 열려있다면 닫기
if cmds.commandPort(':7001', query=True):
    cmds.commandPort(name=':7001', close=True)

# 7002 열기
cmds.commandPort(name=':7002', sourceType='python')
```

---

### 4-5. "No module named 'maya'" 에러

**증상:**
```
ModuleNotFoundError: No module named 'maya'
```

**원인:** Maya 코드를 일반 Python으로 직접 실행함

**잘못된 방법:**
- ❌ `Ctrl+F10` (Run) - 일반 Python 실행
- ❌ `python3 test_maya_connection.py` - 터미널에서 직접 실행

**올바른 방법:**
- ✅ `F5` (External Tools: Run in Maya)
- ✅ 우클릭 > `External Tools > Run in Maya`
- ✅ `python3 run_in_maya.py test_maya_connection.py` (터미널)

---

### 4-6. mayapy 실행 안 됨

**증상:**
```
Permission denied: run_with_mayapy.sh
```

**원인:** 실행 권한 없음

**해결:**
```bash
chmod +x ~/.pycharm_tools/run_with_mayapy.sh
```

---

## 5. Maya 자동 Command Port 열기 (선택)

Maya를 실행할 때마다 자동으로 command port를 열고 싶다면:

### userSetup.py 생성

**파일:** `~/maya/2025/scripts/userSetup.py`

```python
import maya.cmds as cmds

def setup_pycharm_command_port():
    """Maya 시작 시 PyCharm용 command port 자동 열기"""
    port = 7002
    try:
        if cmds.commandPort(f':{port}', query=True):
            print(f"✓ Command port :{port} is already open")
        else:
            cmds.commandPort(name=f':{port}', sourceType='python')
            print(f"✓ PyCharm command port opened on :{port}")
    except Exception as e:
        print(f"✗ Failed to open command port: {e}")

# Maya 시작 시 자동 실행
setup_pycharm_command_port()
```

**생성 후:**
- Maya를 재시작하면 자동으로 7002 포트가 열림
- 수동으로 command port를 열 필요 없음

---

## 6. 정리

### ✅ 완료 체크리스트

- [ ] External Tools 2개 등록 (Run in Maya, Run with mayapy)
- [ ] 단축키 2개 설정 (F5, Shift+F5)
- [ ] mayapy standalone 테스트 성공
- [ ] Maya GUI 연결 테스트 성공
- [ ] (선택) userSetup.py 설정

### 📖 추가 참고

- **README.md** - 전체 개요 및 사용법
- **트러블슈팅** - 문제 발생 시 이 문서의 4장 참고

---

**설정 완료!** 🎉

이제 PyCharm에서 F5를 누르면 Maya로 코드가 전송됩니다!
