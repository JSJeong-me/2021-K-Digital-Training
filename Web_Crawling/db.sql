-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.2.14-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- pythondb 데이터베이스 구조 내보내기
DROP DATABASE IF EXISTS `pythondb`;
CREATE DATABASE IF NOT EXISTS `pythondb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `pythondb`;

-- 테이블 pythondb.tbl_crawlingdata 구조 내보내기
DROP TABLE IF EXISTS `tbl_crawlingdata`;
CREATE TABLE IF NOT EXISTS `tbl_crawlingdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `contents` text DEFAULT NULL,
  `keyword` varchar(50) DEFAULT NULL,
  `regdate` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 pythondb.tbl_crawlingdata:~0 rows (대략적) 내보내기
DELETE FROM `tbl_crawlingdata`;
/*!40000 ALTER TABLE `tbl_crawlingdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_crawlingdata` ENABLE KEYS */;

-- 테이블 pythondb.tbl_keyword 구조 내보내기
DROP TABLE IF EXISTS `tbl_keyword`;
CREATE TABLE IF NOT EXISTS `tbl_keyword` (
  `keyword` varchar(50) NOT NULL,
  PRIMARY KEY (`keyword`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 pythondb.tbl_keyword:~0 rows (대략적) 내보내기
DELETE FROM `tbl_keyword`;
/*!40000 ALTER TABLE `tbl_keyword` DISABLE KEYS */;
INSERT INTO `tbl_keyword` (`keyword`) VALUES
	('로마'),
	('바로셀로나'),
	('파리');
/*!40000 ALTER TABLE `tbl_keyword` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
