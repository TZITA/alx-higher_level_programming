-- Creates the table unique_id on MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT '1',
	name VARCHAR(256),
	PRIMARY KEY (id)
);
ALTER TABLE unique_id ADD UNIQUE(id);
