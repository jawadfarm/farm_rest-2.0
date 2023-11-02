import os
import requests
import bs4
import urllib.parse
import time
def infile():
    print("back=bback")
    namefile=input("name file or new file=name file(.txt):")
    fv=open(f"{namefile}","a")
    if namefile == "bback":
        ur()
    else:
        urt = input("url:")
    u = requests.get(f"{urt}")
    x = 0
    for i in range(3):
        x += 1
        print(x)
        time.sleep(1)
    print("farm_harvest\n________\n(rest)")
    time.sleep(2)
    fv.write(f"{u}")
    print(f"{u}\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"[{u.cookies}]\n\n\n\n\n-____________________________________________________________________________________________________________________________________________________________________________-")
    fv.write(f"\n\ncookie:{u.cookies}")
    print(f"{u.content}\n\n\n\n\n\n\n\n\n")
    fv.write(f"\n\n{u.content}")
    print(" 0                         0\n-___________________________-")
    input("")
    print(
        f"[{u.cookies}]\n\n\n\n\n-____________________________________________________________________________________________________________________________________________________________________________-")

    html = u.text
    fv.write(f"\n\n{html}")
    html1 = bs4.BeautifulSoup(html, "html.parser")
    fv.write(f"{html1}")
    print(f"{html1}\n\n\n\n\n\n\n\n\n\n\n\n\n")
    html75 = html1.findAll("html", attrs={"": ""})
    fv.write(f"\n\n\nhtml:{html75}")
    print("html text:")
    if html75:
        for html73 in html75:
            print(f"{html73.text}\n\n")
        fv.write(f"\n\n\nhtml:{html73}")
        fv.write(f"\n\nhtml txt:{html73.text}")
    else:
        print("---------\nNone\n--------")
    scrip = html1.findAll("script", attrs={"": ""})
    fv.write(f"\n\n\nscript:{scrip}")
    print("script text:")
    if scrip:
        for scrip1 in scrip:
            print(f"{scrip1.text}\n\n")
        fv.write(f"\n\nscript file{scrip1}")
        fv.write(f"\n\nscript txt{scrip1.text}")
    else:
        print("---------\nNone\n--------")
    links = html1.find_all("a")
    print("links:")
    response = requests.get(urt)

    if response.status_code == 200 :
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a", href=True)

        for link in links:
            full_link = urllib.parse.urljoin(urt, link["href"])
            fv.write(f"\n\nlink: {full_link}")
            print(full_link)
        fv.close()
        ur()
    else:
        print("False")
        print("\n\n\n\n")
        print(f"for({u.url})\n")
        fv.write(f"\nfor:{u.url}")
        a = input("Do you want to search for something specific? yes or no:")
        if a == "نعم" or a == "yes" or a == "يب":
            rt = input("Type:")
            nm = input("Parameter:")
            h = input(f"{nm}:")
            html56 = html1.find(f"{rt}", attrs={f"{nm}": f"{h}"})
            if html56 :
                fv.write(f"\n\n{html56}")
            else:
                print(html56)
                html46 = html1.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                r = input("text or no:")
                if r == "text" or r == "txt":
                    print(f"{html46}\n\n\n")
                    if html46:
                        fv.write(f"\n\nall you:{html46}")
                    for html43 in html46:
                        print(html43.text)
                    print(len(html46))
                    fv.write(f"\n\n{html43}")
                    sr = bs4.BeautifulSoup(html, "lxml")
                    se = input("num:")
                    sea = int(se)
                    html47 = sr.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                    print("\n")
                    print(html47[sea].text)
                    fv.write(f"\n\n{html47[sea].text}")
                    print(":farm harvest:")
                    fv.close()
                    ur()
                elif r == 'no':
                    fv.write(f"\n\n{html46}")
                    print(f"{html46}\n\n\n")
                    for html44 in html46:
                        print(html44)
                    print(len(html46))
                    fv.write(f"\n\n{html44}")
                    sr = bs4.BeautifulSoup(html, "lxml")
                    se = input("num:")
                    sea = int(se)
                    html47 = sr.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                    print(html47[sea])
                    fv.write(f"\n\n{html47[sea]}")
                    print(":farm harvest:")
                    fv.close()
                    ur()
                else:
                    a()
        else:
            fv.close()
            ur()
def redfile():
    f = input("namefile:")
    rd = open(f"{f}", "r")
    fv = rd.read()
    print(fv)
    rd.close()
def opennewfile():
    o=open("farmurlback.txt","a")
    o.close()
def closefile():
    c=open("farmurlback.txt")
    c.close()
def clearfile():
    c=open("farmurlback.txt","w")
    c.close()
def ea():
    ex=input("you want exit?:")
    if ex=="yes":
        exit("farm_harvest")
    else:
        l()
def read():
    rd=open("farmurlback.txt","r")
    s=rd.readlines()
    print(len(s),s)
    rd.close()
def a():
    print("(|farm<>harvest|)")
    print("""||||||||||||\n|____2.0____|\n||||||||||||""")
    print("robot 2.?")
    ur()
def ur():
    d=open("farmurlback.txt","a")
    time.sleep(1)
    urt=input("url or mod:")
    if urt == "exit":
        ea()
    elif urt == "help":
        print("exit = exit\nurl = scan\nin file or inf\nclose file or clof\nback =back url\nclear file or clf\nopen new file or of\nread file or rf == read file")
        ur()
    elif urt =="clear":
        print(os.system("clear"))
        print ( "(|farm<>harvest|)" )
        print ( """||||||||||||\n|____1.8___|""" )
        print ( "robot 2.?" )
        ur()
    elif urt =="claer":
        print("*clear")
        ur()
    elif urt=="close file" or urt=="clof":
        closefile()
        ur()
    elif urt=="clf" or urt=="clear file":
        clearfile()
        ur()
    elif urt=="open file" or urt=="opennewfile" or urt=="of":
        opennewfile()
        ur()
    elif urt=="in file" or urt=="inf":
        infile()
        ur()
    elif urt == "read file" or urt=="rf":
        redfile()
        ur()
    elif urt=="back":
        d=open("farmurlback.txt","r")
        e=d.readlines()
        r=d.read()
        lr=len(r)
        print(r)
        if lr==None:
            print("not find url")
            ur()

        else:
            f = 0
            for i in e:
                print(f"{f}:{i}")
                f += 1

            sd = input("num:")
            sdd=int(sd)
            cf=e[sdd]
            print(cf)

            u = requests.get(f"{cf}")
            x = 0
            for i in range(3):
                x += 1
                print(x)
                time.sleep(1)
            print("farm_harvest\n________\nrest")
            time.sleep(2)
            r = u.headers
            for k in r:
                print(f"\n{k}:{r[k]}")
            print(f"{u}\n\n\n\n\n\n\n\n\n\n\n\n\n")
            d.close()
            print(
                f"[{u.cookies}]\n\n\n\n\n-____________________________________________________________________________________________________________________________________________________________________________-")
            print(f"{u.content}\n\n\n\n\n\n\n\n\n")
            print(" 0                         0\n-___________________________-")
            input("")
            print(
                f"[{u.cookies}]\n\n\n\n\n-____________________________________________________________________________________________________________________________________________________________________________-")

            html = u.text
            html1 = bs4.BeautifulSoup(html, "html.parser")
            print(f"{html1}\n\n\n\n\n\n\n\n\n\n\n\n\n")
            html75 = html1.findAll("html", attrs={"": ""})
            print("html text:")
            if html75:
                for html75 in html75:
                    print(f"{html75.text}\n\n")
            else:
                print("---------\nNone\n--------")
            scrip = html1.findAll("script", attrs={"": ""})
            print("script text:")
            if scrip:
                for scrip in scrip:
                    print(f"{scrip.text}\n\n")
            else:
                print("---------\nNone\n--------")
            links = html1.find_all("a")
            print("links:")
            response = requests.get(cf)

            if response.status_code == 200:
                soup = bs4.BeautifulSoup(response.text, "html.parser")

                links = soup.find_all("a", href=True)

                for link in links:
                    full_link = urllib.parse.urljoin(urt, link["href"])
                    print(full_link)
            else:
                print("False")
                print("\n\n\n\n")
                print(f"for({u.url})\n")
                a = input("Do you want to search for something specific? yes or no:")
                if a == "نعم" or a == "yes" or a == "يب":
                    rt = input("Type:")
                    nm = input("Parameter:")
                    h = input(f"{nm}:")
                    html56 = html1.find(f"{rt}", attrs={f"{nm}": f"{h}"})
                    print(html56)
                    html46 = html1.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                    r = input("text or no:")
                    if r == "text" or r == "txt":
                        print(f"{html46}\n\n\n")
                        for html46 in html46:
                            print(html46.text)
                        print(len(html46))
                        sr = bs4.BeautifulSoup(html, "lxml")
                        se = input("num:")
                        sea = int(se)
                        html47 = sr.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                        print("\n")
                        print(html47[sea].text)
                        print(":farm harvest:")
                        ur()
                    elif r == 'no':
                        print(f"{html46}\n\n\n")
                        for html46 in html46:
                            print(html46)
                        print(len(html46))
                        sr = bs4.BeautifulSoup(html, "lxml")
                        se = input("num:")
                        sea = int(se)
                        html47 = sr.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                        print(html47[sea])
                        print(":farm harvest:")
                        ur()
                    else:
                        a()
                else:
                    a()
            for link in links:
                href = link.get("href")
                if href:
                    print(href)
            print("\n\n\n")
            if response.status_code == 100:
                soupf = bs4.BeautifulSoup(response.text, "html.parser")

                script_tags = soupf.find_all("script")

                for script in script_tags:
                    script_text = script.get_text()
                    links = soupf.findall(r'href=["\'](http[s]?://.*?)["\']', script_text)

                    if links:
                        print(" script url:")
                        for link in links:
                            print(link)
            else:
                print("False")
                print("\n\n\n\n")
                print(f"for({u.url})\n")
                a = input("Do you want to search for something specific? yes or no:")
                if a == "نعم" or a == "yes" or a == "يب":
                    rt = input("Type:")
                    nm = input("Parameter:")
                    h = input(f"{nm}:")
                    html56 = html1.find(f"{rt}", attrs={f"{nm}": f"{h}"})
                    print(html56)
                    html46 = html1.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                    r = input("text or no:")
                    if r == "text" or r == "txt":
                        print(f"{html46}\n\n\n")
                        for html46 in html46:
                            print(html46.text)
                        print(len(html46))
                        sr = bs4.BeautifulSoup(html, "lxml")
                        se = input("num:")
                        sea = int(se)
                        html47 = sr.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                        print("\n")
                        print(html47[sea].text)
                        print(":farm harvest:")
                        ur()
                    elif r == 'no':
                        print(f"{html46}\n\n\n")
                        for html46 in html46:
                            print(html46)
                        print(len(html46))
                        sr = bs4.BeautifulSoup(html, "lxml")
                        se = input("num:")
                        sea = int(se)
                        html47 = sr.findAll(f"{rt}", attrs={f"{nm}": f"{h}"})
                        print(html47[sea])
                        print(":farm harvest:")
                        ur()
                    else:
                        a()
                else:
                    a()
    else:
        u=requests.get(f"{urt}")
        x=0
        for i in range(3):
            x+=1
            print(x)
            time.sleep(1)
        print("farm_harvest\n________")
        print("rest")
        time.sleep(2)
        r=u.headers
        for k in r:
                print(f"\n{k}:{r[k]}")
        print(f"{u}\n\n\n\n\n\n\n\n\n\n\n\n\n")
        d.write(f"\n{urt}")
        d.close()
        print(f"\n[{u.cookies}]\n\n\n\n\n-____________________________________________________________________________________________________________________________________________________________________________-")
        print(f"{u.content}\n\n\n\n\n\n\n\n\n")
        print(                            " 0                         0\n-___________________________-")
        input("")
        print(f"[{u.cookies}]\n\n\n\n\n-____________________________________________________________________________________________________________________________________________________________________________-")

        html=u.text
        html1=bs4.BeautifulSoup(html,"html.parser")
        print(f"{html1}\n\n\n\n\n\n\n\n\n\n\n\n\n")
        html75 = html1.findAll ("html", attrs={"": ""} )
        print("html text:")
        if html75:
            for html75 in html75:
                print(f"{html75.text}\n\n")
        else:
            print("---------\nNone\n--------")
        scrip=html1.findAll("script",attrs={"": ""})
        print("script text:")
        if scrip:
            for scrip in scrip:
                print ( f"{scrip.text}\n\n" )
        else:
            print("---------\nNone\n--------")
        links = html1.find_all ( "a" )
        print ( "links:" )
        response = requests.get ( urt )

        if response.status_code == 200:
            soup = bs4.BeautifulSoup ( response.text, "html.parser" )

            links = soup.find_all ( "a", href=True )

            for link in links:
                full_link = urllib.parse.urljoin ( urt, link [ "href" ] )
                print ( full_link )
        else:
            print ( "False" )
            print ( "\n\n\n\n" )
            print ( f"for({u.url})\n" )
            a = input ( "Do you want to search for something specific? yes or no:" )
            if a == "نعم" or a == "yes" or a == "يب":
                rt = input ( "Type:" )
                nm = input ( "Parameter:" )
                h = input ( f"{nm}:" )
                html56 = html1.find ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                print ( html56 )
                html46 = html1.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                r = input ( "text or no:" )
                if r == "text" or r == "txt":
                    print ( f"{html46}\n\n\n" )
                    for html46 in html46:
                        print ( html46.text )
                    print ( len ( html46 ) )
                    sr = bs4.BeautifulSoup ( html, "lxml" )
                    se = input ( "num:" )
                    sea = int ( se )
                    html47 = sr.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                    print ( "\n" )
                    print ( html47 [ sea ].text )
                    print ( ":farm harvest:" )
                    ur ()
                elif r == 'no':
                    print ( f"{html46}\n\n\n" )
                    for html46 in html46:
                        print ( html46 )
                    print ( len ( html46 ) )
                    sr = bs4.BeautifulSoup ( html, "lxml" )
                    se = input ( "num:" )
                    sea = int ( se )
                    html47 = sr.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                    print ( html47 [ sea ] )
                    print ( ":farm harvest:" )
                    ur ()
                else:
                    a ()
            else:
                a ()


        for link in links:
            href = link.get ( "href" )
            if href:
                print ( href )
        print("\n\n\n")
        if response.status_code == 100:
            soupf = bs4.BeautifulSoup ( response.text, "html.parser" )

            script_tags = soupf.find_all ( "script" )

            for script in script_tags:
                script_text = script.get_text ()
                links = soupf.findall ( r'href=["\'](http[s]?://.*?)["\']', script_text )

                if links:
                    print ( " script url:" )
                    for link in links:
                        print ( link )
        else:
            print ( "False" )
            print ( "\n\n\n\n" )
            print ( f"for({u.url})\n" )
            a = input ( "Do you want to search for something specific? yes or no:" )
            if a == "نعم" or a == "yes" or a == "يب":
                rt = input ( "Type:" )
                nm = input ( "Parameter:" )
                h = input ( f"{nm}:" )
                html56 = html1.find ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                print ( html56 )
                html46 = html1.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                r = input ( "text or no:" )
                if r == "text" or r == "txt":
                    print ( f"{html46}\n\n\n" )
                    for html46 in html46:
                        print ( html46.text )
                    print ( len ( html46 ) )
                    sr = bs4.BeautifulSoup ( html, "lxml" )
                    se = input ( "num:" )
                    sea = int ( se )
                    html47 = sr.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                    print ( "\n" )
                    print ( html47 [ sea ].text )
                    print ( ":farm harvest:" )
                    ur ()
                elif r == 'no':
                    print ( f"{html46}\n\n\n" )
                    for html46 in html46:
                        print ( html46 )
                    print ( len ( html46 ) )
                    sr = bs4.BeautifulSoup ( html, "lxml" )
                    se = input ( "num:" )
                    sea = int ( se )
                    html47 = sr.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                    print ( html47 [ sea ] )
                    print ( ":farm harvest:" )
                    ur ()
                else:
                    a ()
            else:
                a ()

        print ( "\n\n\n\n" )
        print(f"for({u.url})\n")
        a = input ( "Do you want to search for something specific? yes or no:" )
        if a == "نعم" or a=="yes" or a=="يب":
            rt = input ( "Type:" )
            nm=input("Parameter:")
            h =input(f"{nm}:")
            html56 = html1.find ( f"{rt}", attrs={f"{nm}": f"{h}"})
            print(html56)
            html46 = html1.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
            r=input("text or no:")
            if r=="text" or r=="txt":
                print(f"{html46}\n\n\n")
                for html46 in html46:
                    print(html46.text)
                print(len(html46))
                sr = bs4.BeautifulSoup ( html, "lxml" )
                se = input ( "num:" )
                sea = int (se)
                html47 = sr.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                print("\n")
                print ( html47[sea].text )
                print(":farm harvest:")
                ur()
            elif r == 'no':
                print(f"{html46}\n\n\n")
                for html46 in html46:
                    print (html46)
                print(len(html46))
                sr = bs4.BeautifulSoup ( html, "lxml" )
                se = input ( "num:" )
                sea = int(se)
                html47 = sr.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                print (html47[sea])
                print(":farm harvest:")
                ur()
            else:
                a()
        else:
            a ()
def fv():
    try: ur()
    except FileNotFoundError:
        print(" \n((((((name file)))))\n")
        fv()
    except OSError:
        ur()
def g():
    try:
        ur()
    except requests.exceptions.MissingSchema:
        print ( "false" )
        print("(https://)")
        g()
    except requests.exceptions.ConnectionError:
        print("false")
        g()
    except ValueError:
        g()
    except IndexError:
        print("false")
        l()
    except TypeError:
        g()
    except UnboundLocalError:
        l()
    except KeyboardInterrupt:
        ex = input ( "?you want exit:" )
        if ex == "yes":
            exit ()
        else:
            l ()
    except SyntaxError:
        g()
    except OSError:
        g()
def l():
    try:
        a()
    except requests.exceptions.MissingSchema:
        print ( "false" )
        print("(https://)")
        g()
    except requests.exceptions.ConnectionError:
        print("false")
        g()
    except IndexError:
        g()
    except ValueError:
        g()
    except TypeError:
        g()
    except UnboundLocalError:
        l()
    except KeyboardInterrupt:
        ex = input ( "?you want exit:" )
        if ex == "yes":
            exit ()
        else:
            l()
    except SyntaxError:
        g()
    except OSError:
        print("Error (name file)")
        g()

l()