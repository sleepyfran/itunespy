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
import json
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from datetime import datetime

import copy
import pycountry


import pycountry

class ResultItem(object):
    """
    Defines a general result item
    """

    if TYPE_CHECKING:
        # These fields are dynamically queried. They are defined here to help
        # type checkers and IDEs.
        primary_genre_id: int
        primary_genre_name: str

        artist_id: int
        amg_artist_id: int
        artist_name: str
        artist_link_url: str
        artist_view_url: str

        track_id: int
        track_name: str
        track_censored_name: str
        track_view_url: str
        track_number: int
        track_count: int
        preview_url: str
        artwork_url_30: str
        artwork_url_60: str
        artwork_url_100: str
        artwork_url_512: str
        track_price: float
        track_hd_price: float
        track_rental_price: float
        track_hd_rental_price: float
        release_date: str
        track_explicitness: str
        disc_count: int
        disc_number: int
        country: str
        currency: str
        content_advisory_rating: str
        short_description: str
        long_description: str
        is_streamable: bool

        collection_id: int
        collection_name: str
        collection_censored_name: str
        collection_view_url: str
        collection_price: float
        collection_hd_price: float
        collection_explicitness: str
        copyright: str

        genres: List[str]
        genre_ids: List[str]
        price: float
        description: str
        formatted_price: str

        artist_ids: List[str]
        average_user_rating: float
        user_rating_count: int
        average_user_rating_for_current_version: float
        user_rating_count_for_current_version: int
        screenshort_urls: List[str]
        ipad_screenshot_urls: List[str]
        features: List[str]
        supported_devices: List[str]
        advisories: List[str]
        is_game_center_enabled: bool
        track_content_rating: str
        version: str
        seller_name: str
        seller_url: str
        bundle_id: str
        release_notes: str
        is_vpp_device_based_licensing_enabled: bool
        minimum_os_version: str

    def __init__(self, json: Dict[str, Any]) -> None:
        """
        Initializes the ResultItem class from the JSON provided
        :param json: String. Raw JSON data to fetch information from.
        The country is used for further requests from this item.
        """
        self.json = copy.deepcopy(json)

    @property
    def type(self) -> str:
        return self.json.get('wrapperType') or self.kind  # type: ignore

    @property
    def track_type(self) -> str:
        if 'wrapperType' in self.json:
            return self.kind  # type: ignore
        else:
            raise AttributeError

    @property
    def artist_radio_url(self) -> str:
        return self.json["radioStationUrl"]  # type: ignore

    @property
    def track_time(self) -> int:
        return self.json["trackTimeMillis"]  # type: ignore

    @property
    def file_size(self) -> int:
        return self.json["fileSizeBytes"]  # type: ignore

    @property
    def language_codes(self) -> List[str]:
        return self.json["languageCodesISO2A"]  # type: ignore

    def get_artwork_url(self, size: int = 1500) -> str:
        """
        Returns the artwork URL for this item. The URL refers to an artwork
        image of the specified size (or smaller if the size is larger than the
        maximum available image size).
        :param size: The maximum size the returned image should have. Usually
                     artwork images are available up to 600x600 pixels.
        """
        return self.artwork_url_100.replace('100x100', f'{size}x{size}')

    if sys.version_info >= (3, 7):
        @property
        def parsed_release_date(self) -> datetime:
            """
            Returns a datetime representation of the item's release_date. This
            method is only available when using Python 3.7 or later.
            """
            return datetime.fromisoformat(self.release_date.replace('Z', '+00:00'))

    def get_country(self, format: str = 'alpha_2') -> str:
        """
        Returns the item's country in the specified format.

        :param format: The format specifier. Must be supported by pycountry.
                       Valid formats include 'alpha_2', 'alpha_3' and 'name'.
        :return: String. The item's country in the specified format.
        """
        return getattr(pycountry.countries.get(alpha_3=self.country), format)  # type: ignore

    def __getattr__(self, item: str) -> Any:
        components = item.split('_')
        key = components[0] + ''.join(x.title() for x in components[1:])
        try:
            return self.json[key]
        except KeyError:
            raise AttributeError from None

    def __repr__(self) -> str:
        """
        Retrieves all keys in the class as a String
        :return: String. All the keys available in the class
        """
        return json.dumps(self.json, indent=2)
