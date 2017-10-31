from random import randint
import webbrowser
import time
#add other websites into this list
url = ['https://www.youtube.com/watch?v=-qlJiGGvPUI','https://www.youtube.com/watch?v=8tdg6-kABS4','https://www.youtube.com/watch?v=ZbZSe6N_BXs','https://www.youtube.com/watch?v=gOrnLU8LyAU']
check = False

# opening browser function
def openweb():
    x = randint(0,len(url)) 
    return webbrowser.open(url[x])

if __name__ == "__main__":
    while True:
        if not check:
            start_time = time.time()
            check=True

        if time.time() - start_time > 7200:
            print "time to take a break!"
            openweb()
            check=False
    

















