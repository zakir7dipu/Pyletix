import arrow

class DateUtil:
    @staticmethod
    def now(tz='UTC'):
        return arrow.now(tz)

    @staticmethod
    def format(date_val, fmt='YYYY-MM-DD HH:mm:ss'):
        if isinstance(date_val, str):
            date_val = arrow.get(date_val)
        return date_val.format(fmt)

    @staticmethod
    def human_readable(date_val):
        if isinstance(date_val, str):
            date_val = arrow.get(date_val)
        return date_val.humanize()

    @staticmethod
    def parse(date_str):
        return arrow.get(date_str)
