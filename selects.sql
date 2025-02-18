--название и продолжительность самого длительного трека

select track_name , duration_seconds 
from tracks
order by duration_seconds desc 
limit 1;

--название треков, продолжительность которых не менее 3,5 минут

select track_name 
from tracks t 
where duration_seconds >= 210;

--названия сборников, вышедших в период с 2018 по 2020 год включительно

select collection_name 
from collections c 
where release_year between 2018 and 2020;

--исполнители, чьё имя состоит из одного слова

select artist_name
from artists a 
where artist_name not like '% %' and artist_name not like '%-%';

--название треков, которые содержат слово «мой» или «my»

select track_name 
from tracks t 
where track_name ilike '%my%' or track_name ilike '%мой%';

--количество исполнителей в каждом жанре

select g.genre_name , count(ag.artist_id) as cnt
from genres g 
	left join artists_genres ag 
		on g.genre_id = ag.genre_id 
group by g.genre_id ;


--количество треков, вошедших в альбомы 2019–2020 годов

select count(t.track_id) as count_tracks
from albums a 
	left join tracks t on t.album_id = a.album_id 
where a.release_year between 2019 and 2020;


--средняя продолжительность треков по каждому альбому

select a.album_name, avg(t.duration_seconds) as avg_seconds
from albums a 
	left join tracks t on a.album_id = t.album_id 
group by a.album_id;


--все исполнители, которые не выпустили альбомы в 2020 году

select artist_name
from artists a 
where artist_name not in (
							select distinct a.artist_name 
							from artists a 
								join artists_albums aa 
									on a.artist_id = aa.artist_id 
								join albums a2 
									on aa.album_id = a2.album_id 
							where a2.release_year = 2020);


--названия сборников, в которых присутствует конкретный исполнитель (выберите его сами)

select c.collection_name 
from collections c 
	join collections_tracks ct
		on c.collection_id = ct.collection_id 
	join tracks t 
		on t.track_id = ct.track_id 
	join albums a 
		on t.album_id = a.album_id 
	join artists_albums aa
		on aa.album_id = a.album_id 
	join artists a2 
		on a2.artist_id = aa.artist_id 
where a2.artist_name = 'Depeche Mode';