import json
# josn_sreing ='{"name": "alise","age":"25"}'
# data = json.loads(josn_sreing)
# print(data["name"]) 
# print(data["age"]) 
 
# python_data = {
#     "name": "leha",
#     "gruz": 200,
#     "skills": []
# }
# json_string = json.dumps(python_data, indent =4)
# print (json_string)
# with open("./json/data.json","r") as file:
#     data =  json.load(file)

# print(data)
# print(data["name"])    
data = {
    "name": "nicola2",
    "age":52,
    "hobbies":["Mass shootin","grandson of miyagi","cooki cliker", "owner  of faith"]
}
with open("./json/output.json","r") as  file:
    json.dump(data, file, indent=4)