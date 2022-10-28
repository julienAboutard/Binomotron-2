import mariadb

yabinomotron = mariadb.connect(
  host="localhost",
  user="vincent",
  password="CuissonLente",
   database="Binomotron"
)

mycursor = yabinomotron.cursor()

# Create a list of students if it does not already exists
mycursor.execute("CREATE TABLE IF NOT EXISTS Students (id INT AUTO_INCREMENT PRIMARY KEY, First_Name VARCHAR(255), Last_Name VARCHAR(255))")

# Making sure the list is empty
mycursor.execute("TRUNCATE TABLE Students") 

# Add students to the list
sql = "INSERT INTO Students (First_Name, Last_Name) VALUES (%s, %s)"
val = [
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

mycursor.executemany(sql, val)
yabinomotron.commit()

mycursor.execute("SELECT * FROM Students")

myresult = mycursor.fetchall()