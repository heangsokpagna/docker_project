docker-compose up --build

curl http://localhost:5423/health

docker exec -it mysql_container mysql -uroot -proot

USE testdb;
CREATE TABLE test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));
INSERT INTO test_table (name) VALUES ('Alice'), ('Bob');
