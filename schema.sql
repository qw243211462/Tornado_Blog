drop database if EXISTS blog;

create database blog;

use blog;

grant all on blog.* to 'tong@Tong' identified by 'qw13198321328';

create TABLE user(
  `id` mediumint not null auto_increment comment '用户id' ,
  `user_email` varchar(50) not null COMMENT '用户邮箱',
  `user_password` VARCHAR(50) not NULL COMMENT  '用户密码',
  `user_admin` BOOL  NULL DEFAULT 0 COMMENT '是否为管理员',
  `user_name` varchar(50) not null COMMENT '用户名',
  `user_image` varchar(500) null DEFAULT NUll COMMENT '用户头像',
  `user_created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '用户创建时间',
  primary key (`id`)
) engine=innodb DEFAULT CHARSET=utf8;

CREATE TABLE articles (
  `id` mediumint not null auto_increment COMMENT '博客内容id',
  `article_category` VARCHAR(50) not NULL COMMENT '文章种类',
  `article_title` VARCHAR(50) NOT NULL COMMENT '文章标题',
  `article_content` mediumtext not null COMMENT  '文章内容',
  `article_click_number` int NOT NULL DEFAULT 0 COMMENT '文章点击次数',
  `article_comment_number` INT NOT NULL DEFAULT 0 COMMENT '文章评论次数',
  `article_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '文章创建时间',
  primary key (`id`)
) engine=innodb DEFAULT CHARSET=utf8;

CREATE TABLE category(
  `id` mediumint not null auto_increment COMMENT '文章种类id',
  `category_name` VARCHAR(50) NOT NULL COMMENT '文章种类名称',
  primary key (`id`)
) engine=innodb DEFAULT CHARSET=utf8;

CREATE TABLE comments(
  `id` mediumint not null auto_increment COMMENT '评论id',
  `article_id` mediumint NOT NULL COMMENT  '文章id',
  `comment_people_name` VARCHAR(50) NOT NULL COMMENT '评论者姓名',
  `comment_people_image` varchar(500) null COMMENT '评论者头像',
  `comment_contents` mediumtext not null COMMENT '评论内容',
  `comment_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '评论发布时间',
  primary key (`id`),
  FOREIGN KEY(`article_id`) REFERENCES articles(`id`)
) engine=innodb DEFAULT CHARSET=utf8;
