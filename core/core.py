import datetime
from .enums.ProductType import ProductType
from .enums.Weekday import Weekday
from .classes.AvailableDeliveryDate import AvailableDeliveryDate

def get_delivery_dates(postal_code, products):
    """The output of this function should return a list of available delivery dates for the upcoming 14 days. """
    datetime_now = datetime.datetime.now()
    upcoming_dates = [datetime_now + datetime.timedelta(days = x) for x in range(14)]
    valid_delivery_dates = []

    for product in products:
        product_delivery_days = [x for x in upcoming_dates if x.strftime("%A") in product.delivery_days]

        match product.type:
            case ProductType.NORMAL:
                    valid_delivery_dates.extend(_get_valid_days_in_advance(product_delivery_days, datetime_now, product.days_in_advance))
            case ProductType.EXTERNAL:
                    valid_delivery_dates.extend(_get_valid_external_product(product_delivery_days, datetime_now))
            case ProductType.TEMPORARY:
                    valid_delivery_dates.extend(_get_valid_temporary_product(datetime_now, product.delivery_days))
            case _:
                    raise Exception(f"Product with id: {product.id} has no type.")
             
    delivery_dates = _revamp_delivery_dates(postal_code, valid_delivery_dates, datetime_now)
    return delivery_dates

def _get_valid_days_in_advance(product_delivery_days, datetime_now, days_in_advance):
    valid_delivery_dates = [x for x in product_delivery_days if (x - datetime_now).days > days_in_advance]
    return valid_delivery_dates

def _get_valid_external_product(product_delivery_days, datetime_now):
    external_product_days_in_advance = 5
    valid_delivery_dates = _get_valid_days_in_advance(product_delivery_days, datetime_now, external_product_days_in_advance)
    return valid_delivery_dates

def _get_valid_temporary_product(datetime_now, delivery_days):
    weekday = datetime_now.weekday()
    days_left_of_the_week = 7 - weekday
    dates_left = [datetime_now + datetime.timedelta(days = x) for x in range(days_left_of_the_week)]
    valid_delivery_dates = [x for x in dates_left if x.strftime("%A") in delivery_days]
    return valid_delivery_dates

def _revamp_delivery_dates(postal_code, delivery_dates, datetime_now):
    available_delivery_dates = [AvailableDeliveryDate(postal_code, x, _is_green_day(x)) for x in delivery_dates]      
    sorted_available_delivery_dates = _sort_delivery_dates(available_delivery_dates, datetime_now)
    return sorted_available_delivery_dates

def _is_green_day(delivery_date):
    green_day = Weekday.WEDNESDAY == delivery_date.strftime("%A")
    return green_day

def _sort_delivery_dates(delivery_dates, datetime_now):
    delivery_dates.sort(key = lambda x: (x.delivery_date, ((x.delivery_date - datetime_now).days < 4 and x.is_green_delivery)), reverse = False)
    return delivery_dates