from nada_dsl import *


def my_nada_program():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define inputs
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform computation (example: add two secret integers)
    result = my_int1 + my_int2

    # Define outputs
    output = Output(result, "result_output", party1)

    # Return outputs as a list
    return [output]
