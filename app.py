#!/usr/bin/env python3
"""
Epson Ink Pad Resetter - Web Application
Simple GUI para resetar impressoras Epson via browser
"""

from flask import Flask, render_template, request, jsonify
import re
from struct import pack, unpack
import os
import sys

try:
    from easysnmp import Session
except ImportError:
    print("ERROR: easysnmp não instalado. Execute: pip install easysnmp")
    sys.exit(1)

app = Flask(__name__)

# Configurações
EEPROM_LINK = "1.3.6.1.4.1.1248.1.2.2.44.1.1.2.1"
READ_PREFIX = "124.124.7.0."
WRITE_PREFIX = "124.124.16.0."
WRITE_MIDDLE = ".66.189.33."
WRITE_SUFFIX = ".0.78.98.115.106.99.98.122.98"

PRINTER_MODELS = {
    "L355": {"password": [74, 54], "base": 0x0},
    "L3160": {"password": [74, 54], "base": 0x0},
    "L3250": {"password": [74, 54], "base": 0x0},
    "L4160": {"password": [74, 54], "base": 0x0},
    "M1170": {"password": [74, 54], "base": 0x0},
    "ET-2850": {"password": [74, 54], "base": 0x0},
    "ET-2860": {"password": [74, 54], "base": 0x0},
}

WASTE_COUNTERS = {
    "counter_1": {"addrs": [48, 49], "limit": 6345},
    "counter_2": {"addrs": [50, 51], "limit": 3416},
    "counter_3": {"addrs": [252, 253], "limit": 1300},
}

class EpsonPrinter:
    def __init__(self, ip, snmp_community="public"):
        self.ip = ip
        self.snmp_community = snmp_community
        self.session = None
        self.model = "Unknown"
    
    def connect(self):
        try:
            self.session = Session(
                hostname=self.ip,
                community=self.snmp_community,
                version=1,
                timeout=5
            )
            self.session.get("1.3.6.1.2.1.1.5.0")
            self.get_model()
            return True, "Conectado com sucesso!"
        except Exception as e:
            return False, f"Erro ao conectar: {str(e)}"
    
    def get_model(self):
        try:
            response = self.session.get("1.3.6.1.2.1.1.5.0").value
            self.model = response
            return response
        except:
            return "Unknown"
    
    def read_eeprom_addr(self, addr):
        if not self.session:
            raise Exception("Not connected")
        
        config = PRINTER_MODELS.get(self.model, {"password": [74, 54], "base": 0x0})
        split_addr = unpack("BB", pack(">H", addr))
        password = config["password"]
        oid = f"{EEPROM_LINK}.{READ_PREFIX}{password[0]}.{password[1]}.65.190.160.{split_addr[1]}.{split_addr[0]}"
        
        response = self.session.get(oid).value
        match = re.findall(r"EE:[0-9A-F]{6}", response)
        if not match:
            raise ValueError(f"Invalid response: {response}")
        
        response = match[0][3:]
        return response[4:6]
    
    def write_eeprom(self, addr, value):
        if not self.session:
            raise Exception("Not connected")
        
        config = PRINTER_MODELS.get(self.model, {"password": [74, 54], "base": 0x0})
        split_addr = unpack("BB", pack(">H", addr))
        password = config["password"]
        oid = f"{EEPROM_LINK}.{WRITE_PREFIX}{password[0]}.{password[1]}{WRITE_MIDDLE}{split_addr[1]}.{split_addr[0]}.{value}{WRITE_SUFFIX}"
        
        self.session.get(oid)
    
    def read_waste_counter(self):
        results = {}
        for counter_name, counter_info in WASTE_COUNTERS.items():
            try:
                config = PRINTER_MODELS.get(self.model, {"password": [74, 54], "base": 0x0})
                addrs = counter_info["addrs"]
                limit = counter_info["limit"]
                addr_list = self._transform_addrs(config["base"], addrs[::-1])
                values = [self.read_eeprom_addr(addr) for addr in addr_list]
                counter_value = int("".join(values), 16)
                percentage = min((counter_value / limit) * 100, 100)
                results[counter_name] = {
                    "percentage": round(percentage, 2),
                    "filled": counter_value >= limit
                }
            except Exception as e:
                results[counter_name] = {"error": str(e)}
        return results
    
    def reset_waste_counter(self):
        config = PRINTER_MODELS.get(self.model, {"password": [74, 54], "base": 0x0})
        all_addrs = []
        for counter_info in WASTE_COUNTERS.values():
            addrs = counter_info["addrs"]
            all_addrs.extend(self._transform_addrs(config["base"], addrs[::-1]))
        
        for addr in all_addrs:
            self.write_eeprom(addr, 0)
        
        return self.read_waste_counter()
    
    @staticmethod
    def _transform_addrs(base, addrs):
        return [(base << 8) | (n & 0xFF) for n in addrs]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status', methods=['POST'])
def api_status():
    try:
        data = request.json
        ip = data.get('ip')
        
        if not ip:
            return jsonify({"success": False, "error": "IP não fornecido"})
        
        printer = EpsonPrinter(ip)
        success, message = printer.connect()
        
        if not success:
            return jsonify({"success": False, "error": message})
        
        status = printer.read_waste_counter()
        
        return jsonify({
            "success": True,
            "model": printer.model,
            "status": status
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/reset', methods=['POST'])
def api_reset():
    try:
        data = request.json
        ip = data.get('ip')
        
        if not ip:
            return jsonify({"success": False, "error": "IP não fornecido"})
        
        printer = EpsonPrinter(ip)
        success, message = printer.connect()
        
        if not success:
            return jsonify({"success": False, "error": message})
        
        status_after = printer.reset_waste_counter()
        
        return jsonify({
            "success": True,
            "model": printer.model,
            "status_after": status_after,
            "message": "Reset completo! Almofada zerada!"
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🖨️  Epson Ink Pad Resetter - Web Interface")
    print("="*60)
    print("\n✅ Servidor rodando em: http://localhost:5000")
    print("\n🌐 Abra seu navegador e acesse: http://localhost:5000")
    print("\n💡 Ctrl+C para parar o servidor\n")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)
