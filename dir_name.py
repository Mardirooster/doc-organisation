import os
import cv2


def show_clusters(directory):
    print(directory)
    dirs = [os.path.join(directory,o) for o in os.listdir(directory) if os.path.isdir(os.path.join(directory,o)) and o.replace('-','1').isdigit()]
    dirs.sort(key = lambda x: len(os.listdir(x)), reverse=True)
    #print(dirs)
    for d in dirs:     
        files = [os.path.join(d, f) for f in os.listdir(d) if f.endswith(".png")]
        print(d, " ", len(files))
        count = 0
        for f in files:
            image = cv2.imread(f)
            small = cv2.resize(image, (0,0), fx=0.3, fy=0.3) 
            cv2.imshow(f,small)
            count += 1
            if count%20 == 0:
                k = cv2.waitKey(0)
                if k == 32:                   
                    break
                cv2.destroyAllWindows()
        q = cv2.waitKey(0)
        if q != 27:
            dirname = input("enter dir name...")
            count = 0
            while os.path.isdir(os.path.join(directory,dirname)):
                dirname = (dirname[:-1] if count else dirname) + str(count)
                count += 1 
            os.rename(d, os.path.join(directory,dirname))
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
            break


path = "C:\\Unnamed\\"
dirs = [os.path.join(path, 'dir'+str(x)) for x in range(29)][25:]
print(dirs)
for d in dirs:
    show_clusters(d)