import json
import unittest

import httpretty
from sure import expect

from mercedesapi import MercedesApi

VEHICLE_ID = "54321"

TEST_JSON = '{"key": "value"}'
TOKEN = "12345"
api = MercedesApi(TOKEN)


class GetBasedRequestTest(unittest.TestCase):

    @httpretty.activate
    def test_get_vehicle_ids(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles")
        self.assertEqual(api.get_vehicle_ids(), json.loads(TEST_JSON))
        _assert_header_contain_auth()

    @httpretty.activate
    def test_get_vehicle_information(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID)
        self.assertEqual(api.get_vehicle_information(VEHICLE_ID),
                         json.loads(TEST_JSON))
        _assert_header_contain_auth()

    @httpretty.activate
    def test_get_tire_state(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID + "/tires")
        self.assertEqual(api.get_tire_state(VEHICLE_ID), json.loads(TEST_JSON))
        _assert_header_contain_auth()

    @httpretty.activate
    def test_get_location(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID + "/location")
        self.assertEqual(api.get_location(VEHICLE_ID), json.loads(TEST_JSON))
        _assert_header_contain_auth()

    @httpretty.activate
    def test_get_odometer(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID + "/odometer")
        self.assertEqual(api.get_odometer(VEHICLE_ID), json.loads(TEST_JSON))
        _assert_header_contain_auth()

    @httpretty.activate
    def test_get_fuel_state(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID + "/fuel")
        self.assertEqual(api.get_fuel_state(VEHICLE_ID), json.loads(TEST_JSON))
        _assert_header_contain_auth()

    @httpretty.activate
    def test_get_charge_state(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID + "/stateofcharge")
        self.assertEqual(api.get_charge_state(VEHICLE_ID),
                         json.loads(TEST_JSON))
        _assert_header_contain_auth()

    @httpretty.activate
    def test_get_doors_state(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID + "/doors")
        self.assertEqual(api.get_doors_state(VEHICLE_ID), json.loads(TEST_JSON))
        _assert_header_contain_auth()


def _prepare_call(expected_url):
    httpretty.register_uri(httpretty.GET,
                           expected_url,
                           body=TEST_JSON,
                           content_type="application/json")


def _assert_header_contain_auth():
    expect(httpretty.last_request().headers.get("content-type")).being.equal(
        "application/json")
    expect(httpretty.last_request().headers.get("Authorization")).being.equal(
        "Bearer " + TOKEN)


if __name__ == '__main__':
    unittest.main()
