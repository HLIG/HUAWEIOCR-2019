import logging
def wait_key(target = None):
    import cv2
    key = cv2.waitKey()& 0xFF
    if target == None:
        return key
    if type(target) == str:
        target = ord(target)
    while key != target:
        key = cv2.waitKey()& 0xFF

    logging.debug('Key Pression caught:%s'%(target))
