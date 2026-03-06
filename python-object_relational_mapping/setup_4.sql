USE hbtn_0e_4_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    state_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

INSERT INTO cities (name, state_id) VALUES 
("San Francisco", 1), ("San Jose", 1), ("Los Angeles", 1), ("Fremont", 1), ("Livermore", 1),
("Page", 2), ("Phoenix", 2),
("Dallas", 3), ("Houston", 3), ("Austin", 3),
("New York", 4),
("Las Vegas", 5), ("Reno", 5), ("Henderson", 5), ("Carson City", 5);
