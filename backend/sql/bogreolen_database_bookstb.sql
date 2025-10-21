CREATE DATABASE  IF NOT EXISTS 'bogreolen_database';
USE 'bogreolen_database';

DROP TABLE IF EXISTS 'bookstb';
CREATE TABLE 'bookstb' (
  'bookid' int NOT NULL AUTO_INCREMENT,
  'title' varchar(30) NOT NULL,
  'authorid' int NOT NULL,
  'image' varchar(30) NOT NULL,
  'summary' varchar(200) NOT NULL,
  'year' int NOT NULL,
  'categoryid' int NOT NULL,
  PRIMARY KEY ('bookid')
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
