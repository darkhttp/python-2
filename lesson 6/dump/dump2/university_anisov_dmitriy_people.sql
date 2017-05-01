-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: university_anisov_dmitriy
-- ------------------------------------------------------
-- Server version	5.7.16-log

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
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `idPeople` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `second_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `d_of_b` varchar(45) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  PRIMARY KEY (`idPeople`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 DELAY_KEY_WRITE=1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
INSERT INTO `people` VALUES (1,'Дмитрий','Анисов','Александрович','24/03/1996','89210010'),(2,'Иван','Пупкин','Васильевичё','21/02/1996','890000'),(3,'Василий','Абрамов','Сергеевичё','11/09/1996','89000001'),(4,'Лена','Беликова','Дмитриевна','16/12/1996','89000002'),(18,'Андрей','Кукушкин','Леонидович','24/01/1995','1313312'),(20,'Никита','Попов','Викторович','12/08/1995','231231'),(21,'Александр','Щукин','Александрович','30/03/1996','231921'),(22,'Александр','Щукин','Александрович','30/03/1996','231923'),(23,'Александр','Щукин','Александрович','30/03/1996','231924'),(25,'цфвф','вфвфв','фвфв','фвфв','21313'),(26,'awsda','asdasd','adads','123123','8999999999'),(27,'adaa','adadawd','dadwad','123123','8999999999'),(28,'Какойто','adadawd','dadwad','123123','8999999999'),(29,'Студент','Студент','Студент','24/03/1996','8999999991'),(30,'Студенттт','Студенттт','Студентт','24/03/1996','8999999994'),(31,'Грин','Гринович','Гриновский','24/03/1996','89999999999'),(32,'Цезарь','Цезарь','Цезарь','24/03/1996','8999999912');
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-01 19:05:53
