import subprocess
import os
os.mkdir("VideoClips")
subprocess.run(["scenedetect", "-i","/home/aman/Desktop/Mini-Project/testVideo.mp4", "-o", "/home/aman/Desktop/Mini-Project/VideoClips", "detect-content", "-t", "27",
"split-video"])