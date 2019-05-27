/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost:3306
 Source Schema         : hdcar

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 19/05/2019 06:57:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 77 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_blacklist
-- ----------------------------
DROP TABLE IF EXISTS `car_blacklist`;
CREATE TABLE `car_blacklist`  (
  `plate_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `black_time` date NOT NULL,
  `vlolation_info` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`plate_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_car
-- ----------------------------
DROP TABLE IF EXISTS `car_car`;
CREATE TABLE `car_car`  (
  `plate_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `in_date` datetime(6) NULL,
  `out_date` datetime(6) NULL DEFAULT NULL,
  `stay_date` int(11) NULL DEFAULT NULL,
  `money` decimal(6, 2) NULL DEFAULT NULL,
  `car_type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `enter_info` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `exit_info` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`plate_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_car_school
-- ----------------------------
DROP TABLE IF EXISTS `car_car_school`;
CREATE TABLE `car_car_school`  (
  `plate_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `word_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `idcard` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `partment_id` int(11) NOT NULL,
  PRIMARY KEY (`plate_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_chage_money
-- ----------------------------
DROP TABLE IF EXISTS `car_chage_money`;
CREATE TABLE `car_chage_money`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `charge_type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `total_money` decimal(6, 2) NOT NULL,
  `charge_time` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 47 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_charge
-- ----------------------------
DROP TABLE IF EXISTS `car_charge`;
CREATE TABLE `car_charge`  (
  `plate_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `charge_type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `charge_time` datetime(6) NULL,
  `collector` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`plate_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_charge_standard
-- ----------------------------
DROP TABLE IF EXISTS `car_charge_standard`;
CREATE TABLE `car_charge_standard`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hour_money` decimal(5, 2) NOT NULL,
  `day_money` decimal(5, 2) NOT NULL,
  `cross_money` decimal(5, 2) NOT NULL,
  `able` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_images
-- ----------------------------
DROP TABLE IF EXISTS `car_images`;
CREATE TABLE `car_images`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entry_image` longblob NULL,
  `exit_image` longblob NULL,
  `plate_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_log
-- ----------------------------
DROP TABLE IF EXISTS `car_log`;
CREATE TABLE `car_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `operation` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `operation_time` datetime(6) NULL,
  `ip_address` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_online
-- ----------------------------
DROP TABLE IF EXISTS `car_online`;
CREATE TABLE `car_online`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `login_time` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_partment
-- ----------------------------
DROP TABLE IF EXISTS `car_partment`;
CREATE TABLE `car_partment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `partment_id` int(11) NOT NULL,
  `partment_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_plate
-- ----------------------------
DROP TABLE IF EXISTS `car_plate`;
CREATE TABLE `car_plate`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plate_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_power
-- ----------------------------
DROP TABLE IF EXISTS `car_power`;
CREATE TABLE `car_power`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `power_id` int(11) NOT NULL,
  `power_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for car_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `car_userinfo`;
CREATE TABLE `car_userinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `job` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `idcard` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `power_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- View structure for car_school_view
-- ----------------------------
DROP VIEW IF EXISTS `car_school_view`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`localhost` SQL SECURITY DEFINER VIEW `car_school_view` AS select `car_car_school`.`plate_number` AS `plate_number`,`car_car_school`.`name` AS `name`,`car_car_school`.`sex` AS `sex`,`car_car_school`.`word_number` AS `word_number`,`car_car_school`.`idcard` AS `idcard`,`car_car_school`.`phone` AS `phone`,`car_partment`.`partment_name` AS `partment_name` from (`car_car_school` join `car_partment`) where (`car_car_school`.`partment_id` = `car_partment`.`partment_id`);

-- ----------------------------
-- View structure for charge_money_view
-- ----------------------------
DROP VIEW IF EXISTS `charge_money_view`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`localhost` SQL SECURITY DEFINER VIEW `charge_money_view` AS select `car_charge`.`plate_number` AS `plate_number`,`car_car`.`car_type` AS `car_type`,`car_car`.`stay_date` AS `stay_date`,`car_car`.`money` AS `money`,`car_charge`.`charge_type` AS `charge_type`,`car_charge`.`charge_time` AS `charge_time`,`car_charge`.`collector` AS `collector` from (`car_car` join `car_charge`) where (`car_car`.`plate_number` = `car_charge`.`plate_number`);

-- ----------------------------
-- View structure for user_view
-- ----------------------------
DROP VIEW IF EXISTS `user_view`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`localhost` SQL SECURITY DEFINER VIEW `user_view` AS select `car_userinfo`.`id` AS `id`,`car_userinfo`.`name` AS `name`,`car_userinfo`.`sex` AS `sex`,`car_userinfo`.`job` AS `job`,`car_userinfo`.`idcard` AS `idcard`,`car_userinfo`.`phone` AS `phone`,`car_power`.`power_name` AS `power_name` from (`car_userinfo` join `car_power`) where (`car_userinfo`.`power_id` = `car_power`.`power_id`);

-- ----------------------------
-- Triggers structure for table car_car
-- ----------------------------
DROP TRIGGER IF EXISTS `stay_time_insert`;
delimiter ;;
CREATE TRIGGER `stay_time_insert` BEFORE INSERT ON `car_car` FOR EACH ROW begin
set New.stay_date=(select ABS(TIMESTAMPDIFF(MINUTE,New.out_date,New.in_date)));
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table car_car
-- ----------------------------
DROP TRIGGER IF EXISTS `money_insert`;
delimiter ;;
CREATE TRIGGER `money_insert` BEFORE INSERT ON `car_car` FOR EACH ROW begin
declare hour_m FLOAT;
DECLARE across_m FLOAT;
DECLARE day_m FLOAT;
declare m  FLOAT;

select hour_money,day_money,cross_money into hour_m,day_m,across_m from car_charge_standard where able = 1;


if New.car_type != '学校车辆' and New.enter_info != New.exit_info and New.stay_date < 30 then
    set m = across_m;
elseif New.car_type != '学校车辆' and New.stay_date < 1400 then
    set m = hour_m * CEIL(New.stay_date/30) /2;
elseif New.car_type != '学校车辆' and New.stay_date > 1400 then
    set m = day_m;
elseif New.car_type = '学校车辆' then
    set m = 0;
else
    set m = 0;
end if;
set New.money = m;
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table car_car
-- ----------------------------
DROP TRIGGER IF EXISTS `money`;
delimiter ;;
CREATE TRIGGER `money` BEFORE UPDATE ON `car_car` FOR EACH ROW begin
declare hour_m FLOAT;
DECLARE across_m FLOAT;
DECLARE day_m FLOAT;
declare m  FLOAT;

select hour_money,day_money,cross_money into hour_m,day_m,across_m from car_charge_standard where able = 1;


if New.car_type != '学校车辆' and New.enter_info != New.exit_info and New.stay_date < 30 then
    set m = across_m;
elseif New.car_type != '学校车辆' and New.stay_date < 1400 then
    set m = hour_m * CEIL(New.stay_date/30) /2;
elseif New.car_type != '学校车辆' and New.stay_date > 1400 then
    set m = day_m;
elseif New.car_type = '学校车辆' then
    set m = 0;
else
		set m = 0;
end if;
set New.money = m;
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table car_car
-- ----------------------------
DROP TRIGGER IF EXISTS `stay_time`;
delimiter ;;
CREATE TRIGGER `stay_time` BEFORE UPDATE ON `car_car` FOR EACH ROW begin
set New.stay_date=(select ABS(TIMESTAMPDIFF(MINUTE,New.out_date,New.in_date)));
end
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
