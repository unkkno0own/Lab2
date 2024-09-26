
def calculate_product(n):
    product = 1
    for i in range(1, 2 * n, 2): 
        product *= i
    return product
