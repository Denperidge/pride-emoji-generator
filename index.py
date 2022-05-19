from requests import request
from json import loads

def get(action, **additional_params):
    preset_parameters = {
        "format": "json",
        "action": action
        }
    full_parameters = preset_parameters | additional_params
    
    return loads(request("GET", "https://lgbtqia.fandom.com/api.php", params=full_parameters).text)


flag_query = get("query", list="allimages", titles=["Flags"])
flags = flag_query["query"]["allimages"]
print(len(flags))
for flag in flags:
    print(flag)