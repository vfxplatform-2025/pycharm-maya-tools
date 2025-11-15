#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Maya 연결 테스트 스크립트
PyCharm External Tools로 실행 테스트
"""

import maya.cmds as cmds

print("=" * 50)
print("Maya Connection Test")
print("=" * 50)

# Maya 버전 확인
maya_version = cmds.about(version=True)
print(f"Maya Version: {maya_version}")

# 현재 씬 정보
current_file = cmds.file(query=True, sceneName=True)
print(f"Current Scene: {current_file if current_file else 'Untitled'}")

# 씬의 모든 오브젝트 리스트
all_objects = cmds.ls()
print(f"Total Objects in Scene: {len(all_objects)}")

# 테스트: Sphere 생성
try:
    sphere_name = "pycharm_test_sphere"

    # 기존에 있으면 삭제
    if cmds.objExists(sphere_name):
        cmds.delete(sphere_name)
        print(f"Deleted existing: {sphere_name}")

    # 새로 생성
    sphere = cmds.polySphere(name=sphere_name, radius=2.0)
    print(f"✓ Created sphere: {sphere[0]}")

    # 위치 변경
    cmds.move(0, 5, 0, sphere[0])
    print(f"✓ Moved sphere to (0, 5, 0)")

    # 색상 변경 (빨간색)
    shader = cmds.shadingNode('lambert', asShader=True, name=f'{sphere_name}_shader')
    cmds.setAttr(f'{shader}.color', 1, 0, 0, type='double3')
    cmds.select(sphere[0])
    cmds.hyperShade(assign=shader)
    print(f"✓ Applied red shader")

except Exception as e:
    print(f"✗ Error creating sphere: {e}")

print("=" * 50)
print("Test Complete!")
print("=" * 50)
