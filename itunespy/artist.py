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

class Artist:
    def __init__(self, json):
        if 'artistName' in json:
            self.artist_name = json['artistName']
        else:
            self.artist_name = None

        if 'artistLinkUrl' in json:
            self.artist_link_url = json['artistLinkUrl']
        else:
            self.artist_link_url = None

        if 'artistId' in json:
            self.artist_id = json['artistId']
        else:
            self.artist_id = None

        if 'amgArtistId' in json:
            self.artist_amg_id = json['amgArtistId']
        else:
            self.artist_amg_id = None

        if 'primaryGenreName' in json:
            self.artist_genre_name = json['primaryGenreName']
        else:
            self.artist_genre_name = None

        if 'primaryGenreId' in json:
            self.artist_genre_id = json['primaryGenreId']
        else:
            self.artist_genre_id = None

        if 'radioStationUrl' in json:
            self.artist_radio_url = json['radioStationUrl']
        else:
            self.artist_radio_url = None

    # For debugging purposes
    def print_info(self):
        print(self.artist_name)
        print(self.artist_link_url)
        print(self.artist_id)
        print(self.artist_amg_id)
        print(self.artist_genre_name)
        print(self.artist_genre_id)
        print(self.artist_link_url)
        print()
