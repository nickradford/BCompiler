import sys

sys.path.append("../")

from JavaEmitter import *

j = JavaEmitter()

j.debugOn()

j.add(Opcode.IMUL)


j.finish()