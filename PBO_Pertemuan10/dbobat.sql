-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2024 at 05:07 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `obat`
--

-- --------------------------------------------------------

--
-- Table structure for table `dbobat`
--

CREATE TABLE `dbobat` (
  `id` int(11) NOT NULL,
  `kdobat` int(11) DEFAULT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `berat` varchar(10) DEFAULT NULL,
  `bentuk` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dbobat`
--

INSERT INTO `dbobat` (`id`, `kdobat`, `nama`, `berat`, `bentuk`) VALUES
(1, 1, 'paracetamol', '10mg', 'tablet'),
(4, 3, 'amoxcylyn', '9mg', 'tablet'),
(5, 4, 'dumolex', '2mg', 'tablet'),
(6, 5, 'xanax', '5mg', 'tablet');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dbobat`
--
ALTER TABLE `dbobat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kdobat` (`kdobat`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dbobat`
--
ALTER TABLE `dbobat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
