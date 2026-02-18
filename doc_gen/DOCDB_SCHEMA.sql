CREATE TABLE identifier (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE type (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE library (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    content_markdown TEXT
);

CREATE TABLE entity (
    id INTEGER PRIMARY KEY,
    library_id INTEGER NOT NULL,
    identifier_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    content_markdown TEXT,
    snippet_markdown TEXT,
    UNIQUE(identifier_id, library_id),
    FOREIGN KEY (library_id) REFERENCES library(id),
    FOREIGN KEY (identifier_id) REFERENCES identifier(id),
    FOREIGN KEY (type_id) REFERENCES type(id)
);

CREATE TABLE member (
    id INTEGER PRIMARY KEY,
    entity_id INTEGER NOT NULL,
    identifier_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    content_markdown TEXT,
    UNIQUE(identifier_id, entity_id),
    FOREIGN KEY (entity_id) REFERENCES entity(id),
    FOREIGN KEY (identifier_id) REFERENCES identifier(id),
    FOREIGN KEY (type_id) REFERENCES type(id)
);

CREATE INDEX idx_entity_identifier ON entity(identifier_id);
CREATE INDEX idx_entity_unique ON entity(identifier_id, library_id);

CREATE INDEX idx_member_identifier ON member(identifier_id);
CREATE INDEX idx_member_unique ON member(identifier_id, entity_id);
