import json

Chewbacca = '''{
	"name": "Chewbacca",
	"height": "228",
	"mass": "112",
	"hair_color": "brown",
	"skin_color": "unknown",
	"eye_color": "blue",
	"birth_year": "200BBY",
	"gender": "male",
	"homeworld": "https://swapi.dev/api/planets/14/",
	"films": [
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/2/",
		"https://swapi.dev/api/films/3/",
		"https://swapi.dev/api/films/6/"
	],
	"species": [
		"https://swapi.dev/api/species/3/"
	],
	"vehicles": [
		"https://swapi.dev/api/vehicles/19/"
	],
	"starships": [
		"https://swapi.dev/api/starships/10/",
		"https://swapi.dev/api/starships/22/"
	],
	"created": "2014-12-10T16:42:45.066000Z",
	"edited": "2014-12-20T21:17:50.332000Z",
	"url": "https://swapi.dev/api/people/13/"
}'''
Chewbacca = json.loads(Chewbacca)
# print(Chewbacca['name'])
# print(type(Chewbacca))

Chewbacca['name'] = "Katy Perry"
Chewbacca_str = json.dumps(Chewbacca)
print(Chewbacca_str)