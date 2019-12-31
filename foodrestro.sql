-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 23, 2019 at 08:05 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodrestro`
--

-- --------------------------------------------------------

--
-- Table structure for table `fooditem`
--

CREATE TABLE `fooditem` (
  `uid` int(8) NOT NULL,
  `foodname` varchar(45) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fooditem`
--

INSERT INTO `fooditem` (`uid`, `foodname`, `price`, `quantity`) VALUES
(1, '[1, 65]', 65, 1),
(4, '[1, 65]', 65, 1),
(4, '[0, 0]', 0, 0),
(4, '[0, 0]', 0, 0),
(4, '[0, 0]', 0, 0),
(4, '[0, 0]', 0, 0),
(4, '[0, 0]', 0, 0),
(4, '[0, 0]', 0, 0),
(4, '[0, 0]', 0, 0),
(4, '[0, 0]', 0, 0),
(4, '[0, 0]', 0, 0),
(5, '[1, 65]', 65, 1),
(5, '[1, 300]', 300, 1),
(5, '[1, 50]', 50, 1),
(6, '[1, 65]', 65, 1),
(10, '[1, 65]', 65, 1),
(13, '[1, 65]', 65, 1),
(13, 'burger', 65, 1),
(13, 'colddrink', 50, 1),
(14, 'burger', 65, 1),
(14, 'colddrink', 50, 1),
(15, 'burger', 65, 1),
(15, 'burger', 65, 1),
(15, 'cake', 300, 1),
(16, 'burger', 65, 1),
(16, 'cake', 300, 1),
(17, 'burger', 65, 1),
(17, 'cake', 300, 1),
(17, 'icecream', 100, 1),
(17, 'colddrink', 50, 1),
(18, 'cake', 300, 1),
(19, 'cake', 300, 1),
(20, 'burger', 65, 1),
(20, 'cake', 300, 1),
(20, 'pizza', 300, 1),
(20, 'cookie', 80, 1),
(20, 'icecream', 100, 1),
(20, 'colddrink', 50, 1),
(20, 'coffee', 60, 1),
(21, 'cake', 300, 1),
(22, 'cake', 300, 1),
(23, 'burger', 65, 1),
(23, 'cake', 300, 1),
(23, 'pizza', 300, 1),
(23, 'icecream', 100, 1),
(23, 'colddrink', 50, 1),
(24, 'burger', 65, 1),
(24, 'cake', 300, 1),
(24, 'pizza', 300, 1),
(24, 'icecream', 100, 1),
(24, 'colddrink', 50, 1),
(24, 'chai', 30, 1),
(25, 'cake', 300, 1),
(26, 'burger', 130, 2),
(26, 'cake', 600, 2),
(26, 'pizza', 600, 2),
(26, 'thali', 150, 1),
(26, 'cookie', 80, 1),
(26, 'icecream', 100, 1),
(26, 'colddrink', 50, 1),
(26, 'coffee', 60, 1),
(26, 'chai', 30, 1),
(26, 'water', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `foodrest`
--

CREATE TABLE `foodrest` (
  `id` int(11) NOT NULL,
  `uname` varchar(45) NOT NULL,
  `mobileno` int(11) NOT NULL,
  `totalamt` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `foodrest`
--

INSERT INTO `foodrest` (`id`, `uname`, `mobileno`, `totalamt`) VALUES
(1, 'ganesh', 2147483647, 65),
(2, 'vishram', 2147483647, 115),
(3, 'ganesh', 2147483647, 65),
(4, 'kill', 2147483647, 65),
(5, 'afif', 2147483647, 415),
(6, 'value', 2147483647, 65),
(7, 'key', 2147483647, 65),
(8, 'life', 1526354559, 65),
(9, 'jerry', 2147483647, 115),
(10, 'billy', 1595624832, 65),
(11, 'jimmy', 2147483647, 65),
(12, 'jake', 2147483647, 65),
(13, 'avtar', 2147483647, 65),
(14, 'dhruv', 2147483647, 115),
(15, 'vicky', 2147483647, 65),
(16, 'happy', 1265895412, 365),
(17, 'happy', 1245326521, 515),
(18, 'happy', 1236547899, 300),
(19, 'happy', 1245789865, 300),
(20, 'happy', 1245789865, 955),
(21, 'sad', 2123565421, 300),
(22, 'happy', 2147483647, 300),
(23, 'vikas', 1254956845, 815),
(24, 'sachin', 2147483647, 845),
(25, 'very', 1265348970, 300),
(26, 'jol', 2147483647, 1810);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fooditem`
--
ALTER TABLE `fooditem`
  ADD KEY `index` (`uid`);

--
-- Indexes for table `foodrest`
--
ALTER TABLE `foodrest`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fooditem`
--
ALTER TABLE `fooditem`
  MODIFY `uid` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `foodrest`
--
ALTER TABLE `foodrest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fooditem`
--
ALTER TABLE `fooditem`
  ADD CONSTRAINT `fooditem_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `foodrest` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
