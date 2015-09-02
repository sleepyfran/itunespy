# Version 1.5
- Now you can get a Track time in *minutes* and *hours* using get_track_time_minutes() and get_track_time_hours()
- The function get_tracks() in MusicAlbum now stores all tracks in _track_list if it's empty
- You can also get the full playing time of an album using get_album_time()
- search_director and search_movie implemented

# Version 1.3
- Deprecated use of artist_genre_name and artist_genre_id in favor of primary_genre_name and primary_genre_id since those properties can be in artists, albums, tracks and more.

# Version 1.2.1
- Removed unused dependency

# Version 1.2
- Now you can simply str() result_item (and any subclass) to show all its properties

# Version 1.1
- Solved missing track_id

# Version 1.0
- Initial release
