from __future__ import annotations
 
from typing import Any
 
from builder import ConcreteBuilder


builder = ConcreteBuilder()


print("Build a product with setting A")
builder.build_setting_A() 
builder.product.show_all_config()


print("Build a product with setting B")
builder.build_setting_B() 
builder.product.show_all_config()

