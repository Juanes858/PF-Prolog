% --- Pruebas para motor.pl ---

:- [motor].

:- begin_tests(motor).

% Prueba para marcas unicas
 test(marcas_unicas) :-
    assertz(resultado('Aerox 155','Scooter',155,'Yamaha',14050000,'Japón',790,5,4,3,4,4,3)),
    assertz(resultado('NMAX','Scooter',155,'Yamaha',13550000,'Japón',765,4,4,3,4,5,2)),
    assertz(resultado('CB125F','Urbana',124,'Honda',7990000,'Japón',790,3,4,3,4,3,2)),
    setof(M, resultado(_,_,_,M,_,_,_,_,_,_,_,_,_), Marcas),
    Marcas = ['Honda','Yamaha'],
    retractall(resultado(_,_,_,_,_,_,_,_,_,_,_,_,_)).

% Prueba para segmentos unicos
 test(segmentos_unicos) :-
    assertz(resultado('Aerox 155','Scooter',155,'Yamaha',14050000,'Japón',790,5,4,3,4,4,3)),
    assertz(resultado('CB125F','Urbana',124,'Honda',7990000,'Japón',790,3,4,3,4,3,2)),
    setof(S, resultado(_,S,_,_,_,_,_,_,_,_,_,_,_), Segmentos),
    Segmentos = ['Scooter','Urbana'],
    retractall(resultado(_,_,_,_,_,_,_,_,_,_,_,_,_)).

% Prueba para paises unicos
 test(paises_unicos) :-
    assertz(resultado('Aerox 155','Scooter',155,'Yamaha',14050000,'Japón',790,5,4,3,4,4,3)),
    assertz(resultado('CB125F','Urbana',124,'Honda',7990000,'Japón',790,3,4,3,4,3,2)),
    assertz(resultado('Dio','Scooter',109,'Honda',6790000,'India',765,3,4,3,4,3,2)),
    setof(P, resultado(_,_,_,_,_,P,_,_,_,_,_,_,_), Paises),
    Paises = ['India','Japón'],
    retractall(resultado(_,_,_,_,_,_,_,_,_,_,_,_,_)).

% Prueba para motos de un pais
 test(motos_pais) :-
    assertz(resultado('Aerox 155','Scooter',155,'Yamaha',14050000,'Japón',790,5,4,3,4,4,3)),
    assertz(resultado('Dio','Scooter',109,'Honda',6790000,'India',765,3,4,3,4,3,2)),
    findall(N, resultado(N,_,_,_,_,"Japón",_,_,_,_,_,_,_), Lista),
    Lista = ['Aerox 155'],
    retractall(resultado(_,_,_,_,_,_,_,_,_,_,_,_,_)).

% Prueba para motos con cilindraje mayor a X
 test(motos_mayor_cilindraje) :-
    assertz(resultado('Aerox 155','Scooter',155,'Yamaha',14050000,'Japón',790,5,4,3,4,4,3)),
    assertz(resultado('CB125F','Urbana',124,'Honda',7990000,'Japón',790,3,4,3,4,3,2)),
    findall(N, (resultado(N,_,Cilindraje,_,_,_,_,_,_,_,_,_,_), Cilindraje > 130), Lista),
    Lista = ['Aerox 155'],
    retractall(resultado(_,_,_,_,_,_,_,_,_,_,_,_,_)).

% Prueba para motos con precio menor a X
 test(motos_menor_precio) :-
    assertz(resultado('Aerox 155','Scooter',155,'Yamaha',7000000,'Japón',790,5,4,3,4,4,3)),
    assertz(resultado('CB125F','Urbana',124,'Honda',9000000,'Japón',790,3,4,3,4,3,2)),
    findall(N, (resultado(N,_,_,_,Precio,_,_,_,_,_,_,_,_), Precio < 8000000), Lista),
    Lista = ['Aerox 155'],
    retractall(resultado(_,_,_,_,_,_,_,_,_,_,_,_,_)).

:- end_tests(motor).