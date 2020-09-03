/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 01/09/2020 15:49:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for command_table
-- ----------------------------
DROP TABLE IF EXISTS `command_table`;
CREATE TABLE `command_table`  (
  `OBJECTID` bigint(20) NOT NULL,
  `DEPARTMENT` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `OFFICE` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ROADNAME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `NAME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `POST` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `PHONENUMBER` bigint(20) NULL DEFAULT NULL,
  `OFFICETELEPHONE` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`OBJECTID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of command_table
-- ----------------------------
INSERT INTO `command_table` VALUES (1, '指挥体系', '指挥长', 'NULL', '王  峰', '书记', 15538337733, 66909600);
INSERT INTO `command_table` VALUES (2, '指挥体系', '指挥长', NULL, '李锦勇', '主  任', 15617810753, 66909399);
INSERT INTO `command_table` VALUES (3, '指挥体系', '副指挥长', NULL, '张淑利', '党工委委员', 13938564957, 66909609);
INSERT INTO `command_table` VALUES (4, '指挥体系', '副指挥长', NULL, '张  旭', '副科级干部', 18638021688, 66909619);
INSERT INTO `command_table` VALUES (5, '指挥体系', '副指挥长', NULL, '苏精适', '副书记', 13838158688, 66909606);
INSERT INTO `command_table` VALUES (6, '平台力量', '党政办公室', '西一街', '马  超', '党政办主任', 13633866639, 66908026);
INSERT INTO `command_table` VALUES (7, '平台力量', '党政办公室', '云台路', '宋琼阁', '党建办主任', 15003840006, 66908052);
INSERT INTO `command_table` VALUES (8, '平台力量', '纪工委监察办公室', '益民路', '张锋涛', '主  任', 13838042088, 66909608);
INSERT INTO `command_table` VALUES (9, '平台力量', '综合执法办公室', '正兴街、兴盛路、福寿街', '李海涛', '主  任', 13683804102, 66909613);
INSERT INTO `command_table` VALUES (10, '平台力量', '公共服务办公室', '自由路', '王利杰', '科  长', 17320133344, 66909392);
INSERT INTO `command_table` VALUES (11, '平台力量', '区域发展办公室', '民主路', '林璞楠', '主  任', 13938582388, 66909398);
INSERT INTO `command_table` VALUES (12, '平台力量', '公共安全管理办公室', '二七路', '薛运涛', '科  长', 13393736771, 66909615);
INSERT INTO `command_table` VALUES (13, '平台力量', '社区服务中心', '自由路支路', '贺  淼', '主  任', 18103969997, 66909451);
INSERT INTO `command_table` VALUES (14, '平台力量', '社会治安综合治理中心', '解放路', '张  涂', '主  任', 13598883689, 66909119);
INSERT INTO `command_table` VALUES (15, '平台力量', '退役军人服务站', '民主路北段', '白  利', '科  长', 17838356977, 66909612);
INSERT INTO `command_table` VALUES (16, '应急力量', '执法中队', NULL, '石静磊', '队  长', 13607649603, NULL);
INSERT INTO `command_table` VALUES (17, '应急力量', '执法中队', NULL, '付中江', '副队长', 15838317776, NULL);
INSERT INTO `command_table` VALUES (18, '应急力量', '执法中队', NULL, '王  东', NULL, 15938722973, NULL);
INSERT INTO `command_table` VALUES (19, '应急力量', '执法中队', NULL, '张家耀', NULL, 13633812399, NULL);
INSERT INTO `command_table` VALUES (20, '应急力量', '执法中队', NULL, '李  宇', NULL, 18737134937, NULL);
INSERT INTO `command_table` VALUES (21, '应急力量', '执法中队', NULL, '杨泽付', NULL, 18695861018, NULL);
INSERT INTO `command_table` VALUES (22, '应急力量', '执法中队', NULL, '乔  飞', NULL, 15225059057, NULL);
INSERT INTO `command_table` VALUES (23, '应急力量', '执法中队', NULL, '岳  珂', NULL, 15188330242, NULL);
INSERT INTO `command_table` VALUES (24, '应急力量', '执法中队', NULL, '韩  栋', NULL, 15803991317, NULL);
INSERT INTO `command_table` VALUES (25, '应急力量', '执法中队', NULL, '顾松涛', NULL, 13939077758, NULL);
INSERT INTO `command_table` VALUES (26, '应急力量', '执法中队', NULL, '孟建伟', NULL, 13598829118, NULL);
INSERT INTO `command_table` VALUES (27, '应急力量', '执法中队', NULL, '高黎园', NULL, 15890089668, NULL);
INSERT INTO `command_table` VALUES (28, '应急力量', '执法中队', NULL, '董  红', NULL, 13598872652, NULL);
INSERT INTO `command_table` VALUES (29, '应急力量', '执法中队', NULL, '陈  潇', NULL, 18539298800, NULL);
INSERT INTO `command_table` VALUES (30, '应急力量', '综合执法办公室', NULL, '李海涛', '主  任', 13683804102, 66909613);
INSERT INTO `command_table` VALUES (31, '应急力量', '综合执法办公室', NULL, '乔志伟', '副主任', 15936250757, NULL);
INSERT INTO `command_table` VALUES (32, '应急力量', '综合执法办公室', NULL, '赵  磊', '副主任', 18538265052, NULL);
INSERT INTO `command_table` VALUES (33, '应急力量', '综合执法办公室', NULL, '罗建业', NULL, 17839973680, NULL);
INSERT INTO `command_table` VALUES (34, '应急力量', '综合执法办公室', NULL, '曹  霄', NULL, 13526557507, NULL);
INSERT INTO `command_table` VALUES (35, '应急力量', '综合执法办公室', NULL, '欧建利', NULL, 13838045058, NULL);
INSERT INTO `command_table` VALUES (36, '应急力量', '综合执法办公室', NULL, '王  雨', NULL, 18538265031, NULL);
INSERT INTO `command_table` VALUES (37, '应急力量', '城市管理协管队', NULL, '赵世代', '队  长', 15137175177, NULL);
INSERT INTO `command_table` VALUES (38, '应急力量', '城市管理协管队', NULL, '朱春民', '副队长', 13838253296, NULL);
INSERT INTO `command_table` VALUES (39, '应急力量', '城市管理协管队', NULL, '李光辉', NULL, 13072666343, NULL);
INSERT INTO `command_table` VALUES (40, '应急力量', '城市管理协管队', NULL, '胡亚飞', NULL, 13837199530, NULL);
INSERT INTO `command_table` VALUES (41, '应急力量', '城市管理协管队', NULL, '赵  琛', NULL, 15515615595, NULL);
INSERT INTO `command_table` VALUES (42, '应急力量', '城市管理协管队', NULL, '闫  闯', NULL, 13523555842, NULL);
INSERT INTO `command_table` VALUES (43, '应急力量', '城市管理协管队', NULL, '曾  澳', NULL, 13838049935, NULL);
INSERT INTO `command_table` VALUES (44, '应急力量', '城市管理协管队', NULL, '赵灿世', NULL, 18203603008, NULL);
INSERT INTO `command_table` VALUES (45, '应急力量', '城市管理协管队', NULL, '程永红', NULL, 13592601103, NULL);
INSERT INTO `command_table` VALUES (46, '应急力量', '巡防中队', NULL, '董利强', '队  长', 13937122595, NULL);
INSERT INTO `command_table` VALUES (47, '应急力量', '巡防中队', NULL, '赵建伟', NULL, 13838181502, NULL);
INSERT INTO `command_table` VALUES (48, '应急力量', '巡防中队', NULL, '海  彬', NULL, 13653817821, NULL);
INSERT INTO `command_table` VALUES (49, '应急力量', '巡防中队', NULL, '刘  强', NULL, 15136136952, NULL);
INSERT INTO `command_table` VALUES (50, '应急力量', '巡防中队', NULL, '张红志', NULL, 18839782537, NULL);
INSERT INTO `command_table` VALUES (51, '应急力量', '巡防中队', NULL, '王成贤', NULL, 15093406928, NULL);
INSERT INTO `command_table` VALUES (52, '应急力量', '巡防中队', NULL, '张贇昊', NULL, 18539449208, NULL);
INSERT INTO `command_table` VALUES (53, '应急力量', '巡防中队', NULL, '李  博', NULL, 18838209270, NULL);

SET FOREIGN_KEY_CHECKS = 1;
