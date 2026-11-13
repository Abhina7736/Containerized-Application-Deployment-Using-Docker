CREATE TABLE IF NOT EXISTS visitors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    purpose VARCHAR(255) NOT NULL,
    check_in TIMESTAMP,
    check_out TIMESTAMP
);
