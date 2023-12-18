import os
import zipfile
from random import randint
from typing import Optional
import requests
from selenium.webdriver import Chrome, ChromeOptions

class RequestsDriver:

    @staticmethod
    def get_proxy_extension(session: requests.Session) -> str:
        """
        Generates a proxy extension for Chrome based on a given requests.Session.

        Args:
        session (requests.Session): The session object to extract the proxy from.

        Returns:
        str: Path to the generated proxy extension file.
        """
        return RequestsDriver(session)._setup_proxy_extension()

    def __init__(
        self, 
        session: requests.Session, 
        driver_path: Optional[str] = None, 
        driver: Optional[Chrome] = None,
        do_not_set_proxy: bool = False,
        custom_options: Optional[ChromeOptions] = None
    ):
        """
        Initialize the RequestsDriver object.

        Args:
        session (requests.Session): The session to transfer to the WebDriver.
        driver_path (Optional[str]): The path to the ChromeDriver executable.
        driver (Optional[Chrome]): An existing Chrome WebDriver instance.
        do_not_set_proxy (bool): Whether to ignore the session's proxy setting.
        custom_options (Optional[ChromeOptions]): Custom options for the WebDriver.
        """
        self.session = session
        self.proxy_extension = None
        self.session_proxy = session.proxies.get('http') if not do_not_set_proxy else None
        self.driver_path = driver_path or os.environ.get('CHROMEDRIVER_PATH')
        self.custom_options = custom_options or ChromeOptions()
        self.driver = driver if driver is not None else self._init_driver()
    
    def _clean_extension(self) -> None:
        """
        Cleans up the proxy extension file if it exists.
        """
        if self.proxy_extension: 
            os.remove(self.proxy_extension)

    def _init_driver(self) -> Chrome:
        """
        Initializes the Chrome WebDriver with custom options and proxy settings.

        Returns:
        Chrome: The initialized Chrome WebDriver instance.
        """
        if self.session_proxy:
            self.proxy_extension = self._setup_proxy_extension()
            self.custom_options.add_extension(self.proxy_extension)

        return Chrome(executable_path=self.driver_path, options=self.custom_options)

    def _setup_proxy_extension(self) -> str:
        """
        Sets up the proxy extension for Chrome based on the session's proxy.

        Returns:
        str: Path to the generated proxy extension file.
        """
        manifest_json, background_js = self._create_proxy_extension_files()
        pluginfile = f'proxy_auth_plugin_{randint(1, 9e12)}.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        return pluginfile

    def _create_proxy_extension_files(self) -> tuple[str, str]:
        """
        Creates the proxy extension files for Chrome.

        Returns:
        tuple[str, str]: The manifest.json and background.js content for the extension.
        """
        proxy_host, proxy_port = self.session_proxy.split('//')[1].split(':')
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 3,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "service_worker": "background.js"
            }
        }
        """

        background_js = f"""
        var config = {{
                mode: "fixed_servers",
                rules: {{
                    singleProxy: {{
                        scheme: "http",
                        host: "{proxy_host}",
                        port: parseInt({proxy_port})
                    }},
                    bypassList: ["localhost"]
                }}
            }};
        chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});
        """
        return manifest_json, background_js

    def set_cookies(self, url: str) -> None:
        """
        Sets the cookies from the session to the WebDriver after visiting the specified URL.

        Args:
        url (str): The URL to visit before setting cookies.
        """
        self.driver.get(url)
        for cookie in self.session.cookies:
            self.driver.add_cookie({
                'name': cookie.name,
                'value': cookie.value,
                'domain': cookie.domain
            })
        self.driver.refresh()

    def get_driver(self) -> Chrome:
        """
        Returns the Chrome WebDriver instance.

        Returns:
        Chrome: The Chrome WebDriver instance.
        """
        return self.driver
