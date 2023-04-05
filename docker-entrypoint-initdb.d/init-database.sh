#!/bin/bash



set -e


#psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
#  create table if not exists public.user_account
#(
#    id serial
#        primary key
#);
#
#alter table public.user_account
#    owner to postgres;
#
#create table if not exists public.movie
#(
#    id   serial
#        primary key,
#    name varchar(200) not null
#);
#
#alter table public.movie
#    owner to postgres;
#
#create table if not exists public.genre
#(
#    id   serial
#        primary key,
#    name varchar(30) not null
#);
#
#alter table public.genre
#    owner to postgres;
#
#create table if not exists public.tag
#(
#    id        serial
#        primary key,
#    user_id   integer      not null
#        references public.user_account,
#    movie_id  integer      not null
#        references public.movie,
#    name      varchar(300) not null,
#    timestamp varchar      not null
#);
#
#alter table public.tag
#    owner to postgres;
#
#create table if not exists public.rating
#(
#    id        serial
#        primary key,
#    user_id   integer          not null
#        references public.user_account,
#    movie_id  integer          not null
#        references public.movie,
#    timestamp varchar          not null,
#    rating    double precision not null
#);
#
#alter table public.rating
#    owner to postgres;
#
#create table if not exists public.link
#(
#    id       serial
#        primary key,
#    movie_id integer     not null
#        references public.movie,
#    "imdbId" varchar(30) not null,
#    "tmdbId" varchar(30) not null
#);
#
#alter table public.link
#    owner to postgres;
#
#create table if not exists public.movie_genres
#(
#    movie_id integer
#        references public.movie,
#    genre_id integer
#        references public.genre
#);
#
#alter table public.movie_genres
#    owner to postgres;
#
#INSERT INTO public.genre (id, name) VALUES (1, 'Action');
#INSERT INTO public.genre (id, name) VALUES (2, 'Adventure');
#INSERT INTO public.genre (id, name) VALUES (3, 'Animation');
#INSERT INTO public.genre (id, name) VALUES (4, 'Children');
#INSERT INTO public.genre (id, name) VALUES (5, 'Comedy');
#INSERT INTO public.genre (id, name) VALUES (6, 'Crime');
#INSERT INTO public.genre (id, name) VALUES (7, 'Documentary');
#INSERT INTO public.genre (id, name) VALUES (8, 'Drama');
#INSERT INTO public.genre (id, name) VALUES (9, 'Fantasy');
#INSERT INTO public.genre (id, name) VALUES (10, 'Film-Noir');
#INSERT INTO public.genre (id, name) VALUES (11, 'Horror');
#INSERT INTO public.genre (id, name) VALUES (12, 'Musical');
#INSERT INTO public.genre (id, name) VALUES (13, 'Mystery');
#INSERT INTO public.genre (id, name) VALUES (14, 'Romance');
#INSERT INTO public.genre (id, name) VALUES (15, 'Sci-Fi');
#INSERT INTO public.genre (id, name) VALUES (16, 'Thriller');
#INSERT INTO public.genre (id, name) VALUES (17, 'War');
#INSERT INTO public.genre (id, name) VALUES (18, 'Western');
#INSERT INTO public.genre (id, name) VALUES (19, 'IMAX');
#
#EOSQL

git config pull.rebase false
git config --global --add core.sharedRepository group
git config --global --add safe.directory /movie_recommendations
git fetch
git pull


python3 docker_start.py 5432
python3 csv_parser/Parser.py
