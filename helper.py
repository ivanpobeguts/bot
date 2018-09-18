import ephem
from datetime import datetime


def count_constellation(planet_name):
    today_date = str(datetime.today().date())

    if planet_name == 'Mars':
        planet = ephem.Mars(today_date)
    elif planet_name == 'Mercury':
        planet = ephem.Mercury(today_date)
    elif planet_name == 'Venus':
        planet = ephem.Venus(today_date)
    elif planet_name == 'Jupiter':
        planet = ephem.Jupiter(today_date)
    elif planet_name == 'Saturn':
        planet = ephem.Saturn(today_date)
    elif planet_name == 'Uranus':
        planet = ephem.Uranus(today_date)
    elif planet_name == 'Neptune':
        planet = ephem.Neptune(today_date)
    elif planet_name == 'Pluto':
        planet = ephem.Pluto(today_date)
    else:
        return None

    constel = ephem.constellation(planet)
    return constel[1]
