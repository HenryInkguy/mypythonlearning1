# Challenge 024
# Make a script that reads the name of a city and says if it starts or not with the name "Santo".

city = str(input("Tell me the name of that city you wanted to visit, it started with something like 'Santo', I guess.\n")).strip()
uppy = city.upper()
santo = uppy.find('SANTO')

if santo == 0:
    print("Haha, I knew it! Well, when will you finally go visit that place anyways?")
else:
    print("Really? I could swear its first name was Santo...")
    