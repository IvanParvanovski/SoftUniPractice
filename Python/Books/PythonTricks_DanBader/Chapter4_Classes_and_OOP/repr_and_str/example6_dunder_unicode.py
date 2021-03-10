# class Car(object):
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#
#     def __repr__(self):
#         return '{}({!r}, {!r})'.format(
#             self.__class__.__name__,
#             self.color, self.mileage
#         )
#
#     def __unicode__(self):
#         return u'a {self.color} car'.format(self=self)
#
#     def __str__(self):
#         return unicode(self).encode('utf-8')
