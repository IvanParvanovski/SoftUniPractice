from string import Template

name = 'Ivan'
error = 404

t = Template('Hey $name, there is a $error error!')

print(t.substitute(name=name, error=hex(error)))
