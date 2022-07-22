import json
import pickle
import sys
import os

sys.path.append(os.path.join(os.getcwd(), ".."))
from ej_2.services.tuler import Tuler
from ej_2.services.ferretero import Ferretero
from ej_2.enums.risk_enum import RiskEnum

with open(os.path.join("data", "input_data.json")) as f:
    input_data = json.load(f)
with open(os.path.join("data", "output_data.pickle"), "rb") as file:
    expected_output = pickle.load(file)


def choose_model(input: dict):
    obj = None
    if input["product_name"] == RiskEnum("ferretero").value:
        obj = Ferretero(
            user_id=input["user_id"],
            product_name=input["product_name"],
            input_data=input["input_data"],
        )
    elif input["product_name"] == RiskEnum("tuler").value:
        obj = Tuler(
            user_id=input["user_id"],
            product_name=input["product_name"],
            input_data=input["input_data"],
        )
    return obj


def check_result(output_data):
    assert output_data == expected_output
    print("Buen trabajo")


def main():
    output_data = []
    for input in input_data:
        obj = choose_model(input)
        output_data.append(obj.risk_analysis())
    check_result(output_data)


if __name__ == "__main__":
    main()
