#!/usr/bin/python
# Made with <3 by Fran González (@spaceisstrange)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a
#  copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

import requests
from itunespy import artist
from itunespy import album
from itunespy import track

'''
    This is a simple API made in my free time. It's not perfect, but it works well.
    I'm accepting any pull request to improve it, just follow the code style.
    For examples and documentation, take a look at the README.md
'''

# --------
# Searches
# --------

'''
    Term: The URL-encoded text string you want to search for. Example: Steven Wilson.
           The function will take care of spaces so you don't have to.
    Country: The two-letter country code for the store you want to search.
              For a full list of the codes: http://en.wikipedia.org/wiki/%20ISO_3166-1_alpha-2
    Media: The media type you want to search for. Since this module is made for music I recommend leaving it blank.
    Entity: The type of results you want returned, relative to the specified media type. Example: musicArtist.
             Full list: musicArtist, musicTrack, album, musicVideo, mix, song
    Attribute: The attribute you want to search for in the stores, relative to the specified media type.
    Limit: The number of search results you want the iTunes Store to return.
'''

# Defines a general search. Returns the JSON data of the specified arguments
def search(term, country='US', media='music', entity='musicArtist', attribute=None, limit=50):
    search_url = _url_builder(term, country, media, entity, attribute, limit)
    r = requests.get(search_url)

    try:
        return r.json()['results'], r.json()['resultCount']
    except:
        return None, None

# Defines an artist search. Returns a list of Artist instances. If there is no result, it'll raise a LookupError
def search_artist(term, country='US', media='music', entity='musicArtist', attribute=None, limit=50):
    json, result_count = search(term, country, media, entity, attribute, limit)

    if result_count == 0:
        raise LookupError('No artists found with the keyword ' + str(term))

    artist_list = []

    for item in json:
        artist_result = artist.Artist(item)
        artist_list.append(artist_result)

    return artist_list

# Defines an album search. Returns a list of album instances. If there is no result, it'll raise a LookupError
def search_album(term, country='US', media='music', entity='album', attribute=None, limit=50):
    json, result_count = search(term, country, media, entity, attribute, limit)

    if result_count == 0:
        raise LookupError('No albums found with the keyword ' + str(term))

    album_list = []

    for item in json:
        album_result = album.Album(item)
        album_list.append(album_result)

    return album_list

# Defines a track search. Return a list of track instances. If there is no result, it'll raise a LookupError
def search_track(term, country='US', media='music', entity='musicTrack', attribute=None, limit=50):
    json, result_count = search(term, country, media, entity, attribute, limit)

    if result_count == 0:
        raise LookupError('No tracks found with the keyword ' + str(term))

    track_list = []

    for item in json:
        track_result = track.Track(item)
        track_list.append(track_result)

    return track_list

# --------
# Lookups
# --------


# --------
# Parameters
# --------
base_url = 'https://itunes.apple.com/search?term='
ampersand = '&'
parameters = {
    0: 'term=',
    1: 'country=',
    2: 'media=',
    3: 'entity=',
    4: 'attribute=',
    5: 'limit='
}

# --------
# Private
# --------
def _url_builder(term, country='US', media='music', entity='musicArtist', attribute=None, limit=50):
    built_url = base_url + _parse_query(term)
    built_url += ampersand + parameters[1] + country
    built_url += ampersand + parameters[2] + media
    built_url += ampersand + parameters[3] + entity

    if attribute is not None:
        built_url += ampersand + parameters[4] + attribute

    built_url += ampersand + parameters[5] + str(limit)

    return built_url

def _parse_query(query):
    return str(query).replace(' ', '+')
