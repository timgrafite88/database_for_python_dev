create database my_music_site;

create table genres (genre_id serial primary key,
					 genre_name varchar(100) not null);
									
create table artists (artist_id serial primary key,
					  artist_name varchar(255) not null);
					
create table albums (album_id serial primary key,
					 album_name varchar(255),
					 release_year int check(release_year between 1900 and 2100));

create table artists_genres (artist_genre_id serial primary key,
					 		 artist_id int references artists(artist_id),
					 		 genre_id int references genres(genre_id));

create table artists_albums (artist_album_id serial primary key,
					 		 artist_id int references artists(artist_id),
					 		 album_id int references albums(album_id));	

create table tracks (track_id serial primary key,
					 track_name varchar(255),
					 album_id int references albums(album_id),
					 duration_seconds int check(duration_seconds between 10 and 600));
					
create table collections (collection_id serial primary key,
						  collection_name varchar(255),
						  release_year int check(release_year between 1900 and 2100));

create table collections_tracks (collection_track_id serial primary key,
								 collection_id int references collections(collection_id),
								 track_id int references tracks(track_id));
