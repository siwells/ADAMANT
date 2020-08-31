import json

from helpers.Constants import EMPTY


class StringParser:
    @staticmethod
    def between(data, str_before, str_after) -> str:
        # Find and validate before-part.
        pos_a = data.find(str_before)
        if pos_a == -1:
            return ""
        # Find and validate after part.
        pos_b = data.find(str_after, pos_a)
        if pos_b == -1:
            return ""
        # Return middle part.
        adjusted_pos_a = pos_a + len(str_before)
        if adjusted_pos_a >= pos_b:
            return ""
        value = data[adjusted_pos_a:pos_b]
        return str.strip(value)

    @staticmethod
    def before(data, before):
        # Find first part and return slice before it.
        pos_a = data.find(before)
        if pos_a == -1:
            return ""
        return data[0:pos_a]

    @staticmethod
    def after(data, after):
        # Find and validate first part.
        pos_a = data.rfind(after)
        if pos_a == -1:
            return ""
        # Returns chars after the found string.
        adjusted_pos_a = pos_a + len(after)
        if adjusted_pos_a >= len(data):
            return ""
        return data[adjusted_pos_a:]

    @staticmethod
    def is_json(json_str: str = EMPTY):
        json_str = StringParser.dict_to_string(json_str)
        try:
            json.loads(str(json_str))
        except ValueError:
            return False
        return True

    @staticmethod
    def dict_to_string(json_str: str = EMPTY):
        if isinstance(json_str, dict):
            json_str = json.dumps(json_str)
        return json_str
