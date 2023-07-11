import Funciones as fn
while True:

    fn.menu()
    elegir = fn.validar_opcion()
    if elegir == 1:
        fn.validar_rut()
        fn.mostrar_concierto()
        fn.cant_entradas()
        fn.columna()
        fn.fila()
        fn.compra()
    elif elegir ==2:
        fn.mostrar_concierto()

    elif elegir == 3:
        fn.ver_listadorut()

    elif elegir == 4:
        fn.comprastotales()

    else:
        fn.salir()
        break