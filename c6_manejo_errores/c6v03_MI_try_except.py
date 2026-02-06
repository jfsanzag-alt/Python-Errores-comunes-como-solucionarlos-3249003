import requests

# Pruebas de distintas excepciones
# URL Correcta y resultado O
# No se pudo establecer conexión con internet exceptions.ConnectionError
# Error de timeout. exceptions.Timeout
# URL QUE NO EXISTE (Error 404/500) exceptions.HTTPError
# URL Correcta pero no se puede decodificar contenido JSON. JSONErrorCode
# URL Correcta pero Error de lógica. ValueError, IndexError


def procesar_repuesta(endpoint, nombre_buscado):
    try:
        # Hacemos la petición
        request = requests.get(endpoint, timeout=0.1)
        
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

    except requests.JSONDecodeError:
        print("No se pudo decodificar el contenido de la respuesta")
    except requests.exceptions.ConnectionError:
        print("🌐 Error de red: No se pudo establecer la conexión con el servidor.")
    except requests.exceptions.Timeout:
        print("⏳ El servidor tardó demasiado en responder.")
    except requests.exceptions.HTTPError as err:
        print(f"❌ Error de URL: No se encontró el recurso (404). Detalle: {err}")
    except ValueError as e:
        print(f"⚠️ Error de Lógica: {e}")
    except Exception as e:
        print(f"🔥 Error inesperado: {type(e).__name__} - {e}")
    else:
        print("Ejecución sin errores")
    finally:
        print("Fin del procesamiento del endpoint")

# --- PRUEBAS ---

# URL CORRECTA (Lista de los primeros 20 Pokémon)
url_ok = "https://pokeapi.co/api/v2/pokemon/"

# URL QUE NO EXISTE (Error 404)
url_error = "https://pokeapi.co/api/v2/esta-ruta-esta-mal/"

# Esta URL devuelve texto plano, NO un JSON
url_provocar_error = "https://pokeapi.co/robots.txt"

# Simular error de timeout, usando 0.01 y este enlace
url_provocar_timeout = "https://www.renfe.com/es/es/grupo-renfe/transporte-sostenible/tren-bici"

print("\n--- CASO 1: URL CORRECTA ---")
procesar_repuesta(url_ok, "bulbasaur")

print("\n--- CASO 2: NOMBRE INCORRECTO (Error de lógica) ---")
procesar_repuesta(url_ok, "agumon") # Agumon no es un Pokémon ;)

print("\n--- CASO 3: URL INCORRECTA (Error 404) ---")
procesar_repuesta(url_error, "bulbasaur")

print("\n--- CASO: Forzando JSONDecodeError ---")
procesar_repuesta(url_provocar_error, "bulbasaur")

print("\n--- CASO: Forzando timeout ---")
procesar_repuesta(url_provocar_timeout, "bulbasaur")
