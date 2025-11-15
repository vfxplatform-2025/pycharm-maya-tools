# PyCharm Maya Tools

PyCharm에서 Maya 개발을 위한 External Tools 패키지 (MayaCharm 플러그인 대체)

## 특징

- ✅ **플러그인 불필요** - PyCharm 기본 기능(External Tools)만 사용
- ✅ **Maya 2025 지원** - 최신 Maya 버전과 완벽 호환
- ✅ **포트 충돌 해결** - NoMachine과 충돌하지 않는 7002 포트 사용
- ✅ **두 가지 실행 모드**
  - Maya GUI 연동 (Socket 통신)
  - mayapy standalone 실행
- ✅ **쉬운 설치** - 홈 디렉토리에 한 번만 설치
- ✅ **커스터마이징 가능** - Python 스크립트로 자유롭게 수정 가능

## 빠른 시작

### 1. 설치

```bash
# 홈 디렉토리에 설치
bash install.sh
```

설치 완료 후:
- `~/.pycharm_tools/run_in_maya.py`
- `~/.pycharm_tools/run_with_mayapy.sh`
- `~/.pycharm_tools/test_maya_connection.py`
- `~/.pycharm_tools/test_mayapy_standalone.py`

### 2. PyCharm 설정

**Settings (`Ctrl+Alt+S`) > Tools > External Tools > Add (+)**

#### Tool 1: Run in Maya (Maya GUI 연동)

| 항목 | 값 |
|------|-----|
| Name | `Run in Maya` |
| Description | `Send code to running Maya GUI` |
| Program | `/usr/bin/python3` |
| Arguments | `/home/$USER/.pycharm_tools/run_in_maya.py $FilePath$` |
| Working directory | `$FileDir$` |
| ✓ Synchronize files after execution | |
| ✓ Open console for tool output | |

#### Tool 2: Run with mayapy (Standalone)

| 항목 | 값 |
|------|-----|
| Name | `Run with mayapy` |
| Description | `Execute script with mayapy standalone` |
| Program | `/home/$USER/.pycharm_tools/run_with_mayapy.sh` |
| Arguments | `$FilePath$` |
| Working directory | `$FileDir$` |
| ✓ Synchronize files after execution | |
| ✓ Open console for tool output | |

### 3. 단축키 설정 (선택)

**Settings > Keymap > 검색: "External Tools"**

- `Run in Maya` → `F5` (추천)
- `Run with mayapy` → `Shift+F5` (추천)

## 사용 방법

### Maya GUI 연동 (run_in_maya.py)

**1. Maya 실행 및 Command Port 열기:**

Maya Script Editor에서 실행:
```python
import maya.cmds as cmds
cmds.commandPort(name=':7002', sourceType='python')
print("✓ Command port opened on :7002")
```

**2. PyCharm에서 코드 실행:**
- 파일 열기
- 우클릭 > `External Tools > Run in Maya`
- 또는 단축키 `F5`

**3. Maya Script Editor에서 결과 확인**

---

### mayapy Standalone (run_with_mayapy.sh)

**PyCharm에서:**
- 파일 열기
- 우클릭 > `External Tools > Run with mayapy`
- 또는 단축키 `Shift+F5`

**결과가 PyCharm 콘솔에 출력됨**

## 테스트

### Test 1: mayapy Standalone (Maya 실행 불필요)

```bash
~/.pycharm_tools/run_with_mayapy.sh ~/.pycharm_tools/test_mayapy_standalone.py
```

**예상 결과:**
```
✓ Maya standalone initialized
✓ Created cube: test_cube
✓ Created sphere: test_sphere
✓ Scene saved to: /tmp/pycharm_maya_test.ma
```

### Test 2: Maya GUI 연동 (Maya 실행 필요)

**준비:**
1. Maya 실행
2. Command Port 열기 (`:7002`)

**실행:**
```bash
python3 ~/.pycharm_tools/run_in_maya.py ~/.pycharm_tools/test_maya_connection.py
```

**Maya에서 확인:**
- 빨간 구체가 (0, 5, 0)에 생성됨

## 트러블슈팅

### "Connection refused" 에러

**원인:** Maya command port가 열리지 않음

**해결:**
```python
# Maya Script Editor에서 실행
import maya.cmds as cmds
cmds.commandPort(name=':7002', sourceType='python')
```

### "No module named 'maya'" 에러

**원인:** 일반 Python으로 Maya 코드를 직접 실행함

**해결:**
- ❌ `python3 test_maya_connection.py` (직접 실행)
- ✅ `python3 run_in_maya.py test_maya_connection.py` (Maya로 전송)
- ✅ PyCharm External Tools 사용

### 포트 충돌 (7001 already in use)

**원인:** NoMachine이 7001 포트 사용 중

**해결:** 이미 7002 포트로 설정되어 있음 (별도 조치 불필요)

### PyCharm 변수 치환 안 됨

**증상:** `$UserHome$` 같은 변수가 그대로 남음

**해결:** 절대 경로 사용
```
/home/m83/.pycharm_tools/run_in_maya.py  (O)
$UserHome$/.pycharm_tools/run_in_maya.py (X)
```

## 파일 구조

```
~/.pycharm_tools/
├── run_in_maya.py              # Maya GUI로 코드 전송
├── run_with_mayapy.sh          # mayapy standalone 실행
├── test_maya_connection.py     # Maya GUI 연결 테스트
├── test_mayapy_standalone.py   # mayapy standalone 테스트
├── README.md                   # 이 파일
└── PYCHARM_SETUP.md           # PyCharm 설정 상세 가이드
```

## 기술 사양

- **Maya 버전:** Maya 2025 (2024, 2023도 호환)
- **Python:** Python 3.x
- **플랫폼:** Linux (Rocky 9)
- **포트:** 7002 (NoMachine 충돌 방지)
- **의존성:** 없음 (PyCharm 기본 기능만 사용)

## MayaCharm과 비교

| 기능 | MayaCharm | PyCharm Maya Tools |
|------|-----------|-------------------|
| Maya로 코드 전송 | ✓ | ✓ |
| mayapy 실행 | ✓ | ✓ |
| 디버거 연결 | ✓ | ✗ |
| 최신 PyCharm 호환 | ✗ (2024.3 오류) | ✓ |
| 포트 충돌 해결 | ✗ | ✓ (7002) |
| 커스터마이징 | ✗ | ✓ (Python 스크립트) |
| 설치 | 플러그인 설치 | 스크립트 복사 |

## 라이선스

MIT License

## 기여

Issues와 Pull Requests를 환영합니다!

## 작성자

M83 VFX Studio - Technical Director Team
