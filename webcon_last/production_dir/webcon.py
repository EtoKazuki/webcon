# -*-coding:utf-8-*-


import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import sys
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt


# ボタンが押下されたときのコールバック関数
def search_db(place, platform, genre):
    # データベースの接続
    c = sqlite3.connect("gamedata.db")

    # 両方とも選択しないが選ばれた場合
    if((platform == "選択しない") & (genre == "選択しない")):
        if(place == "日本"):
            item = c.execute("""
                SELECT year, sum(JP_Sales) FROM game_table
                GROUP BY year
                """)
        elif(place == "アメリカ"):
            item = c.execute("""
                SELECT year, sum(NA_Sales) FROM game_table
                GROUP BY year
                """)
        elif(place == "ヨーロッパ"):
            item = c.execute("""
                SELECT year, sum(EU_Sales) FROM game_table
                GROUP BY year
                """)
        elif(place == "その他"):
            item = c.execute("""
                SELECT year, sum(EU_Sales) FROM game_table
                GROUP BY year
                """)
        else:
            item = c.execute("""
                SELECT year, sum(Global_Sales) FROM game_table
                GROUP BY year
                """)
    # platformで選択しないが選ばられ場合
    elif(platform == "選択しない"):
        if(place == "日本"):
            item = c.execute("""
                SELECT year, sum(JP_Sales) FROM game_table
                WHERE  Genre= '{}'
                GROUP BY year
                """.format(genre))
        elif(place == "アメリカ"):
            item = c.execute("""
                SELECT year, sum(NA_Sales) FROM game_table
                WHERE Genre='{}'
                GROUP BY year
                """.format(genre))
        elif(place == "ヨーロッパ"):
            item = c.execute("""
                SELECT year, sum(EU_Sales) FROM game_table
                WHERE Genre='{}'
                GROUP BY year
                """.format(genre))
        elif(place == "その他"):
            item = c.execute("""
                SELECT year, sum(EU_Sales) FROM game_table
                WHERE Genre='{}'
                GROUP BY year
                """.format(genre))
        else:
            item = c.execute("""
                SELECT year, sum(Global_Sales) FROM game_table
                WHERE Genre='{}'
                GROUP BY year
                """.format(genre))

    # genreで選択されないが選ばれた場合
    elif(genre == "選択しない"):
        if(place == "日本"):
            item = c.execute("""
                SELECT year, sum(JP_Sales) FROM game_table
                WHERE Platform='{}'
                GROUP BY year
                """.format(platform))
        elif(place == "アメリカ"):
            item = c.execute("""
                SELECT year, sum(NA_Sales) FROM game_table
                WHERE Platform='{}'
                GROUP BY year
                """.format(platform))
        elif(place == "ヨーロッパ"):
            item = c.execute("""
                SELECT year, sum(EU_Sales) FROM game_table
                WHERE  Platform='{}'
                GROUP BY year
                """.format(platform))
        elif(place == "その他"):
            item = c.execute("""
                SELECT year, sum(EU_Sales) FROM game_table
                WHERE  Platform='{}'
                GROUP BY year
                """.format(platform))
        else:
            item = c.execute("""
                SELECT year, sum(Global_Sales) FROM game_table
                WHERE  Platform='{}'
                GROUP BY year
                """.format(platform))

    # 両方とも選択された場合
    else:
        if(place == "日本"):
            item = c.execute("""
                SELECT year, sum(JP_Sales) FROM game_table
                WHERE  Platform='{}' and Genre='{}'
                GROUP BY year
                """.format(platform, genre))
        elif(place == "アメリカ"):
            item = c.execute("""
                SELECT year, sum(NA_Sales) FROM game_table
                WHERE  Platform='{}' and Genre='{}'
                GROUP BY year
                """.format(platform, genre))
        elif(place == "ヨーロッパ"):
            item = c.execute("""
                SELECT year, sum(EU_Sales) FROM game_table
                WHERE  Platform='{}' and Genre='{}'
                GROUP BY year
                """.format(platform, genre))
        elif(place == "その他"):
            item = c.execute("""
                SELECT year, sum(EU_Sales) FROM game_table
                WHERE  Platform='{}' and Genre='{}'
                GROUP BY year
                """.format(platform, genre))
        else:
            item = c.execute("""
                SELECT year, sum(Global_Sales) FROM game_table
                WHERE  Platform='{}' and Genre='{}'
                GROUP BY year
                """.format(platform, genre))

    # 選択した値を変数に代入
    if(platform == "選択しない"):
        platform = ""
    if(genre == "選択しない"):
        genre = ""
    return_plat = platform
    return_genre = genre
    # SQLから呼び出された結果を格納
    items = item.fetchall()
    tuple_item = tuple(items)
    return_list = [tuple_item, return_plat, return_genre]
    c.close()

    return return_list


def make_graph(result_list):
    result = result_list[0]
    plat = str(result_list[1])
    genre = str(result_list[2])
    year_list = []
    sales_list = []
    # 粘土と売り上げをそれぞれのリストに追加していく
    for i in range(len(result)):
        year_list.append(int(result[i][0]))
        sales_list.append(float(result[i][1]))

    plt.figure(figsize=(10, 4.5))
    plt.plot(year_list, sales_list)

    if((not plat) & (not genre)):
        plt.title("Sales Graph")
    elif(plat == ""):
        plt.title("{} game Sales Graph".format(genre))
    elif(genre == ""):
        plt.title("{} as Platform Sales Graph".format(plat))

    plt.xlabel("Year")
    plt.ylabel("Sales(dollars in millions)")
    plt.show()
# -------------------------------


# GUI部分の作成
root = tk.Tk()
# -----------------------------
label = tk.Label(text="売上")
label.pack()

combo_place = ttk.Combobox(root, state='readonly')
combo_place["values"] = ("日本", "アメリカ", "ヨーロッパ", "その他", "総売上")
combo_place.current(0)
combo_place.pack()
# -----------------------------
label_plat = tk.Label(text="プラットフォーム")
label_plat.pack()

combo_plat = ttk.Combobox(root, state='readonly')
combo_plat["values"] = ("選択しない", "3DS", "DS", "GBA", "GC", "N64", "PC", "PS", "PS2",\
                        "PS3", "PS4", "PSV", "SNES", "Wii", "WiiU", "X360", \
                        "XB", "XOne", "3DO", "DC", "NG", "SAT", "TG16", "GEN",\
                        "PCFX", "WS", "GG", "SCD", "GB", "NES", "2600")
combo_plat.current(0)
combo_plat.pack()
# -----------------------------
label_genre = tk.Label(text="ジャンル")
label_genre.pack()

combo_genre = ttk.Combobox(root, state='readonly')
combo_genre["values"] = ("選択しない", "Action", "Adventure", "Fighting", "Misc", "Platform",\
                         "Puzzle", "Racing", "Role-Playing", "Shooter", "Simulation",\
                         "Sports", "Strategy")
combo_genre.current(0)
combo_genre.pack()

# コールバック関数にsearch_dbを定義
button = tk.Button(text="表示", command=lambda: make_graph(search_db(combo_place.get(), combo_plat.get(), combo_genre.get())))
button.pack()

# -----------------------------
button_quit = tk.Button(text="終了", command=lambda: sys.exit(1))
button_quit.pack(side="top", pady=10)
# -----------------------------

root.geometry("300x300")
root.title("Game Sales")
root.mainloop()
