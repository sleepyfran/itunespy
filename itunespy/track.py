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

class Track:
    def __init__(self, json):
        if 'artistId' in json:
            self.artist_id = json['artistId']
        else:
            self.artist_id = None

        if 'collectionId' in json:
            self.album_id = json['collectionId']
        else:
            self.album_id = None

        if 'trackId' in json:
            self.track_id = json['trackId']
        else:
            self.track_id = None

        if 'artistName' in json:
            self.artist_name = json['artistName']
        else:
            self.artist_name = None

        if 'collectionName' in json:
            self.album_name = json['collectionName']
        else:
            self.album_name = None

        if 'trackName' in json:
            self.track_name = json['trackName']
        else:
            self.track_name = None

        if 'collectionCensoredName' in json:
            self.album_censored_name = json['collectionCensoredName']
        else:
            self.album_censored_name = None

        if 'trackCensoredName' in json:
            self.track_censored_name = json['trackCensoredName']
        else:
            self.track_censored_name = None

        if 'artistViewUrl' in json:
            self.artist_view_url = json['artistViewUrl']
        else:
            self.artist_view_url = None

        if 'collectionViewUrl' in json:
            self.album_view_url = json['collectionViewUrl']
        else:
            self.album_view_url = None

        if 'trackViewUrl' in json:
            self.track_view_url = json['trackViewUrl']
        else:
            self.track_view_url = None

        if 'previewUrl' in json:
            self.preview_url = json['previewUrl']
        else:
            self.preview_url = None

        if 'artworkUrl30' in json:
            self.artwork_url_30 = json['artworkUrl30']
        else:
            self.artwork_url_30 = None

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

        if 'trackPrice' in json:
            self.track_price = json['trackPrice']
        else:
            self.track_price = None

        if 'releaseDate' in json:
            self.release_date = json['releaseDate']
        else:
            self.release_date = None

        if 'collectionExplicitness' in json:
            self.album_explicitness = json['collectionExplicitness']
        else:
            self.album_explicitness = None

        if 'trackExplicitness' in json:
            self.track_explicitness = json['trackExplicitness']
        else:
            self.track_explicitness = None

        if 'discCount' in json:
            self.disc_count = json['discCount']
        else:
            self.disc_count = None

        if 'discNumber' in json:
            self.disc_number = json['discNumber']
        else:
            self.disc_number = None

        if 'trackCount' in json:
            self.track_count = json['trackCount']
        else:
            self.track_count = None

        if 'trackNumber' in json:
            self.track_number = json['trackNumber']
        else:
            self.track_number = None

        if 'trackTimeMillis' in json:
            self.track_time = json['trackTimeMillis']
        else:
            self.track_time = None

        if 'country' in json:
            self.country = json['country']
        else:
            self.country = None

        if 'currency' in json:
            self.currency = json['currency']
        else:
            self.currency = None

        if 'primaryGenreName' in json:
            self.genre_name = json['primaryGenreName']
        else:
            self.genre_name = None

        if 'radioStationUrl' in json:
            self.radio_station_url = json['radioStationUrl']
        else:
            self.radio_station_url = None

        if 'isStreamable' in json:
            self.is_streamable = json['isStreamable']
        else:
            self.is_streamable = None

    def print_info(self):
        print(self.artist_id)
        print(self.album_id)
        print(self.track_id)
        print(self.artist_name)
        print(self.album_name)
        print(self.track_name)
        print(self.album_censored_name)
        print(self.track_censored_name)
        print(self.artist_view_url)
        print(self.album_view_url)
        print(self.track_view_url)
        print(self.preview_url)
        print(self.artwork_url_30)
        print(self.artwork_url_60)
        print(self.artwork_url_100)
        print(self.album_price)
        print(self.track_price)
        print(self.release_date)
        print(self.album_explicitness)
        print(self.track_explicitness)
        print(self.disc_count)
        print(self.disc_number)
        print(self.track_count)
        print(self.track_number)
        print(self.track_time)
        print(self.country)
        print(self.currency)
        print(self.genre_name)
        print(self.radio_station_url)
        print(self.is_streamable)
