import json
import unittest

import httpretty
import six
from sure import expect

from mercedesapi import MercedesApi

VEHICLE_ID = "54321"

TEST_JSON = '{"status": "INITIATED"}'
TOKEN = "12345"
api = MercedesApi(TOKEN)


class PostBasedRequestTest(unittest.TestCase):

    @httpretty.activate
    def test_lock_doors(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID + "/doors")
        self.assertEqual(api.lock_doors(VEHICLE_ID), json.loads(TEST_JSON))
        _assert_header_contain_auth()
        expect(
            httpretty.last_request().body).being.equal(
            six.b('{"command": "LOCK"}'))

    @httpretty.activate
    def test_unlock_doors(self):
        _prepare_call(
            "https://api.mercedes-benz.com/experimental/connectedvehicle/v1"
            "/vehicles/" + VEHICLE_ID + "/doors")
        self.assertEqual(api.unlock_doors(VEHICLE_ID), json.loads(TEST_JSON))
        _assert_header_contain_auth()
        expect(
            httpretty.last_request().body).being.equal(
            six.b('{"command": "UNLOCK"}'))


def _prepare_call(expected_url):
    httpretty.register_uri(httpretty.POST,
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
