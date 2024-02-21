CREATE TABLE messages (
    ssid text PRIMARY KEY,
    created_time timestamp,
    from_number text,
    last_update timestamp,
    status text,
    to_number text
)