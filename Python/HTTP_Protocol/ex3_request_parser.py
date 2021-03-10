class DataInfo:
    def __init__(self, req):
        self.req = req

    def get_method(self):
        return self.req[0].lower().strip()

    def get_func_and_protocol(self):
        return self.req[1].split()

    def get_func(self):
        return self.get_func_and_protocol()[0]

    def get_protocol(self):
        return self.get_func_and_protocol()[1]

    def get_version(self):
        return self.req[2]


def is_path_valid_command(cmd):
    return cmd != 'END'


def does_method_exist(met, path_met):
    return met == path_met


def does_func_exist(fnc, path_fnc):
    return fnc == path_fnc


def is_path_found(check):
    return check


def check_if_given_path_exist():
    for path in paths:
        path_func = path[1]
        path_method = path[2]

        if does_method_exist(method, path_method):
            if does_func_exist(func, path_func):
                return True
    return False


def output_message(status_number, status):
    return f'{protocol}/{version} {status_number} {status}\n' \
           f'Content-Length: {len(status)}\n' \
           f'Content-Type: text/plain\n\n' \
           f'{status}'


paths = list()

while True:
    command = input()

    if not is_path_valid_command(command):
        break

    pth = command
    paths.append(pth.split('/'))

request = input().split('/')

data_info = DataInfo(request)
method = data_info.get_method()
func = data_info.get_func()
protocol = data_info.get_protocol()
version = data_info.get_version()
found = check_if_given_path_exist()

error_status_number = '404'
error_status = 'Not Found'

successful_status_number = '200'
successful_status = 'OK'

message = ""
if found:
    message = output_message(error_status_number, error_status)
else:
    message = output_message(successful_status_number, successful_status)

print(message)
