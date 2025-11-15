#!/bin/bash
# PyCharm에서 현재 파일을 mayapy로 실행하는 스크립트

MAYAPY="/usr/autodesk/maya2025/bin/mayapy"
MAYA_LOCATION="/usr/autodesk/maya2025"

# Maya 라이브러리 경로 설정
export LD_LIBRARY_PATH="${MAYA_LOCATION}/lib:$LD_LIBRARY_PATH"

FILE_PATH="$1"

if [ -z "$FILE_PATH" ]; then
    echo "Usage: $0 <python_file>"
    exit 1
fi

if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File not found: $FILE_PATH"
    exit 1
fi

echo "Running $FILE_PATH with mayapy..."
echo "─────────────────────────────────────────"

$MAYAPY "$FILE_PATH"

EXIT_CODE=$?
echo "─────────────────────────────────────────"
echo "Exit code: $EXIT_CODE"

exit $EXIT_CODE
