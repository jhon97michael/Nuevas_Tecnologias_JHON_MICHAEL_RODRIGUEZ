---Creacion de base de datos----------------
CREATE DATABASE Divina_Providencia

USE Divina_Providencia

------Creación de tablas--------------------

CREATE TABLE defensoras(
	codigo_defensora VARCHAR(8) PRIMARY KEY NOT NULL,
	nombre_defensora VARCHAR(80) NOT NULL,
	centrozonal_defensora VARCHAR(100) NOT NULL,
	telefono_defensora BIGINT NOT NULL,
	email_defensora VARCHAR(100) NOT NULL)

CREATE TABLE profesional(
	ID_profesional INT PRIMARY KEY NOT NULL,
	nombre_profesional VARCHAR(80) NOT NULL,
	apellido_profesional VARCHAR(80) NOT NULL,
	profesion_profesional VARCHAR(60) NOT NULL,
	telefono_profesional BIGINT NOT NULL,
	email_profesional VARCHAR(100) NOT NULL)

CREATE TABLE NNAJ(
	ID_NNAJ INT PRIMARY KEY NOT NULL,
	nombre_NNAJ VARCHAR(80) NOT NULL,
	apellido_NNAJ VARCHAR(80) NOT NULL,
	fechaNacimiento_NNAJ DATE NOT NULL,
	edad_NNAJ SMALLINT NOT NULL,
	lugarNacimiento_NNAJ VARCHAR(200) NOT NULL,
	lugarResidencia_NNAJ VARCHAR(200) NOT NULL,
	motivoIngreso_NNAJ VARCHAR(200) NOT NULL,
	codigo_defensora VARCHAR(8),
	CONSTRAINT UNO FOREIGN KEY (codigo_defensora) REFERENCES defensoras(codigo_defensora))

CREATE TABLE expedientes(
	ID_expediente INT PRIMARY KEY IDENTITY,
	estudioCaso_expediente VARBINARY,
	evaluacionIntegradora VARBINARY,
	planCaso_expediente VARBINARY,
	seguimientoPC_expedeinte VARBINARY,
	codigo_defensora VARCHAR(8),
	CONSTRAINT DOS FOREIGN KEY (codigo_defensora) REFERENCES defensoras(codigo_defensora))

CREATE TABLE NNAJ_profesional(
	ID_NNAJ INT,
	ID_profesional INT,
	CONSTRAINT TRES FOREIGN KEY (ID_NNAJ) REFERENCES NNAJ(ID_NNAJ),
	CONSTRAINT CUATRO FOREIGN KEY (ID_profesional) REFERENCES profesional(ID_profesional))

CREATE TABLE profesional_expediente(
	ID_profesional INT,
	ID_expediente INT,
	CONSTRAINT CINCO FOREIGN KEY (ID_profesional) REFERENCES profesional(ID_profesional),
	CONSTRAINT SEIS FOREIGN KEY (ID_expediente) REFERENCES expedientes(ID_expediente))

-------Consultas en SQL-------------
