import os
added=[]
absent=[]
d=0
for dir in sorted(os.listdir()):
    if os.path.isdir(dir):
        current=[]
        added.append("#"+dir)
        a=""
        c=e=0
#change ZOMBIETYPES.json in a repeating path to search in folders/repeating path
        for b in open(os.path.join(dir,"ZOMBIETYPES.json"),'r').readlines():
#depth x containes { x
#            if "{" in b:
#                c+=b.count("{")
#depth x containes } x-1
            if "}" in b:
                c-=b.count("}")
#depth x containes [ x
#            if "[" in b:
#                e+=b.count("[")
#depth x containes ] x-1
            if "]" in b:
                e-=b.count("]")
            if c==2 and e==2:
                a+=b[17:-2]+"	"
                if a.count("	")>d:
                    d=a.count("	")
            elif a != "":
                current.append(a)
                if not a in added:
                    added.append(a)
                a=""
#depth x containes { x+1
            if "{" in b:
                c+=b.count("{")
#depth x containes } x
#            if "}" in b:
#                c-=b.count("}")
#depth x containes [ x+1
            if "[" in b:
                e+=b.count("[")
#depth x containes ] x
#            if "]" in b:
#                e-=b.count("]")
        for b in added:
            if not(b in current or "#" in b):
                absent.append(b)
        absent.append("#"+dir)
g=open("t.tsv","w")
for a in added:
    if "#" in a:
        e+=1
        #g=open("t.tsv","a")
        if e==1:
            g.write(d*"	")
            for b in absent:
                if "#" in b:
                    g.write(b[1:]+'	')
    else:
        c=1
        g.write('''
'''+a[:-1]+(d-a.count("  "))*"  ")
        f="X"
        for b in absent:
            if a==b or e>c:
                f=" "
            if "#" in b:
                c+=1
                g.write('	'+f)
                f="X"
g.close()
os.system("open -a Microsoft\ Excel t.tsv")
