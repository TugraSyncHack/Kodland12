import matplotlib.pyplot as plt
import sqlite3

def create_graph(city_name=None):
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()

    if city_name:
        cursor.execute("SELECT lat, lng FROM cities WHERE name=?", (city_name,))
    else:
        cursor.execute("SELECT lat, lng FROM cities")
    
    data = cursor.fetchall()
    conn.close()

    if not data: 
        return None

    plt.figure(figsize=(10, 6))
    lats = [row[0] for row in data]
    lngs = [row[1] for row in data]
    
    plt.scatter(lngs, lats, color='blue', alpha=0.6)
    plt.title("City Map")
    plt.grid(True)
    
    img_path = "map.png"
    plt.savefig(img_path)
    plt.close()
    return img_path
