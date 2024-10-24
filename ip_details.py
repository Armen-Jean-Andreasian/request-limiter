from datetime import datetime, timedelta


class IpDetails:
    __instances = dict()

    def __new__(cls, *args, **kwargs):
        ip = kwargs.get('ip') if 'ip' in kwargs else args[0]

        if ip in cls.__instances:
            return cls.__instances[ip]
        else:
            obj = super().__new__(cls)
            cls.__instances[ip] = obj
            return obj

    def __init__(self, ip: str):
        self.ip = ip
        self.warning_level = 0
        self.next_request = None

    def check(self):
        if self.warning_level is None:
            raise NotImplementedError(f"[Bug found] Blacklist doesn't contain IP {self.ip}. This IP is permanently blocked.")

        if not self.next_request:
            self.next_request = datetime.now() + timedelta(seconds=5)
            return True
        else:
            if self.next_request > datetime.now():
                self.warning_level += 1
                self.next_request = datetime.now() + timedelta(seconds=5)
                return False
            else:
                self.warning_level = 0
                self.next_request = datetime.now() + timedelta(seconds=5)
                return True


    @property
    def waiting_time(self):
        return f"{self.next_request - datetime.now()}"

    @property
    def tries_left(self):
        return f"{3 - self.warning_level}"
