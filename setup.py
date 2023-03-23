from sys import platform
from cx_Freeze import setup, Executable


base = "Win32GUI" if platform == "win32" else None

build_exe_options = {"zip_include_packages": ["requests", "PySide6"]}

setup(
    name='Crypto PY',
    version='0.0.1',
    description='Cotações de cryptomoedas da api2 Binance e acompanhamento de carteira.',
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="assets/favicon.ico")],
)
