
class Frame:
    def __init__(self,V):
        self.type = self.__class__.__name__.lower()
        self.val  = V
        self.slot = {}
        self.nest = []
        
    def __repr__(self):
        return self.dump()
    def dump(self,depth=0,prefix=''):
        tree = self.pad(depth) + self.head(prefix)
        if not depth: Frame.dumped = []
        if self in Frame.dumped: return tree + ' _/'
        else: Frame.dumped.append(self)
        for i in self.slot:
            tree += self.slot[i].dump(depth+1,i+' = ')
        for j in self.nest:
            tree += j.dump(depth+1)
        return tree
    def head(self,prefix=''):
        return '%s<%s:%s> @%x' % (prefix,self.type,self.val,id(self))
    def pad(self,n):
        return '\n' + '\t' * n
            
    def __setitem__(self,key,that):
        self.slot[key] = that ; return self
    def __getitem__(self,key):
        return self.slot[key]
    def __floordiv__(self,that):
        self.nest.append(that)
    def __lshift__(self,that):
        self.slot[that.val] = that ; return self
        
class Primitive(Frame): pass

class String(Primitive): pass
class Symbol(Primitive): pass

class IO(Frame): pass

class File(IO): pass
class Dir(IO): pass

class Meta(Frame): pass

class Module(Meta): pass

class Class(Meta): pass
class Func(Meta): pass
class Method(Func): pass
class Var(Meta): pass
class Field(Var): pass

module      = Module('P')
dir         = Dir('~/' + module.val)    ; module // dir
project     = File('.project')          ; dir // project
pydev       = File('.pydevproject')     ; dir // pydev
gitignore   = File('.gitignore')        ; dir // gitignore
makefile    = File('Makefile')          ; dir // makefile

readme      = File('README.md')         ; module // readme  ; readme // module
title   = String('homoiconic metaPython')                   ; readme // title
author  = String('Dmitry Ponyatov <<dponyatov@gmail.com>>') ; readme // author
license = String('CC BY-NC-ND')                             ; readme // license
github  = String('https://github.com/ponyatov/P')           ; readme // github

py          = File('meta.py')           ; module // py
settings    = Dir('.settings')          ; dir // settings
settings    // File('org.eclipse.core.runtime.prefs')
settings    // File('org.eclipse.core.resources.prefs')

print module
