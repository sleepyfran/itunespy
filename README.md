# itunespy [![PyPI version](https://badge.fury.io/py/itunespy.svg)](http://badge.fury.io/py/itunespy)

itunespy is a simple library to fetch data from the iTunes Store API made for Python 3.5 and beyond.

**Important**: Since version 1.6 _itunespy_ no longer supports versions below Python 3.5. You can still use any previous versions but those won't get any further updates or features.

## Installing
You can install it from *pip*:
    
    pip install itunespy

Or you can simply clone this project anywhere in your computer:

    git clone https://github.com/sleepyfran/itunespy.git

And then enter the cloned repo and execute:

    python setup.py install
## Dependencies

itunespy requires [Requests](https://github.com/kennethreitz/requests) and [pycountry](https://github.com/flyingcircusio/pycountry) installed.

## Examples and information
Search an artist and show all its album's names:

```python
import itunespy

artist = itunespy.search_artist('Steven Wilson')  # Returns a list
albums = artist[0].get_albums()  # Get albums from the first result

for album in albums:
    print(album.collection_name)
```

Or search an album and show all its song's names and length, and finally the album length:

```python
import itunespy

album = itunespy.search_album('One Hour By The Concrete Lake')  # Returns a list
tracks = album[0].get_tracks()  # Get tracks from the first result

for track in tracks:
    print(track.artist_name + ': ' + track.track_name + str(track.get_track_time_minutes()))
print('Total playing time: ' + str(album[0].get_album_time()))
```

Or search for a track:

```python
import itunespy

track = itunespy.search_track('Iter Impius')  # Returns a list
print(track[0].artist_name + ': ' + track[0].track_name + ' | Length: ' + str(track[0].get_track_time_minutes())) # Get info from the first result
```

Or ebook authors:

```python    
import itunespy

author = itunespy.search_book_author('Fyodor Dostoevsky')  # Search for Dostoevsky

books = author[0].get_books()  # Get books from the firs result

for book in books:
    print(book.track_name)  # Show each book's name
```

Or software:
```python    
import itunespy

telegram = itunespy.search_software('Telegram')

print(telegram[0].track_name)  # Prints 'Telegram Messenger'
```

Basically, every *search_* method is just an alias for a general search with certain parameters to make your life easier.

I made the basic ones, if you miss any, make an issue and provide information about the type you want added.

You can also perform a lookup:

```python
import itunespy

lookup = itunespy.lookup(upc=720642462928) # Lookup for the Weezer's album 'Weezer'

for item in lookup:
    print(item.artist_name + ': ' + item.collection_name)
```

Since every search or lookup can return more than one object type, every object in the returned list has a 'type' property, so you can check if it's an artist, album or track like this:
```python
import itunespy

lookup = itunespy.lookup(id=428011728)  # Steven Wilson's ID

for l in lookup:
    if l.type == 'artist':
        print('Artist!')
        print(l.artist_type)  # Since it's an artist, you can also check its artist type
```

For a complete list, take a look at the *wrapperType* and *kind* documentation in the iTunes API's site.

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
**Note 2**: In specific searches, like *search_artist* or *search_album*, etc, don't change entity, since it's configured inside the function to retrieve an specific entity.

For lookups, the same parameters apply except for *term*, which changes to a couple of id fields:
    
    id: iTunes ID of the artist/album/track
    artist_amg_id: All Music Guide ID of the artist
    upc: UPCs/EANs

Every search and lookup will **always** return a list of *result_item* instances, except if it's an artist, album, movie artist or an ebook author, which inheritates from *result_item* but has extra methods, like *get_albums* in *music_artist*. Each object has their own variables, following the iTunes API names adapted to Python syntax.

To take a look at all of this simply go to the [item_result](https://github.com/sleepyfran/itunespy/blob/master/itunespy/result_item.py) class.

## Contributing
I'm accepting any pull request to improve or fix anything in the library, just fork the project and hack it!
