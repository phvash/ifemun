from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

file1 = drive.CreateFile()
file1.SetContentFile('test.png')
file1.Upload()
print(file1)