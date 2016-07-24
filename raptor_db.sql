-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-07-2016 a las 01:02:49
-- Versión del servidor: 5.5.49-0ubuntu0.14.04.1
-- Versión de PHP: 5.5.9-1ubuntu4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `raptor`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`speakerblack`@`%` PROCEDURE `getDownloaUser`(IN `_user` INT)
    NO SQL
SELECT id_track, fecha FROM descargas_x_usuario WHERE id_usuario = _user$$

CREATE DEFINER=`speakerblack`@`%` PROCEDURE `getLastDownload`(IN `_iduser` INT)
    NO SQL
SELECT id_track FROM descargas_x_usuario 
WHERE id_usuario = _iduser
ORDER BY id_track DESC LIMIT 1$$

CREATE DEFINER=`speakerblack`@`%` PROCEDURE `insertDownload`(IN `_user` INT, IN `_track` INT)
    NO SQL
INSERT INTO descargas_x_usuario (id_track,id_usuario,fecha) VALUES (_track,_user,CURDATE())$$

CREATE DEFINER=`speakerblack`@`%` PROCEDURE `insertFaq`(IN `_id_user` INT, IN `_comentario` VARCHAR(599))
    NO SQL
INSERT INTO faq (id_user,comentario,fecha) VALUES (_id_user,_comentario,CURDATE())$$

CREATE DEFINER=`speakerblack`@`%` PROCEDURE `insertUser`(IN `_android_user` VARCHAR(100))
    NO SQL
IF NOT EXISTS ( SELECT COUNT(*) FROM usuario WHERE android_id = _android_user ) THEN
	INSERT INTO usuario (android_id) VALUES (_android_user);
	SELECT "1" AS state,"Usuario registrado" AS message;
ELSE
	SELECT "0" AS state,"Ya existe un usuario con este id" AS message;
END IF$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `descargas_x_usuario`
--

CREATE TABLE IF NOT EXISTS `descargas_x_usuario` (
  `id_usuario` int(11) NOT NULL,
  `id_track` int(11) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `descargas_x_usuario`
--

INSERT INTO `descargas_x_usuario` (`id_usuario`, `id_track`, `fecha`) VALUES
(-1, 17148848, '2016-05-18'),
(-1, 17148850, '2016-05-18'),
(-1, 116380652, '2016-06-15'),
(-1, 67238735, '2016-07-06'),
(-1, 69804441, '2016-07-06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `faq`
--

CREATE TABLE IF NOT EXISTS `faq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_user` int(11) NOT NULL,
  `comentario` varchar(600) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` date NOT NULL,
  `estado` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `faq`
--

INSERT INTO `faq` (`id`, `id_user`, `comentario`, `fecha`, `estado`) VALUES
(1, -1, 'FAQ de prueba', '2016-05-17', 0),
(2, -1, 'Desde el servicio', '2016-05-17', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `android_id` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `android_id`) VALUES
(1, 'prueba@prueba.com');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
