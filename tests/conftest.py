# conftest.py
# Copyright 2024, 2025 Michael Konrad 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ast import literal_eval
from os import path
import pytest


class Helpers:
    @staticmethod
    def get_single_docker_secret(file_path: str) -> str:
        if path.exists(file_path):
            with open(file_path, "r") as f:
                secret = literal_eval(f.read())

            return secret

    @staticmethod
    def get_multiple_docker_secret(file_path: str) -> dict:
        if path.exists(file_path):
            with open(file_path, "r") as f:
                secrets = literal_eval(f.read())

            return secrets

@pytest.fixture
def helpers():
    return Helpers