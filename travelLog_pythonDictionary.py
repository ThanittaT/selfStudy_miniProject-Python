"""
#---Nesting Dictionary in dictionary

travel_log = {"France":{"ctities_visited":["Paris","Lille","Dijon"], "total visit":12},"Germany":{"ctities_visited":["Berlin", "Hamburg", "Stuttgart"], "totalvisit":5}}
"""

#Nesting Dictionary in a List
travel_log = [
  {"country":"France",
    "total_visit": 12,
    "cities_visited":["Paris","Lille","Dijon"]
  },
  {
    "country": "Germany",
    "total_visit": 5,
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"]
  }
]

#------challenge Dictionary---

def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["total_visit"] = times_visited
  new_country["cities_visited"] = cities_visited
  travel_log.append(new_country)


#---Calling function
print("---This is challenge result: --- \n")
add_new_country("Russia", 2, ["Moscow", "Saint Peterburg"])
print(travel_log)


"""
--------Expected Result: --------
:
---This is challenge result: --- 

[{'country': 'France', 'total_visit': 12, 'cities_visited': ['Paris', 'Lille', 'Dijon']},
 {'country': 'Germany', 'total_visit': 5, 'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart']}, 
 {'country': 'Russia', 'total_visit': 2, 'cities_visited': ['Moscow', 'Saint Peterburg']}]

--------------------------------------------
"""


