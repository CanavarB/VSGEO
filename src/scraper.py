from . import constants
import requests
from geopy.geocoders import Nominatim




class Scraper():
    geolocator = Nominatim(user_agent="CB-VSGEO")
    def __init__(self, username):
        self.name = username

        try:
            self.session = requests.Session()
            self.sites = self.getUserSites()
        except Exception as e:
            raise e
    
    @staticmethod
    def vscoAPI2Query(wants : str, params : dict[str : str], session : requests.Session = None):
        if session is None: session = requests.Session()
        
        return session.get('http://vsco.co/api/2.0/%s' % (wants), params=params, headers=constants.visituserinfo,).json()
    @staticmethod
    def coords(media):
        if 'location_coords' in media and media['location_coords'] is not None:
            return media['location_coords']
        else:
            return False
    @staticmethod
    def getLocationFromMedia(media):
        if 'location_coords' in media and media['location_coords'] is not None:
            return Scraper.geolocator.reverse('%s,%s' % (media['location_coords'][1], media['location_coords'][0]))
        else:
            return False
    @staticmethod
    def device(media):
        try:
            meta = media['image_meta']
            if 'make' in meta:
                return meta['make'] + ' ' + meta['model']
        except:
            return False
    
    def getUserSites(self):
        response = Scraper.vscoAPI2Query(wants='sites', params={'subdomain': self.name}, session=self.session)        
        
        if 'errorType' in response:
            raise UserNotFoundError(username=self.name, type=0)
        elif 'has_grid' not in response['sites'][0] or response['sites'][0]['has_grid'] is False:
            raise UserNotFoundError(username=self.name, type=1)
        else:
            return response['sites'][0]

    def getMediaList(self, border = None):
        if border == None: border = [0,float("inf")]
        start = border[0]
        end = border[1]

        if end == None: end = float("inf")
        self.mediaList = list()
        nextCursor = None
        

        multip = 1
        while ((multip * 10) < end):
            medias = self.session.get("https://vsco.co/api/3.0/medias/profile",
                                        params={"site_id": self.sites['id'], "limit":10, "cursor": nextCursor}, 
                                        headers=constants.visituserinfo,).json()
            
            self.mediaList += [media['image'] if 'image' in media else media['video'] for media in medias['media']]
            
            if 'next_cursor' in medias:
                nextCursor = medias['next_cursor']
                multip += 1
            else:
                break
        
        if start:
            del self.mediaList[:start]
            """ for media in self.mediaList:
                i = self.mediaList.index(media)
                if i < start:
                    print(border)
                    self.mediaList.pop(i)
                    i -= 1
                else:
                    break """
        if end:
            del self.mediaList[len(self.mediaList) if end == float("inf") else end:]
            """ for i, e in reversed(list(enumerate(self.mediaList))):
                
                if i >= end - start:
                    self.mediaList.pop(i)
                else:
                    break """

        return self.mediaList
    

class UserNotFoundError(ValueError):
    errorTypes = {
        0 : '%s username not found.',
        1 : 'The %s profile is not launched'
    }
    def __init__(self, username : str, type: int):
        self.message = self.errorTypes[type] % username
    
    def __str__(self) -> str:
        return self.message




