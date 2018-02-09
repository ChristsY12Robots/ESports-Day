# -*- mode: python -*-

block_cipher = None


a = Analysis(['test.py'],
             pathex=['Z:\\Sixth Form\\Computer Science\\8-2-18\\ESports-Day-master\\Source\\Games\\Test\\lib'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=["Z:\Sixth Form\Computer Science\8-2-18\ESports-Day-master\Source\Games\Test\lib\csv_edit.py" , 
						"Z:\Sixth Form\Computer Science\8-2-18\ESports-Day-master\Source\Games\Test\lib\profile.py" , 
						"Z:\Sixth Form\Computer Science\8-2-18\ESports-Day-master\Source\Games\Test\lib\mysql\connector\__init__.py"
						],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='test',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='test')
