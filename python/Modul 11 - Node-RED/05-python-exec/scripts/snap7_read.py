import snap7
from snap7.util import get_real
from snap7.snap7types import *

# Forbindelsesparametre
ip = "192.168.0.1"
rack = 0
slot = 1

# Datablock-parametre
db_number = 1
start_offset = 0
size = 4  # 4 bytes for REAL

# Opret forbindelse
client = snap7.client.Client()
client.connect(ip, rack, slot)

# Læs data
data = client.db_read(db_number, start_offset, size)

# Parse værdi
val = get_real(data, 0)
print(val)

# Afbryd forbindelse
client.disconnect()
