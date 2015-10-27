from BaseE import BaseE as BE

class Inherit(BE):
    ext = 'the ext'
    def echo(self):
        print self.server, self.ext

if __name__ == '__main__':
    i = Inherit()
    i.echo()
