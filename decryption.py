import assets

alphabets = assets.alphabetLoad()

encrypted_text = input('Encrypted Text: ')
encrypted_text = '''YKC3F89{Ãx*yôô-{ó+ÂaûW]$È,edÓ3Ù;]{°wê,í3L]ûIÕjÓ[2Î°}dEoÇ[ÌM;Z4@-u;Gb{Íx
Jsªdfî{ÂeJHàÙLÚÍÔWé%êãÊÒzÃF*ªvc%)ãu0-bWúª$Ô Ãòf1W?1Ó{fõu]8º}ÌXbíCÃrb
ÒEKHosgèÈ-:mÇ(Ì?dNÔb,+Ré9Ù{õjkÊ5Ù°Õdyo94.,cÂò(p]1ÉO"HZÓ@b(,"q7óM_Ô6J)6bYçé%êfáúî STâ4MkÍã#O[U
õ9È1ièT=vdrÎììÕ=tÚÉcKÃmÀâsu8É;Glí20]vi,hQ?@a2R4w8ô?
T,M[fÕj:sÀI°îd_TfGKãiZªàSòxûZ$éîc!oê5jObóèHònJiUÍ/P3XòÁáÈz98b?2ôvããuO[U
õ9È1ièTbv%rÍì#Kõi0XÂpÌ!2B.ÀI{1bÃò=%)Pi°í2Â@Á Q
BÔES_3L@û:m}Óõ*ãÛ(kÂofVL,EIªàvÃIbP,Òm_;sc5f"@Â+é Mqi"ÍHP3X3AYÕÁê,Ê
çô%95pì#yAúqÃórlÓê1ôà2úw ChAI:ã4mpgí(p:rÇÌKÒW]Èêê1:#3=ÀÇjNîo:_ZL]$RõîHst;KÁ385°1
sqZÍÒÔkHÀÛjÕoE&sÒ.+#7óí=â]a)Db?L3XR*.Õó6úêªtJváúpìr.ÂN;$ê 2ì°8YfÎNI =tÚÉb?r!TÓC(-EFeJ%D
âMiªÊd}285m4ÂwoâÊºdDZèPîÌÊ(°°ªÙ_ÍÍ8êK;ÀÎgÔx1G2[ÍZc!Sì.9GY1eû!tWÛzÈÔìewÈÔoç
ÂGZm8@Sk
ZRhÓKíB°ósAGJJ3°Î=wÍ5c08*p3NTÓ+J5h;WìC=ìÕ(jÁIºH3ªcmjwrECÊZÉMTÌ@I/-NBfÁéÓmÇGÇ,e!]ÒLÃxiÂ{UªÎçSy,MOPBª_õígèz+: 3Bcû ÒoE8ôº4Jw7SbHÉéWcJpD âò:;WD1@VRqtx8:$4x28.Á0E1%xh=%)Pi°í2ÂÇ6rû5iÂIFk!Ó9Ú7ìjÌÊ(;R1ãÔe=GYgÙZÍÒ5uÚI:
VãRFèÚ5f5ÁóKAòMgèzk:-ªx.*vÈîÇrfº8JADtpnÊbW(qÈDliÉs/d?b@{]Qi0Íô$&!ÀûC(ì6Ù$ÂòûVBîb°P&;3ÓV°gÕÂR:0!ÓÀÚ78h!FU;L!éÓTfq-óÊIwyLf6Gú}3x'''
encrypted_text_test = '''v5êÛÒS%&+'''
key = input('Key (number:time): ').split(':')
encrypted_text = list(encrypted_text)

alphabet_cryptography = assets.alphabetFind(alphabets, key)

for index_text, character in enumerate(encrypted_text):
    if character == '\n' or character == '§' or character == '₢' or character == '"':
        continue
    character_alphabet_index = alphabet_cryptography.index(character)
    index_criptography = character_alphabet_index
    full_sweep = int(key[0]) + index_text
    for _ in range(full_sweep):
        if index_criptography < 0:
            index_criptography = len(alphabet_cryptography)-1
        index_criptography -= 1    
    encrypted_text[index_text] = alphabet_cryptography[index_criptography]

dec = ''.join(encrypted_text)
print(dec)