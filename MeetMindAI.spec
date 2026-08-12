# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['phase1/ui.py'],
    pathex=['.', 'phase1'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'phase1.meeting_audio_worker',
        'phase1.system_audio',
        'phase2.privacy_mode',
        'phase2.privacy_ui',
        'pyaudiowpatch',
        'speech_recognition',
        'PySide6',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MeetMindAI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)