# %%
import requests
from loguru import logger
from functools import lru_cache


@lru_cache
def get_photovoltaic_data(
    latitude,
    longitude,
    pv_tech,
    pv_peak_power,
    pv_loss,
    pv_angle,
    pv_azimuth,
    start_year=None,
    end_year=None,
):
    """
    Dokumentation:
    "https://joint-research-centre.ec.europa.eu/pvgis-photovoltaic-geographical-information-system/getting-started-pvgis/api-non-interactive-service_en"
    """
    query = (
        f"https://re.jrc.ec.europa.eu/api/seriescalc?lat={latitude}&lon={longitude}&horirrad=1&outputformat=json&pvcalculation=1"
        f"{'&startyear='+str(start_year) if start_year else ''}"
        f"{'&endyear='+str(end_year) if end_year else ''}"
        f"&peakpower={pv_peak_power}"
        f"&pvtechchoice={pv_tech}"
        f"&angle={pv_angle}"
        f"&aspect={pv_azimuth}"
        f"&loss={pv_loss}"
    )
    logger.info(f"query: {query}")

    response = requests.get(query)
    return response.json()


# %%
# result = get_photovoltaic_data(
#     latitude=50,
#     longitude=50,
#     pv_peak_power=2,
#     pv_tech="CIS",
#     pv_loss=0,
#     pv_angle=0,
#     pv_azimuth=0,
# )
# # result
# [
#     {"time": data["time"], "PV system power": data["P"]}
#     for data in result["outputs"]["hourly"]
# ]

# https://re.jrc.ec.europa.eu/api/seriescalc?lat=&lon=&horirrad=1&outputformat=json&pvcalculation=1&peakpower=1&pvtechchoice=&angle=45&aspect=180&loss=0

# %%
# %%
