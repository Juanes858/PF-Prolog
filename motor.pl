% ----------------------------------------------------------------------
% motor.pl: Motor de inferencia y reglas para el sistema experto de motos
% ----------------------------------------------------------------------
% Este archivo contiene las reglas y hechos en Prolog que permiten realizar consultas y
% recomendaciones sobre motos. Cada regla está documentada y acompañada de un ejemplo de uso.
% Esto facilita la comprensión y reutilización del conocimiento codificado.

% Declaramos moto/13 como dynamic para permitir la inserción y borrado de hechos desde Python
:- dynamic moto/13.

% ----------------------------------------------------------------------
% agregar_hecho/13
% Inserta un hecho moto/13 en la base de conocimiento.
% Uso típico desde Python para cargar datos desde CSV.
% Ejemplo de uso:
% ?- agregar_hecho('XR150L','Enduro',150,'Honda',12000000,'Japón',825,8,9,7,8,10,5).
% (Altura en milímetros, no en metros)
% ----------------------------------------------------------------------
agregar_hecho(Nombre,Segmento,Cilindraje,Marca,Precio,Pais,Altura,EconomiaRepuestos,Fiabilidad,Estetica,Durabilidad,Popularidad,Exclusividad) :-
    assertz(moto(Nombre,Segmento,Cilindraje,Marca,Precio,Pais,Altura,EconomiaRepuestos,Fiabilidad,Estetica,Durabilidad,Popularidad,Exclusividad)).


% ----------------------------------------------------------------------    
% moto_recomendada/8
% Recomendación de motos basada en los criterios del usuario.
% Los argumentos pueden ser variables anónimas (_) si el usuario no filtra por ese criterio.
% Ejemplo de uso:
% ?- moto_recomendada(_, 'Enduro', _, _, 8000000, 15000000, 870, M).
%   Devuelve motos del segmento 'Enduro', precio entre 8 y 15 millones, altura mínima 870mm.
% ?- moto_recomendada('Japón', _, _, _, _, _, _, M).
%   Devuelve todas las motos de Japón.
% Argumentos:
%   Pais, Segmento, Marca, CilindrajeMin, PrecioMin, PrecioMax, AlturaMin, Moto
% ----------------------------------------------------------------------
moto_recomendada(Pais, Segmento, Marca, CilindrajeMin, PrecioMin, PrecioMax, AlturaMin, Moto) :-
    moto(Moto, SegmentoM, CilindrajeM, MarcaM, PrecioM, PaisM, AlturaM, _, _, _, _, _, _),
    (var(Pais); Pais == PaisM),
    (var(Segmento); Segmento == SegmentoM),
    (var(Marca); Marca == MarcaM),
    (var(CilindrajeMin); CilindrajeM >= CilindrajeMin),
    (var(PrecioMin); PrecioM >= PrecioMin),
    (var(PrecioMax); PrecioM =< PrecioMax),
    (var(AlturaMin); AlturaM >= AlturaMin).

% ----------------------------------------------------------------------
% marcas/1
% Obtiene las marcas únicas de motos en la base de conocimiento.
% Ejemplo de uso:
% ?- marcas(M).
% ----------------------------------------------------------------------
marcas(M) :- moto(_, _, _, M, _, _, _, _, _, _, _, _, _).

% ----------------------------------------------------------------------
% segmentos/1
% Obtiene los segmentos únicos de motos en la base de conocimiento.
% Ejemplo de uso:
% ?- segmentos(S).
% ----------------------------------------------------------------------
segmentos(S) :- moto(_, S, _, _, _, _, _, _, _, _, _, _, _).

% ----------------------------------------------------------------------
% paises/1
% Obtiene los países de origen únicos de las motos.
% Ejemplo de uso:
% ?- paises(P).
% ----------------------------------------------------------------------
paises(P) :- moto(_, _, _, _, _, P, _, _, _, _, _, _, _).

% ----------------------------------------------------------------------
% motos_pais/2
% Obtiene los nombres de motos de un país específico.
% Ejemplo de uso:
% ?- motos_pais(Nombre, 'Argentina').
% ----------------------------------------------------------------------
motos_pais(N, P) :- moto(N, _, _, _, _, P, _, _, _, _, _, _, _).

% ----------------------------------------------------------------------
% motos_mayor_cilindraje/2
% Obtiene los nombres de motos con cilindraje mayor a X.
% Ejemplo de uso:
% ?- motos_mayor_cilindraje(250, Nombre).
% ----------------------------------------------------------------------
motos_mayor_cilindraje(X, N) :- moto(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _), Cilindraje > X.

% ----------------------------------------------------------------------
% motos_menor_cilindraje/2
% Obtiene los nombres de motos con cilindraje menor a X.
% Ejemplo de uso:
% ?- motos_menor_cilindraje(250, Nombre).
% ----------------------------------------------------------------------
motos_menor_cilindraje(X, N) :- moto(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _), Cilindraje < X.

% ----------------------------------------------------------------------
% motos_entre_cilindraje/3
% Obtiene los nombres de motos con cilindraje entre X e Y.
% Ejemplo de uso:
% ?- motos_entre_cilindraje(150, 250, Nombre).
% ----------------------------------------------------------------------
motos_entre_cilindraje(X, Y, N) :-
    moto(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _), 
    Cilindraje >= X,
    Cilindraje =< Y.

% ----------------------------------------------------------------------
% motos_mayor_precio/2
% Obtiene los nombres de motos con precio mayor a X.
% Ejemplo de uso:
% ?- motos_mayor_precio(100000, Nombre).
% ----------------------------------------------------------------------
motos_mayor_precio(X, N) :- moto(N, _, _, _, Precio, _, _, _, _, _, _, _, _), Precio > X.

% ----------------------------------------------------------------------
% motos_menor_precio/2
% Obtiene los nombres de motos con precio menor a X.
% Ejemplo de uso:
% ?- motos_menor_precio(100000, Nombre).
% ----------------------------------------------------------------------
motos_menor_precio(X, N) :- moto(N, _, _, _, Precio, _, _, _, _, _, _, _, _), Precio < X.

% ----------------------------------------------------------------------
% motos_entre_precio/3
% Obtiene los nombres de motos con precio entre X e Y.
% Ejemplo de uso:
% ?- motos_entre_precio(50000, 100000, Nombre).
% ----------------------------------------------------------------------
motos_entre_precio(X, Y, N) :-
    moto(N, _, _, _, Precio, _, _, _, _, _, _, _, _), 
    Precio >= X,
    Precio =< Y.

% ----------------------------------------------------------------------
% motos_mayor_altura/2
% Obtiene los nombres de motos con altura mayor a X.
% Ejemplo de uso:
% ?- motos_mayor_altura(850, Nombre).
% ----------------------------------------------------------------------
motos_mayor_altura(X, N) :- moto(N, _, _, _, _, _, Altura, _, _, _, _, _, _), Altura > X.

% ----------------------------------------------------------------------
% motos_menor_altura/2
% Obtiene los nombres de motos con altura menor a X.
% Ejemplo de uso:
% ?- motos_menor_altura(800, Nombre).
% ----------------------------------------------------------------------
motos_menor_altura(X, N) :- moto(N, _, _, _, _, _, Altura, _, _, _, _, _, _), Altura < X.

% ----------------------------------------------------------------------
% motos_entre_altura/3
% Obtiene los nombres de motos con altura entre X e Y.
% Ejemplo de uso:
% ?- motos_entre_altura(750, 850, Nombre).
% ----------------------------------------------------------------------
motos_entre_altura(X, Y, N) :-
    moto(N, _, _, _, _, _, Altura, _, _, _, _, _, _), 
    Altura >= X,
    Altura =< Y.
