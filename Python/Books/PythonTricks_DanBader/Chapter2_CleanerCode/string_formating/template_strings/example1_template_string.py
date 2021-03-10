from string import Template
name = 'Ivan'
t = Template('Hey, $name!')
print(t.substitute(name=name))
