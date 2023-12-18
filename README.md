# reqdriver

A Python package that seamlessly transfers a `requests.Session` to a Selenium WebDriver, maintaining session cookies and proxy settings. Ideal for web scraping and automated browsing with pre-established session states.

![banner](https://raw.githubusercontent.com/glizzykingdreko/reqdriver/main/img/banner.jpg)

<p align="center">
    <a href="https://pypi.org/project/reqdriver/">
        <img src="https://img.shields.io/pypi/v/reqdriver.svg" alt="PyPI Version"/>
    </a>
    <a href="https://github.com/glizzykingdreko/reqdriver">
        <img src="https://img.shields.io/badge/GitHub-glizzykingdreko%2Freqdriver-g" alt="GlizzykingDreko"/>
    </a>
</p>

## Features

- **Transfer Session Cookies**: Easily transfer cookies from a `requests.Session` to a Selenium WebDriver.
- **Proxy Integration**: Set up a Chrome WebDriver with the same proxy settings as your `requests.Session`.
- **Flexible WebDriver Management**: Use an existing WebDriver instance or let reqdriver create one for you.
- **Custom WebDriver Options**: Customize your WebDriver with additional options.

## Installation

```bash
pip install reqdriver
```

## Usage

### Basic Usage

Import the `RequestsDriver` class from the `reqdriver` package:

```python
from reqdriver import RequestsDriver
import requests
```

### Transferring Cookies

Transfer cookies from a `requests.Session`:

```python
session = requests.Session()
session.cookies.set('test_cookie', '12345', domain='example.com')

req_driver = RequestsDriver(session)
req_driver.set_cookies('http://example.com')

driver = req_driver.get_driver()
driver.get('http://example.com')
```

### Setting Proxies

Set up a WebDriver with the same proxy settings as your `requests.Session`:

```python
session = requests.Session()
session.proxies = {
    'http': 'http://192.168.3.2:8080'
}

req_driver = RequestsDriver(session)
driver = req_driver.get_driver()
driver.get('http://example.com')
```

### Using Custom WebDriver Options

Pass your custom Chrome WebDriver options:

```python
from selenium.webdriver.chrome.options import Options

custom_options = Options()
custom_options.add_argument('--headless')

session = requests.Session()
req_driver = RequestsDriver(session, custom_options=custom_options)

driver = req_driver.get_driver()
driver.get('http://example.com')
```

### Using Existing WebDriver

Pass your already created WebDriver instance:

```python
from selenium import webdriver

existing_driver = webdriver.Chrome(executable_path='path_to_chromedriver')
session = requests.Session()
req_driver = RequestsDriver(session, driver=existing_driver)

req_driver.set_cookies('http://example.com')
existing_driver.get('http://example.com')
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

Distributed under the MIT License. See `LICENSE` for more information.


## My links

- [Website](https://glizzykingdreko.github.io/)
- [GitHub](https://github.com/glizzykingdreko)
- [Twitter](https://mobile.twitter.com/glizzykingdreko)
- [Medium](https://medium.com/@glizzykingdreko)
- [Email](mailto:glizzykingdreko@protonmail.com)