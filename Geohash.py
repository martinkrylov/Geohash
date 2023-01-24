class Geohash:
    base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
    MAX_PRECISION = 18
    LONGITUDE_MIN = -180
    LONGITUDE_MAX = 180
    LATITUDE_MIN = -90
    LATITUDE_MAX = 90

    #Given a laitude and longitude returns a geohash with the given precision
    @staticmethod
    def encode(latitude,longitude,precision):
        Geohash.validateInput(latitude,longitude,precision)
        geohash = ''
        latMin = Geohash.LATITUDE_MIN
        latMax = Geohash.LATITUDE_MAX
        lonMin = Geohash.LONGITUDE_MIN
        lonMax = Geohash.LONGITUDE_MAX
        evenBit = True
        index = 0
        bits = 0

        while(len(geohash)<precision):
            if(evenBit):
                lonMid = (lonMin+lonMax)/2.0
                if(longitude<lonMid):
                    lonMax = lonMid
                    index *= 2
                else:
                    lonMin = lonMid
                    index *= 2
                    index += 1
            else:
                latMid = (latMin+latMax)/2.0
                if(latitude<latMid):
                    latMax = latMid
                    index *= 2
                else:
                    latMin = latMid
                    index *= 2
                    index += 1
            evenBit = not evenBit
            bits += 1
            if(bits == 5):
                geohash += Geohash.base32[index]
                bits = 0
                index = 0
        return geohash


    #Given a geohash it returns a laitude and longitude
    def decode(geohash):
        print("hi")

    @staticmethod
    def isValidLongitude(longitude):
        return Geohash.LONGITUDE_MIN<=longitude and longitude<=Geohash.LONGITUDE_MAX
    
    @staticmethod
    def isValidLatitude(latitude):
        return Geohash.LATITUDE_MIN<=latitude and latitude<=Geohash.LATITUDE_MAX

    @staticmethod
    def isValidPrecision(precision):
        return 0<precision and precision<=Geohash.MAX_PRECISION

    def validateInput(latitude,longitude,precision):
        if(not Geohash.isValidLatitude(latitude)): 
            raise ValueError('Invalid Latitude')
            return false
        if(not Geohash.isValidLongitude(longitude)): 
            raise ValueError('Invalid Longitude')
            return false

    @staticmethod
    def adjacent(geohash, direction):
        geohash = geohash.lower()
        direction = direction.lower()

        if(len(geohash) == 0):
            raise ValueError('Invalid Geohash')


        
