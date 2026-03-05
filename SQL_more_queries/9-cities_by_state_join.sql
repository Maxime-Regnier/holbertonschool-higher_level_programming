CREATE TABLE IF NOT EXISTS states (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id)
);

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;