import cv2 


def FrameCapture(path): 
      
    vidObj = cv2.VideoCapture(path)
    success = 1
  
    while success: 
        success, image = vidObj.read() 
        cv2.imwrite("/home/aman/Desktop/Mini-Project/Frames/frame%d.jpg" % count, image) 
  
        count += 1


if __name__ == '__main__': 

    FrameCapture("/home/aman/Desktop/Mini-Project/testVideo.mp4") 





