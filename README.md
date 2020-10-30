# BME680

[![Build Status](https://travis-ci.com/cmur2/python-bme680.svg?branch=master)](https://travis-ci.com/cmur2/python-bme680)

https://shop.pimoroni.com/products/bme680

The state-of-the-art BME680 breakout lets you measure temperature, pressure, humidity, and indoor air quality.

## About this Fork

In general this fork tries to improve some details of the [original pimoroni/bme680-python repo](https://github.com/pimoroni/bme680-python):

- use standard unit for pressure measurement (Pascal instead Hectopascal, user can convert if he likes)
- floating point precision for measurement compensations (user has all precision available to choose *based on measurement settings and datasheet* how much is trustable)
- no redundant tweaking of measurement settings after soft reset

## Development

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/bme680-breakout
* Get help - http://forums.pimoroni.com/c/support
