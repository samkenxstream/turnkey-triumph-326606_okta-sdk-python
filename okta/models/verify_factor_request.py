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


class VerifyFactorRequest:
    def __init__(self, config=None):
        if config:
            self.activation_token = config["activationToken"]
            self.answer = config["answer"]
            self.attestation = config["attestation"]
            self.client_data = config["clientData"]
            self.next_pass_code = config["nextPassCode"]
            self.pass_code = config["passCode"]
            self.registration_data = config["registrationData"]
            self.state_token = config["stateToken"]
        else:
            self.activation_token = None
            self.answer = None
            self.attestation = None
            self.client_data = None
            self.next_pass_code = None
            self.pass_code = None
            self.registration_data = None
            self.state_token = None

# End of File Generation
