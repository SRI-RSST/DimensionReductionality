# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['dim_reduce.py'],
    pathex=[],
    binaries=[],
    datas=[('dim_reduce_icon.png','.'),],
    hiddenimports = [],
    hookspath=['.\\hooks\\'],
    hooksconfig={},
    runtime_hooks=None,
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [('v', None, 'OPTION')],
    name='DimReduceGUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='dim_reduce_icon.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)