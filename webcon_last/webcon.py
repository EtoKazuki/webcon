# -*- coding: utf-8 -*-

from contextlib import closing
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

dbname = "gamedata.db"
list_plat = []
list_count = []

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    sql = "select platform, count(*) from game_table group by platform"
    c.execute(sql)
    for row in c:
        list_plat.append(row[0])
        list_count.append(row[1])
    c.close()

x_width = 0.5
x_loc = np.array(range(len(list_count))) + x_width

plt.bar(x_loc, list_count, width=x_width)
plt.xticks(x_loc, list_plat)

plt.show()
