create schema "examen"

-- Creación Tabla Tipos Reactor
create table examen.tipos_reactor (
	id SERIAL primary key,
	tipo VARCHAR(50) unique not null
);
comment on table examen.tipos_reactor is 'Tipos de reactor';
comment on column examen.tipos_reactor.id is 'Autoincremental de la tabla';
comment on column examen.tipos_reactor.tipo is 'Tipo de reactor';


-- Creación Tabla Países
create table examen.paises (
	id SERIAL primary key,
	pais VARCHAR(50) unique not null
);
comment on table examen.paises is 'Países de los reactores';
comment on column examen.paises.id is 'Autoincremental de la tabla';
comment on column examen.paises.pais is 'País del reactor';

-- Creación Tabla ubicacion
create table examen.ubicacion (
 	id SERIAL primary key,
 	ciudad VARCHAR(50),
 	"id_pais" INT references examen.paises (id) on update cascade on delete cascade
);
comment on table examen.ubicacion is 'Ubicación de los reactores';
comment on column examen.ubicacion.id is 'Autoincremental de la tabla';
comment on column examen.ubicacion.ciudad is 'Ciudad más cercana al reactor';
comment on column examen.ubicacion."id_pais" is 'Llave foránea que relaciona la ciudad más cercana del reactor con su país';

-- Creación Tabla estados
create table examen.estados (
	id SERIAL primary key,
	estado VARCHAR(50) unique not null
);
comment on table examen.estados is 'Estados de los reactores';
comment on column examen.estados.id is 'Autoincremental de la tabla';
comment on column examen.estados.estado is 'Estado de reactor';

-- Creación Tabla Reactores
create table examen.reactores (
	id SERIAL primary key,
	nombre VARCHAR(100) not null,
	"potencia_termica" numeric not null,
	"primera_fecha_reaccion" TIMESTAMP,
	"id_tipo_reactor" INT references examen.tipos_reactor (id) on update cascade on delete cascade,
	"id_ubicacion" INT references examen.ubicacion (id) on update cascade on delete cascade,
	"id_estado" INT references examen.estados (id) on update cascade on delete cascade	
);
comment on table examen.reactores is 'Reactores';
comment on column examen.reactores.id is 'Autoincremental de la tabla';
comment on column examen.reactores.nombre is 'Nombre del reactor';
comment on column examen.reactores."potencia_termica" is 'Potencia del reactor en KW';
comment on column examen.reactores."primera_fecha_reaccion" is 'Primera fecha de reacción del reactor';
comment on column examen.reactores."id_tipo_reactor" is 'Llave foránea que relaciona reactor con su tipo de reactor';
comment on column examen.reactores."id_ubicacion" is 'Llave foránea que relaciona reactor con su ubicación';
comment on column examen.reactores."id_estado" is 'Llave foránea que relaciona reactor con su estado';
