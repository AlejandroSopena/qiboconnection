""" Tests methods for Device """

import json

import pytest

from qiboconnection.devices.device import Device
from qiboconnection.devices.offline_device import OfflineDevice, OfflineDeviceInput
from qiboconnection.devices.quantum_device import QuantumDevice, QuantumDeviceInput
from qiboconnection.devices.quantum_device_calibration_details import (
    CalibrationDetails,
    CalibrationDetailsInput,
)
from qiboconnection.devices.quantum_device_characteristics import (
    QuantumDeviceCharacteristics,
    QuantumDeviceCharacteristicsInput,
)
from qiboconnection.devices.simulator_device import SimulatorDevice
from qiboconnection.devices.simulator_device_characteristics import (
    SimulatorDeviceCharacteristics,
)
from qiboconnection.devices.util import (
    create_device,
    is_offline_device_input,
    is_quantum_device_input,
)
from qiboconnection.typings.device import (
    DeviceInput,
    DeviceStatus,
    SimulatorDeviceCharacteristicsInput,
    SimulatorDeviceInput,
)

from .data import (
    device_inputs,
    quantum_device_characteristics_inputs,
    quantum_device_inputs,
    simulator_device_characteristics_inputs,
    simulator_device_inputs,
)


@pytest.mark.parametrize("device_input", device_inputs)
def test_device_constructor(device_input: DeviceInput):
    device = Device(device_input=device_input)
    assert isinstance(device, Device)


@pytest.mark.parametrize("device_input", device_inputs)
def test_device_string_representation(device_input: DeviceInput):
    device = Device(device_input=device_input)

    assert (
        device.__str__()
        == f"<Device: device_id={device._device_id}, device_name='{device._device_name}', status='{device._status.value}', channel_id=None>"
    )


@pytest.mark.parametrize("device_input", device_inputs)
def test_device_dict_representation(device_input: DeviceInput):
    device = Device(device_input=device_input)
    expected_dict = {
        "device_id": device._device_id,
        "device_name": device._device_name,
        "status": device._status.value,
    }
    assert device.__dict__ == expected_dict


@pytest.mark.parametrize("device_input", device_inputs)
def test_device_json_representation(device_input: DeviceInput):
    device = Device(device_input=device_input)
    expected_dict = {
        "device_id": device._device_id,
        "device_name": device._device_name,
        "status": device._status.value,
    }
    assert device.toJSON() == json.dumps(expected_dict, indent=2)


@pytest.mark.parametrize("simulator_device_input", simulator_device_inputs)
def test_simulator_device_constructor(simulator_device_input: SimulatorDeviceInput):
    assert isinstance(simulator_device_input, SimulatorDeviceInput)
    device = SimulatorDevice(device_input=simulator_device_input)
    assert isinstance(device, SimulatorDevice)


@pytest.mark.parametrize("simulator_device_input", simulator_device_inputs)
def test_simulator_device_dict_representation(
    simulator_device_input: SimulatorDeviceInput,
):
    device = SimulatorDevice(device_input=simulator_device_input)
    expected_dict = {
        "device_id": device._device_id,
        "device_name": device._device_name,
        "status": device._status.value,
    }
    if device._characteristics:
        expected_dict |= {"characteristics": device._characteristics.__dict__}
    assert device.__dict__ == expected_dict


@pytest.mark.parametrize("simulator_device_input", simulator_device_inputs)
def test_simulator_device_json_representation(
    simulator_device_input: SimulatorDeviceInput,
):
    device = SimulatorDevice(device_input=simulator_device_input)
    expected_dict = {
        "device_id": device._device_id,
        "device_name": device._device_name,
        "status": device._status.value,
    }
    if device._characteristics:
        expected_dict |= {"characteristics": device._characteristics.__dict__}
    assert device.toJSON() == json.dumps(expected_dict, indent=2)


@pytest.mark.parametrize("simulator_device_characteristics_input", simulator_device_characteristics_inputs)
def test_simulator_device_characteristics_constructor(
    simulator_device_characteristics_input: SimulatorDeviceCharacteristicsInput,
):
    characteristics = SimulatorDeviceCharacteristics(characteristics_input=simulator_device_characteristics_input)
    assert isinstance(characteristics, SimulatorDeviceCharacteristics)


@pytest.mark.parametrize("simulator_device_characteristics_input", simulator_device_characteristics_inputs)
def test_simulator_device_characteristics_json_representation(
    simulator_device_characteristics_input: SimulatorDeviceCharacteristicsInput,
):
    characteristics = SimulatorDeviceCharacteristics(characteristics_input=simulator_device_characteristics_input)
    expected_dict = {
        "type": characteristics._type.value,
        "cpu": characteristics._cpu,
        "gpu": characteristics._gpu,
        "os": characteristics._os,
        "kernel": characteristics._kernel,
        "ram": characteristics._ram,
    }
    assert characteristics.toJSON() == json.dumps(expected_dict, indent=2)


@pytest.mark.parametrize("quantum_device_input", quantum_device_inputs)
def test_quantum_device_constructor(quantum_device_input: QuantumDeviceInput):
    assert isinstance(quantum_device_input, QuantumDeviceInput)
    device = QuantumDevice(device_input=quantum_device_input)
    assert isinstance(device, QuantumDevice)


@pytest.mark.parametrize("quantum_device_input", quantum_device_inputs)
def test_quantum_device_dict_representation(
    quantum_device_input: QuantumDeviceInput,
):
    device = QuantumDevice(device_input=quantum_device_input)
    expected_dict = {
        "device_id": device._device_id,
        "device_name": device._device_name,
        "status": device._status.value,
    }
    if device._characteristics:
        expected_dict |= {"characteristics": device._characteristics.__dict__}
    if device._calibration_details:
        expected_dict |= {"calibration_details": device._calibration_details.__dict__}
    if device._last_calibration_time:
        expected_dict |= {"last_calibration_time": device._last_calibration_time.__str__()}
    assert device.__dict__ == expected_dict


@pytest.mark.parametrize("quantum_device_characteristics_input", quantum_device_characteristics_inputs)
def test_quantum_device_characteristics_constructor(
    quantum_device_characteristics_input: QuantumDeviceCharacteristicsInput,
):
    characteristics = QuantumDeviceCharacteristics(characteristics_input=quantum_device_characteristics_input)
    assert isinstance(characteristics, QuantumDeviceCharacteristics)


@pytest.mark.parametrize("quantum_device_characteristics_input", quantum_device_characteristics_inputs)
def test_quantum_device_characteristics_json_representation(
    quantum_device_characteristics_input: QuantumDeviceCharacteristicsInput,
):
    characteristics = QuantumDeviceCharacteristics(characteristics_input=quantum_device_characteristics_input)
    expected_dict = {
        "type": characteristics._type.value,
    }
    assert characteristics.toJSON() == json.dumps(expected_dict, indent=2)


@pytest.mark.parametrize("device_input", device_inputs)
def test_offline_device_constructor(device_input: DeviceInput):
    offline_device_input_dict = device_input.__dict__.copy()
    offline_device_input_dict["status"] = DeviceStatus.OFFLINE.value

    offline_device_input = OfflineDeviceInput(**offline_device_input_dict)
    device = OfflineDevice(device_input=offline_device_input)
    assert isinstance(device, OfflineDevice)


@pytest.mark.parametrize("device_input", device_inputs)
def test_is_offline_device_input(device_input: DeviceInput):
    device_input_dict = device_input.__dict__.copy()
    device_input_dict["status"] = DeviceStatus.OFFLINE.value

    offline_device_input = OfflineDeviceInput(**device_input_dict)
    assert is_offline_device_input(device_input=offline_device_input.__dict__)


@pytest.mark.parametrize("device_input", device_inputs)
def test_is_offline_device_input_rises_valueerror(device_input: DeviceInput):
    device_input_dict = device_input.__dict__.copy()
    device_input_dict["status"] = None

    offline_device_input = OfflineDeviceInput(**device_input_dict)
    with pytest.raises(ValueError) as e_info:
        _ = is_offline_device_input(device_input=offline_device_input.__dict__)

    assert e_info.value.args[0] == "'status' missing in device_input keys"


@pytest.mark.parametrize("quantum_device_input", quantum_device_inputs)
def test_is_quantum_device_input(quantum_device_input: QuantumDeviceInput):
    assert is_quantum_device_input(device_input=quantum_device_input.__dict__)


@pytest.mark.parametrize("device_input", device_inputs)
def test_create_offline_device(device_input: DeviceInput):
    device_input_dict = device_input.__dict__.copy()
    device_input_dict["status"] = DeviceStatus.OFFLINE.value

    offline_device_input = OfflineDeviceInput(**device_input_dict)
    device = create_device(device_input=offline_device_input.__dict__)
    assert isinstance(device, OfflineDevice)


@pytest.mark.parametrize("simulator_device_input", simulator_device_inputs)
def test_create_simulator_device(simulator_device_input: SimulatorDeviceInput):
    """Test whether the utils function create_device() decides to properly create a simulator device when it meets
    a dictionary that has the properties of a simulator."""
    stripped_down_simulator_device_input = simulator_device_input.__dict__.copy()

    stripped_down_simulator_device_input["characteristics"] = stripped_down_simulator_device_input[
        "_characteristics"
    ].__dict__
    del stripped_down_simulator_device_input["_characteristics"]

    device = create_device(device_input=stripped_down_simulator_device_input)
    assert isinstance(device, SimulatorDevice)


@pytest.mark.parametrize("quantum_device_input", quantum_device_inputs)
def test_create_quantum_device(quantum_device_input: QuantumDeviceInput):
    """Test whether the utils function create_device() decides to properly create a quantum devices when it meets
    a dictionary that has the properties of a quantum device."""
    stripped_down_quantum_device_input = quantum_device_input.__dict__.copy()

    stripped_down_quantum_device_input["characteristics"] = stripped_down_quantum_device_input[
        "_characteristics"
    ].__dict__
    del stripped_down_quantum_device_input["_characteristics"]

    stripped_down_quantum_device_input["calibration_details"] = stripped_down_quantum_device_input[
        "_calibration_details"
    ].__dict__
    del stripped_down_quantum_device_input["_calibration_details"]

    device = create_device(device_input=stripped_down_quantum_device_input)
    assert isinstance(device, QuantumDevice)
