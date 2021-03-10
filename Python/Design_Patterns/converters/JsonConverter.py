from json import loads

BUFFER_SIZE = 1 << 10


def get_str(bytes):
    try:
        return bytes.decode()
    except:
        return bytes


class JsonConverter:
    def convert_from_stream(self, stream):
        stream.seek(0)
        parts = []

        while True:
            part = stream.read(BUFFER_SIZE)
            if not part:
                break
            parts.append(part)

        json = ''.join(str(x) for x in parts)
        return loads(json)
