-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 05, 2012 at 06:16 PM
-- Server version: 5.5.24-log
-- PHP Version: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `facebank`
--

-- --------------------------------------------------------

--
-- Table structure for table `fbsearchlog`
--

CREATE TABLE IF NOT EXISTS `fbsearchlog` (
  `RunId` int(11) NOT NULL AUTO_INCREMENT,
  `BatchId` int(11) DEFAULT NULL,
  `RunDate` datetime DEFAULT NULL,
  `Keyword` varchar(50) DEFAULT NULL,
  `HarvestedThisRun` int(11) DEFAULT NULL,
  `TotalHarvested` int(11) DEFAULT NULL,
  `RunTime` float DEFAULT NULL,
  PRIMARY KEY (`RunId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=338 ;

-- --------------------------------------------------------

--
-- Table structure for table `searchbank`
--

CREATE TABLE IF NOT EXISTS `searchbank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `run_id` int(11) DEFAULT NULL,
  `fid` varchar(250) DEFAULT NULL,
  `from_name` varchar(250) DEFAULT NULL,
  `from_id` bigint(20) DEFAULT NULL,
  `keyword` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `posted` datetime DEFAULT NULL,
  `message` varchar(5000) DEFAULT NULL,
  `story` varchar(5000) DEFAULT NULL,
  `link` varchar(1500) DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  `comments` int(11) DEFAULT NULL,
  `shares` int(11) DEFAULT NULL,
  `harvested` datetime DEFAULT NULL,
  `page_likes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12255 ;

-- --------------------------------------------------------

--
-- Table structure for table `searches`
--

CREATE TABLE IF NOT EXISTS `searches` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `run_id` int(11) DEFAULT NULL,
  `fid` varchar(250) DEFAULT NULL,
  `from_name` varchar(250) DEFAULT NULL,
  `from_id` bigint(20) DEFAULT NULL,
  `keyword` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `posted` datetime DEFAULT NULL,
  `message` varchar(5000) DEFAULT NULL,
  `story` varchar(5000) DEFAULT NULL,
  `link` varchar(1500) DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  `comments` int(11) DEFAULT NULL,
  `shares` int(11) DEFAULT NULL,
  `harvested` datetime DEFAULT NULL,
  `page_likes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MEMORY DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
