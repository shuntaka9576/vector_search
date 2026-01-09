import os


examples_path, products_path = (
    os.path.join(
        os.path.dirname(__file__),
        "esci-data",
        "shopping_queries_dataset",
        f"shopping_queries_dataset_{suffix}",
    )
    for suffix in ("examples", "products")
)

print(examples_path)
print("----")
print(products_path)
