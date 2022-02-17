"""
This module creates the map of friends locations using the .json file.
"""

from geopy.geocoders import Nominatim
import folium
from twitter2 import get_data


def transform_address_to_coordinaters(address):
    """
    This module transorms adress to coordinates
    >>> transform_address_to_coordinaters("Lviv, Ukraine")
    (49.841952, 24.0315921)
    """
    geo = Nominatim(user_agent="main.py")
    while True:
        try:
            location = geo.geocode(address)
            longitude = location.longitude
            latitude = location.latitude
            return(latitude, longitude)
        except:
            if not ' ' in address:
                return -1
            else:
                address = ' '.join(address.split(' ')[:-1])


def main(raw):
    """
    Main function.
    """
    data = get_data(raw)
    map = folium.Map(zoom_start=10)
    main_layer = folium.FeatureGroup(name='Friend locations')
    for friend in data["users"]:
        friend_coords = transform_address_to_coordinaters(friend['location'])
        if friend_coords == -1:
            continue
        main_layer.add_child(folium.Marker(location=[friend_coords[0],
                                                     friend_coords[1]], popup=friend['name']))
    map.add_child(main_layer)
    map.save('/templates/Map.html')


if __name__ == "__main__":
    main()
