function requestValidator(obj) {
    const uriRegexPattern = /^[\w.\d]+$/;
    const messageRegexPattern = /[<>\\&'"]/;
    const errorMessage = 'Invalid request header: Invalid ';

    function isURIValid(uri) {
        if (uri == undefined) {
            return false;
        }

        return uri.match(uriRegexPattern) ? true : false;
    }

    function isMessageValid(message) {
        if (message == undefined) {
            return false;
        }

        return message.match(messageRegexPattern) ? false : true;
    }

    const possibleMethods = ['GET', 'POST', 'DELETE', 'CONNECT'];
    const possibleVersions = ['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0'];

    if (Object.entries(obj).length == 0) {
        return obj;
    }

    if (!possibleMethods.includes(obj.method)) {
        throw new Error(errorMessage + 'Method');
    } else if (!isURIValid(obj.uri)) {
        throw new Error(errorMessage + 'URI');
    } else if (!isMessageValid(obj.message)) {
        throw new Error(errorMessage + 'Message');
    } else if (!possibleVersions.includes(obj.version)) {
        throw new Error(errorMessage + 'Version');
    }

    return obj;
}

module.exports = {
    requestValidator,
};
