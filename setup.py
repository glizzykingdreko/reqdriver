from setuptools import setup, find_packages

setup(
    name='reqdriver',
    version='0.1.2',
    author='glizzykingdreko',  # Replace with your name
    author_email='glizzykingdreko@protonmail.com',  # Replace with your email
    description='Effortlessly transfer sessions from Python requests to Selenium WebDriver.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/glizzykingdreko/reqdriver',  # Replace with the URL of your repo
    packages=find_packages(),
    install_requires=[
        'selenium>=3.141.0',
        'requests>=2.25.1'
    ],
    keywords='web scraping browser automation selenium webdriver python requests session transfer automated testing web automation selenium browser http requests cookie management proxy handling selenium sessions web testing data scraping selenium cookies',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
