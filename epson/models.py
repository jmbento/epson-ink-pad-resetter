"""
Epson Printer Models Configuration
"""

PRINTER_MODELS = {
    "L355": {"password": [74, 54], "base": 0x0},
    "L3160": {"password": [74, 54], "base": 0x0},
    "L3250": {"password": [74, 54], "base": 0x0},
    "L4160": {"password": [74, 54], "base": 0x0},
    "M1170": {"password": [74, 54], "base": 0x0},
    "ET-2850": {"password": [74, 54], "base": 0x0},
    "ET-2860": {"password": [74, 54], "base": 0x0},
    "default": {"password": [74, 54], "base": 0x0},
}

WASTE_COUNTERS = {
    "counter_1": {"addrs": [48, 49], "limit": 6345},
    "counter_2": {"addrs": [50, 51], "limit": 3416},
    "counter_3": {"addrs": [252, 253], "limit": 1300},
}

EEPROM_LINK = "1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1"
READ_PREFIX = "124.124.7.0."
WRITE_PREFIX = "124.124.16.0."
WRITE_MIDDLE = ".66.189.33."
WRITE_SUFFIX = ".0.78.98.115.106.99.98.122.98"
