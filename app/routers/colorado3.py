import pandas as pd
import requests

from io import StringIO

session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://www.sos.state.co.us',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.sos.state.co.us',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

response1 = session.get("https://www.sos.state.co.us/biz/AdvancedSearchCriteria.do", headers=headers)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://www.google.com/recaptcha/api2/bframe?hl=en&v=-QbJqHfGOUB8nuVRLvzFLVed&k'
               '=6LcGUXEUAAAAAGQ75fIgC7gLaX07HJrY9_k-ninI',
    'Content-Type': 'application/x-protobuffer',
    'Origin': 'https://www.google.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = {
    'k': '6LcGUXEUAAAAAGQ75fIgC7gLaX07HJrY9_k-ninI',
}

data = ('\n\x18-QbJqHfGOUB8nuVRLvzFLVed\x12¤\v03AFcWeA7MV5yHArdPgdRFGst0JMVVOE875rtDWxMzzb031HjsLMvM3j'
        '-AJiSWlOnDjBR3AbAa54Bwl49DimcV0t2ebp91ojLBGZ0AYxB8IYMUfqaxfPGHHsnkKqJj8AtwfUo9Q4an0'
        '-vOxdE7LTo2nF70OEpK2Rv1n5myDGDWHqx9n5MjDjoM_jCsABDdR7Is0cTCMjVPX3-0IegZVL1KtHr'
        '-MzR5aZcXbu5hfuySnxdZaDlakCilWxpLdPxqWEwKitZ1EW1gNDDvQze_1AIQbNZo_E38Sq7NUV_sTkwvoKlMkEisikepbJZscJp6UuPLqLWIu'
        '7O9JJ9ZMFb0g79asvFgH3XqIB-jqxZShSYBHKRt1Mc5z1gmLGmunTJLGlshPgZpp3m21f1fKUDA9YLAvLPe0VSxvXk3fhG91T0zn72kGy3KZLT'
        '-U-1uwOnxHeKk2oGbB_2jr0flTjEoCCGtGl9A5mgLRdp7_kKDgQlMlZEY8aanNYbqYBjx4dYvfEpIcZr-_6cDP6ZWfQqBApHd9kWBH-08ZFXcj'
        'egrGxg9nor-qdu4NfsjeuiVq1oZkY89KMtXJJSUG_zvis-DuPzsV1h_I60Bn4OXoZPYSKLejZHyarcSMDrsraKuDhexJ4kMPjKXq8qiTYuQNPv'
        'qlSszjUAqbWCfl3fKAENaln3RHCgRjflG13qm-T54WbYrGScx1yi-EwunTzdQGW9qxEuBeAFjEopD2LXGhk7Fs58HrYFDKS9gUjRSXmZ1iIVwA'
        'jwiJ9tzIqoye7o79ufH3kQnsvCGkzRTVtNlxiMoAtgVqiwac7AATyLZFn8J2bV8gWeo6wU2AHhRG9cizb_crlFu-C6q-hpS3SVueGAbFHt3QPk'
        'EagHjgdWM8D8bHk8stpB-2fQSDnfzoodgn3jXQDoHz5mHOitxE54wUABzukwff0TzrFNLcBSNy97c2WiZ7GZxeE1pppRD21kxR-A7geCNR6w55'
        'dhnHyJOf4TUE97NdXXG8RQzRmlBcqZUUWDqE46jG2y6rF9XBGdgYqZMJfmezFtcFoT6Yi8r9LvPbUeApy0ShXOGCkM1o-20i56KL2KX4LRmsea'
        'nm6dvDB5NvPd2J5zvTRkTKm7qRoyfdi-NKjo77_-zqkOcxNIWtqBQFZEV0G1NVMHdnAyNat3eHf2L6ZOb28AEtlVLbzzp9zaaENf1W7vbDBWQb'
        'WEFP2SOx2VF14MVqaeT0Km8yhm_9Iq7jzfrpmy6scNjtOhb9QiEDMpr1Nq-PIAbVycM0XXbSRTJNltIOy4Bv_kU0R2fn5nB9H_UAufCtpxVNHZ'
        'qN-vppe7Riz3X0VcAwo4NFC6AzlPRtqPuUdPbImLBapfeoi_nhcFZsyWnJPxwSGFX8uEaxurQMsCSFKuYGSM6V0OH4NfHR4lOYwcs_FfbWt5kY'
        'eTMmwdBm3ignG9N7g"¬\t!CgygDAkKAAQeHOiMbQEHDwAE04P5s5wDZy0jssNqOctOPoOi2kpz5rqisrEEmtNrc34wbHP8Es1z1J9K7eQP5Fe5'
        'kNE66kJDEAlhP3ndDnu3su0tELTI1hYNU_sZSi5LF5REdyhgLwjwMPaG-_Ev8oV2VXwqkPpIIZY1XSqMCfBc8czrdwiieTnJgQd_so3d0Ku0Fu'
        'XMChOUwoGL8KU9sisz_Dby1Fj-bzYTmYBIKqClKgFOK9MUVKFYfc06FpBpNDslmz0iTVzColgTOYs4cvOVHnmfK4KxDOB6w8YCtpgAouKcqvBl'
        'V4jMhMpnKuk3jwpmxCixtEFUmy5zrzBhmm792S5JtKp2oxEOjRLSsKc2OpczMvx0ld55vtC7aM3vAfP7imFBQ54u5EsGle3ie0NOYrVjCXcZ_4'
        'lG-SdmVnJ5xaI1JGkSyVT4_9NJ8DclTOVIjHOo76dIc-huUnG6cvlkgxa7Bl4DMq6_EJfi07JKzR1GZ5leh7TehrE9A9Erj0mlHvxtlSS0BeF_'
        'Cf7WSoBV0E2G0gquQD2FAoMFVHqcxu60MMuf-AgHZ_j1EduADAosfxGr23AxfouxszUn74XZFDlB2BFVq2NGDT6Q2sOqcQqp1jMQ4jnqkgcvhN'
        '3yo4Jwm6ABaFsiihz4PsP8ELLQ4LvA8mNuOSUZm1IJvWbEalLW4zVgeo2XFysJ0jaZwHil-aWDQeycB_Ck2x7xBj7b331IgJy3G5Lugtf643NM'
        'qi998wKmfkwO1kSW6FWvbbP7fWViDkWSQs0TbjBx1uhuzAOE4Pdr6_m_yjtcpE_GJhAv_pOCtL6-i2acoF8QQcGZlP1_Z04M6NgABaLMvdPV7Q'
        'DqZ-7yD7WAP1g44bgOIqVo34O3lrj-w18NqwuQFH4WzwqY1tivk_UfQIbdrmd4eTdyllToVMyZKOMQOaVk-rkKmfcWu-yk7_DMwRKRSXMlClIR'
        'NIg-RI0DZj2AKhNQLvzOLvD7x2kV5yUpkw2v9scLIuHCeCwA-uPIW3DcGimw9IQOQdX338W2Ixpx7ZSSWO-wn0LLLUIaqgC-PMghOA7gHJhHkx'
        'oaxUC3jZ_ST4-dNBz4VqqGfwuOYM0JcjVCO5KAdSs8RgkweiCcc-NjBaH7Fuuh-3_bgw2NJZ_q5MGwp72Wa3TvPO2WbSrMCuLa8ZfyDef0Ljb-'
        'W6N5Tr8*\n10159761622\x02fi:ð\x0105ANTvZwV2dfkulGjoOpI9KzQ9Dsh5TRX-lIEHORZe3IqVmJ_UuK2whEb5v3byryYrCeYrd4yBOz2'
        'uhckwgO_H1xVbkN5AjphTfCwpECRplKd9jhIBuhSqmDqCR5fQcKpsn9BinUsszv4ic_-kWJJYuWAo7i8d48D5fIHpoqc_l6cBNM-sc-QgG7ke7'
        'Ye0uRIqpAbpt-TmlAfpMir0HhXKDDR_OdMkgfy719qUKuctvv23Pwr(6LcGUXEUAAAAAGQ75fIgC7gLaX07HJrY9_k-ninI\x82\x01Ï 0MAQk'
        'ODxJFmV5fYpXprq-y5jn-_8M2dzpAA4fJ3aKjptot8vP3Kn4DBAd6jlNUV4reo6Sn2y7z9PgrfwQFCHuPVFVYi9-kpajcL_T1-Sx7cHt-gcfIl'
        'RfUGNih6qJlq-wvdvn5vICCxhLMlNUWWZ3gI2ap73vztvo1h76DhQXT2aEoIObqs644coD7QMK-ytZPTYoP46iprOAz-Pn9MEQJCg1AlFlaXZD'
        'kqaqt4TT5-v4xRQoLDkGVWltekeDV6SzpNzszALNHy0UNlRPPVaLg3KDv8nB4eW0x_vvLTMgVlFlQkdcnah_p83BsOzkDCcNJFAcV1g9lJiipo'
        'Kzys_u8837LwYXI2FRR19ObpCOdIudsL7HzOTq9zENSR1qeFSpsZeqm5KpvczZ5OoCCBVPK2c7iHaunnyTp7m-zdTs8v85FVElcnaRWXCClJ6r'
        'scnP3BbyLgJPTW9ec5J9kce2n8LS9wXp9uwDFykuPURbanOphcGV4t3xHtbt_xAhLS5FVF2Tb6t_zMSxBMDX6fwKExgvPkd9WZVptpmj687N5w'
        'IBHxtXYVd3bFlTanyOlqqrwtHaEOwo_ElqeodIdnt0gdXKuOvR1hX4DUIsNVFYeZSTemh_k6Gtv8DX5u8lAT0RXmp7lqmqwXmQorS7yNHo9wA2'
        'Ek4ib1-OVm1_kZqqrsXU3RPvK_9MUWszSl5wdYSLorG68MwI3CkZMhAnOUtSYmh_jpfNqeW5Bv0oEgU9PHYuRVlocn6Gnay168cD1yQYMy4YL0'
        'dOYW10hZSiqbHJz9wW8i4CT01xaVWSgp6vqrL09N7wHCPsAxcpLj1EW2pzqYXU6Oz5xgLWI_sRGSsviH6YhZeStbfk9PrA1-n8ChMYMDZDfVmV'
        'abaRr520xtnf7_UMGyRaNnJGk4u1rNK5tebMDQQoNUpcTGBYhXqrk6ajn8Tl2RMb5CkGE00td2eJlaqwmLOk0-jnABAnHj83NUY7Q5GGopLPnd'
        'rN49vmFAI1PSxeZ090j6C5uI-a3-bbERQaFyYfPEJwRGdbo6mYvqTo7ebu8R4LAVA3PkqLa3-WfqKXqNDkEAUpIjcRV1Qxf35IX3mAi56qucbN'
        '3uH7Bw9GIl4yf52IZn2RnrG4vtXk7SP_TmJmc0B8UJ2Uxbehz8q4z-Xw-g8XKjA8SlFjb3yJw5_br_z_6RcBITBDZV5xXWm9mMzS0NcIyw0y-k'
        'EqU043ZmRylJDHwMLJzN4LI-8fTVZERnVjcqinmKXRx84F4g_7OR9ENSpWhHyVd2-C1LCp0AkV-isTPTg1PlZDd3mxpcekr-3wzRQoEDIiWT1k'
        'PY1wnI6pr6q-zO3J9t8JEDI4X1hikXedoJGz1Oj5wgrzD_VJJkReblOXlIt2gqmzv-nEDgHyQRoOG0dQhnymtouI08bozQjUIQ0eGzcpc1iIc2'
        'SYxYqu6LcAvdTt9AYMIi48Q1JWaHSBjsik4LQBBBopSE5AXSlAUl5teImZqLO-x8_p8P00EEwgbX6MVGt9jp-rrMTK1xHtKf1KS3kxSFxre4iJ'
        'oae07soZLTE-C0cbaGWYl6-dnsbZztsF7P4ANTlSITBeaZ2rraOsr7ruBuceBfFGTl1eSn9poYCcoKCvy9fkB_kGKQZCXUxwe1B0h42cmaHj09'
        'UWGPI7OFlhUTmObJhyrKDZ3eHYCfT3CEAnSTxqU156iXOmqr3hw7_Q_icSIyhVUGhgS3p8jMauzcXb5_T7HA0iKldKW42FX7XDxcW-yr_m6-oI'
        'FENKK2qAZm2tl5jEt9_l4QfYGxchVWFZVEdUmo2OvdKzrfD78g7xPkIQUFI3Sm-QiZCWy8C1uQn2E_IRSTk-cVlIiZWXmourwuLE6f35GzBQUm'
        'FlfIeNgKS_sb6t2N8B9_wLFg9mRm9DWXZst5jOtO3d-vwe7jw_O2FIT2Wenbe6iZWn1sTJ0y01Oz4_N3p4iIKbrsexzrvb5f4UBigBEUIoaXV2'
        'po2aq6u96t_i0wgw-kJBVnBZent9c33Glan2vu75Fi4FIl9ocHCDf5uxsse77_Hn4O4wLQgnTEd4RHJ4mXWCqNfT6-XX4eo3FhY8TFZpl4eqrM'
        '-vta_i5dYgNxouGjpuhYhbZISzybikz_INAQYNIzEZbltUgomDiJ_Bt8bR9vYmBvpCVD1qVE1whpGSw6q_6ALb9PUMIg05VlZBX52WdZ_Qmb_L'
        '2s_wJCxBLz1PZF19crCUyq6dmbDC0-Lp8QMPHFYybkKPh5ylr9HM4OkG8N71CRsgLzZNXGWbd7OH1OLz2gX8Kw49QWtPQXR5pZCzidDl1NXS3f'
        'sqRkhEb3VFU6GHiLaw1cvL2ef97yA5W0FNcFd9gYeOo9Hd6t7tDSUCDUAbOFOBk2p5l4Gd3tyku83f6Pv8EyIrYT15TZq4u6e65Ne1zN7y-QQU'
        'JjQ7TltbbXmGk82p5bkGBf8c-hElMkVOUml4gbeTz6PwANsO9TMsQ21odoCJearE0-Hh1AbrFyEwLTcfb0pbjWFddIaZp7C1zNvkGvYyBlNHdG'
        '2cg5O4kszIxQAQIR8xHzAuN09Ubmp-rpasnbzF--zw-iY4QDVpUnVZkYaciIOarrnN1tvyAQpAHFgseZucd5Cy0szp7hP2BAokQjdsUn1Nenib'
        'tqabxPzzBPAPFRguPFtKa2F4kJKG2cze8fba4CUYKzBbVXxsfHpqrXmQorW90dHo9wA2Ek4ib3GObaWy0oqhtcDU3-L5CBFHIz1JT1xxca2Bzs'
        'L21fDgEDs8QDVjUU6RiKZrgpSltLvD2unyKARAFEJZbY5mjrqwmtnV1AcKCRA8NT1PQDJJW2h0gpKfrrrJy93p9gM9GVUpdm6ChHqsysjTzvn1'
        'GR4PME1DeHaLcnOygKbKte4F7R8YAkEwGkN5WD5VZ3mEjpatvMX71xPnNDlWO21gZaWvipq32b3d3tcFNR8kMEJCgWWOlZCeidSlobjM2un2-R'
        'AfKF46dkqXo8eQrunLxM3xHysZTxwxcVuWm4msl9DM3ADmGvACGjlGWWtiYZBxi5ifyNLA1gUTACoCD0dJbFFuep-ws47U1_vABPEF9gEoNmM9'
        'XHKXqpKaqcLb6P3p8h4OIUhAc3BWdIh1v6bFverdAt39DSUQJld3eH6HdquBvJjN6d0I2fsnGx4vSzhWkZCxnrvA4pqxw9Xf6_IEEB1XM29DkJ'
        '2_irzTvroJ9fkAMx9UPXVUj2eDkY-jqsHOBQ8ADfXwBxkrNUNIX2x6rYnFmebUAyXtCBMBGCw8SFRZcH2Lvprp_QEO2xckMRQkND9JUGJyhIuY'
        'nrDBydvs7P4PGCs5OkxdaHSHiJqrtcXP1uj5BBQgJDZHVGVtcoSVoq-6wNLj8foIDiAxQEdcXG5_jpykqrzN3Of4-AobKjRDRlhpeoeSlKa3yM'
        'zb4vQGDRowMEJUXG58fpCirLjGzN7w-wkTGiw-S1NmaHqMmqSutsja6O8DBBYoNkRNUmR2hJOaoLLFy9nq7gATGik8PE5hZ3mFipyvtsjT2Or9'
        'BhglJjhLVF9udIaZo7W_wtTn8_8OECI1QUpeXnCDkJqprL7R3ub4-gwfLTRCSFpteomWlqi7ytLe5PYKDx4rMkRYXmp7gJKmq7_FzuD0-gkYHC'
        '5CSVVhanyQl6u0uMre5vQABhgsNEZUVGZ6hJCcorTI09vq8AIWITA1PlBkb3mHjJ6yvsTY2uwADBgkKDpOW2R2doicqrC7xNbq9wUJEiQ5PUxY'
        'YHKGlKGrrsDV2uv6_A4jKjVFSlxxeYWUmKq_x9Ld5vgNFSUtNEZbZHF_gpSps73O0OL3ABAeHjBFT1xsbH6Tnqi5uszh7fX_CBovOkhQVmh9iZ'
        'KipLbL1-Dq8gUQHTA_QFJndH-HjqGsusbc3O_6CRooKj1IWWZzeIuWqLe9xtnk9wQMFCcyRk5hYnWAk6KqsMPO4u35_hEcMTdDTF9qf42Zmqy8'
        'zdToGfUGDx0uZ0OSpqq3hNPn6_jFAQ72AA4eJC1ETl1rd3uSnKq0w_rW6Pv9CxxVMYCUmKVyrruerLnE1gvn-AEPIFk1hJicqXayv6ezvMzR6P'
        'P-EBIpNUVNU2p4fpOUq7rG1dXs9wINRyM0PUtclaJ-zeHl8r_7z_0qKztmSkxbi3ypl8Sx3eTHudDi7gQMHCk4PUlfX3F9ipfR3g¢\x01Ô\x01'
        'tbMywxMzMsNDE3XSxbMSwyMDAsNTY3XSxbMiw4Myw4NTBdXSxudWxsLFtudWxsLG51bGwsbnVsbCxbMiwwLDBdLFswLG51bGwsMF1dLFsid3d3'
        'LnNvcy5zdGF0ZS5jby51cyIsInd3dy5jb2xvcmFkb3Nvcy5nb3YiLCJ3d3cuZ29vZ2xlLmNvbSIsInd3dy5nc3RhdGljLmNvbSJdXQ'
        ).encode()

response2 = session.post('https://www.google.com/recaptcha/api2/reload', params=params, headers=headers, data=data)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://www.google.com/recaptcha/api2/bframe?hl=en&v=-QbJqHfGOUB8nuVRLvzFLVed&k'
               '=6LcGUXEUAAAAAGQ75fIgC7gLaX07HJrY9_k-ninI',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Origin': 'https://www.google.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = {
    'k': '6LcGUXEUAAAAAGQ75fIgC7gLaX07HJrY9_k-ninI',
}

data = ('v=-QbJqHfGOUB8nuVRLvzFLVed&c=03AFcWeA7v7Vaw4gNeuUXQO1sTugVtQnC2FxbWWJAOVFxBw1GTUab8Ph1JsuCBPLr6p'
        '-v7mDnPsirDBzGNJYjOo29X5KzW3x-MUfJ5720GGvKigA5HzosoTsrhqM4uKCZ8oNKxP3fdV_Pu5sxRjks2IfocM6QheFixQYuhCQm0X'
        '-u8iJjEzhilij3KnPmaZjI5KGoN2W5RQENortK7B0Mr-gcQgPuz'
        '-p6n3mLUkdUoBG8Tw5FMQpG3rlcimZV0oSbkp20ahk6AEKqUJlQaGKTTgNeK4DvIChJzHSdPL0T7JyRdEmYgS8I6yu5sQD5FUYz'
        '-0vsm5wDVbG0tkZzmbyDYDuq8IAeLn4_8b2Q3XjLmXgb63iJ_w2HUxDKzZChiErlvsJ5BdMWR7ynjP7_1P74zBgq6rAHm4JA9'
        '-bSy24ziZtbQ6e9h5AC_ymPu2_9UIm8CYNo0TI9DDbgqiLv2Hq2vwShjWht5xfkh4Pp6d4UL05XRiZHO-Xnea6stC0y5Veqsn8aJ83'
        '-PkU_G9NOuxjPhHoD8HAz1y0W4OyTwg8RT78991WpMKLOczCy8UiNq-dbS_XCIrIxQK4Xd_'
        '-0ZQmbuE_6AYS71pMSu1HcDOAe6CPTTRhGWioxsAQxMr6eXOxa'
        '-tjZ3iar1DhwxYrDh7plKgCFLnZz7iBuPq6r7FMmvBxybFyq_D7YOZK8bHSWscWxv_K5C4a_7suYkNr5CQOhDbksK3o4sz6JJ2bizlE58Wopag'
        '2E1ehvFd4GJwA_EB0N6hTrjCmc2WWdbTfUM1LvktzjFYQqv96Q0A0LLObktwer2bm7dmfjH6t7FuqEMnF6UV4-ri_vYofacfbgpvz3340bpNVi'
        'xLSVqI_ShhMYXRnSRQXYU6sDvH6nNMLPiY896HglCwl0XZetEkeKWzws8g6p8HYKPgBSQzRbjqZJ3AmoSMgCMGkO6wxD6z5z68nXc_NiZkBcsR'
        'nywWwYbYDKvRXqKT1suV4LQ5oGlWidUUCObDn9QeDBDHV3OLS7KJPXmhg6JUUx_AjLgUL2ZIWf67sJ7-y-zImM1QtIVth6UN7tgjb3vYpi-bQe'
        'fSPEmJjj6Qo_GeAXstUfOGiEWeyW2YSbbdYdcql4IrA0liC0tMamnWqWi-9YnUcbERWuSYQDDvGxfwz7B7VdJUoEejcLhnYiiDlVq8-VavEvwt'
        'rKayUWdh3sFOBj6mF4q2jn3lV9fL_IaLUQlgLW1wMPL5PCwZ8XHKpZtVNit0i5RSLq_8_0uU9EvwPhDH0Vr8S7YM-ytPOTo4NaDz8yaFKWM5HX'
        'h9tmCvEWaS4uisHstvOY0wSCAoKD2Nj1ZRI9LoJhaoaVupxdFtfgwTEyosFs_pAHbUlLhKM5ct0CvOpL-iKNslcn2xLNpbbqRDh6tkYBVnFEvg'
        'b1cbSEhNDjIerArxafVfePP5xA7vQtn8ucgu5rMjjlRwQMlYgWH1v5LPkSmNLZuzAmyXSlqGsc0vxa2b0rQ-KEoektGc0o-6o21Zft1H-t3rFf'
        '9MlNX8zjoCZeTvpMCN3yfs3h9HLilhJPGJNpWt0cPUGEundpWC1j4BjGeeSIPfMyqRtInOZssiyABOFwpeeVjXz_o0y5MaTYiWwTLW1bbWgUIv'
        'HP32TOqi-v_XvHnZxKUKf4ONOYnGBjJDTKteZp6Ai9G6chzD1QUO6Jpgox1AcqI0ZwO6sZwMgXw2L2jflEPgzFjOpZ4yTWc1GBJsVZYHHS9Qtk'
        'rWGIUoIl37ja7HoCByA_shDUN_RHMrDZVhjbKr6KxZhEOZo5QnFsXSLRXjVi3hYBcEoIjXgx18KETXCt5JhSAyjlUZMo6vTa5V-FqujZTPZ3pi'
        '6J3-FWkQVh2Mp_Lb3hloI_OuAPhJRVInESaqT8pJJ2PK39qD6fEyRKlRo16pB6Sjm5KAB26l-EmD5NO-LPBqF8d9UCI_uzgKzhBYRvEoGuWG2A'
        'V2-z2En9ojXS-r3bEEQSnV0ukwGotJgxjB9DVvz55m78gZUO4ix4ddBIbrnT6hjg-rwYWMyzX5LxFnjkOe03IN300hY1FDmh-5NGfkXZEqoPw9'
        'uajJigSVxTw4mnrvbZJHZ4UoI9CiXNHd58Ns_Z3cuEoD94Kiv0EunlJ0IPDCsMIUTx2vQzOg_LyVf_89Zw1fUubaGYABphVyKYCDFSe4gQcbpN'
        'YE9Ettg79ZhsvA41H33lONSJzUVu23MvVqz5pZ2skoyIotj1xvZmgFFvktTk0qs0Fj1cc_wvo1xSRfhEVQhEVSloJ2HlyKz3JmmFD7uDzr7WXm'
        '4l3t8QxAcB2GxWNx7Jo7Euc7lXnP-8EWQrFma2Lt-ZpT7rdnSLxUOPkn0BftGYeVyLWGP1RWhHGPGRLINYXx89r8ygRP--HUGr72i2ZC5b93rK'
        'QYYPkTasZs48RL9IbKRCrIAXDZN17HW8WwXjV2kI7ap6q76VQivefRmS4cOGEU4qltvo-7xk9E_CUigJ-XBQCXSMGnavZPzjW74Z79cEPc_no_'
        'As2NuYY67oI-bn7o-olLPV8hQgicVuzg1qAQJfCuV7_xlGqc1df7_wPDnvGIUlNRiy8FtCkRCZKleoUcdE3LHrTD7oXZVpjcJgEIfPVGZXGjqS'
        'xBuZOHI9_FOij-AW7wngGCA59uppjkgTJ28BclXLapEUQ7l-UHqYzS7FipLkOAAc74lWWWsWpk7wPM7MC9-5fTahPHNACAqCgVTjo9iaaePhSe'
        'ybpDqBs-gNTccQQZPcqlzqu4U1faXTX4NChNrON6Cd4jiQgga7-rgsMhUHMUKnAx83CejLWeuUvlf0SEw33EKIzFWd7hZSRTtzJfT6L0NXmh2u'
        'N6M_4-hg-iRhbDMokXWQrk1m-BvHXpWjO1ChwbAXJeA6yuT158XmZN0lucsRmOgjoDU2jLCJ4_njU6gUZP3bX-97QSMyBOe4jIKQbtVVOHBQzp'
        'ldLKFrRgf-PTsv9Y2Pd0AuLjCCwyT87KLHdOfF5E33lRGS80HckTompqOSVatxmohPdXxoVR7QdTsAnwlBB5ZoG_hHTrK5RYD2WsD9AW1duJSe'
        'etwlCm_A8FbPqNnwkOmxlyrTEkWeTMrUCB6MwITqLA8SU3oR5AO3Go_XG1UKPoafycj1OFZb5gKK8gbnJSsLPaR3YIhAXZ63pXS5fb5yQ0_VXY'
        '4TYoLbNQ85InPbHmlmSvQ9KZ4Zo56Ohqncmiss3l_LpV1qZcugQcpHCiLmjp4ERnC9Mv_yTbUy68V0Xoxx59UcfN-bKB9laeeAgOzVz5Hgzofr'
        'myL1h9oVIZdLKnLarCqAdSm82jtC4GoAgajIhtCU_YZdk32UvrSlkH0ywBNAvJA0WYRLRXblaxWIBg2oVb5qyCsUvMt_XEsdIu0FUdo57eBwhx'
        'WyI88hcTJie1L2FblBUGj7zUa0uYQXxkpY8GJTIgxHtonyGOP_U6nHP36MMVxUgYVlwSDebs6R21v8GT-Dwats0nD90LA9eqNHx2kl646kqA9j'
        'bezHfhbZ1gp4LMZ8rLHcFyMmlitDFcZneq-klcEoZs1YZNc98NvZABsJcetBuTEUgQLGCTU9qYRNKlt2pfdXtmY2DsXPgKTIpJRAbwwuZfulDK'
        'JbqnWQj9iFkpbNazAi5fYBDgEcQBOc1z6I7SRFqjUy4CfM-_VtUU7XgPxKEndn-w83wEjN0UVhaBlBLoWgUVa5T3NlaCcUjyryzt9SSA1cFKH7'
        'u0pEq0ts0KCdPLHmVEoaM83ExrvXPHcYs3nxXoXRyY1OnVwScYE--75plN-6dFGdwN30JXvZ4TVvo6tYGyuyjnRXbOQ&response=eyJyZXNwb'
        '25zZSI6IiIsInMiOiIiLCJlIjoiYlhWcyJ9&t=200&ct=200&bg=!qqygrKkKAAQeBNAhbQEHnAgEutFrQapQ_laj_kiuqsvvQP3DV49vU5PFN'
        'Trw7MVtBL7O14SgF4YrksNCehqdpOdJ8vGFt1XgvqB4qPPvrQ22qBOjEjW39WSOv9CazR5FLGOH47rQfCKcgBsWx6szgqn9ys9HmaE5KBVlK8K'
        'SV0ChwCDrzz-v7PRgaWWjPdwbnsYmN0udzL8-59Bzxb5GP0wLpCp14JM5uN0WE0V5gUODCKM_kM84RzAjA4KlGeZHWOxBcVWkh1SaTW7dwLEpb'
        'AUrlxGNKxzSPiy6hTa-mUxXDJtI9fDhDRqsmD-d6v12P861j-wBplGN-lW7kIhZvo2pAGAs7qe0RiudfNbieoiN2fUJFXkTv1QyXuAOSuWKMGE'
        'pYDfQiAEbodS5EszwtTkt0W5LTcBUuNeAPFDSH2qXBE2yOFoTVdokNP1B3IqG0ILysXP_tHfj0n-iFJ4-VIbJ8-KEvnRTVmsg-LDozSo-7Rb55'
        'g8FRaPxPuTMkJcsJlsl0JMtQueIyAqQ9O19-KHKnkmOZqX4IbaCIAfP_0jU_1NnH6FC7FVAuWPbyK281INj3xsFrhKbDzM8bUHdj81vhOmyxuO'
        'T0U2b5VS3Lay9aX_AaPqjjgXfHu9Ga3wAcc6asVqSiIaqwplwk4ggbyygcmAtRDUE6fZSQxiyrknii-Xku98onahgyeKapvxJW942qS9taUSze'
        'LTascZwLkpSxR2BPSxOx7KPNQHw6qNXWB9BUWyha9PLGQK3HzB-7TQe4Wv3kNZHC6BreBl5S62Wfnx7v-s4nhL8PltHC9BpoSvRyrVz_2q2hEQ'
        'slSvru1ReDsqVMXKiqnrRGGHPc5WGSL8tptwkUxyiu_22qLcsYocZ7roWK9s2KuEomlb_EW0apglTJWjIKQrHeV_XXSPz5_eCFGO7FrF5XQLvJ'
        'saN_T01wZCUas6tPj5ytZ_FvgsUjFfT-JBcvdYJ46C87X_GHLEVErMiJ-VKwiEgvidTe-pnaxx6J3e-GEC3b6O8kLqntO19bKzrKgrLkREcXp-'
        'cOWSyPzc4-0vysis56RWacUVf9GKGAKDzyks7PWUQd05n7SsI_vt_ZVqfikWBeaqlibQ4Q0PY_ut3pJj64xMuJLwcu6NpOcueMfknkY-tuZgpe'
        '712gq3tAtBOder5VIonxBCVeWDs_GX5D4EX82oHNTf9Qfo__3dKmcW5f13wp_Ew-YxysfSMsI3KcBza8KVsbPYpezB2BzWNqnhTcMQSo8Km814'
        '8tq1J-G7uOT2qk0rsGz9Q2zjuqZCaMmYYK5O2MtnHgUmysthzusvH4KQ-3ZcDu0PGS3KDx17hWwA2OSaY8pb0tG4lX9s-rcrdJPbliZopvMDFp'
        'dDtGJweJJaj8LwzuDj28M4j_RDn_GqO3dLxZYds6Ap2r7ZtvlvwEbz_TuKQuND0-vb2egwuRwmrjLitgkKvuEqKoaV5j3GOshaP5l0rSepoepp'
        'a4oUot6MCtN_8HBGPzNOs6SBAF6O08HjuoMec6AXMV4m1fUCF-ADcWKQZhLRrgWCIa4BxOHRDDGO1zbEUNlD9sbkbH72oVMnuJLeK8X3QLlXOn'
        'g18pffKGzSJ8LGe9W7aialk0KM6eaSwlwg4MAnQuFtFG8PnynzsTTcZubb46VTCKNhstEDZwVU8QLZVGwbXUddHNuo5DEBlydNK6xs2dozIX5B'
        '6IYF01z6_2rfUSMLvO33ryDzYNSfglikPCYdvVfxUzMV8fRhLIESaWJlHKLxooIw5q_qbU3dv-8LMq1kjnRDF0bd1hByPiEMBZVyMpNtF4p0ta'
        'cvZCbxVryynhgX3-1ogoPwStac-a6i3-rpQvaLiryEox3Lt5gWd2RmQ_r98WN940M3g2l119JQRNDMZmgvOYB1L00KNNV-yHHXH94xybeYq-bp'
        'dzZ_2iL-g1c0UxZgPg8XcQYzRGyR3P-J0z4XghPejSEpsojtGfcWvCqNS7ox0rzluvckSswUQJaCHQn4QLMOiRnWqcDTpCI8WtSv8LflDeOhOa'
        'gX-hmo8iC33_7G-RpuNY0kIZMFA5N08gj0oCvwTDYTTFHMhkiqhEVIJ6apPh6EW5xUxVwPQHL_KnrpsmptOLoxJ5R-VAeqU9lC4_jfxpGoMzWP'
        'IJomvflF71Z53WS1q0xqvmVvffS30MPZrpbolKFGWZ1KF_19lInP2CgZpkX-nR_xrgifTMKHx1dTILbJUkm26bLzpy5lm-nj1mwqbFxqIk2PNp'
        'zH8A90rcMwpgAkc9YBw83e0vjQuDwyCKsaly0mwIEu0JnzmfNMm-SD_w3t_oTWZBkAaUzP1mQBdS26Ta_qbsOD8-yBb0U2sReM_RVSPPEsMjG8'
        '4EYWPHkXrLyLbmKKCerMFqx3-d-8Uin1CmOrv-FtPy4IXPkLpC1kpCbIONeZtnyl8m3KQNpRh0o2jxGBDo4z8sy6VFlyg0gx9qNzN_ofP3mi8W'
        'ue_xC3EqP1UsoB8wyL-KUxTXC02I3hgmDBV5Bg7Yqc9sn_coSAw4pc9Bygm8-KIeBfd7wYWa8wgDGLoRYi_3JoWrhlghpRU0ZyOzy1sy1RhwlC'
        'N3cjNsZ4pANSewXUBkYcetqWfnymEBewjhE9hV705FF7eceGzOl6ye0cYDKbnInyfCurhvNBb6HLtunw-i22VNSWSzZVjraz5HuT-p_6oVEJAi'
        'D0mf95QceAcSGTEs1Qai2dZ7o51kZmsBps-sr2FoVq0RlqaCmmk2L_ws9gLJk_L')

response3 = session.post('https://www.google.com/recaptcha/api2/userverify', params=params, headers=headers, data=data)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Prefer': 'safe',
    'Referer': 'https://www.sos.state.co.us/biz/AdvancedSearchCriteria.do',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.sos.state.co.us',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

data = {
    'dateFrom': '',
    'dateTo': '',
    'includeEntity': 'true',
    'searchName': 'Real-Estate Broker',
    'personName_lastName': '',
    'personName_firstName': '',
    'personName_middleName': '',
    'personName_suffixName': '',
    'entityName': '',
    'g-recaptcha-response': ('03AFcWeA60nMvIrZewo89DXHZAMPqzqTCblkBwWJIQ0VvxAIGo1ystirJFY1bEaes6ajQsA5iQ1zr1PS9oa702XLp'
                             'v62y64aqAOBI8_X69A19HLCqK5VfJKLBfWI6K2WK2WSwYP-bbtKxndAxxcKyXqn3Q43ugNDA0WBi0Nyug48bmUrv4'
                             '9Mznu_Xg7MY8A9rU0ZmOhJKHRoTZvx0vqkzKDbIknXtflIcwM64churFlxCsJC2I0A-NhxYHIa8PlfJf9CSJys4u-'
                             'uUbCYZLnG6W054BrY4XrgwwKQwUDmOzCLKI7qXn12aYw5K_bs-iAZaaEKmXqM7iTSAAMqorTpFcZCjpXVQzqQhZ0u'
                             'ys-IbBDR-pTgEUP7GkSabwUEeFjgm9EF8fLI8SeIVp0EhcxI98pJnC9MHy3NU23QESg95Fz5Ykil66RiYUdOOHrzW'
                             'CS25l_lQSCYIZD0Z_JkZuTJP_ro8Il68LAyiyngQJN57NgrZL2Mi73N-hCsLqULCmjinuU4KRFj-yhOC3l1uR757H'
                             'rSpr7rYC-ZFNBYudxbTuAp4D8PbBzWZS-VGCQf3xONSsrDRYIxYSEbcU9kbB8uOC4J8tEiKXAPO1yG_dzHPYhPfCw'
                             'fhIQLPENxhVRsVTt3D3mZoWZU9BVugSIDIbh9s0uVSAsz4f_O-yxw'),
    'cmd': 'Search',
}

response4 = session.post('https://www.sos.state.co.us/biz/AdvancedSearchCriteria.do', headers=headers, data=data)

tables = pd.read_html(StringIO(response4.text), extract_links="all")

for table in tables:
    print(table)
