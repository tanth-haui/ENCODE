import PyInstaller.__main__
import PyInstaller.config
import os

print("path:", str(os.getcwd()))

distpath ="--distpath=" + r"D:\WORK_CODE\Tan_Project\Encoding_app\encoding_theard_vr5\App"
workpath = "--workpath=" + r"D:\WORK_CODE\Tan_Project\Encoding_app\encoding_theard_vr5\tempo"
PyInstaller.__main__.run([
    # "--onedir",
    "--onefile",
    r"D:\WORK_CODE\Tan_Project\Encoding_app\encoding_theard_vr5\main.py",
    "-nEncoding_v1.5",#App name
    "--windowed",
    distpath,
    workpath,
    "--clean",
    "-y"
])