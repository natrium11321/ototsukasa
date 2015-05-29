DROP TABLE IF EXISTS toilet,reservatioin,toilet_status;
CREATE TABLE toilet (id INT PRIMARY KEY AUTO_INCREMENT,toilet_id INT, pos_lat DOUBLE, pos_lng DOUBLE);
CREATE TABLE reservation (id INT PRIMARY KEY AUTO_INCREMENT,toilet_id INT, reqdt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE toilet_status (id INT PRIMARY KEY AUTO_INCREMENT,toilet_id INT, use_status VARCHAR(50),updatedt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);

INSERT INTO toilet VALUES (NULL,0,35.7139069,139.7581305);
INSERT INTO `toilet_status` (`id`, `toilet_id`, `use_status`, `updatedt`) VALUES (NULL, '0', 'USED', NULL);
