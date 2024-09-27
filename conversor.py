def formatar_cpfs(entrada):
    # Remove espaços extras e divide a string em blocos de 11 dígitos
    cpfs_formatados = []
    for i in range(0, len(entrada), 11):
        numero = entrada[i:i+11]
        cpf_formatado = f"{numero[:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:]}"
        cpfs_formatados.append(cpf_formatado)
    return cpfs_formatados

# Exemplo de uso
entrada = '''
16215694622
16709359654
17909919603
16803691640
16713917640
16721130670
17997873627
17913148640
16942066613
16495580665
16946809670
16830341639
19218539647
16450679638
16834276610
18919107602
18099293690
17862309685
16617666682
18373482601
17064919648
16476769677
18815062661
70544250656
16213981616
16702893620
16357510637
16360413612
19200953654
16437075660
16936044697
17135390636
16203334650
18703090655
16362290690
16940621636
17216787609
19266011657
16302422680
70647103664
16835022647
16249177639
16856027621
19194491674
17015232642
16865132670
16179594643
16749306667
16864967611
16269708664
16297763607
19036139651
16832185669
70550645624
18469642618
16253158643
70585402680
70724247688
16683553610
70575056630
70509892663
16835726610
18167285600
16569475606
19528500617
16810269614
16783978656
18815068600
16212243689
16965050624
18905436676
18541168603
19117475686
16252954640
16144507655
10537077545
17229950686
19471545676
17150988628
19457139682
16155706670
70452142601
15991329664
70751845639
19323716642
16123758632
16808659605
17404583624
16750498663
19229403644
16008441621
16136679655
19196820667
16074590605
18269497630
19312732609
16434287640
16429426696
16468318610
17080799635
70550049690
70648466671
19111506695
16163933605
16290096605
19297329616
17089533611
17537066612
19377792622
19474132607
16019803619
19015901600
15303964680
18936386697
70435815679
19192354696
70639872670
70577840665
09446947561
52544816848
70652435670
16753197664
19471543622
70622079697
70533141621
15789368611
15770568682
16086185603
17285286664
70613517644
16072547605
16490421674
70578795639
17349718608
16434268696
18472895688
15011252655
18249535693
19251455651
18233969680
19080013641
70617798613
70647102692
19111494662
18580301610
18919540675
17587889680
18052974658
14729620607
70165175605
70724248650
19105395623
18009268631
70648666689
19445595661
16400270680
15912614654
12683300514
16859152648
70551118628
70151973679
70517643650
70597209600
17867548602
16622442665
70724242619
70263932605
18148047650
18901705699
70616445679
70613513657
19297318681
17875607671
17746250670
17204684605
70619811641
15427067698
19335063690
15903527698
16523211606
09690928309
70243184654
19199251639
19077913610
17829815607
18213870662
70402788630
18990890632
70699900654
70682619655
15500503626
15469325695
17423792659
70553983636
18267961690
17140086656
17229934648
19121483663
70639870627
70745968686
16432069661
17367164686
70512098689
18319609666
18767720692
70262615681
15449536666
70627228631
19199239698
16529684662
70258602635
17502372610
18928921627
18508705603
19116906632
17290604636
19097160650
14736375620
16297411670
15106333679
17577114650
17286525611
14586881607
14299331435

18611223659
16764770638
16964295607

19246732669
70600229610
18187342650
17305686611
70306263629
19162575694
70581832604
70758548605
70318887606
14884117603
70573408696

70150634684
70270094636
19029982608
17680320683
16887799650
15372137681
19227919627
18882689646

70116658622
19513693600
70147562651
15163240641
18936543628
15846264611
70619813695
00046814604
70272598690
17476668669
16160247638
18901711664
18020898611
19558423610
19048836646

19222759648
17272561661
19202645663
14757310609
17575498621
70533139643
17216767675
16428657619
17804982682
17502811630
14757328648
17824824667
70117911674
17642979622
17285293601
18231672680
16936007651

14504314614
70543131602
18105030608
19375908607
17080829640
15491037680
70117913618
49763720818
70592881636
19314092690
18873756603
70222755644
70533244609
19080797626
70318083671
70549274600
19132101627
70648665607
70318896699
70517642689
70639866603
19541342663
18452279647
70541614673
19223605628
19314594602
14254226675
70652436641
70170099679
19513675610
15770614625
17746267645
18921692665
16750440665
18012847680
17217535670
15932213639
19425522626
17673466627
14736361670
18251103606
16480504682
17423780642
16272502630
17948067680
19456939677
15666195646
70758547633
18614496664
16753177639
17577174637
16358150618
14385840679
70328868680
18653893660
17119088602
18007796665
17406478666
19011160690
70262286688
00212951661
19263224609
70371686610
19796025736
14391340658
'''

# Chama a função e formata os CPFs
cpfs = formatar_cpfs(entrada.replace('\n', ''))
for cpf in cpfs:
    print(cpf)
