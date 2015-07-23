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

import itunespy

class MusicAlbum:
    def __init__(self, json):
        if 'artistId' in json:
            self.artist_id = json['artistId']
        else:
            self.artist_id = None

        if 'collectionId' in json:
            self.album_id = json['collectionId']
        else:
            self.album_id = None

        if 'amgArtistId' in json:
            self.artist_amg_id = json['amgArtistId']
        else:
            self.artist_amg_id = None

        if 'artistName' in json:
            self.artist_name = json['artistName']
        else:
            self.artist_name = None

        if 'collectionName' in json:
            self.album_name = json['collectionName']
        else:
            self.album_name = None

        if 'collectionCensoredName' in json:
            self.album_censored_name = json['collectionCensoredName']
        else:
            self.album_censored_name = None

        if 'artistViewUrl' in json:
            self.artist_view_url = json['artistViewUrl']
        else:
            self.artist_view_url = None

        if 'collectionViewUrl' in json:
            self.album_view_url = json['collectionViewUrl']
        else:
            self.album_view_url = None

        if 'artworkUrl60' in json:
            self.artwork_url_60 = json['artworkUrl60']
        else:
            self.artwork_url_60 = None

        if 'artworkUrl100' in json:
            self.artwork_url_100 = json['artworkUrl100']
        else:
            self.artwork_url_100 = None

        if 'collectionPrice' in json:
            self.album_price = json['collectionPrice']
        else:
            self.album_price = None

        if 'collectionExplicitness' in json:
            self.album_explicitness = json['collectionExplicitness']
        else:
            self.album_explicitness = None

        if 'contentAdvisoryRating' in json:
            self.album_content_advisor_rating = json['contentAdvisoryRating']
        else:
            self.album_content_advisor_rating = None

        if 'trackCount' in json:
            self.track_count = json['trackCount']
        else:
            self.track_count = None

        if 'copyright' in json:
            self.copyright = json['copyright']
        else:
            self.copyright = None

        if 'country' in json:
            self.country = json['country']
        else:
            self.country = None

        if 'currency' in json:
            self.currency = json['currency']
        else:
            self.currency = None

        if 'releaseDate' in json:
            self.release_date = json['releaseDate']
        else:
            self.release_date = None

        if 'primaryGenreName' in json:
            self.genre = json['primaryGenreName']
        else:
            self.genre = None

    def get_tracks(self):
        return itunespy.lookup(id=self.album_id, entity='song')[1:]

    # For debugging purposes
    def print_info(self):
        print(self.artist_id)
        print(self.album_id)
        print(self.artist_amg_id)
        print(self.artist_name)
        print(self.album_name)
        print(self.album_censored_name)
        print(self.artist_view_url)
        print(self.album_view_url)
        print(self.artwork_url_60)
        print(self.artwork_url_100)
        print(self.album_price)
        print(self.album_explicitness)
        print(self.track_count)
        print(self.copyright)
        print(self.country)
        print(self.currency)
        print(self.release_date)
        print(self.genre)
        print()
