import requests
#import urllib3

# Esto silencia la advertencia de "Insecure Request" al usar verify=False
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def procesar_repuesta(endpoint, nombre_buscado):
    try:
        # Hacemos la petición
        request = requests.get(endpoint)
        
        print(f"--- Intentando conectar con: {endpoint} ---")
        
        # 1. Comprobamos si la URL existe (Status 200)
        request.raise_for_status()
        print(f"✅ Conexión exitosa (Código {request.status_code})")

        # 2. Intentamos convertir a JSON
        response = request.json()
        
        # 3. Intentamos acceder al dato (en esta API los resultados están en 'results')
        # Buscaremos el nombre del Pokémon en la lista
        pokemon_list = response['results']
        
        # Buscamos si el nombre existe en la lista que nos dio la API
        encontrado = any(p['name'] == nombre_buscado for p in pokemon_list)
        
        if encontrado:
            print(f"⭐ ¡Éxito! El Pokémon '{nombre_buscado}' está en la lista.")
        else:
            # Forzamos un error de lógica para el ejercicio
            raise ValueError(f"El Pokémon '{nombre_buscado}' no existe en esta página.")

    except requests.exceptions.HTTPError as err:
        print(f"❌ Error de URL: No se encontró el recurso (404). Detalle: {err}")
    except ValueError as e:
        print(f"⚠️ Error de Lógica: {e}")
    except Exception as e:
        print(f"🔥 Error inesperado: {type(e).__name__} - {e}")

# --- PRUEBAS ---

# URL CORRECTA (Lista de los primeros 20 Pokémon)
url_ok = "https://pokeapi.co/api/v2/pokemon/"

# URL QUE NO EXISTE (Error 404)
url_error = "https://pokeapi.co/api/v2/esta-ruta-esta-mal/"

print("\n--- CASO 1: URL CORRECTA ---")
procesar_repuesta(url_ok, "bulbasaur")

print("\n--- CASO 2: NOMBRE INCORRECTO (Error de lógica) ---")
procesar_repuesta(url_ok, "agumon") # Agumon no es un Pokémon ;)

print("\n--- CASO 3: URL INCORRECTA (Error 404) ---")
procesar_repuesta(url_error, "bulbasaur")