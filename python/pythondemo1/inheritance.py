class myfamily:
    def __init__(self ,grandpa,grandma):
        self.mygrandpa=grandpa
        self.mygrandma=grandma
    def welcome(self):
        print(self.mygrandpa,self.mygrandma)

m=myfamily("boomaiya","pichaiyammal")
m.welcome()

class family(myfamily):
    def __init__(self, grandpa, grandma,dad,mom):
        self.mydad=dad
        self.mymom=mom
        super().__init__(grandpa, grandma)
    def home(self):
        print(self.mydad,self.mymom)

m2=family("boomaiya","pichaiyammal","tamilselvam","suppulaxmi")
m2.home()

class sibling(family):
    def __init__(self, grandpa, grandma, dad, mom,sister,brother,sis2):
        self.mysis1=sister
        self.mybrother=brother
        self.mysis2=sis2
        super().__init__(grandpa, grandma, dad, mom)

    def ffamily(self):
        print("mygrandpa name", self.mygrandpa,"my grandma name",self.mygrandma,"my dad name",self.mydad,"my mom name is",self.mymom,"my 1 sister name",self.mysis1,"my brother name",self.mybrother,"my 2 sister name",self.mysis2)
ff=sibling("boomaiya","pichaiyammal","tamilselvam","suppulaxmi","suganya","ashok","surya")
ff.ffamily()

class my(sibling):
    def __init__(self, grandpa, grandma, dad, mom, sister, brother, sis2,i,she):
        self.myself=i
        self.she=she
        super().__init__(grandpa, grandma, dad, mom, sister, brother, sis2)
    def mfam(self):
        print("my name is ",self.myself,"She name is ",self.she,"mygrandpa name", self.mygrandpa,"my grandma name",self.mygrandma,"my dad name",self.mydad,"my mom name is",self.mymom,"my 1 sister name",self.mysis1,"my brother name",self.mybrother,"my 2 sister name",self.mysis2,)
    
f1=my("boomaiya","pichaiyammal","tamilselvam","suppulaxmi","suganya","ashok","surya","arun","rathi")
f1.mfam()

class shefam(my):
    def __init__(self, grandpa, grandma, dad, mom, sister, brother, sis2, i, she,shedad,shemom,shebro):
        self.myflaw=shedad
        self.mymlaw=shemom
        self.machan=shebro
        super().__init__(grandpa, grandma, dad, mom, sister, brother, sis2, i, she)
    def ff(self):
                print("------------------")
                print("my name is ",self.myself,"She name is ",self.she,"mygrandpa name", self.mygrandpa,"my grandma name",self.mygrandma,"my dad name",self.mydad,"my mom name is",self.mymom,"my father in law name",self.myflaw,"my mother in law ",self.mymlaw,"my machan name",self.machan,"my 1 sister name",self.mysis1,"my 2 sister name",self.mysis2,"my brother name",self.mybrother)
wf=shefam("boomaiya","pichaiyammal","tamilselvam","suppulaxmi","suganya","ashok","surya","arun","rathi","kosalaraman","janaki","ajith")
wf.ff()




    
        
    