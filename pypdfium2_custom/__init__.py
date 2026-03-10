import ctypes
import pypdfium2
import pypdfium2.raw as pdfium_raw

# load the same libpdfium used by pypdfium2
pdfium_lib = ctypes.CDLL(pdfium_raw.__file__.replace("__init__.py", "libpdfium.so"))

# expose your function
FPDFFormObj_RemoveObject = pdfium_lib.FPDFFormObj_RemoveObject

FPDFFormObj_RemoveObject.argtypes = [
    ctypes.c_void_p,  # FPDF_FORMHANDLE
    ctypes.c_void_p   # FPDF_PAGEOBJECT
]

FPDFFormObj_RemoveObject.restype = None
