# Exercices MySQL Basics

- Crée une base de données `becode`.
	
		create database becode;
	
- Importe le fichier `students.sql` qui se trouve dans ce dossier.

		mysql -u root -p db_name < ~/Documents/db_name.sql

Dans un second fichier .sql, tu stockeras les requêtes qui te permettront de réaliser ces actions :

- Affiche toutes les données.

		use becode;
		show tables;
		describe school;
		describe students; 
	
- Affiche uniquement les prénoms.

		select prenom from students;

- Affiche les prénoms, les dates de naissance et l’école de chacun.
	
		select prenom, datenaissance, school  from students;

- Affiche uniquement les élèves qui sont de sexe féminin.

		mysql> select prenom, genre from students
   		 	-> where genre = 'F';

- Affiche uniquement les élèves qui font partie de l’école d'Addy.

		Ce n'est pas possible parce que l'école est de type integer


- Affiche uniquement les prénoms des étudiants, par ordre inverse à l’alphabet
(DESC). Ensuite, la même chose mais en limitant les résultats à 2.;

		mysql> select prenom from students
   				 -> ORDER BY prenom DESC
   				 -> LIMIT 2;

- Ajoute Ginette Dalor, née le 01/01/1930 et affecte-la à Bruxelles, toujours en
SQL.

		insert into students (nom, prenom, datenaissance, genre, school) 
		values ('Ginette', 'Dalor', '1930/01/01', 'F', '1');
			
		
- Modifie Ginette (toujours en SQL) et change son sexe et son prénom en “Omer”.
	
		mysql> UPDATE students
	    -> SET nom = "Omer" , genre = 'M'
	    -> WHERE idStudent = 31;
	
- Supprimer la personne dont l’ID est 3.

		mysql> delete from students
	    -> where idStudent = 3;
	
- Modifier le contenu de la colonne School de sorte que "1" soit remplacé par "Liege" et "2" soit remplacé par "Gent". (attention au type de la colonne !)

		 update school 
	    -> set school = 'Ghent'
	    -> where idschool = 2;


- Faire d’autres manipulations pour voir si t’es bien compris.
