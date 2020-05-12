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

'''
    This is a simple module made in my free time. It's not perfect, but it works well.
    I'm accepting any pull request to improve it, just follow the code style.
    For examples and documentation, take a look at the README.md
'''

from typing import Any, Dict, List, Union

import pycountry
import requests
from urllib.parse import urlencode
from itunespy import artist
from itunespy import music_artist
from itunespy import music_album
from itunespy import movie_artist
from itunespy import ebook_artist
from itunespy import track
from itunespy import result_item


# --------
# Searches
# --------
def search(
        term: str,
        country: str = 'US',
        media: str = 'all',
        entity: str = None,
        attribute: str = None,
        limit: int = 50) -> List[result_item.ResultItem]:
    """
    Returns the result of the search of the specified term in an array of result_item(s)
    :param term: String. The URL-encoded text string you want to search for. Example: Steven Wilson.
                 The method will take care of spaces so you don't have to.
    :param country: String. The two-letter country code for the store you want to search.
                    For a full list of the codes: http://en.wikipedia.org/wiki/%20ISO_3166-1_alpha-2
    :param media: String. The media type you want to search for. Example: music
    :param entity: String. The type of results you want returned, relative to the specified media type. Example: musicArtist.
                   Full list: musicArtist, musicTrack, album, musicVideo, mix, song
    :param attribute: String. The attribute you want to search for in the stores, relative to the specified media type.
    :param limit: Integer. The number of search results you want the iTunes Store to return.
    :return: An array of result_item(s)
    """
    search_url = _url_search_builder(term, country, media, entity, attribute, limit)
    r = requests.get(search_url)

    try:
        json = r.json()['results']
        result_count = r.json()['resultCount']
    except:
        raise ConnectionError(general_no_connection)

    if result_count == 0:
        raise LookupError(search_error + str(term))

    return _get_result_list(json, country)

# --------
# Lookups
# --------
def lookup(
        id: Union[str, int] = None,
        artist_amg_id: Union[str, int] = None,
        upc: Union[str, int] = None,
        country: str = 'US',
        media: str = 'all',
        entity: str = None,
        attribute: str = None,
        limit: int = 50) -> List[result_item.ResultItem]:
    """
    Returns the result of the lookup of the specified id, artist_amg_id or upc in an array of result_item(s)
    :param id: String. iTunes ID of the artist, album, track, ebook or software
    :param artist_amg_id: String. All Music Guide ID of the artist
    :param upc: String. UPCs/EANs
    :param country: String. The two-letter country code for the store you want to search.
                    For a full list of the codes: http://en.wikipedia.org/wiki/%20ISO_3166-1_alpha-2
    :param media: String. The media type you want to search for. Example: music
    :param entity: String. The type of results you want returned, relative to the specified media type. Example: musicArtist.
                   Full list: musicArtist, musicTrack, album, musicVideo, mix, song
    :param attribute: String. The attribute you want to search for in the stores, relative to the specified media type.
    :param limit: Integer. The number of search results you want the iTunes Store to return.
    :return: An array of result_item(s)
    """
    # If none of the basic lookup arguments are provided, raise a ValueError
    if id is None and artist_amg_id is None and upc is None:
        raise ValueError(lookup_no_ids)

    lookup_url = _url_lookup_builder(id, artist_amg_id, upc, country, media, entity, attribute, limit)
    r = requests.get(lookup_url)

    try:
        json = r.json()['results']
        result_count = r.json()['resultCount']
    except KeyError:
        raise ConnectionError(general_no_connection)

    if result_count == 0:
        raise LookupError(lookup_error)

    return _get_result_list(json, country)

# --------
# Specific searches and lookups
# --------
# Music
def search_artist(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[music_artist.MusicArtist]:
    return search(term, country, 'music', entities['musicArtist'], attribute, limit)  # type: ignore

def search_album(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[music_album.MusicAlbum]:
    return search(term, country, 'music', entities['album'], attribute, limit)  # type: ignore

def search_track(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[track.Track]:
    return search(term, country, 'music', entities['song'], attribute, limit)  # type: ignore

def lookup_artist(id: Union[str, int] = None, artist_amg_id: Union[str, int] = None, upc: Union[str, int] = None, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, artist_amg_id, upc, country, 'music', entities['musicArtist'], attribute, limit)

def lookup_album(id: Union[str, int] = None, artist_amg_id: Union[str, int] = None, upc: Union[str, int] = None, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, artist_amg_id, upc, country, 'music', entities['album'], attribute, limit)

def lookup_track(id: Union[str, int] = None, artist_amg_id: Union[str, int] = None, upc: Union[str, int] = None, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, artist_amg_id, upc, country, 'music', entities['song'], attribute, limit)

# Movies
def search_director(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[artist.Artist]:
    # Unfortunately 'movieArtist' is not a valid entity so this method may return other artist types as well.
    # Example: Search term 'Michael'
    return search(term, country, 'movie', entities['movieArtist'], attribute, limit)  # type: ignore

def search_movie(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[track.Track]:
    return search(term, country, 'movie', entities['movie'], attribute, limit)  # type: ignore

def lookup_directory(id: Union[str, int], country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, None, None, country, 'movie', entities['movieArtist'], attribute, limit)

def lookup_movie(id: Union[str, int], country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, None, None, country, 'movie', entities['movie'], attribute, limit)

# Books
def search_book(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return search(term, country, 'ebook', entities['ebook'], attribute, limit)

def search_book_author(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[artist.Artist]:
    # Unfortunately 'ebookAuthor' is not a valid entity so this method may return other artist types as well.
    # Example: Search term 'test'
    return search(term, country, 'ebook', entities['ebookAuthor'], attribute, limit)  # type: ignore

def lookup_book(id: Union[str, int] = None, artist_amg_id: Union[str, int] = None, upc: Union[str, int] = None, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, artist_amg_id, upc, country, 'ebook', entities['ebook'], attribute, limit)

def lookup_book_author(id: Union[str, int] = None, artist_amg_id: Union[str, int] = None, upc: Union[str, int] = None, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, artist_amg_id, upc, country, 'ebook', entities['ebookAuthor'], attribute, limit)

# TV Shows
def search_tv_episodes(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return search(term, country, 'tvShow', entities['tvEpisode'], attribute, limit)

def search_tv_season(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return search(term, country, 'tvShow', entities['tvSeason'], attribute, limit)

def lookup_tv_episodes(id: Union[str, int] = None, artist_amg_id: Union[str, int] = None, upc: Union[str, int] = None, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, artist_amg_id, upc, country, 'tvShow', entities['tvEpisode'], attribute, limit)

def lookup_tv_season(id: Union[str, int] = None, artist_amg_id: Union[str, int] = None, upc: Union[str, int] = None, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return lookup(id, artist_amg_id, upc, country, 'tvShow', entities['tvSeason'], attribute, limit)

# Software
def search_software(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return search(term, country, 'software', entities['software'], attribute, limit)

def search_ipad_software(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return search(term, country, 'software', entities['iPadSoftware'], attribute, limit)

def search_mac_software(term: str, country: str = 'US', attribute: str = None, limit: int = 50) -> List[result_item.ResultItem]:
    return search(term, country, 'software', entities['macSoftware'], attribute, limit)
# --------
# Parameters
# --------
base_search_url = 'https://itunes.apple.com/search'
base_lookup_url = 'https://itunes.apple.com/lookup'
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
def _get_result_list(json: List[Dict[str, Any]], country: str) -> List[result_item.ResultItem]:
    """
    Analyzes the provided JSON data and returns an array of result_item(s) based on its content
    :param json: Raw JSON data to analyze
    :return: An array of result_item(s) from the provided JSON data
    """
    result_list: List[result_item.ResultItem] = []

    for item in json:
        if 'country' not in item:
            item['country'] = pycountry.countries.get(alpha_2=country).alpha_3
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

        elif 'kind' in item and item['kind'] == 'ebook':
            ebook_result = result_item.ResultItem(item)
            result_list.append(ebook_result)
        else:
            unknown_result = result_item.ResultItem(item)
            result_list.append(unknown_result)

    return result_list


def _url_search_builder(
        term: str,
        country: str = 'US',
        media: str = 'all',
        entity: str = None,
        attribute: str = None,
        limit: int = 50) -> str:
    """
    Builds the URL to perform the search based on the provided data
    :param term: String. The URL-encoded text string you want to search for. Example: Steven Wilson.
                 The method will take care of spaces so you don't have to.
    :param country: String. The two-letter country code for the store you want to search.
                    For a full list of the codes: http://en.wikipedia.org/wiki/%20ISO_3166-1_alpha-2
    :param media: String. The media type you want to search for. Example: music
    :param entity: String. The type of results you want returned, relative to the specified media type. Example: musicArtist.
                   Full list: musicArtist, musicTrack, album, musicVideo, mix, song
    :param attribute: String. The attribute you want to search for in the stores, relative to the specified media type.
    :param limit: Integer. The number of search results you want the iTunes Store to return.
    :return: The built URL as a string
    """
    query = {
        "term": term,
        "country": country,
        "media": media,
        "limit": limit
    }
    if entity is not None:
        query["entity"] = entity
    if attribute is not None:
        query["attribute"] = attribute

    return base_search_url + "?" + urlencode(query)


def _url_lookup_builder(id: Union[str, int] = None,
                        artist_amg_id: Union[str, int] = None,
                        upc: Union[str, int] = None,
                        country: str = 'US',
                        media: str = 'music',
                        entity: str = None,
                        attribute: str = None,
                        limit: int = 50) -> str:
    """
    Builds the URL to perform the lookup based on the provided data
    :param id: String. iTunes ID of the artist, album, track, ebook or software
    :param artist_amg_id: String. All Music Guide ID of the artist
    :param upc: String. UPCs/EANs
    :param country: String. The two-letter country code for the store you want to search.
                    For a full list of the codes: http://en.wikipedia.org/wiki/%20ISO_3166-1_alpha-2
    :param media: String. The media type you want to search for. Example: music
    :param entity: String. The type of results you want returned, relative to the specified media type. Example: musicArtist.
                   Full list: musicArtist, musicTrack, album, musicVideo, mix, song
    :param attribute: String. The attribute you want to search for in the stores, relative to the specified media type.
    :param limit: Integer. The number of search results you want the iTunes Store to return.
    :return: The built URL as a string
    """
    query = {
        "country": country,
        "media": media,
        "limit": limit
    }
    has_one_argument = False

    if id is not None:
        query["id"] = id
    if artist_amg_id is not None:
        query["amgArtistId"] = artist_amg_id
    if upc is not None:
        query["upc"] = upc

    if entity is not None:
        query["entity"] = entity
    if attribute is not None:
        query["attribute"] = attribute

    return base_lookup_url + "?" + urlencode(query)
