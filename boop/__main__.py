#!/usr/bin/env python3

import boop
import time

from boop.helpers import *

app = boop.BoopSniff("wlx18d6c70f910d", boop.Hopper("wlx18d6c70f910d"))
app.packets = 0

@app.handler(boop.MGMT_DEAUTH)
def pkt(self, p):
    self.packets += 1
    return

@app.handler(boop.MGMT_BEACON)
def pkt(self, p):
    get_ssid(p.info)
    get_security(p)
    self.packets += 1
    return

@app.printer()
def printa(self):
    # Could do something with curses
    while True:
        # print(self.packets)
        time.sleep(5)

app.run()
