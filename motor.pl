:- dynamic resultado/6.

% Cargar hechos desde Python
agregar_resultado(Nombre,Segmento,Cilindraje,Marca,Precio,PaisMarca,Altura,Economía,Fiabilidad,Estética,Durabilidad,Popularidad,Exclusividad) :-
    assertz(resultado(Nombre,Segmento,Cilindraje,Marca,Precio,PaisMarca,Altura,Economía,Fiabilidad,Estética,Durabilidad,Popularidad,Exclusividad)).

% Obtener moto por nombre
moto(Nombre, Segmento, Cilindraje, Marca, Precio, PaisMarca, Altura, Economia, Fiabilidad, Estetica, Durabilidad, Popularidad, Exclusividad) :-
    resultado(Nombre, Segmento, Cilindraje, Marca, Precio, PaisMarca, Altura, Economia, Fiabilidad, Estetica, Durabilidad, Popularidad, Exclusividad).

% Obtener las marcas unicas
marcas(M) :- resultado(_, _, _, M, _, _, _, _, _, _, _, _, _, _).

% Obtener los Segmentos unicos
segmentos(S) :- resultado(_, S, _, _, _, _, _, _, _, _, _, _, _, _).

% Obtener los paises de origen unicos
paises(P) :- resultado(_, _, _, _, _, P, _, _, _, _, _, _, _, _).

% Obtener motos de paises
motos_pais(P, N) :- resultado(N, _, _, _, _, P, _, _, _, _, _, _, _, _).

% Obtener motos con cilindraje mayor a X
motos_mayor_cilindraje(X, N) :- resultado(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _, _), Cilindraje > X.

% Obtener motos con cilindraje menor a X
motos_menor_cilindraje(X, N) :- resultado(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _, _), Cilindraje < X.

% Obtener motos con cilindraje entre X e Y
motos_entre_cilindraje(X, Y, N) :-
    resultado(N, _, Cilindraje, _, _, _, _, _, _, _, _, _, _, _), 
    Cilindraje >= X,
    Cilindraje =< Y.

% Obtener motos con precio mayor a X
motos_mayor_precio(X, N) :- resultado(N, _, _, _, Precio, _, _, _, _, _, _, _, _, _), Precio > X.

% Obtener motos con precio menor a X
motos_menor_precio(X, N) :- resultado(N, _, _, _, Precio, _, _, _, _, _, _, _, _, _), Precio < X.

% Obtener motos con precio entre X e Y
motos_entre_precio(X, Y, N) :-
    resultado(N, _, _, _, Precio, _, _, _, _, _, _, _, _, _), 
    Precio >= X,
    Precio =< Y.

% Obtener motos con altura mayor a X
motos_mayor_altura(X, N) :- resultado(N, _, _, _, _, _, Altura, _, _, _, _, _, _, _), Altura > X.

% Obtener motos con altura menor a X
motos_menor_altura(X, N) :- resultado(N, _, _, _, _, _, Altura, _, _, _, _, _, _, _), Altura < X.

% Obtener motos con altura entre X e Y
motos_entre_altura(X, Y, N) :-
    resultado(N, _, _, _, _, _, Altura, _, _, _, _, _, _, _), 
    Altura >= X,
    Altura =< Y.

% Obtener motos con mejor
motos_menor_precio(X, N) :- resultado(N, _, _, _, _, _, Altura, _, _, _, _, _, _, _), Altura < X.