-- DBPilot Seed Data
CREATE TABLE IF NOT EXISTS customers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (first_name, last_name, email, city) VALUES
('Rahul', 'Sharma', 'rahul.sharma@example.com', 'Delhi'),
('Aman', 'Verma', 'aman.verma@example.com', 'Mumbai'),
('Priya', 'Patel', 'priya.patel@example.com', 'Bangalore'),
('Neha', 'Gupta', 'neha.gupta@example.com', 'Delhi'),
('Vikram', 'Singh', 'vikram.singh@example.com', 'Pune')
ON CONFLICT (email) DO NOTHING;