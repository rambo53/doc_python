from __future__ import annotations

from handler import *
from client import Client
product_A_hendler = TypeAProductHandler()
product_B_hendler = TypeBProductHandler()
product_C_hendler = TypeCProductHandler()
product_D_hendler = TypeDProductHandler()
product_A_hendler.set_inner_handler(product_B_hendler).set_inner_handler(product_C_hendler).set_inner_handler(product_D_hendler)

client = Client() 
products= ["p1","p3","p5","p7","p10"]
print("============================")
client.work_on(product_A_hendler, products)
print("============================")
client.work_on(product_B_hendler, products)
 