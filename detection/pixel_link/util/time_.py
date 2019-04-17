def timestamp2str(timestamp): 
    import datetime
    d = datetime.datetime.fromtimestamp(timestamp) 
    str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f") 
    # 2015-08-28 16:43:37.283000' 
    return str1 
