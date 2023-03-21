import pytest

from api.api_request import restful_booker
from resources.prepare_data import prepare_data
from helpers.models import delete_fields, parametrize_list_of_objects
from serializers.booking import BodyBookingIds


fields_to_test = parametrize_list_of_objects(BodyBookingIds)


@pytest.mark.parametrize('model, path', fields_to_test)
def test_optional_fields_get_bookind_ids(model, path):
    data = prepare_data('get_ids')
    delete_fields('optional', data, model, path)
    get_ids = restful_booker.get_booking_ids(data)

    assert get_ids.status_code == 200, f'{get_ids.text}'
    assert type(get_ids.json()['bookingid']) is list
