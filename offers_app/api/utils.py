def filter_creator_id(request, queryset):
    """
    Filters the queryset by user_id, the parameter being used is creator_id.
    """
    creator_id_param = request.query_params.get('creator_id', None)
    if creator_id_param is not None:
        queryset = queryset.filter(user_id=creator_id_param)
    return queryset

def filter_max_delivery_time(request, queryset):
    """
    Filters the queryset by min_delivery_time that is less or equal to the max_delivery_time parameter.
    """
    max_delivery_time_param = request.query_params.get('max_delivery_time', None)
    if max_delivery_time_param is not None:
        queryset = queryset.filter(min_delivery_time__lte=max_delivery_time_param)
    return queryset

def return_offer_data(user_id):
    """
    Returns offer data for testing purposes.
    """
    offer_data = {'user': user_id,
                  'title': 'Test offer',
                  'description': 'Test description',
                  'min_price': 1.00,
                  'min_delivery_time': 1,
                  'details': [{
                                'title': 'Basic Package',
                                'revisions': 1,
                                'delivery_time_in_days': 2,
                                'price': 1.00,
                                'features': 'Feature1,Feature2',
                                'offer_type': 'basic',
                                },
                                {
                                'title': 'Standard Package',
                                'revisions': 2,
                                'delivery_time_in_days': 2,
                                'price': 1.00,
                                'features': 'Feature1,Feature2',
                                'offer_type': 'standard',
                                },
                                {
                                'title': 'Premium Package',
                                'revisions': 3,
                                'delivery_time_in_days': 3,
                                'price': 1.00,
                                'features': 'Feature1,Feature2',
                                'offer_type': 'premium',
                                }]
                    }
    return offer_data