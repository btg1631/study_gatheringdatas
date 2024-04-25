from googlestore import get_data

data_dict ={
    'tripadvisor' : 'https://play.google.com/store/apps/details?id=com.tripadvisor.tripadvisor'
    , 'triple' : 'https://play.google.com/store/apps/details?id=com.titicacacorp.triple'
    , 'myrealtrip' : 'https://play.google.com/store/apps/details?id=com.mrt.ducati'
    , 'skyscanner' : 'https://play.google.com/store/apps/details?id=net.skyscanner.android.main'
}

for k,v in data_dict.items():
    get_data(k,v)
    pass