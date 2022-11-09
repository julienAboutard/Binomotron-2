# import mariadb
import mysql.connector

yabinomotron = mysql.connector.connect(
# yabinomotron = mariadb.connect(
  host="localhost",
  user="vincent",
  password="CuissonLente",
  database="Binomotron"
)
mycursor = yabinomotron.cursor()

# Create a table of students if it does not already exists
mycursor.execute("CREATE TABLE IF NOT EXISTS Students (id INT AUTO_INCREMENT PRIMARY KEY, First_Name VARCHAR(255), Last_Name VARCHAR(255))")

# Create a table for briefs and its related data
mycursor.execute("CREATE TABLE IF NOT EXISTS Briefs (id INT AUTO_INCREMENT PRIMARY KEY, Brief_Name VARCHAR(255), Simplonline VARCHAR(255), Group_Length INT)")

# Making sure the table is empty
mycursor.execute("TRUNCATE TABLE Students")
mycursor.execute("TRUNCATE TABLE Briefs") 

# Add students to the table
sql_students = "INSERT INTO Students (First_Name, Last_Name) VALUES (%s, %s)"
val_students = [
('Alice', 'Lafon'),
('Audrey', 'Costes'),
('Christelle', 'Wittmann'),
('Djamila', 'Chabane'),
('Dorine', 'Paris'),
('Florian', 'Berthelot'),
('Hayel', 'Bendib'),
('Julien', 'Aboutard'),
('Marwin', 'Launay'),
('Nawel', 'Ouarti'),
('Tomislav', 'Bockaj'),
('Vincent', 'Boettcher'),
('Wahid', 'Ameur')
]

mycursor.executemany(sql_students, val_students)
yabinomotron.commit()

# Add briefs and its data to the table named brief
sql_briefs = "INSERT INTO Briefs (Brief_Name, Simplonline, Group_Length) VALUES (%s, %s, %s)"
val_briefs = [
("Mon environnement de développement IDE", "https://simplonline.co/briefs/720263d7-9f1e-44ef-822d-79e21b5b0dc2", 1),
("Configuration de l'envionnement numérique de travail", "https://simplonline.co/briefs/d88b7277-e371-4450-942f-e8cdf7dd98bc", 1),
("Aide au diagnostic", "https://simplonline.co/briefs/49caaf1d-e301-41fc-b75c-bde1cfedf450", 2),
("Mon premier algorithme de machine learning", "https://simplonline.co/briefs/9031f788-375a-4767-8593-b7854a97707e", 1),
("Présenter un algorithme de machine learning", "https://simplonline.co/briefs/dd8f3d9e-9718-4c13-93f8-cc624e787934", 2),
("YAB - Yet Another Binomotron", "https://simplonline.co/briefs/ee7ef768-a817-49bb-9c80-05a828744007", 2),
("YAB Enhanced", "https://simplonline.co/briefs/6e0d6f1d-f54c-482a-9708-35cec05d28e5", 2),
("Education Nationale", 'Gateway Error, AGAIN?', 3),
("Torrent Site", 'This link is illegal', 6),
("Site de lecture en ligne", 'This link will change', 14)
]

mycursor.executemany(sql_briefs, val_briefs)
yabinomotron.commit()