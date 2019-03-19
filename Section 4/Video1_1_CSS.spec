# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:/Eclipse_Oxygen_workspace_Packt_HandsOn_GUI/Packt_HandsOn_GUI/Section4/Video1_1_CSS.py'],
             pathex=['C:\\Eclipse_Oxygen_workspace_Packt_HandsOn_GUI\\Packt_HandsOn_GUI\\Section4'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Video1_1_CSS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
