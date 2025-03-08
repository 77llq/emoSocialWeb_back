-- MySQL dump 10.13  Distrib 5.7.31, for Win64 (x86_64)
--
-- Host: localhost    Database: emosocialapp_db
-- ------------------------------------------------------
-- Server version	5.7.31

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add user profile',8,'add_userprofile'),(30,'Can change user profile',8,'change_userprofile'),(31,'Can delete user profile',8,'delete_userprofile'),(32,'Can view user profile',8,'view_userprofile'),(33,'Can add email',9,'add_email'),(34,'Can change email',9,'change_email'),(35,'Can delete email',9,'delete_email'),(36,'Can view email',9,'view_email'),(37,'Can add fans',10,'add_fans'),(38,'Can change fans',10,'change_fans'),(39,'Can delete fans',10,'delete_fans'),(40,'Can view fans',10,'view_fans'),(41,'Can add friends',11,'add_friends'),(42,'Can change friends',11,'change_friends'),(43,'Can delete friends',11,'delete_friends'),(44,'Can view friends',11,'view_friends'),(45,'Can add friends request',12,'add_friendsrequest'),(46,'Can change friends request',12,'change_friendsrequest'),(47,'Can delete friends request',12,'delete_friendsrequest'),(48,'Can view friends request',12,'view_friendsrequest'),(49,'Can add moments',13,'add_moments'),(50,'Can change moments',13,'change_moments'),(51,'Can delete moments',13,'delete_moments'),(52,'Can view moments',13,'view_moments'),(53,'Can add moments comment',14,'add_momentscomment'),(54,'Can change moments comment',14,'change_momentscomment'),(55,'Can delete moments comment',14,'delete_momentscomment'),(56,'Can view moments comment',14,'view_momentscomment'),(57,'Can add moments like',15,'add_momentslike'),(58,'Can change moments like',15,'change_momentslike'),(59,'Can delete moments like',15,'delete_momentslike'),(60,'Can view moments like',15,'view_momentslike'),(61,'Can add board',16,'add_board'),(62,'Can change board',16,'change_board'),(63,'Can delete board',16,'delete_board'),(64,'Can view board',16,'view_board'),(65,'Can add emoji',17,'add_emoji'),(66,'Can change emoji',17,'change_emoji'),(67,'Can delete emoji',17,'delete_emoji'),(68,'Can view emoji',17,'view_emoji');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(16,'emoSocialApp','board'),(9,'emoSocialApp','email'),(17,'emoSocialApp','emoji'),(10,'emoSocialApp','fans'),(11,'emoSocialApp','friends'),(12,'emoSocialApp','friendsrequest'),(13,'emoSocialApp','moments'),(14,'emoSocialApp','momentscomment'),(15,'emoSocialApp','momentslike'),(7,'emoSocialApp','user'),(8,'emoSocialApp','userprofile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-05-14 03:27:26.193586'),(2,'auth','0001_initial','2024-05-14 03:27:26.761852'),(3,'admin','0001_initial','2024-05-14 03:27:26.904444'),(4,'admin','0002_logentry_remove_auto_add','2024-05-14 03:27:26.910457'),(5,'admin','0003_logentry_add_action_flag_choices','2024-05-14 03:27:26.917442'),(6,'contenttypes','0002_remove_content_type_name','2024-05-14 03:27:27.011223'),(7,'auth','0002_alter_permission_name_max_length','2024-05-14 03:27:27.065049'),(8,'auth','0003_alter_user_email_max_length','2024-05-14 03:27:27.124854'),(9,'auth','0004_alter_user_username_opts','2024-05-14 03:27:27.132870'),(10,'auth','0005_alter_user_last_login_null','2024-05-14 03:27:27.179765'),(11,'auth','0006_require_contenttypes_0002','2024-05-14 03:27:27.181732'),(12,'auth','0007_alter_validators_add_error_messages','2024-05-14 03:27:27.188716'),(13,'auth','0008_alter_user_username_max_length','2024-05-14 03:27:27.242553'),(14,'auth','0009_alter_user_last_name_max_length','2024-05-14 03:27:27.299388'),(15,'auth','0010_alter_group_name_max_length','2024-05-14 03:27:27.355238'),(16,'auth','0011_update_proxy_permissions','2024-05-14 03:27:27.362220'),(17,'auth','0012_alter_user_first_name_max_length','2024-05-14 03:27:27.415079'),(18,'emoSocialApp','0001_initial','2024-05-14 03:27:27.520029'),(19,'emoSocialApp','0002_user_idnumber_alter_user_type_and_more','2024-05-14 03:27:28.435023'),(20,'sessions','0001_initial','2024-05-14 03:27:28.474890'),(21,'emoSocialApp','0003_alter_userprofile_avatar','2024-05-15 08:04:16.208651'),(22,'emoSocialApp','0004_board','2024-05-15 08:17:23.399444'),(23,'emoSocialApp','0003_board','2024-05-15 08:32:02.659485'),(24,'emoSocialApp','0004_emoji_alter_user_password','2024-05-22 10:08:50.640950'),(25,'emoSocialApp','0004_alter_user_password','2024-05-22 12:32:39.562799'),(26,'emoSocialApp','0005_userprofile_profilebp','2024-05-26 10:29:07.092062'),(27,'emoSocialApp','0006_alter_userprofile_avatar_alter_userprofile_profilebp','2024-05-27 07:13:55.407280'),(28,'emoSocialApp','0007_friends_intimacy','2024-06-03 12:48:15.729483');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('iina3dri104xu0bbw9alztijte4iavvc','eyJjb2RlIjoibVkySE0ifQ:1sDGSi:ha1sTAI7M__ZY7OP0Wqrhl6Kz6ouwhQvCyRj2yHI7Zg','2024-06-15 04:35:24.810006');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_board`
--

DROP TABLE IF EXISTS `emosocialapp_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_board` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `postTopic` varchar(64) NOT NULL,
  `postContent` varchar(255) NOT NULL,
  `postTime` varchar(64) NOT NULL,
  `postId_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emoSocialApp_board_postId_id_c91ff8f8_fk_emoSocialApp_user_id` (`postId_id`),
  CONSTRAINT `emoSocialApp_board_postId_id_c91ff8f8_fk_emoSocialApp_user_id` FOREIGN KEY (`postId_id`) REFERENCES `emosocialapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_board`
--

LOCK TABLES `emosocialapp_board` WRITE;
/*!40000 ALTER TABLE `emosocialapp_board` DISABLE KEYS */;
INSERT INTO `emosocialapp_board` VALUES (4,'2024/5/27','下午17：17，发布新公告','2024-05-27 17:17:42','a182d2e6-81be-4126-8012-c5c79ee1170d'),(11,'发布新公告！','本系统将于今晚七点开始维护！','2024-06-01 12:40:10','a182d2e6-81be-4126-8012-c5c79ee1170d');
/*!40000 ALTER TABLE `emosocialapp_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_email`
--

DROP TABLE IF EXISTS `emosocialapp_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_email` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `emailTopic` varchar(32) NOT NULL,
  `emailContent` varchar(255) NOT NULL,
  `sendTime` varchar(64) NOT NULL,
  `receiveId_id` varchar(255) DEFAULT NULL,
  `sendId_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emoSocialApp_email_receiveId_id_c84537be_fk_emoSocialApp_user_id` (`receiveId_id`),
  KEY `emoSocialApp_email_sendId_id_cd6bbda4_fk_emoSocialApp_user_id` (`sendId_id`),
  CONSTRAINT `emoSocialApp_email_receiveId_id_c84537be_fk_emoSocialApp_user_id` FOREIGN KEY (`receiveId_id`) REFERENCES `emosocialapp_user` (`id`),
  CONSTRAINT `emoSocialApp_email_sendId_id_cd6bbda4_fk_emoSocialApp_user_id` FOREIGN KEY (`sendId_id`) REFERENCES `emosocialapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_email`
--

LOCK TABLES `emosocialapp_email` WRITE;
/*!40000 ALTER TABLE `emosocialapp_email` DISABLE KEYS */;
INSERT INTO `emosocialapp_email` VALUES (8,'最近怎么样？','过得好吗','2024年05月27日 (星期一) 下午06 : 52','b2d07f96-781b-4eb0-adb3-8167feb8e581','b8cd9132-693f-497d-933f-d3c81cda70fb'),(9,'最近过得好吗？','最近怎么样，好久没联系了，过得还好吗？','2024年05月28日 (星期二) 下午06 : 33','b8cd9132-693f-497d-933f-d3c81cda70fb','b2d07f96-781b-4eb0-adb3-8167feb8e581'),(14,'好久没联系了！','最近过得还好吗？','2024年06月01日 (星期六) 下午12 : 38','b2d07f96-781b-4eb0-adb3-8167feb8e581','3eee19ed-a05d-41a7-ab43-89ee82c9ea6b');
/*!40000 ALTER TABLE `emosocialapp_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_fans`
--

DROP TABLE IF EXISTS `emosocialapp_fans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_fans` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fansId_id` varchar(255) DEFAULT NULL,
  `userId_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emoSocialApp_fans_fansId_id_9728409b_fk_emoSocialApp_user_id` (`fansId_id`),
  KEY `emoSocialApp_fans_userId_id_da93ea00_fk_emoSocialApp_user_id` (`userId_id`),
  CONSTRAINT `emoSocialApp_fans_fansId_id_9728409b_fk_emoSocialApp_user_id` FOREIGN KEY (`fansId_id`) REFERENCES `emosocialapp_user` (`id`),
  CONSTRAINT `emoSocialApp_fans_userId_id_da93ea00_fk_emoSocialApp_user_id` FOREIGN KEY (`userId_id`) REFERENCES `emosocialapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_fans`
--

LOCK TABLES `emosocialapp_fans` WRITE;
/*!40000 ALTER TABLE `emosocialapp_fans` DISABLE KEYS */;
INSERT INTO `emosocialapp_fans` VALUES (10,'b2d07f96-781b-4eb0-adb3-8167feb8e581','daa65b21-a34e-437e-adf0-9983de150ae0'),(25,'b8cd9132-693f-497d-933f-d3c81cda70fb','b2d07f96-781b-4eb0-adb3-8167feb8e581'),(26,'b2d07f96-781b-4eb0-adb3-8167feb8e581','b8cd9132-693f-497d-933f-d3c81cda70fb'),(27,'b8cd9132-693f-497d-933f-d3c81cda70fb','daa65b21-a34e-437e-adf0-9983de150ae0'),(29,'b8cd9132-693f-497d-933f-d3c81cda70fb','c34e015c-392b-4a73-81ed-9a07a01ba86d'),(30,'b8cd9132-693f-497d-933f-d3c81cda70fb','eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d'),(38,'3eee19ed-a05d-41a7-ab43-89ee82c9ea6b','b2d07f96-781b-4eb0-adb3-8167feb8e581'),(39,'3eee19ed-a05d-41a7-ab43-89ee82c9ea6b','c34e015c-392b-4a73-81ed-9a07a01ba86d'),(40,'b2d07f96-781b-4eb0-adb3-8167feb8e581','3eee19ed-a05d-41a7-ab43-89ee82c9ea6b');
/*!40000 ALTER TABLE `emosocialapp_fans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_friends`
--

DROP TABLE IF EXISTS `emosocialapp_friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_friends` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `friendId_id` varchar(255) DEFAULT NULL,
  `userId_id` varchar(255) NOT NULL,
  `intimacy` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emoSocialApp_friends_friendId_id_9084bc7b_fk_emoSocial` (`friendId_id`),
  KEY `emoSocialApp_friends_userId_id_b59f8053_fk_emoSocialApp_user_id` (`userId_id`),
  CONSTRAINT `emoSocialApp_friends_friendId_id_9084bc7b_fk_emoSocial` FOREIGN KEY (`friendId_id`) REFERENCES `emosocialapp_user` (`id`),
  CONSTRAINT `emoSocialApp_friends_userId_id_b59f8053_fk_emoSocialApp_user_id` FOREIGN KEY (`userId_id`) REFERENCES `emosocialapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_friends`
--

LOCK TABLES `emosocialapp_friends` WRITE;
/*!40000 ALTER TABLE `emosocialapp_friends` DISABLE KEYS */;
INSERT INTO `emosocialapp_friends` VALUES (1,'daa65b21-a34e-437e-adf0-9983de150ae0','b2d07f96-781b-4eb0-adb3-8167feb8e581','30'),(11,'b8cd9132-693f-497d-933f-d3c81cda70fb','b2d07f96-781b-4eb0-adb3-8167feb8e581','100'),(16,'3eee19ed-a05d-41a7-ab43-89ee82c9ea6b','b2d07f96-781b-4eb0-adb3-8167feb8e581','50');
/*!40000 ALTER TABLE `emosocialapp_friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_friendsrequest`
--

DROP TABLE IF EXISTS `emosocialapp_friendsrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_friendsrequest` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `receiveRequestId_id` varchar(255) DEFAULT NULL,
  `sendRequestId_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emoSocialApp_friends_receiveRequestId_id_b5ed490c_fk_emoSocial` (`receiveRequestId_id`),
  KEY `emoSocialApp_friends_sendRequestId_id_c488ff2e_fk_emoSocial` (`sendRequestId_id`),
  CONSTRAINT `emoSocialApp_friends_receiveRequestId_id_b5ed490c_fk_emoSocial` FOREIGN KEY (`receiveRequestId_id`) REFERENCES `emosocialapp_user` (`id`),
  CONSTRAINT `emoSocialApp_friends_sendRequestId_id_c488ff2e_fk_emoSocial` FOREIGN KEY (`sendRequestId_id`) REFERENCES `emosocialapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_friendsrequest`
--

LOCK TABLES `emosocialapp_friendsrequest` WRITE;
/*!40000 ALTER TABLE `emosocialapp_friendsrequest` DISABLE KEYS */;
INSERT INTO `emosocialapp_friendsrequest` VALUES (18,'8d1f88a2-c367-4e65-b391-391c9fd0684d','b2d07f96-781b-4eb0-adb3-8167feb8e581');
/*!40000 ALTER TABLE `emosocialapp_friendsrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_moments`
--

DROP TABLE IF EXISTS `emosocialapp_moments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_moments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `postTime` varchar(64) NOT NULL,
  `postContent` varchar(255) NOT NULL,
  `postPic` varchar(255) DEFAULT NULL,
  `postVideo` varchar(255) DEFAULT NULL,
  `postId_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emoSocialApp_moments_postId_id_c26c724b_fk_emoSocialApp_user_id` (`postId_id`),
  CONSTRAINT `emoSocialApp_moments_postId_id_c26c724b_fk_emoSocialApp_user_id` FOREIGN KEY (`postId_id`) REFERENCES `emosocialapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_moments`
--

LOCK TABLES `emosocialapp_moments` WRITE;
/*!40000 ALTER TABLE `emosocialapp_moments` DISABLE KEYS */;
INSERT INTO `emosocialapp_moments` VALUES (28,'2024-05-15 17:43:55','图片朋友圈','http://127.0.0.1:8000/moments/Snipaste_2024-05-15_17-43-42.jpg','','b2d07f96-781b-4eb0-adb3-8167feb8e581'),(29,'2024-05-15 17:47:11','视频朋友圈','','http://127.0.0.1:8000/videos/35d3bc7cd986d0aa674fabb6fb28f870.mp4','b2d07f96-781b-4eb0-adb3-8167feb8e581'),(30,'2024-05-16 22:56:02','今天很开心，吃了小火锅','','','daa65b21-a34e-437e-adf0-9983de150ae0'),(49,'2024-05-29 13:50:49','明天谁和我一起去吃火锅呢？','','','b2d07f96-781b-4eb0-adb3-8167feb8e581'),(50,'2024-05-29 17:58:21','去川西玩了','http://127.0.0.1:8000/moments/微信图片_20240529175807.jpg','','89cced28-8678-46a5-b7d2-00c3b28589d2'),(51,'2024-05-29 17:59:31','好无聊啊','','','eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d'),(52,'2024-05-29 18:00:40','这件衣服好看吗？','http://127.0.0.1:8000/moments/5.jpg','','c34e015c-392b-4a73-81ed-9a07a01ba86d'),(53,'2024-05-29 18:01:47','今天去动物园了','http://127.0.0.1:8000/moments/7.jpg','','b8cd9132-693f-497d-933f-d3c81cda70fb'),(54,'2024-05-29 18:21:56','明天就要毕业答辩了','http://127.0.0.1:8000/moments/6.jpg','','b0abe837-267d-4382-97e4-3cce91845d4d'),(55,'2024-05-29 18:25:02','毕业快乐','http://127.0.0.1:8000/moments/8.jpg','','8d1f88a2-c367-4e65-b391-391c9fd0684d');
/*!40000 ALTER TABLE `emosocialapp_moments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_momentscomment`
--

DROP TABLE IF EXISTS `emosocialapp_momentscomment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_momentscomment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `commentContent` varchar(64) DEFAULT NULL,
  `commentId_id` varchar(255) DEFAULT NULL,
  `momentId_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emoSocialApp_moments_commentId_id_256da5f5_fk_emoSocial` (`commentId_id`),
  KEY `emoSocialApp_moments_momentId_id_e373cfb3_fk_emoSocial` (`momentId_id`),
  CONSTRAINT `emoSocialApp_moments_commentId_id_256da5f5_fk_emoSocial` FOREIGN KEY (`commentId_id`) REFERENCES `emosocialapp_user` (`id`),
  CONSTRAINT `emoSocialApp_moments_momentId_id_e373cfb3_fk_emoSocial` FOREIGN KEY (`momentId_id`) REFERENCES `emosocialapp_moments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_momentscomment`
--

LOCK TABLES `emosocialapp_momentscomment` WRITE;
/*!40000 ALTER TABLE `emosocialapp_momentscomment` DISABLE KEYS */;
INSERT INTO `emosocialapp_momentscomment` VALUES (8,'味道怎么样？','b8cd9132-693f-497d-933f-d3c81cda70fb',30),(9,'有人一起吗？','b2d07f96-781b-4eb0-adb3-8167feb8e581',49),(10,'还不错呢','b8cd9132-693f-497d-933f-d3c81cda70fb',52),(11,'帅','b8cd9132-693f-497d-933f-d3c81cda70fb',50),(12,'小鹿好可爱','89cced28-8678-46a5-b7d2-00c3b28589d2',53),(13,'好看呢','89cced28-8678-46a5-b7d2-00c3b28589d2',52),(14,'出来玩吗？','89cced28-8678-46a5-b7d2-00c3b28589d2',51),(15,'在弄毕设吗？','89cced28-8678-46a5-b7d2-00c3b28589d2',29),(16,'漂亮！','89cced28-8678-46a5-b7d2-00c3b28589d2',28),(17,'下次和我一起去吧！','eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d',53),(22,'毕业快乐！','3eee19ed-a05d-41a7-ab43-89ee82c9ea6b',55);
/*!40000 ALTER TABLE `emosocialapp_momentscomment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_momentslike`
--

DROP TABLE IF EXISTS `emosocialapp_momentslike`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_momentslike` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `likeId_id` varchar(255) DEFAULT NULL,
  `momentId_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emoSocialApp_moments_likeId_id_66892a7f_fk_emoSocial` (`likeId_id`),
  KEY `emoSocialApp_moments_momentId_id_cf01a901_fk_emoSocial` (`momentId_id`),
  CONSTRAINT `emoSocialApp_moments_likeId_id_66892a7f_fk_emoSocial` FOREIGN KEY (`likeId_id`) REFERENCES `emosocialapp_user` (`id`),
  CONSTRAINT `emoSocialApp_moments_momentId_id_cf01a901_fk_emoSocial` FOREIGN KEY (`momentId_id`) REFERENCES `emosocialapp_moments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_momentslike`
--

LOCK TABLES `emosocialapp_momentslike` WRITE;
/*!40000 ALTER TABLE `emosocialapp_momentslike` DISABLE KEYS */;
INSERT INTO `emosocialapp_momentslike` VALUES (21,'b8cd9132-693f-497d-933f-d3c81cda70fb',30),(22,'b2d07f96-781b-4eb0-adb3-8167feb8e581',49),(23,'b8cd9132-693f-497d-933f-d3c81cda70fb',52),(24,'b8cd9132-693f-497d-933f-d3c81cda70fb',50),(25,'89cced28-8678-46a5-b7d2-00c3b28589d2',53),(26,'89cced28-8678-46a5-b7d2-00c3b28589d2',51),(27,'89cced28-8678-46a5-b7d2-00c3b28589d2',29),(29,'eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d',50),(30,'eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d',49),(31,'eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d',30),(32,'eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d',29),(33,'eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d',28),(34,'eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d',53),(35,'b2d07f96-781b-4eb0-adb3-8167feb8e581',54),(36,'b2d07f96-781b-4eb0-adb3-8167feb8e581',55),(42,'3eee19ed-a05d-41a7-ab43-89ee82c9ea6b',55);
/*!40000 ALTER TABLE `emosocialapp_momentslike` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_user`
--

DROP TABLE IF EXISTS `emosocialapp_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_user` (
  `id` varchar(255) NOT NULL,
  `account` varchar(16) NOT NULL,
  `password` varchar(255) NOT NULL,
  `type` varchar(16) NOT NULL,
  `idNumber` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account` (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_user`
--

LOCK TABLES `emosocialapp_user` WRITE;
/*!40000 ALTER TABLE `emosocialapp_user` DISABLE KEYS */;
INSERT INTO `emosocialapp_user` VALUES ('3eee19ed-a05d-41a7-ab43-89ee82c9ea6b','27851184621','1c6088d152a1daf8b9f565104a3d51a1c7faf925b3a7d2fc61c72e09b2c3fadc','普通用户','220381200112201133'),('661140f6-ffea-40df-81b6-f55978cb8e85','admin123','Lq123321','管理员','220381231551231'),('89cced28-8678-46a5-b7d2-00c3b28589d2','1233211','1c6088d152a1daf8b9f565104a3d51a1c7faf925b3a7d2fc61c72e09b2c3fadc','普通用户','51231313551356'),('8d1f88a2-c367-4e65-b391-391c9fd0684d','1233216','1c6088d152a1daf8b9f565104a3d51a1c7faf925b3a7d2fc61c72e09b2c3fadc','普通用户','5120204313586'),('a182d2e6-81be-4126-8012-c5c79ee1170d','admin','bfceb69d2f611031f33f0fbb76ed1d1e0d772475297159b1148515cc2d735b49','管理员','2203812313123123'),('b0abe837-267d-4382-97e4-3cce91845d4d','1233214','1c6088d152a1daf8b9f565104a3d51a1c7faf925b3a7d2fc61c72e09b2c3fadc','普通用户','51202405813513'),('b2d07f96-781b-4eb0-adb3-8167feb8e581','123456','bfceb69d2f611031f33f0fbb76ed1d1e0d772475297159b1148515cc2d735b49','普通用户','1231414121241'),('b8cd9132-693f-497d-933f-d3c81cda70fb','2785118462','1c6088d152a1daf8b9f565104a3d51a1c7faf925b3a7d2fc61c72e09b2c3fadc','普通用户','220381200112201133'),('bf842308-3aa5-4304-a59c-b25bc376f41c','admin456','123321Lq','管理员','220381200112201111'),('c34e015c-392b-4a73-81ed-9a07a01ba86d','1233213','1c6088d152a1daf8b9f565104a3d51a1c7faf925b3a7d2fc61c72e09b2c3fadc','普通用户','5120204513551'),('c6ce19b2-5f60-4f49-bda1-fc9fcc8a5240','1233215','1c6088d152a1daf8b9f565104a3d51a1c7faf925b3a7d2fc61c72e09b2c3fadc','普通用户','51513135513367'),('daa65b21-a34e-437e-adf0-9983de150ae0','1111122222','Lq1111122222','普通用户','123131231231'),('eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d','1233212','1c6088d152a1daf8b9f565104a3d51a1c7faf925b3a7d2fc61c72e09b2c3fadc','普通用户','512513395123');
/*!40000 ALTER TABLE `emosocialapp_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emosocialapp_userprofile`
--

DROP TABLE IF EXISTS `emosocialapp_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emosocialapp_userprofile` (
  `id_id` varchar(255) NOT NULL,
  `name` varchar(16) NOT NULL,
  `email` varchar(254) NOT NULL,
  `gender` varchar(16) NOT NULL,
  `birthday` date NOT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `signature` varchar(32) DEFAULT NULL,
  `profileBp` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_id`),
  CONSTRAINT `emoSocialApp_userprofile_id_id_1db323bd_fk_emoSocialApp_user_id` FOREIGN KEY (`id_id`) REFERENCES `emosocialapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emosocialapp_userprofile`
--

LOCK TABLES `emosocialapp_userprofile` WRITE;
/*!40000 ALTER TABLE `emosocialapp_userprofile` DISABLE KEYS */;
INSERT INTO `emosocialapp_userprofile` VALUES ('3eee19ed-a05d-41a7-ab43-89ee82c9ea6b','千青','2785118462@qq.com','男','2024-06-04','http://127.0.0.1:8000/media/user/微信图片_20240601110730.jpg','今天也要加油！','http://127.0.0.1:8000/media/profileBp/微信图片_20240601110735.jpg'),('661140f6-ffea-40df-81b6-f55978cb8e85','admin123','8851325@qq.com','男','2024-06-05','src/profile_bp/defaultAvatar.jpg',NULL,'src/profile_bp/defaultBp.jpg'),('89cced28-8678-46a5-b7d2-00c3b28589d2','懒羊羊','1235513@qq.com','男','2024-05-10','http://127.0.0.1:8000/media/user/微信图片_20240529123254.jpg','Hi, there','http://127.0.0.1:8000/media/profileBp/1.jpg'),('8d1f88a2-c367-4e65-b391-391c9fd0684d','橘子','59983135@qq.com','男','2024-05-06','http://127.0.0.1:8000/media/user/4.jpg','我思故我在','http://127.0.0.1:8000/media/profileBp/3.jpg'),('a182d2e6-81be-4126-8012-c5c79ee1170d','admin','admin@163.com','男','2020-01-01','http://127.0.0.1:8000/media/user/Snipaste_2024-05-15_16-05-00.jpg','管理员账号','src/profile_bp/bp2.jpg'),('b0abe837-267d-4382-97e4-3cce91845d4d','echo','12333513@qq.com','男','2024-05-16','http://127.0.0.1:8000/media/user/1.jpg','闭上眼也是蓝天白云','http://127.0.0.1:8000/media/profileBp/2.jpg'),('b2d07f96-781b-4eb0-adb3-8167feb8e581','1771','123@qq.com','男','2024-05-08','http://127.0.0.1:8000/media/user/微信图片_20240526190642.jpg','现在是24年5月26日下午七点02','http://127.0.0.1:8000/media/profileBp/bp3.jpg'),('b8cd9132-693f-497d-933f-d3c81cda70fb','春天小狗','8865413@qq.com','男','2024-05-08','http://127.0.0.1:8000/media/user/微信图片_20240527163029.jpg','春天要到咯','http://127.0.0.1:8000/media/profileBp/4.jpg'),('bf842308-3aa5-4304-a59c-b25bc376f41c','admin123','1716540434@qq.com','男','2024-05-01','src/profile_bp/defaultAvatar.jpg',NULL,'src/profile_bp/defaultBp.jpg'),('c34e015c-392b-4a73-81ed-9a07a01ba86d','哼哼','995135225@163.com','女','2024-02-13','http://127.0.0.1:8000/media/user/微信图片_20240529123301.jpg','没见过的浪漫 使我安然','http://127.0.0.1:8000/media/profileBp/6.jpg'),('c6ce19b2-5f60-4f49-bda1-fc9fcc8a5240','收敛水','58133325@qq.com','男','2024-05-06','http://127.0.0.1:8000/media/user/7.jpg','他的填充物是遗憾，笑脸是假装','http://127.0.0.1:8000/media/profileBp/5.jpg'),('daa65b21-a34e-437e-adf0-9983de150ae0','大号123','123@qq.com','女','2024-05-09','http://127.0.0.1:8000/media/user/Snipaste_2024-05-14_11-35-41.jpg','我是大号','src/profile_bp/bp1.jpg'),('eb08fbdc-315b-4ac7-86a7-4e8a38ebc56d','Lllichee_-','77513442@qq.com','女','2024-05-11','http://127.0.0.1:8000/media/user/微信图片_20240529123246.jpg','I say \"go','http://127.0.0.1:8000/media/profileBp/3.jpg');
/*!40000 ALTER TABLE `emosocialapp_userprofile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-05 15:53:23
