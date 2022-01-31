class Mama:
    def says(self):
        print('do your homework')

#
# class Sister(Mama):
#     def says(self):
#         super(Sister, self).says()
#         print('and clean your bedroom')


class Sister(Mama):
    def says(self):
        super().says()
        print('and clean your bedroom')

        
anita = Sister()
super(anita.__class__, anita).says()
