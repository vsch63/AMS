CREATE DATABASE  IF NOT EXISTS `agency_sys` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agency_sys`;
-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: agency_sys
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tagency`
--

DROP TABLE IF EXISTS `tagency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tagency` (
  `COMPANYID` int NOT NULL,
  `TAGENCY_ID` int NOT NULL AUTO_INCREMENT,
  `CLIENTID` int NOT NULL,
  `AGENCYCHANNEL` varchar(3) NOT NULL,
  `AGENCYCATEGORY` int NOT NULL,
  `AGENCYSTATUS` varchar(2) NOT NULL,
  `AGENCYLEVEL` varchar(2) NOT NULL,
  `AGENCYREPMGRID` varchar(10) NOT NULL,
  `AGENCYLICENSENO` varchar(15) NOT NULL,
  `AGENCYCODE` varchar(10) NOT NULL,
  PRIMARY KEY (`TAGENCY_ID`),
  KEY `TAGENCY_fk0` (`AGENCYCATEGORY`),
  CONSTRAINT `TAGENCY_fk0` FOREIGN KEY (`AGENCYCATEGORY`) REFERENCES `tagency_category` (`AGENCYCATEGORY_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tagency`
--

LOCK TABLES `tagency` WRITE;
/*!40000 ALTER TABLE `tagency` DISABLE KEYS */;
/*!40000 ALTER TABLE `tagency` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-27 18:52:35
