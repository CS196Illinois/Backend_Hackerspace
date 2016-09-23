# -*- coding: utf-8 -*-
import json
import urllib2
# urllib2
"""
The urllib2 module defines functions and classes which help in opening URLs (mostly HTTP) 
in a complex world — basic and digest authentication, redirections, cookies and more.
"""


artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=tania%20bowra&type=artist").read()


artistJson = json.loads(artistResponse)
print artistResponse['artists']['items'][0]


uid = artistJson['artists']['items'][0]['id']
topTracks = urllib2.urlopen("https://api.spotify.com/v1/artists/" + uid + "/top-tracks?country=SE").read()

topTracksJson = json.loads(topTracks)
print topTracksJson['tracks']
