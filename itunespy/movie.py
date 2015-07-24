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

from itunespy import result_item

class Movie(result_item.ResultItem):
    def __init__(self, json):
        result_item.ResultItem.__init__(self, json)

    # Only for debugging purposes
    def print_info(self):
        result_item.ResultItem.print_info(self)