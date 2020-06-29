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


class Application:
    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]
            self.links = config["_links"]
            self.accessibility = config["accessibility"]
            self.created = config["created"]
            self.credentials = config["credentials"]
            self.features = config["features"]
            self.id = config["id"]
            self.label = config["label"]
            self.last_updated = config["lastUpdated"]
            self.licensing = config["licensing"]
            self.name = config["name"]
            self.profile = config["profile"]
            self.settings = config["settings"]
            self.sign_on_mode = config["signOnMode"]
            self.status = config["status"]
            self.visibility = config["visibility"]
        else:
            self.embedded = None
            self.links = None
            self.accessibility = None
            self.created = None
            self.credentials = None
            self.features = None
            self.id = None
            self.label = None
            self.last_updated = None
            self.licensing = None
            self.name = None
            self.profile = None
            self.settings = None
            self.sign_on_mode = None
            self.status = None
            self.visibility = None

# End of File Generation
