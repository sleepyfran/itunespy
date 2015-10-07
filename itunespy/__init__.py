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
from itunespy import music_artist
from itunespy import music_album
from itunespy import movie_artist
from itunespy import ebook_artist
from itunespy import track
from itunespy import result_item

'''
    This is a simple module made in my free time. It's not perfect, but it works well.
    I'm accepting any pull request to improve it, just follow the code style.
    For examples and documentation, take a look at the README.md
'''

# --------
# Searches
# --------

'''
    term: The URL-encoded text string you want to search for. Example: Steven Wilson.
           The function will take care of spaces so you don't have to.
    country: The two-letter country code for the store you want to search.
              For a full list of the codes: http://en.wikipedia.org/wiki/%20ISO_3166-1_alpha-2
    media: The media type you want to search for. Since this module is made for music I recommend leaving it blank.
    entity: The type of results you want returned, relative to the specified media type. Example: musicArtist.
             Full list: musicArtist, musicTrack, album, musicVideo, mix, song
    attribute: The attribute you want to search for in the stores, relative to the specified media type.
    limit: The number of search results you want the iTunes Store to return.
'''

def search(term, country='US', media='all', entity=None, attribute=None, limit=50):
    search_url = _url_search_builder(term, country, media, entity, attribute, limit)
    r = requests.get(search_url)

    try:
        json = r.json()['results']
        result_count = r.json()['resultCount']
    except:
        raise ConnectionError(general_no_connection)

    if result_count == 0:
        raise LookupError(search_error + str(term))

    return _get_result_list(json)

# --------
# Lookups
# --------

'''
    - Note: You MUST provide at least one of these three id's
    id: iTunes ID of the artist/album/track
    artist_amg_id: All Music Guide ID of the artist
    upc: UPCs/EANs
    ---------------------------------------------------------------------------------------------------------------
    country: The two-letter country code for the store you want to search.
              For a full list of the codes: http://en.wikipedia.org/wiki/%20ISO_3166-1_alpha-2
    media: The media type you want to search for. Since this module is made for music I recommend leaving it blank.
    entity: The type of results you want returned, relative to the specified media type. Example: musicArtist.
             Full list: musicArtist, musicTrack, album, musicVideo, mix, song
    attribute: The attribute you want to search for in the stores, relative to the specified media type.
    limit: The number of search results you want the iTunes Store to return.
'''

# Defines a general lookup. Returns the a list with the artists, albums or tracks
def lookup(id=None, artist_amg_id=None, upc=None, country='US', media='all', entity=None, attribute=None, limit=50):
    # If none of the basic lookup arguments are provided, raise a ValueError
    if id is None and artist_amg_id is None and upc is None:
        raise ValueError(lookup_no_ids)

    lookup_url = _url_lookup_builder(id, artist_amg_id, upc, country, media, entity, attribute, limit)
    r = requests.get(lookup_url)

    try:
        json = r.json()['results']
        result_count = r.json()['resultCount']
    except:
        raise ConnectionError(general_no_connection)

    if result_count == 0:
        raise LookupError(lookup_error)

    return _get_result_list(json)

# --------
# Specific searches and lookups
# --------
# Music
def search_artist(term, country='US', attribute=None, limit=50):
    return search(term, country, 'music', entities['musicArtist'], attribute, limit)

def search_album(term, country='US', attribute=None, limit=50):
    return search(term, country, 'music', entities['album'], attribute, limit)

def search_track(term, country='US', attribute=None, limit=50):
    return search(term, country, 'music', entities['song'], attribute, limit)

def lookup_artist(id=None, artist_amg_id=None, upc=None, country='US', attribute=None, limit=50):
    return lookup(id, artist_amg_id, upc, country, 'music', entities['musicArtist'], attribute, limit)

def lookup_album(id=None, artist_amg_id=None, upc=None, country='US', attribute=None, limit=50):
    return lookup(id, artist_amg_id, upc, country, 'music', entities['album'], attribute, limit)

def lookup_track(id=None, artist_amg_id=None, upc=None, country='US', attribute=None, limit=50):
    return lookup(id, artist_amg_id, upc, country, 'music', entities['song'], attribute, limit)

# Movies
def search_director(term, country='US', attribute=None, limit=50):
    return search(term, country, 'movie', entities['movieArtist'], attribute, limit)

def search_movie(term, country='US', attribute=None, limit=50):
    return search(term, country, 'movie', entities['movie'], attribute, limit)

# Books
def search_book(term, country='US', attribute=None, limit=50):
    return search(term, country, 'ebook', entities['ebook'], attribute, limit)

def search_book_author(term, country='US', attribute=None, limit=50):
    return search(term, country, 'ebook', entities['ebookAuthor'], attribute, limit)

def lookup_book(id=None, artist_amg_id=None, upc=None, country='US', attribute=None, limit=50):
    return lookup(id, artist_amg_id, upc, country, 'ebook', entities['ebook'], attribute, limit)

def lookup_book_author(id=None, artist_amg_id=None, upc=None, country='US', attribute=None, limit=50):
    return lookup(id, artist_amg_id, upc, country, 'ebook', entities['ebookAuthor'], attribute, limit)

# TV Shows
def search_tv_episodes(term, country='US', attribute=None, limit=50):
    return search(term, country, 'tvShow', entities['tvEpisode'], attribute, limit)

def search_tv_season(term, country='US', attribute=None, limit=50):
    return search(term, country, 'tvShow', entities['tvSeason'], attribute, limit)

def lookup_tv_episodes(id=None, artist_amg_id=None, upc=None, country='US', attribute=None, limit=50):
    return lookup(id, artist_amg_id, upc, country, 'tvShow', entities['tvEpisode'], attribute, limit)

def lookup_tv_season(id=None, artist_amg_id=None, upc=None, country='US', attribute=None, limit=50):
    return lookup(id, artist_amg_id, upc, country, 'tvShow', entities['tvSeason'], attribute, limit)

# Software
def search_software(term, country='US', attribute=None, limit=50):
    return search(term, country, 'software', entities['software'], attribute, limit)

def search_ipad_software(term, country='US', attribute=None, limit=50):
    return search(term, country, 'software', entities['iPadSoftware'], attribute, limit)

def search_mac_software(term, country='US', attribute=None, limit=50):
    return search(term, country, 'software', entities['macSoftware'], attribute, limit)
# --------
# Parameters
# --------
base_search_url = 'https://itunes.apple.com/search?term='
base_lookup_url = 'https://itunes.apple.com/lookup?'
ampersand = '&'
entities = {
    'movieArtist': 'movieArtist',
    'movie': 'movie',
    'podcastAuthor': 'podcastAuthor',
    'podcast': 'podcast',
    'musicArtist': 'musicArtist',
    'musicTrack': 'musicTrack',
    'album': 'album',
    'musicVideo': 'musicVideo',
    'mix': 'mix',
    'song': 'song',
    'audiobookAuthor': 'audiobookAuthor',
    'audiobook': 'audiobook',
    'shortFilmArtist': 'shortFilmArtist',
    'shortFilm': 'shortFilm',
    'tvEpisode': 'tvEpisode',
    'tvSeason': 'tvSeason',
    'software': 'software',
    'iPadSoftware': 'iPadSoftware',
    'macSoftware': 'macSoftware',
    'ebook': 'ebook',
    'ebookAuthor': 'ebookAuthor',
    'all': 'all',
    'allArtist': 'allArtist',
    'allTrack': 'allTrack'
}
parameters = {
    0: 'term=',
    1: 'country=',
    2: 'media=',
    3: 'entity=',
    4: 'attribute=',
    5: 'limit=',
    6: 'id=',
    7: 'amgArtistId=',
    8: 'upc='
}
general_no_connection = 'Cannot fetch JSON data'
search_error = 'No results found with the keyword '
artist_search_error = 'No artists found with the keyword '
album_search_error = 'No albums found with the keyword '
track_search_error = 'No tracks found with the keyword '
lookup_error = 'No results with the given parameters'
lookup_no_ids = 'No id, amg id or upc arguments provided'

# --------
# Private
# --------
def _get_result_list(json):
    result_list = []

    for item in json:
        if 'wrapperType' in item:
            # Music
            if item['wrapperType'] == 'artist' and item['artistType'] == 'Artist':
                music_artist_result = music_artist.MusicArtist(item)
                result_list.append(music_artist_result)
            elif item['wrapperType'] == 'collection' and item['collectionType'] == 'Album':
                music_album_result = music_album.MusicAlbum(item)
                result_list.append(music_album_result)
            elif item['wrapperType'] == 'track' and item['kind'] == 'song':
                music_track_result = track.Track(item)
                result_list.append(music_track_result)
            elif item['wrapperType'] == 'track' and item['kind'] == 'music-video':
                music_video_result = track.Track(item)
                result_list.append(music_video_result)
            # Movies
            elif item['wrapperType'] == 'artist' and item['artistType'] == 'Movie Artist':
                movie_artist_result = movie_artist.MovieArtist(item)
                result_list.append(movie_artist_result)
            elif item['wrapperType'] == 'track' and item['kind'] == 'feature-movie':
                movie_result = track.Track(item)
                result_list.append(movie_result)
            # Ebook Author
            elif item['wrapperType'] == 'artist' and item['artistType'] == 'Author':
                ebook_artist_result = ebook_artist.EbookArtist(item)
                result_list.append(ebook_artist_result)
            # Tv Shows
            elif item['wrapperType'] == 'collection' and item['collectionType'] == 'TV Season':
                tv_season_result = result_item.ResultItem(item)
                result_list.append(tv_season_result)
            elif item['wrapperType'] == 'track' and item['kind'] == 'tv-episode':
                tv_episode_result = track.Track(item)
                result_list.append(tv_episode_result)
            # Software
            elif item['wrapperType'] == 'software' and item['kind'] == 'software':
                software_result = result_item.ResultItem(item)
                result_list.append(software_result)
            elif item['wrapperType'] == 'software' and item['kind'] == 'mac-software':
                mac_software_result = result_item.ResultItem(item)
                result_list.append(mac_software_result)

        elif 'kind' in item:
            if item['kind'] == 'ebook':
                ebook_result = result_item.ResultItem(item)
                result_list.append(ebook_result)
        else:
            unknown_result = result_item.ResultItem(item)
            result_list.append(unknown_result)

    return result_list


def _url_search_builder(term, country='US', media='all', entity=None, attribute=None, limit=50):
    built_url = base_search_url + _parse_query(term)
    built_url += ampersand + parameters[1] + country
    built_url += ampersand + parameters[2] + media

    if entity is not None:
        built_url += ampersand + parameters[3] + entity

    if attribute is not None:
        built_url += ampersand + parameters[4] + attribute

    built_url += ampersand + parameters[5] + str(limit)

    return built_url


def _url_lookup_builder(id=None, artist_amg_id=None, upc=None, country='US', media='music', entity=None, attribute=None,
                        limit=50):
    built_url = base_lookup_url
    has_one_argument = False

    if id is not None:
        built_url += parameters[6] + str(id)
        has_one_argument = True

    if artist_amg_id is not None:
        if has_one_argument:
            built_url += ampersand + parameters[7] + artist_amg_id
        else:
            built_url += parameters[7] + str(artist_amg_id)
            has_one_argument = True

    if upc is not None:
        if has_one_argument:
            built_url += ampersand + parameters[8] + upc
        else:
            built_url += parameters[8] + str(upc)

    built_url += ampersand + parameters[1] + country
    built_url += ampersand + parameters[2] + media

    if entity is not None:
        built_url += ampersand + parameters[3] + entity

    if attribute is not None:
        built_url += ampersand + parameters[4] + attribute

    built_url += ampersand + parameters[5] + str(limit)

    return built_url


def _parse_query(query):
    return str(query).replace(' ', '+')
