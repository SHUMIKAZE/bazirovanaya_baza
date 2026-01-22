CREATE TABLE IF NOT EXISTS works (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    original_title TEXT NOT NULL,
    native_title TEXT,
    type TEXT NOT NULL,
    release_year INTEGER
);

CREATE TABLE IF NOT EXISTS ratings (
    work_id INTEGER PRIMARY KEY,
    score REAL CHECK(score BETWEEN 0 AND 10),
    notes TEXT,
    FOREIGN KEY(work_id) REFERENCES works(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS work_genres (
    work_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (work_id, genre_id),
    FOREIGN KEY(work_id) REFERENCES works(id) ON DELETE CASCADE,
    FOREIGN KEY(genre_id) REFERENCES genres(id) ON DELETE CASCADE
);
