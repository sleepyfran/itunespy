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
from typing import Any, Dict

from itunespy import result_item

class Track(result_item.ResultItem):
    """
    Defines a Track whether it's a music track or a movie or a show episode
    """
    def get_track_time_minutes(self, round_number: int = 2) -> float:
        """
        Retrieves the track's length and converts it to minutes
        :param round_number: Int. Number of decimals to round the minutes
        :return: Float. Track length in minutes
        """
        return round(self.track_time / 60000, round_number)

    def get_track_time_hours(self, round_number: int = 2) -> float:
        """
        Retrieves the track's length and converts it to hours
        :param round_number: Int. Number of decimals to round the hours
        :return: Float. Track length in hours
        """
        return round(self.track_time / 6000000, round_number)
