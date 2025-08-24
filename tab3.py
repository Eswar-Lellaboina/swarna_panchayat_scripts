import requests
import random
import pandas as pd
from time import sleep
from constants import *


file_path = 'Pedapalem HT 2024-25 (1) (2).xlsx'
df = pd.read_excel(file_path)
df["Ass No"] = df["Ass No"].fillna(0).astype(int)


first_url = f"https://api.swarnapanchayat.apcfss.in/prtntmapi/getPartial-ownerDetails/{panch_secretariat_id}"

first_res = requests.get(first_url, headers=headers)
first_res.raise_for_status()
first_level_data = first_res.json()
loop_data = first_level_data["data"]
survey_numbers_list = ["206-2A,2B", "234-2B", "246-2,3", "235-1"]

for record in loop_data:
    if record["ownername"] != "NA" and (400 <= int(record["old_assessment_number"]) <= 500):
        property_id = record["property_id"]
        old_assessment_number = record["old_assessment_number"]
        
        second_url = f"https://api.swarnapanchayat.apcfss.in/prtntmapi/get-firsttabdata/{property_id}"
        second_res = requests.get(second_url, headers=headers)
        second_res.raise_for_status()
        second_level_data = second_res.json()
        new_assessment_no = second_level_data["data"][0]["assessment_no"]
        door_no = second_level_data["data"][0]["door_no"]

        third_url = f"https://api.swarnapanchayat.apcfss.in/prtntmapi/get-secondtabdata/{property_id}"
        third_res = requests.get(third_url, headers=headers)
        third_res.raise_for_status()
        third_level_data = third_res.json()["data"][0]
        filtered_df = df[df['Ass No'] == int(old_assessment_number)]

        # Convert to dictionary
        filtered_data_dict = filtered_df.to_dict(orient='records')
        # surname = filtered_data_dict[0]["Owner Name\n/ Establishment Name"].split(" ")[0]
        # name = filtered_data_dict[0]["Owner Name\n/ Establishment Name"].split(" ")[1]
        # relation_person_name = filtered_data_dict[0]["Father Name\n/PanNumber"]
        
        actual_leng = random.randrange(40, 50)
        actual_bred = random.randrange(40, 50)
        flat_lenth = actual_leng - 2 
        flat_breadth = actual_bred - 2
        sq_ft_to_sq_mts = 0.092903
        sq_ft_to_sq_yds = 0.111111
        payload = {
                    "user_id": user_id,
                    "panch_secretariat_id": panch_secretariat_id,
                    "village_id": village_id,
                    "assessment_no": str(old_assessment_number),
                    "ppn": "NA",
                    "habitation": habitation,
                    "survey_no": second_level_data["data"][0]["survey_no"],
                    "construction_fallen": "Y",
                    "lp_approved": "",
                    "lp_no": "",
                    "plot_no": str(old_assessment_number),
                    "door_no": door_no,
                    "building_approved": "N",
                    "age_of_build_date": second_level_data["data"][0]["building_age"].split("-")[2],
                    "age_of_build_month": second_level_data["data"][0]["building_age"].split("-")[1],
                    "age_of_build_year": second_level_data["data"][0]["building_age"].split("-")[0],
                    "nature_property": 2,
                    "nature_landuse": 2,
                    "nature_usage": 1,
                    "nature_ownership": 1,
                    "mode_acquisition": 1,
                    "property_address": door_no,
                    "property_street": property_street,
                    "property_pincode": pincode,
                    "generated_assessment_no": str(new_assessment_no),
                    "east": second_level_data["data"][0]["east"],
                    "west": second_level_data["data"][0]["west"],
                    "north": second_level_data["data"][0]["north"],
                    "south": second_level_data["data"][0]["south"],
                    "owner_occupation": [
                        {
                            "surname": third_level_data["owner_surname"],
                            "name": third_level_data["owner_name"],
                            "gender": third_level_data["gender_id"],
                            "relation_type": 1,
                            "relation_person_surname": third_level_data["guardian_surname"],
                            "relation_person_name": third_level_data["guardian_name"],
                            "address": habitation,
                            "pincode": pincode,
                            "aadhaar_no": "",
                            "mobile_no": "",
                            "email_id": "",
                            "type_of_occupier": third_level_data["occupier_id"],
                            "powner_id": third_level_data["powner_id"]
                        }
                    ],
                    "other_facilities": [
                        "IHHL",
                        "Lpg_Connection",
                        "Power_Connection",
                        "Pucca_Road",
                        "Drainage_Facility",
                        "LPG_Connection"
                    ],
                    "site_length": str(actual_leng),
                    "site_breadth": str(actual_bred),
                    "site_total_area": str(round(actual_leng * actual_bred, 2)),
                    "capital_value_site": str(int(actual_leng * actual_bred * 41.6)),
                    "rate_adopted": "39",
                    "type_of_building": "1",
                    "capital_value_building": str(int(filtered_data_dict[0]["Capital Value"])),
                    "floor_details_total_area": "",
                    "flooor_details": [
                        {
                            "sub_type_list": [
                                {
                                    "classification_id": 1,
                                    "subtypeconstruction_id": 1,
                                    "subtypeconstruction_desc": "Ground, 1st and 2nd"
                                },
                                {
                                    "subtypeconstruction_desc": "Apartments without common walls atleast on 3 sides",
                                    "classification_id": 1,
                                    "subtypeconstruction_id": 2
                                },
                                {
                                    "subtypeconstruction_desc": "Cellar, Mezzanine Floor,stilt and Parking Place",
                                    "classification_id": 1,
                                    "subtypeconstruction_id": 3
                                },
                                {
                                    "subtypeconstruction_desc": "For every extra floor(from 3rd floor onwards) in addition to the rate mentioned at 1A(a)",
                                    "subtypeconstruction_id": 4,
                                    "classification_id": 1
                                },
                                {
                                    "subtypeconstruction_desc": "Ground Floor",
                                    "classification_id": 2,
                                    "subtypeconstruction_id": 5
                                },
                                {
                                    "classification_id": 2,
                                    "subtypeconstruction_id": 6,
                                    "subtypeconstruction_desc": "First Floor"
                                },
                                {
                                    "classification_id": 2,
                                    "subtypeconstruction_id": 7,
                                    "subtypeconstruction_desc": "Structure from 2nd floor onwards(for each floor)"
                                },
                                {
                                    "subtypeconstruction_desc": "Cellar, Mezzanine Floor,stilt and Parking Place",
                                    "classification_id": 2,
                                    "subtypeconstruction_id": 3
                                },
                                {
                                    "subtypeconstruction_id": 8,
                                    "subtypeconstruction_desc": "ACC Sheet , Pantileshabad Stones, Zinc Sheets, Tiles, Mangalore Tiles, Cuddapah Slab, Jack Arch, Madras terrace roof and such other non RCC roofs Structers",
                                    "classification_id": 4
                                },
                                {
                                    "subtypeconstruction_desc": "Cinema Halls, Mills, Factories and similar kind of structures with walls exceeding 10ft height",
                                    "subtypeconstruction_id": 9,
                                    "classification_id": 4
                                },
                                {
                                    "subtypeconstruction_id": 10,
                                    "subtypeconstruction_desc": "Poultry Farms",
                                    "classification_id": 4
                                },
                                {
                                    "subtypeconstruction_desc": "With walls",
                                    "subtypeconstruction_id": 11,
                                    "classification_id": 6
                                },
                                {
                                    "subtypeconstruction_id": 12,
                                    "subtypeconstruction_desc": "Without walls",
                                    "classification_id": 6
                                },
                                {
                                    "subtypeconstruction_desc": "Not Availble",
                                    "classification_id": 0,
                                    "subtypeconstruction_id": 0
                                }
                            ],
                            "floor_no": "9",
                            "category_of_building": "1",
                            "type_of_construction": "1",
                            "sub_type_of_construction": "1",
                            "occupation": "1",
                            "length": str(flat_lenth),
                            "breadth": str(flat_breadth),
                            "total_area": str(round(flat_lenth * flat_breadth, 2)),
                            "total_area_hidden": str(round(flat_lenth * flat_breadth, 2)),
                            "measurment_id": 0,
                            "total_area_in_sqmts": str(round(flat_lenth * flat_breadth * sq_ft_to_sq_mts, 2)),
                            "total_area_in_yards": str(round(flat_lenth * flat_breadth * sq_ft_to_sq_yds, 2))
                        }
                    ],
                    "current_arrear": [
                        {
                            "taxation_type": "1",
                            "financial_year": "2024-25",
                            "house_tax_amount": "",
                            "water_tax": "",
                            "lighting_tax": "",
                            "drianage_tax": "",
                            "library_cess": "",
                            "sports_cess": "",
                            "fire_cess": "",
                            "private_tap_tax": 0,
                            "total_demand": ""
                        }
                    ],
                    "private_tap": "",
                    "private_tap_details": [
                        {
                            "taxation_type_private_tap": "1",
                            "financial_year_private_tap": "2024-25",
                            "tap_fee": ""
                        }
                    ],
                    "site_total_area_sq_mts": str(round(actual_leng * actual_bred * sq_ft_to_sq_mts, 2)),
                    "site_total_area_sq_yards": str(round(actual_leng * actual_bred * sq_ft_to_sq_yds, 2)),
                    "site_rate": "5", #5
                    "capital_value_of_site": 0,
                    "capital_value_building_rate": flat_lenth * flat_breadth * 110,
                    "building_rate": "110", #110
                    "total_capital_value_building_rate": 0
                }
        count = 0
        retry_required = True
        final_url = "https://api.swarnapanchayat.apcfss.in/prtntmapi/insert-floordetails"
        while retry_required and count < 10:
            try:
                response = requests.post(final_url, json=payload, headers=headers)
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
