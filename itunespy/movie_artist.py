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
from typing import Any, Dict, List

import itunespy
from itunespy import result_item, track


class MovieArtist(result_item.ResultItem):
    """
    Defines an Movie Artist
    """
    def __init__(self, json: Dict[str, Any]) -> None:
        """
        Initializes the ResultItem class from the JSON provided
        :param json: String. Raw JSON data to fetch information from
        """
        result_item.ResultItem.__init__(self, json)

    def get_movies(self) -> List[track.Track]:
        """
        Retrieves all the movies published by the artist
        :return: List. Movies published by the artist
        """
        return itunespy.lookup_movie(
            id=self.artist_id,
            country=self.get_country()
        )[1:]
