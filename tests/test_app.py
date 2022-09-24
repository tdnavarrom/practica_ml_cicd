import json

from unittest import TestCase
from unittest.mock import patch

import requests


class TestUrl(TestCase):

    @patch('requests.post')
    def test_post(self, mock_post):

        f = open("resources/payload.json")
        info = json.load(f)
        resp = requests.post("https://us-central1-practicaml-cicd-363402.cloudfunctions.net/heat-disease", data=info, headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with("https://us-central1-practicaml-cicd-363402.cloudfunctions.net/heart-disease", data=info, headers={'Content-Type': 'application/json'})