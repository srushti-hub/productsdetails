def format_product_info(product_id: int, name: str, quantity: int, price: float) -> str:
    """
    Accepts product details and returns a well-formatted string.

    Args:
        product_id (int): Unique identifier for the product
        name (str): Name of the product
        quantity (int): Number of items available
        price (float): Price per item

    Returns:
        str: Formatted product information
    """
    return (
        f"Product Information:\n"
        f"ID       : {product_id}\n"
        f"Name     : {name}\n"
        f"Quantity : {quantity}\n"
        f"Price    : ${price:.2f}"
    )
# Example usage
if __name__ == "__main__":
    print(format_product_info(101, "Laptop", 5, 799.99))