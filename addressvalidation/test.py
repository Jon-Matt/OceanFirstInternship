import geocoder

g = geocoder.locationiq("301 Falls Blvd, Quincy MA 2169", key='6774a6e0ff9f5f')
print(g.location)
z=0
string =""
address = g.address
location = g.location
print (address)
print(location)

location =location.replace(" Blvd", " Boulevard")
while location[z]!=",":
    string = string + location[z]
    print(location[z])
    z = z +1

if address.find(" Blvd") != -1:
    address.replace(" Blvd", " Boulevard")
address = address.replace(',', '')
print(address)
print(address.find(string))

