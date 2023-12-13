import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

@st.cache_data
def load_data():
    # Load data here
    cities_with_count = [
        {"name": "Москва", "count": 279, "coordinates": [55.7558, 37.6176]},
        {"name": "Казань", "count": 83, "coordinates": [55.796127, 49.106405]},
        {"name": "Альметьевск", "count": 9, "coordinates": [54.901422, 52.297446]},
        {"name": "Бугульма", "count": 5, "coordinates": [54.53618, 52.78992]},
        {"name": "Новосибирск", "count": 1, "coordinates": [55.030199, 82.92043]},
        {"name": "Уфа", "count": 37, "coordinates": [54.738762, 55.972055]},
        {"name": "Санкт-Петербург", "count": 12, "coordinates": [59.9343, 30.3351]},
        {"name": "Пермь", "count": 1, "coordinates": [58.004785, 56.241648]},
        {"name": "Владивосток", "count": 4, "coordinates": [43.115536, 131.885485]},
        {"name": "Киев", "count": 5, "coordinates": [50.4501, 30.5234]},
        {"name": "Львов", "count": 2, "coordinates": [49.8397, 24.0297]},
        {"name": "Тюмень", "count": 1, "coordinates": [57.153033, 65.534328]},
        {"name": "Грозный", "count": 1, "coordinates": [43.317444, 45.698265]},
        {"name": "Тверь", "count": 2, "coordinates": [56.859611, 35.911896]},
        {"name": "Куйбышев", "count": 5, "coordinates": [55.44753, 78.32181]},
        {"name": "Гомель", "count": 1, "coordinates": [52.4345, 30.9754]},
        {"name": "Ижевск", "count": 3, "coordinates": [56.8386, 53.3549]},
        {"name": "Краснодар", "count": 1, "coordinates": [45.0355, 38.9753]},
        {"name": "Самара", "count": 2, "coordinates": [53.195, 50.103]},
        {"name": "Набережные Челны", "count": 2, "coordinates": [55.7437, 52.3959]},
        {"name": "Бавлы", "count": 1, "coordinates": [54.3964, 53.2746]},
        {"name": "Махачкала", "count": 1, "coordinates": [42.9849, 47.5047]},
        # Добавьте остальные города здесь
    ]
    return cities_with_count

# Load data
cities_with_count = load_data()

# Create map
map_center = [55.7558, 37.6176]
my_map = folium.Map(location=map_center, zoom_start=5, tiles="OpenStreetMap")

# Create marker cluster
marker_cluster = MarkerCluster().add_to(my_map)

# Place markers on the map with counts
for city in cities_with_count:
    for _ in range(city["count"]):
        folium.Marker(location=city["coordinates"], popup=city["name"]).add_to(marker_cluster)

# Display the map
st.write("City Map with Counts")
folium_static(my_map)
