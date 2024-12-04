import json
# josn_sreing ='{"name": "alise","age":"25"}'
# data = json.loads(josn_sreing)
# print(data["name"]) 
# print(data["age"]) 
 
python_data = {
    "name": "leha",
    "gruz": 200,
    "skills": []
}
json_string = json.dumps(python_data, indent =4)
print (json_string)