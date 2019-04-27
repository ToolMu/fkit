import os
import re

_filename_ascii_strip_re = re.compile(r"[^A-Za-z0-9_.-]")
_filename_gbk_strip_re = re.compile(u"[^\u4e00-\u9fa5A-Za-z0-9_.-]")
_windows_device_files = (
    "CON",
    "AUX",
    "COM1",
    "COM2",
    "COM3",
    "COM4",
    "LPT1",
    "LPT2",
    "LPT3",
    "PRN",
    "NUL",
)


def secure_filename(filename):
    if isinstance(filename, str):
        from unicodedata import normalize

        # filename = normalize("NFKD", filename).encode("ascii", "ignore")
        # filename = filename.decode("ascii")
        filename = normalize("NFKD", filename).encode("utf-8", "ignore")
        filename = filename.decode("utf-8")
    for sep in os.path.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, " ")
    # filename = str(_filename_ascii_strip_re.sub("", "_".join(filename.split()))).strip(
    filename = str(_filename_gbk_strip_re.sub("", "_".join(filename.split()))).strip(
        "._"
    )

    if (
        os.name == "nt"
        and filename
        and filename.split(".")[0].upper() in _windows_device_files
    ):
        filename = "_" + filename

    return filename
