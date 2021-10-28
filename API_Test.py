import http.client

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "f3e173f201msh0ad4390d91633b9p1bdf24jsn712cc54380d9"
    }

conn.request("GET", "/actors/get-all-filmography?nconst=nm0001667", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))