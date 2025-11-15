#!/bin/bash
# PyCharm Maya Tools 설치 스크립트
# 홈 디렉토리에 .pycharm_tools를 생성하고 필요한 파일을 복사합니다

set -e

INSTALL_DIR="$HOME/.pycharm_tools"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=================================================="
echo "PyCharm Maya Tools Installer"
echo "=================================================="
echo ""

# 설치 디렉토리 생성
echo "[1/4] Creating installation directory..."
if [ -d "$INSTALL_DIR" ]; then
    echo "  ⚠️  Directory already exists: $INSTALL_DIR"
    read -p "  Overwrite? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "  Installation cancelled."
        exit 1
    fi
    echo "  Backing up existing directory..."
    mv "$INSTALL_DIR" "$INSTALL_DIR.backup.$(date +%Y%m%d_%H%M%S)"
fi

mkdir -p "$INSTALL_DIR"
echo "  ✓ Created: $INSTALL_DIR"

# 파일 복사
echo ""
echo "[2/5] Copying files..."
cp "$SCRIPT_DIR/run_in_maya.py" "$INSTALL_DIR/"
cp "$SCRIPT_DIR/run_with_mayapy.sh" "$INSTALL_DIR/"
cp "$SCRIPT_DIR/test_maya_connection.py" "$INSTALL_DIR/"
cp "$SCRIPT_DIR/test_mayapy_standalone.py" "$INSTALL_DIR/"
cp "$SCRIPT_DIR/README.md" "$INSTALL_DIR/"
cp "$SCRIPT_DIR/PYCHARM_SETUP.md" "$INSTALL_DIR/"
cp "$SCRIPT_DIR/AUTOCOMPLETE_SETUP.md" "$INSTALL_DIR/"
echo "  ✓ Copied 7 files"

# Stub 파일 복사
echo ""
echo "[3/5] Copying Maya autocomplete stubs..."
if [ -d "$SCRIPT_DIR/stubs" ]; then
    cp -r "$SCRIPT_DIR/stubs" "$INSTALL_DIR/"
    echo "  ✓ Copied stubs directory"
else
    echo "  ⚠️  Warning: stubs directory not found (autocomplete will not work)"
fi

# 실행 권한 설정
echo ""
echo "[4/5] Setting permissions..."
chmod +x "$INSTALL_DIR/run_in_maya.py"
chmod +x "$INSTALL_DIR/run_with_mayapy.sh"
echo "  ✓ Executable permissions set"

# 검증
echo ""
echo "[5/5] Verifying installation..."
if [ -f "$INSTALL_DIR/run_in_maya.py" ] && [ -f "$INSTALL_DIR/run_with_mayapy.sh" ]; then
    echo "  ✓ Installation verified"
else
    echo "  ✗ Installation failed!"
    exit 1
fi

echo ""
echo "=================================================="
echo "✓ Installation Complete!"
echo "=================================================="
echo ""
echo "Installed files:"
echo "  $INSTALL_DIR/run_in_maya.py"
echo "  $INSTALL_DIR/run_with_mayapy.sh"
echo "  $INSTALL_DIR/test_maya_connection.py"
echo "  $INSTALL_DIR/test_mayapy_standalone.py"
echo "  $INSTALL_DIR/README.md"
echo "  $INSTALL_DIR/PYCHARM_SETUP.md"
echo "  $INSTALL_DIR/AUTOCOMPLETE_SETUP.md"
echo "  $INSTALL_DIR/stubs/ (Maya autocomplete)"
echo ""
echo "Next steps:"
echo "  1. Read: $INSTALL_DIR/PYCHARM_SETUP.md"
echo "  2. Configure PyCharm External Tools"
echo "  3. Set keyboard shortcuts (F5, Shift+F5)"
echo "  4. (Optional) Setup autocomplete: $INSTALL_DIR/AUTOCOMPLETE_SETUP.md"
echo ""
echo "Quick test:"
echo "  $INSTALL_DIR/run_with_mayapy.sh $INSTALL_DIR/test_mayapy_standalone.py"
echo ""
