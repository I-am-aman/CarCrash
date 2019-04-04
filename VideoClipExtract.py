import subprocess
import os
subprocess.run(["scenedetect", "-i","/home/aman/Desktop/Mini-Project/videoplayback.mp4", "-o", "/home/aman/Desktop//Mini-Project/VideoClips", "detect-content", "-t", "27",
                "split-video"])
