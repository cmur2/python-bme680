import pytest
import bme680


def test_calc_temperature(smbus, calibration):
    """Validate temperature calculation against mock calibration data."""
    sensor = bme680.BME680()
    sensor.calibration_data = calibration
    assert sensor._calc_temperature(501240) == pytest.approx(2669.81, 0.01)
    assert sensor.calibration_data.t_fine == pytest.approx(136668.78, 0.01)


def test_calc_pressure(smbus, calibration):
    """Validate pressure calculation against mock calibration data."""
    sensor = bme680.BME680()
    sensor.calibration_data = calibration
    sensor._calc_temperature(501240)
    assert sensor._calc_pressure(353485) == pytest.approx(98716.92, 0.01)


def test_calc_humidity(smbus, calibration):
    """Validate humidity calculation against mock calibration data."""
    sensor = bme680.BME680()
    sensor.calibration_data = calibration
    sensor._calc_temperature(501240)
    assert sensor._calc_humidity(19019) == pytest.approx(42410.28, 0.01)


def test_calc_gas_resistance(smbus, calibration):
    """Validate gas calculation against mock calibration data."""
    sensor = bme680.BME680()
    sensor.calibration_data = calibration
    assert int(sensor._calc_gas_resistance(0, 0)) == 12946860


def test_temp_offset(smbus, calibration):
    """Validate temperature calculation with offset against mock calibration data."""
    sensor = bme680.BME680()
    sensor.calibration_data = calibration
    sensor.set_temp_offset(1.99)
    assert sensor._calc_temperature(501240) == pytest.approx(2868.30, 0.01)
    assert sensor.calibration_data.t_fine == pytest.approx(146831.78, 0.01)
