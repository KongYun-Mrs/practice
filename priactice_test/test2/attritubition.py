# -*- coding: utf-8 -*-
import geoip2.database


def get_ip_info(ip):
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    attribution = ""
    try:
        print '=====1111111==='
        response = reader.city(ip)
        iso_code = response.country.iso_code
        print '========'
        country = response.country.names['zh-CN']
        print country

        if country:
            attribution = country
        province = response.subdivisions.most_specific.names['zh-CN']
        if province:
            if province == u'闽':
                province = u'福建'
            attribution = attribution + '-' + province
        city = response.city.names["zh-CN"]
        if city:
            attribution = attribution + '-' + city
    except Exception as ex:
        iso_code = ""
    if not attribution:
        attribution = u'内网地址'
    if attribution == u'香港':
        attribution = u'中国' + '-' + attribution
    if attribution.startswith(u'台湾'):
        attribution = u'中国' + '-' + attribution
        index = attribution.rfind('-')
        attribution = attribution[:index]
    if attribution == u'澳门':
        attribution = u'中国' + '-' + attribution
    return attribution, iso_code


if __name__ == '__main__':
    city, _ = get_ip_info('152.89.224.108')
