from setuptools import setup

setup(
    name='anti_keylogger_scanner',
    version='1.0.0',
    description='A simple anti-keylogger scanner using Tkinter and psutil',
    author='Chirag Khatri',
    py_modules=['anti_keylogger_scanner'],
    install_requires=[
        'psutil'
        'pyinstaller'
    ],
    entry_points={
        'console_scripts': [
            'anti-keylogger-scan=anti_keylogger_scanner:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: End Users/Desktop',
    ],
)
