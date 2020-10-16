# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject
import okta.models.platform_condition_evaluator_platform_operating_system_version\
    as platform_condition_evaluator_platform_operating_system_version


class PlatformConditionEvaluatorPlatformOperatingSystem(
    OktaObject
):
    """
    A class for PlatformConditionEvaluatorPlatformOperatingSystem objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.expression = config["expression"]\
                if "expression" in config else None
            self.type = config["type"]\
                if "type" in config else None
            if "version" in config:
                if isinstance(config["version"],
                              platform_condition_evaluator_platform_operating_system_version.PlatformConditionEvaluatorPlatformOperatingSystemVersion):
                    self.version = config["version"]
                else:
                    self.version = platform_condition_evaluator_platform_operating_system_version.PlatformConditionEvaluatorPlatformOperatingSystemVersion(
                        config["version"]
                    )
            else:
                self.version = None
        else:
            self.expression = None
            self.type = None
            self.version = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "expression": self.expression,
            "type": self.type,
            "version": self.version
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
