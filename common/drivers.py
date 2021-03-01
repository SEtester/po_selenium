from se_utils import DriverNotFoundException
from setting import SE_DRIVERS


class Driver:
    driver = None

    @classmethod
    def driver_obj(cls, driver_name, executable_path=None, options=None):
        if driver_name.lower() not in SE_DRIVERS:
            raise DriverNotFoundException(f'driver:{driver_name}不存在，请检查setting SE_DRIVER的配置')

        if cls.driver is None:
            cls.driver = SE_DRIVERS.get(driver_name.lower())(options=options, executable_path=executable_path)

        return cls.driver


if __name__ == '__main__':
    from setting import CHROME_DRIVER_FOR_MAC

    # driver = Driver.driver_obj('chrome')(chrome_options=head_less_of_chrome(), executable_path=CHROME_DRIVER_FOR_MAC)
    driver = Driver.driver_obj('chrome')(executable_path=CHROME_DRIVER_FOR_MAC)
    driver.get('https://www.baidu.com')
    print(driver.current_url)
    driver.quit()
