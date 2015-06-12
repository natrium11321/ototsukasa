DROP TABLE IF EXISTS toilets,musics,reservations,status,reviews,location;
CREATE TABLE toilets (id INT PRIMARY KEY AUTO_INCREMENT,pos_id INT, sex ENUM('F','M'));
CREATE TABLE musics (id INT PRIMARY KEY AUTO_INCREMENT, toilet_id INT,word TEXT, url TEXT,updatetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE reservations (id INT PRIMARY KEY AUTO_INCREMENT,toilet_id INT,password TEXT, updatetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE status (id INT PRIMARY KEY AUTO_INCREMENT,toilet_id INT, empty ENUM ('Empty','Occupied'),updatetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE reviews (id INT PRIMARY KEY AUTO_INCREMENT,pos_id INT,comment TEXT,updatetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE location (id INT PRIMARY KEY AUTO_INCREMENT, pos_id INT, lat DOUBLE,lng DOUBLE,name TEXT);

INSERT INTO toilets VALUES (NULL,1,'F');
INSERT INTO toilets VALUES (NULL,1,'F');
INSERT INTO toilets VALUES (NULL,2,'M');
INSERT INTO toilets VALUES (NULL,2,'M');

INSERT INTO status VALUES (NULL,1, 'Empty', NULL);
INSERT INTO status VALUES (NULL,2, 'Empty', NULL);
INSERT INTO status VALUES (NULL,3, 'Empty', NULL);
INSERT INTO status VALUES (NULL,4, 'Empty', NULL);

INSERT INTO location VALUES (NULL,1,35.712678,139.761989,'東京大学工学部６号館');
INSERT INTO location VALUES (NULL,2,35.712678,139.761989,'東京大学工学部６号館');

/*テンプレート
INSERT INTO toilets VALUES (NULL,3,'M'); --数字は位置のID適当に増やす 'F' or 'M'
INSERT INTO status VALUES (NULL,4, 'Empty', NULL); --数字だけ増やす
INSERT INTO location VALUES (NULL,1,35.712678,139.761989,'東京大学工学部６号館'); --数字は位置ID 緯度、経度
*/
