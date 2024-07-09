import threading


class DriverManager:
    _driver_thread_local = threading.local()

    @classmethod
    def get_driver(cls):
        return getattr(cls._driver_thread_local, 'driver', None)

    @classmethod
    def set_driver(cls, driver):
        cls._driver_thread_local.driver = driver

    @classmethod
    def unload_driver(cls):
        if hasattr(cls._driver_thread_local, 'driver'):
            del cls._driver_thread_local.driver

    def __init__(self):
        raise NotImplementedError("This class should not be instantiated.")
