# itunespy

itunespy is a simple library to fetch data from the iTunes Store API made for Python 3.X. 

**This project is a work in progress**

## Installing
In order to install the module simply clone this project anywhere in your computer:

    git clone https://github.com/spaceisstrange/itunespy.git

And then enter the cloned repo and execute:

    python setup.py install

I'll add the package to pip once it reaches the final release.

## Examples and information
Search an artist and show all its album's names:

```python
import itunespy

artist = itunespy.search_artist('Steven Wilson') # Returns a list
albums = artist[0].get_albums() # Get albums from the first result

for album in albums:
    print(album.album_name)
```

Or search an album and show all its song's names:

```python
import itunespy

album = itunespy.search_album('One Hour By The Concrete Lake') # Returns a list
tracks = album[0].get_tracks() # Get tracks from the first result

for track in tracks:
    print(track.artist_name + ': ' + track.track_name)
```

Or search for a track:

```python
import itunespy

track = itunespy.search_track('Iter Impius') # Returns a list
print(track[0].artist_name + ': ' + track[0].track_name) # Get info from the first result
```

You can also perform a lookup:
```python
import itunespy

lookup = itunespy.lookup(upc=720642462928) # Lookup for the Weezer's album 'Weezer'

for item in lookup:
    print(item.artist_name + ': ' + item.album_name)
```

Each request has some parameters that you need to know. Searches has these:
    
    term: The URL-encoded text string you want to search for. Example: Steven Wilson.
           The function will take care of spaces so you don't have to.
    country: The two-letter country code for the store you want to search.
              For a full list of the codes: http://en.wikipedia.org/wiki/%20ISO_3166-1_alpha-2
    media: The media type you want to search for. Since this module is made for music I recommend leaving it blank.
    entity: The type of results you want returned, relative to the specified media type. Example: musicArtist.
             Full list: musicArtist, musicTrack, album, musicVideo, mix, song
    attribute: The attribute you want to search for in the stores, relative to the specified media type.
    limit: The number of search results you want the iTunes Store to return.
    
**Note**: Only the *term* is obligatory, the other ones have default values that will be used in case you don't provide any.

For lookups, the same parameters apply except for *term*, that changes to a couple of id fields:
    
    id: iTunes ID of the artist/album/track
    artist_amg_id: All Music Guide ID of the artist
    upc: UPCs/EANs

Every search and lookup will **always** return a list of artists, albums or tracks instances. Each object has their own variables, following the iTune's API names adapted to Python syntax.

To take a look at all of this simply go to the (artist)['https://github.com/spaceisstrange/itunespy/blob/master/itunespy/artist.py'], (album)['https://github.com/spaceisstrange/itunespy/blob/master/itunespy/album.py'] or the (track)['https://github.com/spaceisstrange/itunespy/blob/master/itunespy/track.py'] classes.