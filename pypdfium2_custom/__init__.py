import ctypes
from pypdfium2.raw import bindings


# Access the already-loaded pdfium library
pdfium_lib = bindings._libs["pdfium"]


# expose your function
FPDFFormObj_RemoveObject = pdfium_lib.FPDFFormObj_RemoveObject

FPDFFormObj_RemoveObject.argtypes = [
    ctypes.c_void_p,  # FPDF_FORMHANDLE
    ctypes.c_void_p,  # FPDF_PAGEOBJECT
]

FPDFFormObj_RemoveObject.restype = None