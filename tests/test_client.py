#!/usr/bin/env python
"""client tests"""

import pytest
from darbiadev_ups import UPSServices


def test_invalid_auth_type_error():
    with pytest.raises(ValueError) as exception:
        client = UPSServices(
            base_url="test",
            username="test",
            password="test",
            access_license_number="test",
        )
        client._make_request(
            method="test",
            auth_type="test",
            service="test",
            data={},
        )