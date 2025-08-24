import requests
import random
import pandas as pd
from time import sleep
from constants import *

file_path = 'FINAL TAB2.xlsx'
df = pd.read_excel(file_path)
df["Ass No"] = df["Ass No"].fillna(0).astype(int)


first_url = f"https://api.swarnapanchayat.apcfss.in/prtntmapi/getPartial-ownerDetails/{panch_secretariat_id}"

first_res = requests.get(first_url, headers=headers)
first_res.raise_for_status()
first_level_data = first_res.json()
loop_data = first_level_data["data"]
survey_numbers_list = ["206-2A,2B", "234-2B", "246-2,3", "235-1"]

for record in loop_data:
    if (400 <= int(record["old_assessment_number"]) <= 500):
        property_id = record["property_id"]
        old_assessment_number = record["old_assessment_number"]
        
        second_url = f"https://api.swarnapanchayat.apcfss.in/prtntmapi/get-firsttabdata/{property_id}"
        second_res = requests.get(second_url, headers=headers)
        second_res.raise_for_status()
        second_level_data = second_res.json()
        new_assessment_no = second_level_data["data"][0]["assessment_no"]
        door_no = second_level_data["data"][0]["door_no"]

        filtered_df = df[df['Ass No'] == int(old_assessment_number)]


        # Convert to dictionary
        filtered_data_dict = filtered_df.to_dict(orient='records')
        surname = filtered_data_dict[0]["Owner Name/Establishment Name"].split(" ")[0]
        name = " ".join(filtered_data_dict[0]["Owner Name/Establishment Name"].split(" ")[1:])
        relation_person_name = filtered_data_dict[0]["Father Name/PanNumber"]
        insert_owner_details_url = "https://api.swarnapanchayat.apcfss.in/prtntmapi/insert-ownerdetails"
        payload = {
                    "user_id": user_id,
                    "generated_assessment_no": new_assessment_no,
                    "owner_occupation": [
                        {
                            "surname": surname,
                            "name": name,
                            "gender": 1,
                            "relation_type": 1,
                            "relation_person_surname": surname,
                            "relation_person_name": relation_person_name,
                            "address": habitation,
                            "pincode": pincode,
                            "aadhaar_no": "",
                            "mobile_no": "",
                            "email_id": "",
                            "type_of_occupier": 1,
                            "powner_id": None
                        }
                    ]
                }

        count = 0
        retry_required = True
        while retry_required and count < 10:
            try:
                response = requests.post(insert_owner_details_url, json=payload, headers=headers)
                response.raise_for_status()
                
                if any("error" in str(value) for value in response.json().values()):
                    print("Error text found in dictionary values!")
                    print(response.json())
                    count += 1
                    sleep(3)
                    print(f"retrying {count}")
                else:
                    retry_required = False
            except Exception as ex:
                count += 1
                sleep(3)
                print(ex)
                print(f"retrying 84 {count}")
            # print(payload)
            print(response.text)