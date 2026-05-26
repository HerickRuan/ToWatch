import requests

class TMDBService:
    def __init__(self):
        self.api_key = "c414b769049f42ead97a7a7bab28cde0" 
        self.base_url = "https://api.themoviedb.org/3"

    def buscar(self, query):
        
        url = f"{self.base_url}/search/multi"
        params = {"api_key": self.api_key, "query": query, "language": "pt-BR"}
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                resultados = response.json().get("results", [])
                midias = []
                for item in resultados:
                    tipo = "Filme" if item.get("media_type") == "movie" else "Série/Anime"
                    titulo = item.get("title") if item.get("media_type") == "movie" else item.get("name")
                    data = item.get("release_date") if item.get("media_type") == "movie" else item.get("first_air_date")
                    ano = data.split("-")[0] if data else "N/A"
                    
                    if titulo and item.get("media_type") in ["movie", "tv"]:
                        midias.append({"id": item.get("id"), "titulo": titulo, "tipo": tipo, "ano": ano})
                return midias
        except Exception:
            pass
        return []