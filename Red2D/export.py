import PyInstaller.__main__
import time

print("Starting the export")
time.sleep(1)

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed'
])

print("Your export has finished")
time.sleep(1)
print("You can find the output in the dist folder")
