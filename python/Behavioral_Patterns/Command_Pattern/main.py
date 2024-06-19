from __future__ import annotations

from receiver import Receiver
from command import *
from invoker import Invoker 


receiver = Receiver()
invoker = Invoker(Command_1("str_0"),Command_2(receiver, "str_1", "str_2", 999))
invoker.do_something()