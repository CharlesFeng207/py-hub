import sys
import os

dir_path = sys.argv[1]
dir_name = os.path.basename(dir_path)
archiveName = f"{dir_name}.xcarchive"

print(f"dir_path:{dir_path}")
print(f"dir_name:{dir_name}")
print(f"archiveName:{archiveName}")

os.chdir(dir_path)

os.system("xcodebuild clean -workspace Unity-iPhone.xcworkspace -scheme Unity-iPhone")
os.system(f"xcodebuild archive -workspace Unity-iPhone.xcworkspace -scheme Unity-iPhone -configuration Release -archivePath {archiveName}")
os.system(f"xcodebuild -exportArchive -archivePath {archiveName} -exportPath {dir_name} -exportOptionsPlist ExportOptions.plist")

print("end")
