-- SQLite schema

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    created_at TEXT
);

CREATE TABLE pairs (
    pair_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE,
    a_user INTEGER,
    b_user INTEGER,
    created_at TEXT
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pair_id INTEGER,
    user_id INTEGER,
    content TEXT,
    kind TEXT,
    created_at TEXT
);

CREATE TABLE vocab (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    word TEXT,
    note TEXT,
    created_at TEXT
);
