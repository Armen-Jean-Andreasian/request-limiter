# This file is part of ADG: Anti-DDOS Guard.
#
# ADG: Anti-DDOS Guard is licensed under the GNU General Public License v3.0.
# See the LICENSE file for more details.
#
# Copyright (C) 2024 Armen-Jean Andreasian.

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ip_details import IpDetails


class GuardMemory:
    def __init__(self):
        self.memory = dict()

    def retrieve_ip_details(self, ip: str) -> Union[None, "IpDetails"]:
        return self.memory.get(ip)

    def add_ip(self, ip: str, ip_details: "IpDetails"):
        self.memory[ip] = ip_details

    def __contains__(self, ip: str) -> bool:
        return ip in self.memory

    def __setitem__(self, ip: str, ip_details: "IpDetails") -> None:
        self.memory[ip] = ip_details

    def __getitem__(self, ip: str) -> "IpDetails":
        return self.memory.get(ip)
