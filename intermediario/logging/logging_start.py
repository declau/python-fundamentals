import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%m/%d/%Y %H:%M:%S",
# )

# import helper


logger = logging.getLogger(__name__)

# create handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

# level and format strings

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)


logger.addHandler(stream_h)
logger.addHandler(file_h)

logging.warning("This is a warning")
logging.error("This is a error")

# logging.debug("This is debug message!")
# logging.info("This is a info message!")
# logging.critical("This is a critical message!")
