CREATE TABLE 'share' (
    'id' INT UNSIGNED AUTO_INCREMENT,
    prompt VARCHAR(500) NOT NULL,
    img VARCHAR(300) NOT NULL,
    conversations JSON,
    suggest VARCHAR(5000),
    share_date DATE,
    PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;