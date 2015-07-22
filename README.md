# itunespy

itunespy is a simple library to fetch data from the iTunes Store API made for Python 3.X. 

**This project is a work in progress**

## Installing
In order to install the module simply clone this project anywhere in your computer:

    git clone https://github.com/spaceisstrange/itunespy.git

And then enter the cloned repo and execute:

    python setup.py install

I'll add the package to pip once it reaches the final release.

## Examples
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

## Documentation
Coming soon.