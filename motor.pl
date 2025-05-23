:- dynamic resultado/6.

%moto('Aerox 155', 'Scooter', 155, 'Yamaha', 5000000, 'Japón', 790, 5, 4, 3, 4, 4, 3).

% Cargar hechos desde Python
agregar_resultado(Anio, Fecha, Local, Visitante, GolesLocal, GolesVisitante) :-
    assertz(resultado(Anio, Fecha, Local, Visitante, GolesLocal, GolesVisitante)).

% Cargar hechos desde Python
agregar_hecho(Nombre,Segmento,Cilindraje,Marca,Precio,Pais,Altura,EconomiaRepuestos,Fiabilidad,Estetica,Durabilidad,Popularidad,Exclusividad) :-
    assertz(moto(Nombre,Segmento,Cilindraje,Marca,Precio,Pais,Altura,EconomiaRepuestos,Fiabilidad,Estetica,Durabilidad,Popularidad,Exclusividad)).

% Filtrar motos por rango de precio
% motos_en_rango_precio(+ListaMotos, +PrecioMin, +PrecioMax, -Filtradas)
motos_en_rango_precio([], _, _, []).
motos_en_rango_precio([moto(Nombre,Segmento,Cilindraje,Marca,Precio,Pais,Altura,EconomiaRepuestos,Fiabilidad,Estetica,Durabilidad,Popularidad,Exclusividad)|Resto], PrecioMin, PrecioMax, 
    [moto(Nombre,Segmento,Cilindraje,Marca,Precio,Pais,Altura,EconomiaRepuestos,Fiabilidad,Estetica,Durabilidad,Popularidad,Exclusividad)|Filtradas]) :-
    Precio >= PrecioMin,
    Precio =< PrecioMax,
    motos_en_rango_precio(Resto, PrecioMin, PrecioMax, Filtradas).
motos_en_rango_precio([_|Resto], PrecioMin, PrecioMax, Filtradas) :-
    motos_en_rango_precio(Resto, PrecioMin, PrecioMax, Filtradas).

% Ejemplo de uso:
% motos_en_rango_precio(Lista, 0, 8000000, Filtradas0a8).
% motos_en_rango_precio(Lista, 8000001, 12000000, Filtradas8a12).

% Obtener todos los equipos únicos
equipo(E) :-
    resultado(_, _, E, _, _, _);
    resultado(_, _, _, E, _, _).

% Sumar goles de un equipo (local + visitante)
goles_equipo(E, Total) :-
    findall(GL, resultado(_, _, E, _, GL, _), GolesLocal),
    findall(GV, resultado(_, _, _, E, _, GV), GolesVisitante),
    append(GolesLocal, GolesVisitante, Todos),
    sumlist(Todos, Total).

% Encontrar el equipo con más goles
equipo_con_mas_goles(EquipoMax) :-
    setof(E, equipo(E), Equipos),                 % Obtener equipos únicos
    encontrar_maximo(Equipos, '', 0, EquipoMax).  % Buscar el de más goles

% Dentro de tu archivo Prolog:

encontrar_maximo_goles([], EquipoActual, GolesActual, EquipoActual, GolesActual).
encontrar_maximo_goles([E|Resto], EquipoTemp, GolesTemp, EquipoMax, GolesMax) :-
    goles_equipo(E, GolesE),
    (GolesE > GolesTemp ->
        encontrar_maximo_goles(Resto, E, GolesE, EquipoMax, GolesMax)
    ;
        encontrar_maximo_goles(Resto, EquipoTemp, GolesTemp, EquipoMax, GolesMax)
    ).

mostrar_goles(EquipoMax, GolesMax) :-
    setof(E, equipo(E), Equipos),
    encontrar_maximo_goles(Equipos, '', 0, EquipoMax, GolesMax).

% Recorrer lista de equipos y hallar el que tenga más goles
encontrar_maximo([], EquipoActual, _, EquipoActual).
encontrar_maximo([E|Resto], EquipoTemp, GolesTemp, EquipoMax) :-
    goles_equipo(E, GolesE),
    (GolesE > GolesTemp ->
        encontrar_maximo(Resto, E, GolesE, EquipoMax)
    ;
        encontrar_maximo(Resto, EquipoTemp, GolesTemp, EquipoMax)
    ).
