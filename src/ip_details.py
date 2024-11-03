# This file is part of ADG: Anti-DDOS Guard.
#
# ADG: Anti-DDOS Guard is licensed under the GNU General Public License v3.0.
# See the LICENSE file for more details.
#
# Copyright (C) 2024 Armen-Jean Andreasian.

from datetime import datetime, timedelta


class IpDetails:
    """The info on IP. For each IP only one instance exists"""
    __instances = dict()

    def __new__(cls, *args, **kwargs):
        ip = kwargs.get('ip') if 'ip' in kwargs else args[0]

        if ip in cls.__instances:
            return cls.__instances[ip]
        else:
            obj = super().__new__(cls)
            cls.__instances[ip] = obj
            return obj

    def __init__(self, ip: str, cooldown: int):
        """
        :param ip: IP address of a client
        :param cooldown: Penalty for a client to wait
        """
        self.ip = ip
        self.warning_level = 0
        self.next_request = None
        self.cooldown = cooldown

    def check(self) -> bool:
        """Returns True if IP is eligible to access the source, False otherwise"""
        if self.warning_level is None:
            raise NotImplementedError(
                f"[Bug found] Blacklist doesn't contain IP {self.ip}. This IP is permanently blocked.")

        if not self.next_request:
            self.next_request = datetime.now() + timedelta(seconds=self.cooldown)
            return True
        else:
            if self.next_request > datetime.now():
                self.warning_level += 1
                self.next_request = datetime.now() + timedelta(seconds=self.cooldown)
                return False
            else:
                self.warning_level = 0
                self.next_request = datetime.now() + timedelta(seconds=self.cooldown)
                return True

    @property
    def waiting_time(self):
        return f"{self.next_request - datetime.now()}"

    @property
    def tries_left(self):
        return f"{3 - self.warning_level}"
