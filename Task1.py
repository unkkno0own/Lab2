import math

def calculate_z(alpha):
    z = math.cos(alpha) + math.cos(2 * alpha) + math.cos(6 * alpha) + math.cos(7 * alpha)
    return z

def calculate_product(n):
    product = 1
    for i in range(1, 2*n, 2): 
        product *= i
    return product

def main():
    alpha = float(input("Введіть значення альфа (в радіанах): "))
    z_result = calculate_z(alpha)
    print(f"Результат для z: {z_result}")

    n = int(input("Введіть значення n: "))
    product_result = calculate_product(n)
    print(f"Добуток непарних чисел до {2*n-1}: {product_result}")

if __name__ == "__main__":
    main()
