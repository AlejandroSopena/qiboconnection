""" Test Environment setting """

import enum
import os

import pytest

from qiboconnection.config import Environment, EnvironmentType, get_environment


def test_environment_constructor():
    """Test Environment class constructor."""
    environment_type = EnvironmentType.DEVELOPMENT

    environment = Environment(environment_type=environment_type)
    assert isinstance(environment, Environment)


def test_environment_constructor_raises_value_error_for_unexpected_environment_types():
    """Test Environment class constructor."""

    class EnvironmentType(str, enum.Enum):
        UNEXPECTED = "unexpected"

    with pytest.raises(ValueError) as e_info:
        _ = Environment(environment_type=EnvironmentType.UNEXPECTED)
    assert e_info.value.args[0] == "Environment Type MUST be 'local', 'staging' or 'development'"


def test_staging_environmemt():
    """Test get_environment() returns a STAGING environment when the QIBO_ENVIRONMENT env variable is set to
    'staging'"""
    os.environ["QIBO_ENVIRONMENT"] = EnvironmentType.STAGING.value
    environment = get_environment()
    assert environment.environment_type == EnvironmentType.STAGING


def test_development_environmemt():
    """Test get_environment() returns a DEVELOPMENT environment when the QIBO_ENVIRONMENT env variable is set to
    'development'"""
    os.environ["QIBO_ENVIRONMENT"] = EnvironmentType.DEVELOPMENT.value
    environment = get_environment()
    assert environment.environment_type == EnvironmentType.DEVELOPMENT


def test_local_environmemt():
    """Test get_environment() returns a LOCAL environment when the QIBO_ENVIRONMENT env variable is set to
    'local'"""
    os.environ["QIBO_ENVIRONMENT"] = EnvironmentType.LOCAL.value
    environment = get_environment()
    assert environment.environment_type == EnvironmentType.LOCAL