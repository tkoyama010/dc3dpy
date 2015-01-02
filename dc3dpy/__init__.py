import numpy as np
import ctypes
from ctypes import cdll
dc3d = cdll.LoadLibrary("/usr/lib/dc3d.so")
@np.vectorize
def ux(alpha, x, y, z, depth, dip, al1, al2, aw1, aw2, disl1, disl2, disl3):
  alpha = ctypes.c_float(alpha)
  x = ctypes.c_float(x)
  y = ctypes.c_float(y)   
  z = ctypes.c_float(z)   
  depth = ctypes.c_float(depth)
  dip = ctypes.c_float(dip)
  al1 = ctypes.c_float(al1) 
  al2 = ctypes.c_float(al2)
  aw1 = ctypes.c_float(aw1)
  aw2 = ctypes.c_float(aw2)
  disl1 = ctypes.c_float(disl1) 
  disl2 = ctypes.c_float(disl2)
  disl3 = ctypes.c_float(disl3)
  dc3d.ux.restype = ctypes.c_float
  return  dc3d.ux(alpha, x, y, z, depth, dip, al1, al2, aw1, aw2, disl1, disl2, disl3)
@np.vectorize
def uy(alpha, x, y, z, depth, dip, al1, al2, aw1, aw2, disl1, disl2, disl3):
  alpha = ctypes.c_float(alpha)
  x = ctypes.c_float(x)
  y = ctypes.c_float(y)   
  z = ctypes.c_float(z)   
  depth = ctypes.c_float(depth)
  dip = ctypes.c_float(dip)
  al1 = ctypes.c_float(al1) 
  al2 = ctypes.c_float(al2)
  aw1 = ctypes.c_float(aw1)
  aw2 = ctypes.c_float(aw2)
  disl1 = ctypes.c_float(disl1) 
  disl2 = ctypes.c_float(disl2)
  disl3 = ctypes.c_float(disl3)
  dc3d.uy.restype = ctypes.c_float
  return  dc3d.uy(alpha, x, y, z, depth, dip, al1, al2, aw1, aw2, disl1, disl2, disl3)
@np.vectorize
def uz(alpha, x, y, z, depth, dip, al1, al2, aw1, aw2, disl1, disl2, disl3):
  alpha = ctypes.c_float(alpha)
  x = ctypes.c_float(x)
  y = ctypes.c_float(y)   
  z = ctypes.c_float(z)   
  depth = ctypes.c_float(depth)
  dip = ctypes.c_float(dip)
  al1 = ctypes.c_float(al1) 
  al2 = ctypes.c_float(al2)
  aw1 = ctypes.c_float(aw1)
  aw2 = ctypes.c_float(aw2)
  disl1 = ctypes.c_float(disl1) 
  disl2 = ctypes.c_float(disl2)
  disl3 = ctypes.c_float(disl3)
  dc3d.uz.restype = ctypes.c_float
  return  dc3d.uz(alpha, x, y, z, depth, dip, al1, al2, aw1, aw2, disl1, disl2, disl3)
@np.vectorize
def iret(alpha, x, y, z, depth, dip, al1, al2, aw1, aw2, disl1, disl2, disl3):
  alpha = ctypes.c_float(alpha)
  x = ctypes.c_float(x)
  y = ctypes.c_float(y)   
  z = ctypes.c_float(z)   
  depth = ctypes.c_float(depth)
  dip = ctypes.c_float(dip)
  al1 = ctypes.c_float(al1) 
  al2 = ctypes.c_float(al2)
  aw1 = ctypes.c_float(aw1)
  aw2 = ctypes.c_float(aw2)
  disl1 = ctypes.c_float(disl1) 
  disl2 = ctypes.c_float(disl2)
  disl3 = ctypes.c_float(disl3)
  dc3d.iret.restype = ctypes.c_int
  return  dc3d.iret(alpha, x, y, z, depth, dip, al1, al2, aw1, aw2, disl1, disl2, disl3)

