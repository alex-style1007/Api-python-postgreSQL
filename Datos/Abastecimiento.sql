-- Llenado de tablas
insert into examen."paises"(pais)
(select distinct pais from sin_normalizar.reactores
);

insert into examen.tipos_reactor(tipo)
(select distinct tipo from sin_normalizar.reactores where tipo is not null
);

insert into examen.estados(estado)
(select distinct estado from sin_normalizar.reactores where estado is not null
);

insert into examen.ubicacion(ciudad, id_pais)
(select distinct n.ciudad, p.id from sin_normalizar.reactores n left join examen.paises p on p.pais = n.pais
);

create temp table ubicacion_temp(
	id SERIAL primary key,
	ciudad varchar(100),
	pais varchar(50)
);

insert into ubicacion_temp (ciudad, pais)
(select distinct n.ciudad, p.pais from sin_normalizar.reactores n left join examen.paises p on p.pais = n.pais
);

insert into examen.reactores(nombre, potencia_termica, primera_fecha_reaccion, id_tipo_reactor, id_ubicacion, id_estado)
(	select n.nombre, n.potencia_termica, n.primera_fecha_reaccion , r.id, u.id, e.id 
	from sin_normalizar.reactores n
	left join examen.tipos_reactor r on r.tipo = n.tipo
	left join ubicacion_temp u on u.ciudad = n.ciudad and u.pais = n.pais
	left join examen.estados e on e.estado = n.estado
);