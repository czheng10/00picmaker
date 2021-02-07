# Work 00: Imagine All the Pixels...


def main():
    
    pic = open('image.ppm','w')
    pic.write("P3\n500 500\n255\n")

    for y in range(500):
        for x in range(500):
            newx = x - 250
            newy = y - 250
            if x>=250 and (((newx-125)**2 + (newy-125)**2) < (125**2)):
                    r= 210
                    g= int(x/500 * 255) % 255
                    b= int(y/500 * 255) % 255
                
            elif ((newx**2 + newy**2) < (250**2)):
                r=210
                g= int(y /500 * 255) % 255
                b= int(x /500 * 255) % 255
            else:
                r=0
                g=0
                b=0
            pic.write(str(r) + " " + str(g) + " " + str(b) + " ")
        pic.write("\n")
    pic.close()
        

main()

