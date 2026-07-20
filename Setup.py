from cx_Freeze import setup, Executable
import os


# Inclui todos os arquivos da pasta asset
include_files = []

for root, dirs, files in os.walk("asset"):
    for file in files:
        caminho = os.path.join(root, file)
        include_files.append(caminho)


setup(
    name="Floresta",
    version="1.0",
    description="Floresta - Jogo desenvolvido em Pygame",

    options={
        "build_exe": {
            "packages": [
                "pygame"
            ],

            "include_files": include_files
        }
    },

    executables=[
        Executable(
            "main.py",
            target_name="Floresta.exe"
        )
    ]
)