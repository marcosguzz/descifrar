s = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNH"
frecn = [14.37, 10.325, 8.53, 8.125, 7.445, 6.94, 5.905, 4.87, 4.475, 3.73, 3.115, 2.845, 2.445, 1.83, 1.535, 1.225,
         0.905, 0.81, 0.625, 0.455, 0.345, 0.295, 0.22, 0.105, 0.003, 0.00]
frecL = ['e', 'a', 'o', 'l', 's', 'n', 'd', 'r', 'u', 'i', 't', 'c', 'p', 'm', 'y', 'q', 'b', 'h', 'g', 'f', 'v', 'j',
         'ñ', 'z', 'x', '&']
cont = 0
desenc = ""
usadas = []

print(s.count("A"))
print(len(s))
print(len(s) - s.count(' ') - s.count('.') - s.count(','))

while cont < len(s):
    letra = s[cont]

    if (
            letra == ' ' or letra == ',' or letra == '.' or letra == '0' or letra == '1' or letra == '2' or letra == '3' or letra == '4' or letra == '5' or letra == '6' or letra == '7' or letra == '8' or letra == '9'):
        desenc = desenc + letra
    else:
        porcentaje = ((s.count(letra) / (
                    len(s) - s.count(' ') - s.count('.') - s.count(',') - s.count('0') - s.count('1') - s.count(
                '2') - s.count('3') - s.count('4') - s.count('5') - s.count('6') - s.count('7') - s.count(
                '8') - s.count('9'))) * 100)
        contn = 0
        salir = False
        while contn < len(frecn) and salir == False:
            if frecn[contn] <= porcentaje:
                salir = True
            else:
                contn = contn + 1

        if salir == True:
            if frecL[contn] in usadas:
                difl = 1
                difr = 1
                fuera = False
                while fuera == False:
                    if contn - difl < 0:

                    elif contn + difl > len(frecn):

                    else:
                        if abs(frecn[contn-difl]-porcentaje)<abs(frecn[contn+difr]-porcentaje) and frecL[contn-difl] not in usadas:
                            desenc = desenc + frecL[contn-difl]
                        elif abs(frecn[contn-difl]-porcentaje)>abs(frecn[contn+difr]-porcentaje) and frecL[contn+difr] not in usadas:
                            desenc = desenc + frecL[contn + difr]
                        else:
                            if frecL[contn-difl] in usadas:
                                difl-1
                            if frecL[contn + difl] in usadas:
                                difr+1


            else:
                desenc = desenc + frecL[contn]
                usadas.append(frecL[contn])
        else:
            desenc = desenc + "&"

    cont = cont + 1

# manualmente:

print(desenc)
