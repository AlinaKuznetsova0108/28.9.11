import pytest

from api.api_request import restful_booker
from resources.prepare_data import prepare_data
from helpers.general import get_missing_fields
from helpers.models import delete_fields, get_required_fields_paths, parametrize_list_of_objects
from serializers.booking import *


fields_to_test_1 = parametrize_list_of_objects(BodyToken, required=True)
fields_to_test_2 = parametrize_list_of_objects(BodyCreateBooking, required=True)
fields_to_test_3 = parametrize_list_of_objects(ParamGetBooking, required=True)


@pytest.mark.parametrize('model, path', fields_to_test_1)
def test_required_fields_get_token(model, path):

    data = prepare_data('create_token')
    fields_to_delete = get_required_fields_paths(model, path)
    delete_fields('required', data, model, path)
    create_token = restful_booker.create_token(data)

    assert create_token.status_code == 400, f'{create_token.text}'
    missing_fields = get_missing_fields(fields_to_delete, create_token.json()['detail'])
    assert len(missing_fields) == 0, missing_fields


@pytest.mark.parametrize('model, path', fields_to_test_2)
def test_required_fields_get_token(model, path):

    data = prepare_data('create_booking')
    fields_to_delete = get_required_fields_paths(model, path)
    delete_fields('required', data, model, path)
    create_booking = restful_booker.create_booking(data)

    assert create_booking.status_code == 400, f'{create_booking.text}'
    missing_fields = get_missing_fields(fields_to_delete, create_booking.json()['detail'])
    assert len(missing_fields) == 0, missing_fields


@pytest.mark.parametrize('model, path', fields_to_test_2)
def test_required_fields_get_token(model, path):

    data = prepare_data('get_booking')
    fields_to_delete = get_required_fields_paths(model, path)
    delete_fields('required', data, model, path)
    get_booking = restful_booker.get_booking(data)
    assert get_booking.status_code == 400, f'{get_booking.text}'
    missing_fields = get_missing_fields(fields_to_delete, get_booking.json()['detail'])
    assert len(missing_fields) == 0, missing_fields
