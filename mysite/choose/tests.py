# -*- coding: UTF-8 -*-
import foursquare
import pprint


pp = pprint.PrettyPrinter(indent=4)

print 'tesing'

API_URL = "https://api.foursquare.com/v2/venues/search"
FS_RADIUS = 20000
FS_COORDINATES = '42.6931325, 23.3244314'
CLIENT_ID = "35UKEYL1JB5SCBN1JHL4KTXSQWULWRELA5AMB1SN2UMDYSOK"
CLIENT_SECRET = "GOZQXTNPAXPC1GATPFIF02LBHROZZ3GGD2YRLMNHBG1VRCDI"

client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

venues = client.venues.search(params={'ll': FS_COORDINATES, 'intent': 'browse', 'radius': FS_RADIUS})

venues_count = len(venues.values()[0])


for n in range(0, venues_count):
    venue = venues.values()[0][n]
    if "name" in venue:
        venue_name = venue["name"]
    else:
        venue_name = "ERR: NO NAME"
    if "address" in venue["location"]:
        venue_address = venue["location"]["address"]
    else:
        venue_address = "ERR: NO ADDRESS"
    if venue['categories'][0]['primary'] and "name" in venue["categories"][0]:
        venue_category = venue["categories"][0]["name"]
    else:
        venue_category = "ERR: NO PRIMARY CATEGORY"
    if "distance" in venue["location"]:
        venue_distance = str(venue["location"]["distance"])
    else:
        venue_distance = "ERR: NO DISTANCE"

    print "---".join([venue_name, venue_address, venue_category, venue_distance])















    # available_venues.append(venue["name"])
    # pp.pprint(venue['categories'][0]['primary'])
    # print n

    # a = venues.values()[0][n]
    # for k in a.keys():
    #     if k not in venue_fields:
    #         venue_fields.append(k)

# print available_venues

# pp.pprint(venues.values()[0][1])