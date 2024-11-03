# This file is part of ADG: Anti-DDOS Guard.
#
# ADG: Anti-DDOS Guard is licensed under the GNU General Public License v3.0.
# See the LICENSE file for more details.
#
# Copyright (C) 2024 Armen-Jean Andreasian.

from .blacklist import BlackList
from .memory import GuardMemory
from .ip_details import IpDetails


class AntiDDosGuard:
    __instance = None

    def __new__(cls, *args, **kwargs):
        """
        Making AntiDDosGuard singleton, making one copies of blacklist and memory for all deriving instances.
        """
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.blacklist = BlackList()
            cls.memory = GuardMemory()
        return cls.__instance

    def __init__(self, cooldown: int = 5):
        """
        :param cooldown: Penalty for a client to wait
        """
        self.cooldown = cooldown

    def check(self, ip: str):
        """
        Checking IP Before Proceeding.
        """
        if ip in self.blacklist:
            return "Permanently Blocked"

        else:
            if ip not in self.memory:
                self.memory[ip] = IpDetails(ip=ip, cooldown=self.cooldown)

            ip_detail = self.memory[ip]

            ip_check = ip_detail.check()
            if ip_check:
                return True
            else:
                ip_level = ip_detail.warning_level
                if ip_level > 3:
                    self.blacklist.add(ip)
                    return "Permanently Blocked"
                else:
                    return (f"Please, wait for {ip_detail.waiting_time} seconds. "
                            f"{ip_detail.tries_left} tries left until getting blocked.")
