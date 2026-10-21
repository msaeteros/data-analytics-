/*
a) In the actor table we have columns containing actor_id, first_name, last_name, and last_update 
b) In the film tablew we have columns containing film_id, title, description, release_year, language_id, original_language_id ,
rental_duration, rental_rate, lenght, replacement_cost, rating, special_features,last_update
c) Film_actor contains both actor_id and film_id 
d) In the rental table you are able to retrieve information like rental_id,rental_date, customer_id,etc. From looking at the rental table, understanding the information is kinda easy to read. This is because rental_id and rental_id are in order to be able to track info but, customer_id number sequence is not in order.analyze
e) In the inventory table inventory_id, film_id, store_id, and last_update are included which share two smiliar fields as rental table it being inventory_id and last_update.
f) In order to understand the names of all films that were rented on a specific data you will need to use the rental, inventory, and film tables. This because rental and inventory  both share inventory_id anf incentory table cshars film table field_ filme_id.

*/ 
USE sakila;

SELECT rental_id, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;
