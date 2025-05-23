% --- Pruebas para motor.pl ---

:- [motor].

:- begin_tests(motor).

test(motos_menor_precio) :-
    Lista = [
        moto('Moto1','Marca1',150,7000000,'Urbana',alta,media,alta,media,alta,media),
        moto('Moto2','Marca2',200,9000000,'Sport',media,alta,media,alta,media,alta)
    ],
    motos_menor_precio(Lista, 8000000, Filtradas),
    Filtradas = [moto('Moto1','Marca1',150,7000000,'Urbana',alta,media,alta,media,alta,media)].

:- end_tests(motor).