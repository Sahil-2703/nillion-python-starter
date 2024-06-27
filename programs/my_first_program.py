from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # write the computation for your program here - use my_int1 and my_int2 as inputs
    # make sure you change the output below to be your new output
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))
    my_int4 = SecretInteger(Input(name="my_int4", party=party2))

    # Perform some arithmetic operations
    sum1 = my_int1 + my_int2
    sum2 = my_int3 + my_int4
    total_sum = sum1 + sum2

    product1 = my_int1 * my_int2
    product2 = my_int3 * my_int4
    total_product = product1 * product2

    # Conditional operations
    is_equal = my_int1 == my_int3
    is_greater = my_int2 > my_int4

    return [  
      Output(sum1, "sum1_output", party1),
      Output(sum2, "sum2_output", party2),
      Output(total_sum, "total_sum_output", party1),
      Output(product1, "product1_output", party1),
      Output(product2, "product2_output", party2),
      Output(total_product, "total_product_output", party1),
      Output(is_equal, "is_equal_output", party1),
      Output(is_greater, "is_greater_output", party2)
    ]