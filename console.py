import app as app


def show_question_01() -> None:
    """A call to the pokemons_with_at_and_a() method of the app document and a print the console with the answer.

    Note:
        It has no parameters, no raises, no returns, because all this is handled in the calling method of app.
    """
    result = app.pokemons_with_at_and_a()
    print(
        f"""{result} pokemones poseen en sus nombres "at" y tienen 2 "a" en su nombre."""
    )


def show_question_02() -> None:
    """A call to the species_can_breed() method of the app document and a print the console with the answer.

    Note:
        It has no parameters, no raises, no returns, because all this is handled in the calling method of app.
    """
    result = app.species_can_breed("raichu")
    print(f"El pokemón raichu puede procrear con {result} especies distintas")


def show_question_03() -> None:
    """A call to the max_and_min_weight_by_type() method of the app document and a print the console with the answer.

    Note:
        It has no parameters, no raises, no returns, because all this is handled in the calling method of app.
    """
    result = app.max_and_min_weight_by_type("fighting")
    print(
        f"El máximo y mínimo peso de los pokémon de tipo fighting de primera generación es {result}"
    )


def show_menu_aplication() -> bool:
    """Display a series of print to console, to communicate to the user the options menu.

    Return
    ------
        bool
            A boolean that indicates whether or not to continue executing this menu of options.

    Note:
        It has no parameters, no raises.
    """
    print("-" * 10, "Menu de opciones", "-" * 10)
    print(""" 1 - Cuantos pokemones poseen en sus nombres "at" y tienen 2 "a" """)
    print(" 2 - Cuantas especies de pokémon puede procrear Raichu")
    print(
        " 3 - Ver el máximo y mínimo peso de los pokémon de tipo fighting de primera generación"
    )
    print(" 4 - Salir de la aplicacion")
    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        show_question_01()
    elif opcion_elegida == "2":
        show_question_02()
    elif opcion_elegida == "3":
        show_question_03()
    elif opcion_elegida == "4":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción valida.")
    return continuar_ejecutando


if __name__ == "__main__":

    ejecutando = True
    while ejecutando:

        ejecutando = show_menu_aplication()

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")
