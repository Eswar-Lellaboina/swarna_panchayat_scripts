import requests
import random
from constants import *
import pandas as pd


file_path = 'TAB1.xlsx'
df = pd.read_excel(file_path)
df = df.applymap(lambda x: x.replace('\xa0', ' ') if isinstance(x, str) else x)


loop_data = df.to_dict(orient='records')

url = f"https://api.swarnapanchayat.apcfss.in/prtntmapi/insert-prptydetails"

survey_numbers_list = ["61","95","109","53","64"]

for record in loop_data[30:]:
    random_number = random.randrange(0, 5)
    data = {
        "user_id": user_id,
        "panch_secretariat_id": str(panch_secretariat_id),
        "village_id": str(village_id),
        "assessment_no": str(record["Assesment No/ULPIN No"]),
        "ppn": "NA",
        "habitation": record["Habitation Name"],
        "survey_no": survey_numbers_list[random_number],
        "construction_fallen": "Y",
        "lp_approved": "",
        "lp_no": "",
        "plot_no": str(record["Assesment No/ULPIN No"]),
        "door_no": record["House/Door No."],
        "building_approved": "N",
        "age_of_build_date": str(random.randrange(1, 28)),
        "age_of_build_month": str(random.randrange(1, 13)),
        "age_of_build_year": str(random.randrange(1995, 2016)),
        "nature_property": "2",
        "nature_landuse": "2",
        "nature_usage": "1",
        "nature_ownership": "1",
        "mode_acquisition": "1",
        "property_address": property_street,
        "property_street": property_street,
        "property_pincode": property_pincode,
        "generated_assessment_no": "",
        "east": record["East"],
        "west": record["West"],
        "north": record["North"],
        "south": record["South"],
        "owner_occupation": [
            {
                "surname": "",
                "name": "",
                "gender": "",
                "relation_type": "",
                "relation_person_surname": "",
                "relation_person_name": "",
                "address": "",
                "pincode": "",
                "aadhaar_no": "",
                "mobile_no": "",
                "email_id": "",
                "type_of_occupier": "",
                "powner_id": ""
            }
        ],
        "other_facilities": [],
        "site_length": "",
        "site_breadth": "",
        "site_total_area": 0,
        "capital_value_site": "",
        "rate_adopted": "",
        "type_of_building": "",
        "capital_value_building": "",
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
                "floor_no": "",
                "category_of_building": "",
                "type_of_construction": "",
                "sub_type_of_construction": "",
                "occupation": "",
                "length": "",
                "breadth": "",
                "total_area": 0,
                "total_area_hidden": 0,
                "measurment_id": 0,
                "total_area_in_sqmts": 0,
                "total_area_in_yards": 0
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
        "site_total_area_sq_mts": 0,
        "site_total_area_sq_yards": 0,
        "site_rate": "",
        "capital_value_of_site": 0,
        "capital_value_building_rate": 0,
        "building_rate": "",
        "total_capital_value_building_rate": 0
    }
    count = 0
    retry_required = True
    while retry_required and count < 10:
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            if any("error" in str(value) for value in response.json().values()):
                print("Error text found in dictionary values!")
                count += 1
                print(f"retrying {count}")
            else:
                retry_required = False
        except Exception as ex:
            count += 1
            print(ex)
            print(f"retrying 209 {count}")
        # print(record)
        print(response.text)
