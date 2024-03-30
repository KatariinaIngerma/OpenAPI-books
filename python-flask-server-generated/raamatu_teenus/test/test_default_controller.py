import unittest

from flask import json

from raamatu_teenus.models.raamatu_lisamine201_response import RaamatuLisamine201Response  # noqa: E501
from raamatu_teenus.models.raamatu_loomise_sisend import RaamatuLoomiseSisend  # noqa: E501
from raamatu_teenus.models.raamatu_nimekiri200_response import RaamatuNimekiri200Response  # noqa: E501
from raamatu_teenus.models.raamatu_otsingu_sisend import RaamatuOtsinguSisend  # noqa: E501
from raamatu_teenus.models.raamatust_sone_otsimine201_response import RaamatustSoneOtsimine201Response  # noqa: E501
from raamatu_teenus.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_raamatu_kustutamine(self):
        """Test case for raamatu_kustutamine

        Raamatu kustutamine
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/raamatud/{book_id}'.format(book_id='book_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_raamatu_lisamine(self):
        """Test case for raamatu_lisamine

        Raamatu loomine
        """
        raamatu_loomise_sisend = {"raamatu_id":12345}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/raamatud',
            method='POST',
            headers=headers,
            data=json.dumps(raamatu_loomise_sisend),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_raamatu_nimekiri(self):
        """Test case for raamatu_nimekiri

        Raamatute
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/raamatud',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_raamatust_sone_otsimine(self):
        """Test case for raamatust_sone_otsimine

        Alla tõmmatud raamtust sõne otsimine
        """
        raamatu_otsingu_sisend = {"raamatu_id":12345,"sone":"estonia"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/raamatu_otsing',
            method='POST',
            headers=headers,
            data=json.dumps(raamatu_otsingu_sisend),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
