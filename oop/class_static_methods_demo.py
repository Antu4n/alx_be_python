# class_static_methods_demo.py

class Calculator:
    # class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: does not access class or instance attributes"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: can access class attributes via 'cls'"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()