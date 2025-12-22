from logger import logging

def add(a,b):
    logging.debug("Addition of two numbers is taking place")
    return a+b

logging.debug("Addition function is called")
add(10,10)