create schema "sin_normalizar";

create table sin_normalizar.reactores (
	id SERIAL primary key,
	nombre VARCHAR(100) not null,
	"potencia_termica" numeric not null,
	"primera_fecha_reaccion" TIMESTAMP,
	tipo VARCHAR(50),
	estado VARCHAR(50),
	ciudad VARCHAR(50),
	pais VARCHAR(50) 
);