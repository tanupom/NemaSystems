import jetson.inference
import jetson.utils
import sys
import time

def RunAll(tim):
    list = sys.argv
    list.append("--input-width=3264")
    list.append("--input-height=2448")
    list.append("--output-codec=h265")
    list.append("--bitrate=3000000")
    #list.append("--headless")
    cameras = [
        jetson.utils.videoSource("/dev/video0", argv=sys.argv),     
        jetson.utils.videoSource("/dev/video2", argv=sys.argv),
        jetson.utils.videoSource("/dev/video4", argv=sys.argv),
        jetson.utils.videoSource("/dev/video6", argv=sys.argv)  
    ]

    displays = [
        jetson.utils.videoOutput("/home/infinitysystem/Downloads/TestVideos/C1_"+str(time.time())+".mp4", argv=sys.argv),  
        jetson.utils.videoOutput("/home/infinitysystem/Downloads/TestVideos/C2_"+str(time.time())+".mp4", argv=sys.argv),
        jetson.utils.videoOutput("/home/infinitysystem/Downloads/TestVideos/C3_"+str(time.time())+".mp4", argv=sys.argv),
        jetson.utils.videoOutput("/home/infinitysystem/Downloads/TestVideos/C4_"+str(time.time())+".mp4", argv=sys.argv),
        jetson.utils.videoOutput("/home/infinitysystem/Downloads/TestVideos/CAll_"+str(time.time())+".mp4", argv=sys.argv),
    ]

    detections = []
    images = []

    for index in range(len(cameras)):
        detections.append(None)
        images.append(None)
        detections.append(None)
        images.append(None)
    t = time.time()
    frame = 0
    FPS = 15
    Seconds = tim
    while(abs(t-time.time())<10):
        try:
            dump1 = cameras[0].Capture()
            dump2 = cameras[1].Capture()
            dump3 = cameras[2].Capture()
            dump4 = cameras[3].Capture()
        except Exception as e: print(e)
    # print(abs(t-time.time()))
    while frame<FPS*Seconds:
        #print(abs(t-time.time()))
        try:
            for index in range(len(cameras)):
                images[index] = cameras[index].Capture()
                displays[index].Render(images[index])
            print(frame/FPS)
        except Exception as e: print(e)
        frame = frame + 1
        #displays[4].Render(imgResize)
if __name__ == '__main__':
    print('x')
   #RunAll(20)