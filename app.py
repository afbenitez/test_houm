import requests
import numpy as np


PATH = "https://pokeapi.co/api/v2/"


def pokemons_with_at_and_a() -> int:
    """The number of pokemon that have "at" in their names and have 2 "a" in their name.

    Param
    -----
    It has no parameters, as it does not require input data.

    Raises
    ------
    Exception
    Throws exception if you have an error in the information query or in the request.

    Return
    ------
    int
        Returns an integer which is the number of pokemons that have "at" in their names and have
        2 "a" in their name.
    """

    res = 0
    try:
        # Solicitud al API para conocer el total de pokemones
        response = requests.get(f"{PATH}pokemon").json()
        total_pokemons = response["count"]

        # Solicitud al API con limite del total de pokemones para obtener la informacion de los pokemones
        param = {"limit": total_pokemons}
        all_pokemons = requests.get(f"{PATH}pokemon", params=param).json()
        results = all_pokemons["results"]

        # Recorrido sobre los pokemones, solicitando el nombre y verificando que contenga "at" y 2 "a"
        # Si cumplen la condicion aumenta en 1 el contador counter
        for element in results:
            name = element["name"]
            if name.count("a") == 2 and "at" in name:
                res += 1

    except Exception as e:
        # Imprime la excepcion en caso de presentarse
        print(e)

    finally:
        # Retorna la variable contadora
        return res

def species_can_breed(pokemon_name) -> int:
    """The number of different species with which the pokemon raichu can breed.

    Param
    -----
    pokemon_name: str , default
        The name of the pokemon of which you want to know the different species with which you can breed,
        as default='raichu'

    Raises
    ------
    Exception
    Throws exception if you have an error in the information query or in the request.

    Return
    ------
    int
        Returns an integer which is the number of different species with which the pokemon
        raichu can breed.
    """
    res = 0
    try:
        # Solicitud al API para conocer los egg-groupps que exiten
        response = requests.get(f"{PATH}egg-group/").json()
        results = response["results"]

        # Creacion del diccionario que almacenara la lista de los nombres de pokemones que pertenezcan a un
        # egg-group donde este el pokemon-name
        list_res = []

        # Recorrido sobre los egg-groups existentes
        for element in results:
            group_name = element["name"]

            # Soliticitud al API para obtener la informacion de cada egg-group
            response = requests.get(f"{PATH}egg-group/{group_name}").json()
            pokemons = response["pokemon_species"]

            # Agregar a names los nombres de los pokemones de ese egg-group
            names = []
            for pokemon in pokemons:
                names.append(pokemon["name"])

            # Si el nombre del pokemon_name esta en names, es decir pertenece a ese egg-group
            # La lista sera names y esta se añadira a el dict_res que guarda todos con los que es compatible
            if pokemon_name in names:
                list_res.append(names)

        # Concatena las listas que estan en el diccionario y elimina los repetidos, luego resta 1
        # porque es con especies diferentes y no deberia sumar la misma especie, este valor es guardado en res
        res = len(set(np.concatenate(list_res))) - 1

    except Exception as e:
        # Imprime la excepcion en caso de presentarse
        print(e)

    finally:
        # Retorna la variable res, que almacena el numero de especies diferentes con las que se puede reproducir
        # el pokemon con el nombre pokemon_name
        return res

def max_and_min_weight_by_type(type) -> list:
    """A tuple with the maximum and minimum weight value of the first generation fighting type pokémon

    Param
    -----
    type: str , default
        the type of the pokemon of which we will know the maximum and minimum weight of that type,
        of first generation, and type is default='fighting'

    Raises
    ------
    Exception
    Throws exception if you have an error in the information query or in the request.

    Return
    ------
    list
        A tuple with the maximum and minimum weight value of the first generation fighting type pokemon,
        e.g [max, min]
    """

    res = []
    try:
        # Solicitud al API para obtener la informacion de los pokemones de tipo Type
        pokemons_type = requests.get(f"{PATH}type/{type}").json()
        pokemons = pokemons_type["pokemon"]

        # Se realiza el recorrido sobre los pokemones de ese tipo, se obtiene su nombre para ser guardado si
        # cumple las condiciones. Luego se accede a la url para conocer si es de primera generacion, luego
        # de hacer las comparaciones si cumple con la condicion de que id <= 151 se agrega a la lista de nombres
        # de pokemones de cumplen ambas condiciones
        list_weights_filter = []
        for pokemon in pokemons:
            pokemon_id = int(pokemon["pokemon"]["url"].split("/")[6])
            if pokemon_id <= 151:
                response = requests.get(f"{PATH}pokemon/{pokemon_id}").json()
                weight = response["weight"]
                list_weights_filter.append(weight)

        # Creación de las variables que almacenaran los pesos maximos y minimos
        min_weight = np.inf
        max_weight = -np.inf

        # Recorrido sobre los nombres filtrados, luego se hace una peticion al API de la informacion del
        # pokemon con ese nombre, se accede al peso y se compara con llas variables de maximo y minimo
        # al final del recorrido quedaran guardadas en las variables los valores correspondientes al maximo y minimo
        for actual_weight in list_weights_filter:
            min_weight = min(min_weight, actual_weight)
            max_weight = max(max_weight, actual_weight)

        # Se asigna al retorno res los valores de peso maximo y minimo
        res = [max_weight, min_weight]

    except Exception as e:
        # Imprime la excepcion en caso de presentarse
        print(e)

    finally:
        # Retorna la lista con 2 valores, que corresponden al peso maximo y minimo
        # de un tipo de pokemon de primera generacion
        return res
