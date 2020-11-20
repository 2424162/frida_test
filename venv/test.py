str = '''           country_code CN
                    kpn	KUAISHOU
                    oc	GENERIC
                    egid	DFP842F39F36A6997F407E6EC011E54523D887E676A7BF550BB39A00F8E6EB81
                    hotfix_ver
                    sh	1600
                    appver	6.9.2.11245
                    max_memory	128
                    isp	CMCC
                    browseType	1
                    kpf	ANDROID_PHONE
                    did	ANDROID_4c1d96d144ad9668
                    net	WIFI
                    app	0
                    ud	1222084156
                    c	GENERIC
                    sys	ANDROID_5.1.1
                    sw	900
                    ftt'''
for i in str.split('/t'):
    s = i.split('               ')
    print(s)
