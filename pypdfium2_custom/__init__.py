import ctypes
import pathlib
import pypdfium2_raw


# locate the libpdfium shared library shipped with pypdfium2
lib_path = pathlib.Path(pypdfium2_raw.__file__).parent / "libpdfium.so"

pdfium_lib = ctypes.CDLL(str(lib_path))


FPDFFormObj_RemoveObject = pdfium_lib.FPDFFormObj_RemoveObject

FPDFFormObj_RemoveObject.argtypes = [
    ctypes.c_void_p,  # FPDF_FORMHANDLE
    ctypes.c_void_p,  # FPDF_PAGEOBJECT
]

FPDFFormObj_RemoveObject.restype = None