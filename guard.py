from blacklist import BlackList
from memory import GuardMemory
from ip_details import IpDetails


class AntiDDosGuard:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.blacklist = BlackList()
        self.memory = GuardMemory()

    def check(self, ip: str):
        if ip in self.blacklist:
            return "Permanently Blocked"

        else:
            if ip not in self.memory:
                self.memory[ip] = IpDetails(ip=ip)

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
