#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mayapy Standalone 모드 테스트 스크립트
PyCharm External Tools로 실행 테스트
"""

import maya.standalone
import maya.cmds as cmds

print("=" * 50)
print("mayapy Standalone Test")
print("=" * 50)

# Standalone 모드 초기화
print("Initializing Maya standalone...")
maya.standalone.initialize()
print("✓ Maya standalone initialized")

# Maya 버전 확인
maya_version = cmds.about(version=True)
print(f"Maya Version: {maya_version}")

# 새 씬 생성
cmds.file(new=True, force=True)
print("✓ New scene created")

# Cube 생성
cube = cmds.polyCube(name='test_cube', width=2, height=2, depth=2)
print(f"✓ Created cube: {cube[0]}")

# Sphere 생성
sphere = cmds.polySphere(name='test_sphere', radius=1.5)
print(f"✓ Created sphere: {sphere[0]}")
cmds.move(3, 0, 0, sphere[0])
print(f"✓ Moved sphere to (3, 0, 0)")

# 씬의 모든 transform 노드 리스트
transforms = cmds.ls(type='transform')
print(f"\nTransform nodes in scene:")
for t in transforms:
    print(f"  - {t}")

# 씬 정보
all_objects = cmds.ls()
print(f"\nTotal objects: {len(all_objects)}")

# 임시 파일로 저장 (선택)
import tempfile
import os
temp_file = os.path.join(tempfile.gettempdir(), 'pycharm_maya_test.ma')
cmds.file(rename=temp_file)
cmds.file(save=True, type='mayaAscii')
print(f"\n✓ Scene saved to: {temp_file}")

print("=" * 50)
print("Test Complete!")
print("=" * 50)

# Standalone 종료
maya.standalone.uninitialize()
