from csv import DictReader
import json

temporary_dict = {}

# reading the organizations.csv file and extracting data from it with each row
with open("csv_to_json/organizations.csv", "r") as rf:
    csv_reader = DictReader(rf)
    csv_reader = list(csv_reader)
    for row in csv_reader:
        # organizations.csv contains Organization Id as a uniqued value for each row
        # hence we will have each row information contain in Organization Id as a key
        key = row.get("Organization Id")

        # omitting in temporary dictionary which later will be converted to json file
        temporary_dict[key] = row


# this code will convert python dictionary to json format
# indent are simply indentation
json_object = json.dumps(temporary_dict, indent=4)

# this code will create organizations.json file and will dump json_object in it
with open("csv_to_json/organizations.json", "w") as outfile:
    outfile.write(json_object)
