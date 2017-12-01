-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: Workshop
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Messages`
--

DROP TABLE IF EXISTS `Messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` int(11) NOT NULL,
  `recipient` int(11) NOT NULL,
  `content` text,
  `creation_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sender` (`sender`),
  KEY `recipient` (`recipient`),
  CONSTRAINT `Messages_ibfk_1` FOREIGN KEY (`sender`) REFERENCES `Users` (`id`),
  CONSTRAINT `Messages_ibfk_2` FOREIGN KEY (`recipient`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Messages`
--

LOCK TABLES `Messages` WRITE;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
INSERT INTO `Messages` VALUES (1,12,14,'Hello World','2017-12-01'),(2,15,14,'Hi, sup?!','2017-12-01'),(3,18,12,'Test message no 1','2017-12-01'),(4,18,17,'Test message no 1','2017-12-01'),(5,17,12,'Test message no 1','2017-12-01'),(6,15,14,'Test message no 1','2017-12-01'),(7,15,12,'Test message no 1','2017-12-01'),(8,14,18,'Test message no 1','2017-12-01'),(9,14,17,'Test message','2017-12-01'),(10,16,12,'Test message','2017-12-01'),(11,16,12,'Test message','2017-12-01'),(12,16,12,'True','2017-12-01');
/*!40000 ALTER TABLE `Messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `hashed_password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (2,'abc@def.com','Krzysiek','IrfuU7d0HNidkdaC277bdfff6aee15eb1ee888cf211fa099921a9093b804834b017ea526d57250d2'),(11,'Gosia2@test.com','Gosia2','erehVIfkMi8F2N0T03ba6c4e34500a1700062bcc554942a85022d2c6af32951e71c4a81cd384aaeb'),(12,'user_1@test.com','user_1','nKuTztMMym8NTOkw4511d34c200d74c2a9fb4436bba6dc2f5e8502d1f37c0d904523332f0321b5ed'),(14,'user_2@test.com','user_2','g9QHSZOsXDQvr2lJ0b45fdc2d66121f3bf5b66c2e8835f4d0f1d0962829a639a3f13763ef0588a7f'),(15,'user_3@test.com','user_3','R3Y9YRPmziya08kC90681310dc853e1ece80fabe10057ba338f8aa34002f26e22e51171dd28168bb'),(16,'user_4@test.com','user_4','10Djg6pIqPujMGQ9b90d2f1dd94d57ce48e34abae56f8307754d5ce11188330a9e26138358d46693'),(17,'user_5@test.com','user_5','nrBXPdGOFJT2pwh31c830040c39a1c38564f125ccd75196a311acb798c749cc923083987c481e5aa'),(18,'user_6@test.com','user_6','ualP9Nn9Qy2UXim730400a21129ddd4927293bd040255cfd25dee81bdeb11f87219e39664d04113b');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-01 20:43:39
