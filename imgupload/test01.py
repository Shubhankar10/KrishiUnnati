import base64
import requests


def encode_file(file_name):
    with open(file_name, "rb") as file:
        return base64.b64encode(file.read()).decode("ascii")


def identify_plant(file_names):
    # see the docs for more optional attributes
    params = {
        "api_key": "pldet42MR0v9vxm0pPwZI7c6KmFoG3vR0UyvLr36AdACB2vzp2",
        "images": [encode_file(img) for img in file_names],
        "latitude": 49.1951239,
        "longitude": 16.6077111,
        "datetime": 1582830233,
        # modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers
        "modifiers": ["crops_fast", "similar_images", "health_all", "disease_similar_images"],
        "plant_language": "en",
        # plant details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details
        "plant_details": ["common_names",
                          "edible_parts",
                          "gbif_id"
                          "name_authority",
                          "propagation_methods",
                          "synonyms",
                          "taxonomy",
                          "url",
                          "wiki_description",
                          "wiki_image",
                          ],
        # disease details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Disease-details
        "disease_details": ["common_names", "url", "description"]
        }

    headers = {
        "Content-Type": "application/json"
        }

    response = requests.post("https://api.plant.id/v2/identify",
                             json=params,
                             headers=headers)

    return response.json()



def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

'''
if __name__ == '__main__':
    x=identify_plant(["../img/photo1.jpg"])
    ---
    for y in x.items():
        if (y[0]=='suggestions'):
            
            for data in y:
                if(type(data)==list):
                    for data2 in data:
                        print(data)
            
    #print(x)
    ---
    for key,value in recursive_items(x):
        #print(key)
        
        if(key=='suggestions'):
            for x1 in value:
                for y,z in recursive_items (x1):
                    if(y=='common_names'):
                        print(z)
                    if(y=='value'):
                        print(z)
        if(key=='diseases'):
            for x1 in value:
                for y,z in recursive_items (x1):
                    
                    if(y=='common_names'):
                        print(z)
                    if(y=='description'):
                        print(z)
                    if(y=='local_name'):
                        print(z)
'''