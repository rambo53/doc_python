from __future__ import annotations
from abc import ABC, abstractmethod

from business_logic import BusinessAbstraction, ExtendedBusinessAbstraction
from implementation import ConcreteImplementation1, ConcreteImplementation2


implementation_1 = ConcreteImplementation1()
businessAbstraction_1 = BusinessAbstraction(implementation_1)
businessAbstraction_1.run()

implementation_2 = ConcreteImplementation2()
businessAbstraction_2 = ExtendedBusinessAbstraction(implementation_2)
businessAbstraction_2.run()

    