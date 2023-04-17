from pyscript import Element
body = Element('body')
data = '<nav class="navbar navbar-expand-sm bg-success sticky-top"> <div class="container-fluid"> <a class="navbar-brand text-white nav-link mx-2 google-font" >KLS ระบบเช็คชื่อ รด.</a > </div> </nav> <div class="mx-5 my-3 p-3 box-Edit"> <h3>วิธีเข้าเช็คชื่อ</h3> <ol> <li>กดเลือกหมู่ที่ท่านรับผิดชอบ</li> </ol> </div> <div class="mx-5 my-2 p-3 box-Edit"> <h3>ปี{}/{}</h3> <div class="item-list mx-3"> <ul> <li><a href="{}">หมู่1</a></li> <li><a href="{}">หมู่2</a></li> <li><a href="{}">หมู่3</a></li> <li><a href="{}">หมู่4</a></li> <li><a href="{}">หมู่5</a></li> <li><a href="{}">หมู่พิเศษหญิง</a></li> </ul> </div> </div> <hr style="margin-top: 20%" /> <div class="alert alert-info container text-center mg-100" id="admin"> <a class="btn btn-outline-primary" target="_blank" href="https://l.facebook.com/l.php?u=https%3A%2F%2Fline.me%2FR%2Fti%2Fg%2Fj3GWgy9XON%3Ffbclid%3DIwAR0hmmNvgtaChbdxGcga4jVp_Zrvf6I21ya_9gtj2bnUGuEhoqJmByA4Y1c&h=AT1k_LFxUc8AQ_jAytJ3v1DGrrS1fWdquxu3jdMW96OeFSVieRahuV_TIXmeiEY88M9zPrHhcl54EdsQFDTgXRaxZE_OdJz1s6LLnb0edvl9nit1Ejn5xd6gZCffEjH9Kw8yOQ" >สอบถามเพิ่มเติม</a > <a class="btn btn-outline-primary" target="_blank" href="https://www.facebook.com/timganez/" >ติดต่อผู้พัฒนา</a > </div> <py-script src="data.py"></py-script>'
morning = {
    'P11':'https://docs.google.com/spreadsheets/d/10IYKzeYIQJUXlRUZYSUlbz-MelBkYilCSlQMaw9QsVY/edit?usp=sharing',
    'P12':'https://docs.google.com/spreadsheets/d/1vG8ONBYW5WewDv_qXOLp75GxRj4VEJf4tZvCKgTmH8I/edit?usp=sharing',
    'P13':'https://docs.google.com/spreadsheets/d/1IL1yszNk8qvaOa324esprLRIeRNhl-y1iN0boaQVK08/edit?usp=sharing',
    'P14':'https://docs.google.com/spreadsheets/d/1Shbv5iOxQU2-S11Dzflj_vTlGO6kgKAHZiqps61H0MM/edit?usp=sharing',
    'P15':'https://docs.google.com/spreadsheets/d/1zU9SLDzC3DtgcGJ2XA0r-oOX7hFmLBccoeHHKVp4d6E/edit?usp=sharing',
    'P16':'https://docs.google.com/spreadsheets/d/12_Vze6yPHxdCM5l3t5lYSpYF1zCSwxLH24Ip5u4OI4I/edit?usp=sharing',
    'P21':'https://docs.google.com/spreadsheets/d/1ngVRdnULpWrBYV69srYEy74P-xRcp9-NatBLzPHy8oI/edit?usp=sharing',
    'P22':'https://docs.google.com/spreadsheets/d/1ZRHFU8nrTtZXVfFquf80eWvLooZyetRxx5kvmK6hTM0/edit?usp=sharing',
    'P23':'https://docs.google.com/spreadsheets/d/1Is-Z6nGGp2NzG4J_ek8VfkQHeQMM0Bkis0nMhygQPZU/edit?usp=sharing',
    'P24':'https://docs.google.com/spreadsheets/d/1cSDY7cNT5Kvys9mmzGsC8q-VMkygx6UZQmBXl5jXLXw/edit?usp=sharing',
    'P25':'https://docs.google.com/spreadsheets/d/1FE5qCRmCGXscw3Ju67J8mhojbAtWFFNFX3EuM4FZo-U/edit?usp=sharing',
    'P26':'https://docs.google.com/spreadsheets/d/14q4nULW1ygjbRUNtmozrvaMYaWvpbYAIvFPSdF8myyo/edit?usp=sharing',
    'P31':'https://docs.google.com/spreadsheets/d/1EF5Bk7eK0taJ1gfL5pPRRKKIpAUpVJ3YLjApb1IIYx4/edit?usp=sharing',
    'P32':"https://docs.google.com/spreadsheets/d/1DsoQTBlsA4fMnl5dMGFh1Zdj9loFsHh5Kbsa8aqILhY/edit?usp=sharing",
    'P33':"https://docs.google.com/spreadsheets/d/18KcOwtbw-suI0Z_ISxx5heac8Q306rgc9KlxKZCJ4s4/edit?usp=sharing",
    'P34':"https://docs.google.com/spreadsheets/d/1cjGhFkx3oVVP9xeY1_TzOo2f1FoAsVNCSDrMjnPQZos/edit?usp=sharing",
    'P35':"https://docs.google.com/spreadsheets/d/1mZHqmll4Secj1QFgMvT74ozow51v1NiluWzNmu_c6gM/edit?usp=sharing",
    'P36':"https://docs.google.com/spreadsheets/d/1QswcRsX10WLmYPNfpBS9U30me55SrB7jYXHAu82l95s/edit?usp=sharing"
}
afternoon = {
    'P11':'https://docs.google.com/spreadsheets/d/1KIOMaB8nqieYiRCYPpZ_nQrvmMu9SIafe9OjPZ7neB4/edit?usp=sharing',
    'P12':'https://docs.google.com/spreadsheets/d/d/1KLG94ygSuI-9bDFc8dy6nMnIxw1ivdxPvN_4jZVGusM/edit?usp=sharing',
    'P13':'https://docs.google.com/spreadsheets/d/1fQ1APJddaI6fYCmgmy_VQK_QMuzJ3ZQU__7A4taPyEA/edit?usp=sharing',
    'P14':'https://docs.google.com/spreadsheets/d/1LsXwru_SuEi1vN0z5ZzeEzn9l7X86c3btuubLPHXbPY/edit?usp=sharing',
    'P15':'https://docs.google.com/spreadsheets/d/1E3ku6yWjlfuX3cCW86sHC6RAioX7oAf-lmM4Xr8YA4U/edit?usp=sharing',
    'P16':'https://docs.google.com/spreadsheets/d/1xF0A8UOKAyx3Hjhhyn-dTkXpxfEFN3bWGw-mMVZpqDE/edit?usp=sharing',
    'P21':'https://docs.google.com/spreadsheets/d/1z1qFXYD4xEJG5d8TR_IAyYL35Oec44GWBwdx45KtSKs/edit?usp=sharing',
    'P22':'https://docs.google.com/spreadsheets/d/1ED6c7O2H0bfDmCWfqpEcX7t3AXQa4R8duvcMBwVva9c/edit?usp=sharing',
    'P23':'https://docs.google.com/spreadsheets/d/1YASMOuRze7NK3RticWdVWt2nK46G8GdE2WppcY-n37U/edit?usp=sharing',
    'P24':'https://docs.google.com/spreadsheets/d/1-E80Skcpisk1CL45d0IaWfvf-_zsasl-xWlTnQup0AM/edit?usp=sharing',
    'P25':'https://docs.google.com/spreadsheets/d/1bpgxvcJIAIkaFbSynLhL35HIoFuHtLTUhzDuFTniteM/edit?usp=sharing',
    'P26':'https://docs.google.com/spreadsheets/d/1OcD8VsPccYGsDtKlo8DNBsn7vSajv0dtUmwOboat-BU/edit?usp=sharing',
    'P31':'https://docs.google.com/spreadsheets/d/1TuyWblMTOQsPiZW-uGlnqzgbsQnf127J3Juw4gbJoVk/edit?usp=sharing',
    'P32':"https://docs.google.com/spreadsheets/d/1_VjSNOw0tnUMQpWeoRhjgy8Cvg3DSXjs29wCYOw4OaY/edit?usp=sharing",
    'P33':"https://docs.google.com/spreadsheets/d/16w83gGdvf8o87X-mOx_ERG8YF18wKvpVCk6typAxdIA/edit?usp=sharing",
    'P34':"https://docs.google.com/spreadsheets/d/1XNRCwdeflsw64zlJA4DJjS_Gpxh4dOzhzaxCXOT7P0c/edit?usp=sharing",
    'P35':"https://docs.google.com/spreadsheets/d/1gYig7rbAILEkTF9wK38eOO8bEHAPhNLj2IBmWDgE0YU/edit?usp=sharing",
    'P36':"https://docs.google.com/spreadsheets/d/1BDkFuVMknWhyM2j7En1xIg9rztnLKmbcHgCcPbNvzzs/edit?usp=sharing"
}

def show():
    password = Element('Password')
    username = Element('Username')
    floor = Element('floor').value
    timing = Element('timing').value
    if str(password.value) == 'kls2566' and str(username.value) == 'rd2566':
        if str(floor) == '1':
            if str(timing) == 'เช้า':
                body.element.innerHTML = data.format(str(floor),str(timing),morning[f'P{str(floor)}1'],morning[f'P{str(floor)}2'],morning[f'P{str(floor)}3'],morning[f'P{str(floor)}4'],morning[f'P{str(floor)}5'],morning[f'P{str(floor)}6'])
            else:
                body.element.innerHTML = data.format(str(floor),str(timing),afternoon[f'P{str(floor)}1'],afternoon[f'P{str(floor)}2'],afternoon[f'P{str(floor)}3'],morning[f'P{str(floor)}4'],afternoon[f'P{str(floor)}5'],afternoon[f'P{str(floor)}6'])
        elif str(floor) == '2':
            if str(timing) == 'เช้า':
                body.element.innerHTML = data.format(str(floor),str(timing),morning[f'P{str(floor)}1'],morning[f'P{str(floor)}2'],morning[f'P{str(floor)}3'],morning[f'P{str(floor)}4'],morning[f'P{str(floor)}5'],morning[f'P{str(floor)}6'])
            else:
                body.element.innerHTML = data.format(str(floor),str(timing),afternoon[f'P{str(floor)}1'],afternoon[f'P{str(floor)}2'],afternoon[f'P{str(floor)}3'],morning[f'P{str(floor)}4'],afternoon[f'P{str(floor)}5'],afternoon[f'P{str(floor)}6'])
        elif str(floor) == '3':
            if str(timing) == 'เช้า':
                body.element.innerHTML = data.format(str(floor),str(timing),morning[f'P{str(floor)}1'],morning[f'P{str(floor)}2'],morning[f'P{str(floor)}3'],morning[f'P{str(floor)}4'],morning[f'P{str(floor)}5'],morning[f'P{str(floor)}6'])
            else:
                body.element.innerHTML = data.format(str(floor),str(timing),afternoon[f'P{str(floor)}1'],afternoon[f'P{str(floor)}2'],afternoon[f'P{str(floor)}3'],morning[f'P{str(floor)}4'],afternoon[f'P{str(floor)}5'],afternoon[f'P{str(floor)}6'])
        else:
            body.element.innerHTML = '<a>home</a>'
    else:
        if len(password.value) >= 10 or len(username.value) >= 10 or len(password.value) == 0 or len(username.value) == 0:
            body.element.innerHTML = '<a>home</a>'

