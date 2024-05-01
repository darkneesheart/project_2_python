foroshgah = {
    "code_kala":"100",
    "name_kala":"makaroni",
    "price": 40000,
    "weight": 1/5,
    "brand":"zarmakaron" }

print(foroshgah)
print(foroshgah.keys())
foroshgah["weight"]=2
print(foroshgah.get("name_kala"))
foroshgah["model"]= "pichi"
print(foroshgah)
del foroshgah["price"]
print(foroshgah)
f2={"code_foroshgah":200,
    "name_foroshgah":"setare"}
foroshgah_2= foroshgah.copy()
print(foroshgah.items())
foroshgah.clear()
print(foroshgah)