--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;

CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `rating` int DEFAULT NULL,
  `price` varchar(255) NOT NULL,
  `in_stock` tinyint NOT NULL,
  `nb_availlable` int NOT NULL,
  `img` varchar(255),
  `category` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `author` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
