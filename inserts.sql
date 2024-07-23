insert into artists (artist_name)
values ('Depeche Mode'), ('Queen'), ('A-ha'), ('Daft Punk');

insert into genres (genre_name)
values ('Pop'), ('Rock'), ('Rap'), ('Electro');

insert into albums (album_name, release_year)
values ('Ultra', 1997), ('Discovery', 2001), ('Analogue', 2005);

insert into tracks (track_name, album_id, duration_seconds)
values ('Home', 1, 342), 
		('The Love Thives', 1, 393),
		('Its No Good', 1, 357),
		('Celice', 3, 219),
		('One More Time', 2, 320),
		('Something About Us', 2, 231);

insert into collections (collection_name, release_year)
values ('Gold Ballads', 2019), ('Electro Pop', 2015), ('Dance', 2001), ('Classic Hits', 2017);

insert into artists_genres (genre_id, artist_id)
values (1, 1), (1, 3), (4, 4), (2, 2);

insert into artists_albums (artist_id, album_id)
values (1, 1), (4, 2), (3, 3);

insert into collections_tracks (collection_id, track_id)
values (1, 4), (3, 5), (2, 6), (2, 1);