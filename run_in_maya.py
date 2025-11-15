#!/usr/bin/env python3
"""
PyCharm에서 선택한 코드를 실행 중인 Maya로 전송하는 스크립트
사용법: python run_in_maya.py <file_path> [--selection]
"""
import socket
import sys
import os

MAYA_HOST = 'localhost'
MAYA_PORT = 7002  # Changed from 7001 (port conflict with NoMachine)


def send_to_maya(code, host=MAYA_HOST, port=MAYA_PORT):
    """Maya command port로 코드 전송"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        # 코드 전송
        if isinstance(code, str):
            code = code.encode('utf-8')

        s.send(code + b'\n')
        s.close()

        print(f"✓ Code sent to Maya on port {port}")
        return True

    except ConnectionRefusedError:
        print(f"✗ Error: Maya is not running or command port is not open.")
        print(f"\nTo enable Maya command port, run this in Maya:")
        print(f"  import maya.cmds as cmds")
        print(f"  cmds.commandPort(name=':{port}', sourceType='python')")
        return False

    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_in_maya.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"✗ Error: File not found: {file_path}")
        sys.exit(1)

    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    print(f"Sending {file_path} to Maya...")

    if send_to_maya(code):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
