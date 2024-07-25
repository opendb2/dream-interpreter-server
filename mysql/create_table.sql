CREATE TABLE `dream_share` (
  `id` int (11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `prompt` varchar (2000) CHARACTER SET `utf8` COLLATE `utf8_general_ci` NULL DEFAULT '',
  `img` varchar (500) CHARACTER SET `utf8` COLLATE `utf8_general_ci` NULL DEFAULT '',
  `conversations` varchar (10000) CHARACTER SET `utf8` COLLATE `utf8_general_ci` NULL DEFAULT '',
  `suggest` varchar (5000) CHARACTER SET `utf8` COLLATE `utf8_general_ci` NULL DEFAULT '',
  `share_date` datetime NOT NULL,
  `dream_id` int (11) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8"
CREATE TABLE `dream` (
  `id` int (11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `prompt` varchar (2000) CHARACTER SET `utf8` COLLATE `utf8_general_ci` NULL DEFAULT '',
  `img` varchar (500) CHARACTER SET `utf8` COLLATE `utf8_general_ci` NULL DEFAULT '',
  `conversations` varchar (10000) CHARACTER SET `utf8` COLLATE `utf8_general_ci` NULL DEFAULT '',
  `suggest` varchar (5000) CHARACTER SET `utf8` COLLATE `utf8_general_ci` NULL DEFAULT '',
  `share_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = innodb DEFAULT CHARACTER SET = "utf8"