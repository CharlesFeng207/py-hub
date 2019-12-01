/* SELECT max(lanId) FROM `language`; */
/* show table status like "language"; */

-- 准备删除
-- delete from `language`.`language` where lanId>=2217&&lanId<=2248;
-- delete from `language`.`language` where lanId>=2359&&lanId<=2540;

-- delete from `language`.`language` where lanId>=2660&&lanId<=3700;
-- delete from `language`.`language` where lanId=2128;
/* ALTER TABLE language MODIFY lanId INT NOT NULL AUTO_INCREMENT; */
/* INSERT INTO language (cn) VALUES ("你妹"); */
/* ALTER TABLE language Auto_increment=12426; */
-- SELECT * FROM `language`.`language` where lanId>=2359&&lanId<=2659;
-- SELECT * FROM `language` where lanId>12200;
/* SELECT * FROM `language` where cn="限 时"; */
/* INSERT INTO language ( lanId, cn, en, zh, jp, ko ) VALUES (0, "", "", "", "", ""); */
/* select count(*) from language; */
/* select max(lanId) from language; */
/* drop table language; */
/* CREATE TABLE IF NOT EXISTS `language`(
   `lanId` INT NOT NULL AUTO_INCREMENT,
   `lan0` TEXT,
   `lan1` TEXT,
   `lan2` TEXT,
   `lan3` TEXT,
   `lan4` TEXT,
   PRIMARY KEY ( `lanId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8; */