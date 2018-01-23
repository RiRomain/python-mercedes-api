""" Mercedes API Access
https://developer.mercedes-benz.com/apis/connected_vehicle_experimental_api/docs

"""

import logging

import requests

_LOGGER = logging.getLogger(__name__)
_ENDPOINT = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
_VEHICLES = "vehicles"
_TIRE_INFO = "tires"
_LOCATION_INFO = "location"
_ODOMETER_INFO = "odometer"
_FUEL_STATE = "fuel"
_CHARGE_STATE = "stateofcharge"
_DOORS_ENDPOINT = "doors"
_TIMEOUT = 10

class MercedesApi(object):
    """ Enable access to the Mercedes API """

    def __init__(self, access_token, proxies=None):
        self._access_token = access_token
        self._auth_header = {"content-type": "application/json",
                             "Authorization": "Bearer {}".format(
                                 self._access_token)}
        self._proxies = proxies

    """ Return the vehicles ids list
    [
        {
            "id": "YOUR_VEHICLE_ID",
            "licenseplate": "S-GG-7558",
            "finorvin": "1HM1FA517HEBF4AF2"
        }
    ]
    """

    def get_vehicle_ids(self):
        return self._retrieve_json_at_url(
            "{}/{}".format(_ENDPOINT, _VEHICLES))

    """ Return vehicle information
    {
        "id": "YOUR_VEHICLE_ID",
        "licenseplate": "S-GG-7558",
        "salesdesignation": "E 400 4MATIC Limousine",
        "finorvin": "1HM1FA517HEBF4AF2",
        "nickname": "mmueller",
        "modelyear": "2017",
        "colorname": "iridiumsilber metallic",
        "fueltype": "Benzin",
        "powerhp": "333",
        "powerkw": "245",
        "numberofdoors": "5",
        "numberofseats": "5"
    }
    """

    def get_vehicle_information(self, vehicle_id):
        return self._retrieve_json_at_url(
            "{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id))

    def get_tire_state(self, vehicle_id):
        return self._retrieve_json_at_url(
            "{}/{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id,
                                 _TIRE_INFO))

    def get_location(self, vehicle_id):
        return self._retrieve_json_at_url(
            "{}/{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id,
                                 _LOCATION_INFO))

    def get_odometer(self, vehicle_id):
        return self._retrieve_json_at_url(
            "{}/{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id,
                                 _ODOMETER_INFO))

    def get_fuel_state(self, vehicle_id):
        return self._retrieve_json_at_url(
            "{}/{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id,
                                 _FUEL_STATE))

    def get_charge_state(self, vehicle_id):
        return self._retrieve_json_at_url(
            "{}/{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id,
                                 _CHARGE_STATE))

    def get_doors_state(self, vehicle_id):
        return self._retrieve_json_at_url(
            "{}/{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id,
                                 _DOORS_ENDPOINT))

    def lock_doors(self, vehicle_id):
        return self._post_json_command(
            "{}/{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id,
                                 _DOORS_ENDPOINT), {"command": "LOCK"})

    def unlock_doors(self, vehicle_id):
        return self._post_json_command(
            "{}/{}/{}/{}".format(_ENDPOINT, _VEHICLES, vehicle_id,
                                 _DOORS_ENDPOINT), {"command": "UNLOCK"})

    def _retrieve_json_at_url(self, url):
        try:
            _LOGGER.warning("Connect to URL " + str(url))
            res = requests.get(url,
                               headers=self._auth_header,
                               proxies=self._proxies,
                               timeout=_TIMEOUT)
        except requests.exceptions.Timeout:
            _LOGGER.exception(
                "Connection to the api timed out at URL %s", _VEHICLES)
            return
        if res.status_code != 200:
            _LOGGER.exception(
                "Connection failed with http code %s", res.status_code)
            return
        return res.json()

    def _post_json_command(self, url, command):
        try:
            _LOGGER.warning("Connect to URL " + str(url))
            res = requests.post(url,
                                json=command,
                                headers=self._auth_header,
                                proxies=self._proxies,
                                timeout=_TIMEOUT)
        except requests.exceptions.Timeout:
            _LOGGER.exception(
                "Connection to the api timed out at URL %s", _VEHICLES)
            return
        if res.status_code != 200:
            _LOGGER.exception(
                "Connection failed with http code %s", res.status_code)
            return
        return res.json()
