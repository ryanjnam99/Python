INSERT INTO dojos (name)
VALUES("Bushido");

INSERT INTO dojos (name)
VALUES("Kazoku");

INSERT INTO dojos (name)
VALUES("Yamato")

DELETE FROM dojos_and_ninjas_schema.dojos WHERE id =1 ;
DELETE FROM dojos_and_ninjas_schema.dojos WHERE id =2 ;
DELETE FROM dojos_and_ninjas_schema.dojos WHERE id =3 ;

INSERT INTO dojos (name)
VALUES("Aikido");

INSERT INTO dojos (name)
VALUES("Musashi");

INSERT INTO dojos (name)
VALUES("Tengu")

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Ryan", "Nam", 23, 4);

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Jason", "Lee", 23, 4);

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Matthew", "Teh", 23, 4);

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Ryan", "Joon", 23, 5);

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Charles", "Lee", 23, 5);

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Kevin", "Lou", 23, 5);

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Bryan", "Soo", 23, 6);

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Charles", "Nam", 23, 6);

INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES("Byson", "Daniels", 23, 6);

SELECT * FROM ninjas WHERE dojo_id = 4;

SELECT * FROM ninjas WHERE dojo_id = 6;

SELECT * FROM dojos
JOIN ninjas ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = 11;

SELECT * FROM dojos
JOIN ninjas ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = 6;

SELECT * FROM dojos
JOIN ninjas ON ninjas.dojo_id = dojos.id;