
from . import vsgeo
from termcolor import colored



printable = True
def printMedia(media):
    global printable
    if printable:
        print('---------------------------------------------')
        print(media['permalink'])
        if media['description']: print(colored('Description: ', 'green'), media['description'])
        printable = False




def main():

    VSGEO = vsgeo.Vsgeo()
    args = VSGEO.args


    VSGEO.printUsername()

    if args.siteId:
        VSGEO.printUserSideID()

    for media in VSGEO.mediaList():
        global printable
        printable = True
        
        if args.location:
            loc = VSGEO.user.getLocationFromMedia(media)
            if loc:
                printMedia(media=media)
                print(colored("Location: ", 'red'), loc)
        if args.device:
            dev = VSGEO.user.device(media)
            if dev:
                printMedia(media=media)
                print(colored("Device: ", 'red'), dev)
        if args.coords:
            coord = VSGEO.user.coords(media)
            if coord:
                printMedia(media=media)
                print(colored("Coords: ", 'red'), coord[0], coord[1], end= ' | ')
                for i in coord:
                    m = (i % 1) * 60
                    s = (m % 1) * 60
                    d = int(i)
                    m = int(m)
                    s = int(s)

                    direction = None
                    if i < 0:
                        if i == coord[0]:
                            direction = 'W'
                        else:
                            direction = 'S'
                    else:
                        if i == coord[0]:
                            direction = 'E'
                        else:
                            direction = 'N'
                    print('%d°%d\'%d\'\' %c  ' % (d, m, s, direction), end= '')
                print() 

        if args.raw:
            printMedia(media=media)
            print(media)



if __name__ == "__main__":
    exit(main())