% Declaramos resultado/13 como dynamic para permitir la inserción y borrado de hechos desde Python
:- dynamic moto/13.

% Cargar hechos desde Python
% La regla agregar_hecho ahora acepta 13 argumentos, en el mismo orden que el CSV y el hecho moto/13, para insertar hechos correctamente desde Python
agregar_hecho(Nombre,Segmento,Cilindraje,Marca,Precio,Pais,Altura,EconomiaRepuestos,Fiabilidad,Estetica,Durabilidad,Popularidad,Exclusividad) :-
    assertz(moto(Nombre,Segmento,Cilindraje,Marca,Precio,Pais,Altura,EconomiaRepuestos,Fiabilidad,Estetica,Durabilidad,Popularidad,Exclusividad)).

% Obtener moto por nombre
% moto(_, Segmento, Cilindraje, _, Precio, _, Altura, Economia, Fiabilidad, Estetica, Durabilidad, Popularidad, Exclusividad) :-
%     moto(Nombre, Segmento, Cilindraje, Marca, Precio, PaisMarca, Altura, Economia, Fiabilidad, Estetica, Durabilidad, Popularidad, Exclusividad).

% Obtener las marcas unicas
marcas(M) :- moto(_, _, _, M, _, _, _, _, _, _, _, _, _).

% Obtener los Segmentos unicos
segmentos(S) :- moto(_, S, _, _, _, _, _, _, _, _, _, _, _).

% Obtener los paises de origen unicos
paises(P) :- moto(_, _, _, _, _, P, _, _, _, _, _, _, _).

% Obtener motos de un país (corrigiendo la aridad y el orden de los argumentos)
motos_pais(N, P) :- moto(N, _, _, _, _, P, _, _, _, _, _, _, _).

% Obtener motos con cilindraje mayor a X
motos_mayor_cilindraje(X, N) :- moto(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _), Cilindraje > X.

% Obtener motos con cilindraje menor a X
motos_menor_cilindraje(X, N) :- moto(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _), Cilindraje < X.

% Obtener motos con cilindraje entre X e Y
motos_entre_cilindraje(X, Y, N) :-
    moto(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _), 
    Cilindraje >= X,
    Cilindraje =< Y.

% Obtener motos con precio mayor a X
motos_mayor_precio(X, N) :- moto(N, _, _, _, Precio, _, _, _, _, _, _, _, _), Precio > X.

% Obtener motos con precio menor a X
motos_menor_precio(X, N) :- moto(N, _, _, _, Precio, _, _, _, _, _, _, _, _), Precio < X.

% Obtener motos con precio entre X e Y
motos_entre_precio(X, Y, N) :-
    moto(N, _, _, _, Precio, _, _, _, _, _, _, _, _), 
    Precio >= X,
    Precio =< Y.

% Obtener motos con altura mayor a X
motos_mayor_altura(X, N) :- moto(N, _, _, _, _, _, Altura, _, _, _, _, _, _), Altura > X.

% Obtener motos con altura menor a X
motos_menor_altura(X, N) :- moto(N, _, _, _, _, _, Altura, _, _, _, _, _, _), Altura < X.

% Obtener motos con altura entre X e Y
motos_entre_altura(X, Y, N) :-
    moto(N, _, _, _, _, _, Altura, _, _, _, _, _, _), 
    Altura >= X,
    Altura =< Y.
