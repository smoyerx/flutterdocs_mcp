CREATE TABLE identifier (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE entity_type (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE member_type (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE library (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    content_markdown TEXT NOT NULL
);

CREATE TABLE entity (
    id INTEGER PRIMARY KEY,
    library_id INTEGER NOT NULL,
    identifier TEXT NOT NULL,
    entity_type_id INTEGER NOT NULL,
    content_markdown TEXT NOT NULL,
    UNIQUE(identifier, library_id),
    FOREIGN KEY (library_id) REFERENCES library(id),
    FOREIGN KEY (entity_type_id) REFERENCES entity_type(id)
);

CREATE TABLE member (
    id INTEGER PRIMARY KEY,
    entity_id INTEGER NOT NULL,
    identifier_id INTEGER NOT NULL,
    member_type_id INTEGER NOT NULL,
    content_markdown TEXT NOT NULL,
    UNIQUE(identifier_id, entity_id),
    FOREIGN KEY (entity_id) REFERENCES entity(id),
    FOREIGN KEY (identifier_id) REFERENCES identifier(id),
    FOREIGN KEY (member_type_id) REFERENCES member_type(id)
);

CREATE INDEX idx_entity_unique ON entity(identifier, library_id);

CREATE INDEX idx_member_unique ON member(identifier_id, entity_id);

CREATE VIRTUAL TABLE content_search USING fts5(
    identifier,
    content_markdown,
    content='entity',
    content_rowid='id',
    tokenize='porter'
);
