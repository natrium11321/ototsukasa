DROP TABLE IF EXISTS toilet,reservatioin,toilet_status;
CREATE TABLE toilet (id INT, pos_lat DOUBLE, pos_lng DOUBLE);
CREATE TABLE reservation (id INT, reqdt DATETIME);
CREATE TABLE toilet_status (id INT, use_status VARCHAR(50),updatedt DATETIME);

INSERT INTO toilet VALUES (0,35.7139069,139.7581305);
