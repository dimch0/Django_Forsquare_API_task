from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import Venue

import foursquare

#0dd682

API_URL = "https://api.foursquare.com/v2/venues/search"
FS_RADIUS = 20000
FS_COORDINATES = '42.6931325, 23.3244314'
CLIENT_ID = "35UKEYL1JB5SCBN1JHL4KTXSQWULWRELA5AMB1SN2UMDYSOK"
CLIENT_SECRET = "GOZQXTNPAXPC1GATPFIF02LBHROZZ3GGD2YRLMNHBG1VRCDI"

client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

venues = client.venues.search(params={'ll': FS_COORDINATES, 'intent': 'browse', 'radius': FS_RADIUS})

venues_count = len(venues.values()[0])

selected_venue_id_list = []

# for v in Venue.objects.all():
#     v.delete()


def index(request):
    if len(Venue.objects.all()) != venues_count:
        for n in range(0, venues_count):
            venue = venues.values()[0][n]
            if "name" in venue:
                venue_name = venue["name"]
            else:
                venue_name = "n/a"
            if "address" in venue["location"]:
                venue_address = venue["location"]["address"]
            else:
                venue_address = "n/a"
            if venue['categories'][0]['primary'] and "name" in venue["categories"][0]:
                venue_category = venue["categories"][0]["name"]
            else:
                venue_category = "n/a"
            if "distance" in venue["location"]:
                venue_distance = str(venue["location"]["distance"])
            else:
                venue_distance = "n/a"

            v = Venue(name=venue_name,
                      address=venue_address,
                      category=venue_category,
                      distance=venue_distance,
                      selected=False
                      )
            if v not in Venue.objects.all():
                v.save()
    # venue = get_object_or_404(Venue, v_id)
    venue_list = Venue.objects.all()
    context = {'venue_list': venue_list, 'FS_COORDINATES': FS_COORDINATES, 'FS_RADIUS':FS_RADIUS / 1000}
    return render(request, 'choose/home.html', context)


        # try:
        #     selected_venue = venue.get(pk=request.POST[venue.name])
        # except (KeyError, Venue.DoesNotExist):
        #     return render(request, 'choose/home.html', {
        #         'venue': venue,
        #         'error_message': "You didn't select a venue.",
        #     })
        # else:
        #     selected_venue.selected = True
        #     selected_venue.save()
        #     return HttpResponseRedirect(reverse('choose:results'))

def result(request):
    selected_venue_list = []
    venue_list = Venue.objects.all()
    selected_venue_ids = request.POST.getlist('check_venue')
    for i in selected_venue_ids:
        for v in venue_list:
            if str(i).replace("/", "") == str(v.id):
                selected_venue_list.append(v)

    return render(request, "choose/result.html", {"selected_venue_list": selected_venue_list})
