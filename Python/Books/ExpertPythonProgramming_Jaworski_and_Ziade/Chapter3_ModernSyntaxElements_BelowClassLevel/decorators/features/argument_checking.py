rpc_info = {}


def xml_rpc(in_=(), out=(type(None,))):
    def _xml_rpc(function):
        # registering the signature
        func_name = function.__name__
        rpc_info[func_name] = (in_, out)

        def _check_types(elements, types):
            """Sub-function that checks the types."""
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements, types))

            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError('arg #%d should be %s' % (index, of_the_right_type))

        def __xml_rpc(*args):
            # checking what goes in
            checkable_args = args[1:] # removing self
            _check_types(checkable_args, in_)

            # running the function
            res = function(*args)

            # checking what hoes out
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out)

            # the function and the type
            # checking succeeded
            return res
        return __xml_rpc
    return _xml_rpc


class RPCView:
    @xml_rpc((int, int))
    def accept_integers(self, int1, int2):
        print('received %d and %d' % (int1, int2))

    @xml_rpc((str,), (int,))
    def accept_phrase(self, phrase):
        print('received %s' % phrase)
        return 12


print(rpc_info)
my = RPCView()
my.accept_integers(1, 2)
