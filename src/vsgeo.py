import argparse
import re
from .scraper import Scraper
from termcolor import colored

class Vsgeo():
    def __init__(self):
        self.args = self.__parser()
        self.user = Scraper(self.args.username)
        
    def printUsername(self):
        print(colored(self.user.name + ' :', 'red', attrs=['bold']))
    def printUserSideID(self):
        print("Site ID: ", self.user.sites['id'])
    def mediaList(self):
        return self.user.getMediaList(self.args.border)
    
    def __parser(self):
        def borderType(arg):
            
            standartException = argparse.ArgumentTypeError(
                    '''Border usage: <start>,<end> or <start> <end> or <start>, or <end>\n
                    Examples: [2,5]\t[2 5]\t[2,]\t[5]''') 
            
            mat = re.compile(r"^(\d+),(\d*)$|^ *(\d+)$").match(arg)
            if not mat: raise standartException

            if mat.group(3):                   return [0, int(mat.group(3))]
            elif mat.group(1) or mat.group(2):
                a = mat.group(1)
                b = mat.group(2)
                border = [None, None]
                border[0] = int(a) if a else 0
                border[1] = int(b) if b else float("inf")

                if border[0] >= border[1]:
                    raise argparse.ArgumentTypeError("Start value must be lower than end value")
                print(border)
                return border
            
            
            raise standartException
        
        parser = argparse.ArgumentParser(
            description="OSINT for VSCO Accounts"
        )
        parser.add_argument(
            "username",
            type=str,
            help="VSCO user to scrape info.",
        )
        parser.add_argument(
            "-s", 
            "--siteId",
            action="store_true",
            help="Grabs VSCO siteID for user"
        )
        parser.add_argument(
            "-l", 
            "--location",
            action="store_true",
            help="Scrapes location info of a user"
        )
        parser.add_argument(
            "-d", 
            "--device",
            action="store_true",
            help="Scrapes device info of a user"
        )
        parser.add_argument(
            "-c", 
            "--coords",
            action="store_true",
            help="Scrapes coordinate info of a user"
        )
        parser.add_argument(
            "-r", 
            "--raw",
            action="store_true",
            help="Raw info"
        )
        parser.add_argument(
            "-b",
            "--border",
            type=borderType,
            help="Border" #combak: better explanation
        )

        args = parser.parse_args()
        
        return args