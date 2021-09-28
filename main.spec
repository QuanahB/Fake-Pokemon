# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/quanahbennett/PycharmProjects/pythonProject1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('DancingZombies.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/DancingZombies.gif', "DATA"),
            ('DeepFreeze.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/DeepFreeze.gif', "DATA"),
            ('EnchantedEyes.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/EnchantedEyes.gif', "DATA"),
            ('FallingTower.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/FallingTower.gif', "DATA"),
            ('Godzilla.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/Godzilla.gif', "DATA"),
            ('GreenM.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/GreenM.gif', "DATA"),
            ('HydraPride.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/HydraPride.gif', "DATA"),
            ('OminousSpell.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/OminousSpell.gif', "DATA"),
            ('PinkThing.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/PinkThing.gif', "DATA"),
            ('RainyDay.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/RainyDay.gif', "DATA"),
            ('Solid_black.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/Solid_black.gif', "DATA"),
            ('Unite.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/Unite.gif', "DATA"),
            ('WeirdAlien.gif','/Users/quanahbennett/PycharmProjects/pythonProject1/WeirdAlien.gif', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
app = BUNDLE(exe,
             name='main.app',
             icon=None,
             bundle_identifier=None)
