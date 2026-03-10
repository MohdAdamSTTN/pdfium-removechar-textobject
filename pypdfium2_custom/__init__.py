import ctypes
import pypdfium2.raw as pdfium_raw

# get the already-loaded pdfium library
pdfium_lib = pdfium_raw._LIB

# expose your function
FPDFFormObj_RemoveObject = pdfium_lib.FPDFFormObj_RemoveObject

FPDFFormObj_RemoveObject.argtypes = [
    ctypes.c_void_p,  # FPDF_FORMHANDLE
    ctypes.c_void_p,  # FPDF_PAGEOBJECT
]

FPDFFormObj_RemoveObject.restype = None