-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 25, 2020 at 07:31 AM
-- Server version: 5.5.54
-- PHP Version: 5.3.4

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `chatbot`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointmentdb`
--

CREATE TABLE IF NOT EXISTS `appointmentdb` (
  `sno` int(100) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `location` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `dtype` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `appointmentdb`
--

INSERT INTO `appointmentdb` (`sno`, `fname`, `lname`, `contact`, `location`, `gender`, `dtype`, `date`) VALUES
(3, 'kishan', 'sinha', 8756342210, 'mumbai', 'Male ', 'Fever', '2020-04-25'),
(4, 'rakesh', 'mishra', 9057683211, 'Mumbai', 'Male ', 'Headache', '2020-04-25'),
(5, 'madhav', 'soni', 8976543892, 'nashik', 'Male ', 'Chest Pain', '2020-04-25');

-- --------------------------------------------------------

--
-- Table structure for table `doc`
--

CREATE TABLE IF NOT EXISTS `doc` (
  `fname` varchar(100) NOT NULL,
  `mname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `pwd` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doc`
--

INSERT INTO `doc` (`fname`, `mname`, `lname`, `contact`, `email`, `gender`, `uname`, `pwd`) VALUES
('sandip', 'kumar', 'sharma', 98764452213, 'sandip@gmail.com', 'Male ', 'sandip', 'sandip12345'),
('sahil', 'kumar', 'mishra', 8976545563, 'sahil@ymail.com', 'Male ', 'sahil', 'sahil123');

-- --------------------------------------------------------

--
-- Table structure for table `schedule`
--

CREATE TABLE IF NOT EXISTS `schedule` (
  `SL_NO` int(100) NOT NULL,
  `day` varchar(100) NOT NULL,
  `time1` varchar(100) NOT NULL,
  `time2` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `schedule`
--

INSERT INTO `schedule` (`SL_NO`, `day`, `time1`, `time2`) VALUES
(1, 'sunday', 'OFF', 'OFF'),
(2, 'monday', '09.00 AM - 12.00 PM', '04.00 PM -09.00 PM'),
(3, 'tuesday', '09.00 AM - 12.00 PM', '05.00 PM - 09.00 PM'),
(4, 'wednesday', '09.00 AM - 12.00 PM', '05.00 PM - 09.00 PM'),
(5, 'thursday', '09.00 AM - 12.00 PM', '05.00 PM - 09.00 PM'),
(6, 'friday', '09.00 AM - 12.00 PM', '05.00 PM - 09.00 PM'),
(7, 'saturday', '09.00 AM - 02.00 PM', 'OFF');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `fname` varchar(100) DEFAULT NULL,
  `mname` varchar(100) NOT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `contact` varchar(10) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`fname`, `mname`, `lname`, `contact`, `email`, `gender`, `uname`, `pwd`, `location`) VALUES
('madhav', 'shekhar', 'soni', '9077456210', 'madhav@gmail.com', 'Male ', 'madhav', 'madhav12345', 'nashik'),
('priyanka', 'shekhar', 'chavhan', '7856432190', 'priyanka@ymail.com', 'Female', 'priyanka', 'priyanka@123', 'mumbai'),
('samiksha', 'rajesh', 'more', '8976554610', 'samiksha@gmail.com', 'Male', 'samiksha', 'Samiksha@123', 'Aurangabad');
