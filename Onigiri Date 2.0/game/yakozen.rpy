label yakozen:
    scene corredor with dissolve
    show noname err
    
    noname "Ok, então eu tenho que ser bem discreta..."
    hide noname with dissolve
    "Noname encontra escadas de emergência do prédio"
    show noname err
    noname "Indo pelas escadas, talvez eu encontre essa prisão. Com certeza deve ser no subsolo, já que em cima só tem os apartamentos dos moradores..."
    
    scene prisao1 with dissolve
    show yakozen at right
    show prisao2
    
    yakozen "Mas veja só quem está aqui."
    
    show noname at left with dissolve
    show yakozen err
    
    yakozen "Hm, pensei que era a Pam. Quem é você?"
    
    show noname envergonhada
    noname "Ah, e-eu me chamo Noname."
    
    show yakozen
    yakozen "Noname? Muito prazer, Noname, eu me chamo Yakozen."
    show yakozen err
    yakozen "É uma pena que não posso ir até aí te dar um aperto de mão, como qualquer pessoa educada faria. Espero que entenda minha situação."
    
    show noname
    show yakozen
    yakozen "Me diga, Noname, o que te traz até a prisão do Onigiri? Normalmente a Pam não me deixa receber visitas, por acaso hoje é meu aniversário?"
    show yakozen err
    yakozen "Faz alguns meses que estou aqui, aí acabei perdendo a noção do tempo."
    
    menu:
        "Não sei se é seu aniversário, mas hoje é dia 30 de Julho de 2017. Eu vim aqui porque eu acho muito estranho o Onigiri ter uma prisão.":
            jump naoYakozen1
        "Não sei se é seu aniversário, mas hoje é dia 30 de Julho de 2017. E a Pam realmente não tinha me deixado vir...":
            show noname err
            jump continuaYakozen1
            
    label naoYakozen1:
        yakozen "Eu também confesso que uma prisão no subsolo de um prédio é algo bem esquisito. Acho que aqui era pra ser uma garagem, mas devem tê-la adaptado por minha causa."
        show noname hm
        noname "A Pam me disse que você atacou o Onigiri ano passado. Por que fez isso?"
        yakozen "Não é óbvio?"
        show noname err
        show yakozen malvado
        yakozen "A Pam disse que eu ataquei o Onigiri e não falou quais eram as minhas intenções? Ou você está se fazendo de tola? Minha flor, eu ape-"
        
        label aparecePamYakozen:
            show pam seria at center
            pam "PARADOS! Vocês dois aí! Noname, eu te pedi para não visitar o Yakozen! Ele é um cara perigoso."
            show yakozen aff
            yakozen "Tinha que ser a estraga prazeres..."
            show noname surpresa
            show pam naocreio
            pam "Francamente, esses novatos só se metem em enrrascadas. Vamos embora daqui, Noname."
            noname "Pam, desculpa, eu só..."
            show pam facepalm
            pam "Não é pra mim que você vai se explicar, é pra Sii."
        
            scene recepcao1 with dissolve
            show sii at right
            show recepcao2
            
            show noname err at center
            show pam naocreio at left
            
            pam "Sii..."
            show sii err
            sii "Xii... Tava com o Yakozen também?"
            show pam facepalm
            pam "Eu acho que não sei explicar o quanto o Yakozen é perigoso. Pode me dar uma força?"
            show sii opa
            sii "Claro, fofa, vai lá cuidar da sua vida, beber uma água... Eu cuido a partir daqui."
            
            hide pam with dissolve
            show noname chorando
            noname "Sii, eu não queria dar problemas pra Pam. Me perdoe, eu só estava curiosa."
            show sii err
            sii "Tudo bem, querida. Eu sei que desperta a curiosidade de todo mundo ter um vilão perigoso aqui, não numa prisão de verdade."
            show sii feliz
            sii "Mas o Onigiri tem muitas pessoas bem fortes, como rangers, paladinos, sereias, magos elementais, pessoal que treinou com super sayajins... E sempre tem aquele povo criativo com planos mirabolantes."
            sii "Por isso que é melhor manter um vilão desse porte aqui no Onigiri. As pessoas mais forte da blogosfera estão tudo aqui por perto."
            show sii competitiva
            sii "Qualquer emergência, eles {i}VUASH{/i}, e aparecem pra nos socorrer!"
            noname "Mas desculpa ter causado problemas..."
            show sii opa
            sii "Tá tudo bem, querida, tá tudo bem... A Pam não está brava com você, ela só está cansada e estava preocupada com a sua segurança. Vai lá pro seu quarto, descansar, limpar essa cara, ok?"
            noname "O-ok..."
            show sii feliz
            sii "Qualquer coisa, leva a Pam no Neko Party e compra um milkshake pra ela! Ela adora o de morango!"
            show noname feliz
            noname "Tá! Brigada, Sii."
            hide noname with dissolve
            show sii opa
            sii "Esses novatos, viu?"
            
            jump noname
            
        label continuaYakozen1:
            show yakozen malvado
            yakozen "Ela não te deixou vir e, mesmo assim, você veio pra cá?"
            show yakozen
            yakozen "Por que esse interesse em me conhecer? Ela deve ter te avisado quem eu sou, não?"
            show noname mas
            menu:
                "Avisou... Mas eu achei estranho a história dela":
                    jump continuaYakozen2
                "Avisou... Mas eu queria ver com meus próprios olhos quem era você.":
                    jump naoYakozen2
                    
            label naoYakozen2:
                show yakozen malvado
                yakozen "Ohhh... Você não conhece o ditado que a curiosidade matou o gato, não é mesmo?"
                show noname err
                yakozen "Vir aqui por sua própria conta e risco é realmente uma tolice de sua parte, Noname. Eu deve-"
                
                jump aparecePamYakozen
            
            label continuaYakozen2:
                yakozen "Estranho? O que ela te contou?"
                noname "Ela me disse que encontrou você no meio de uma floresta vendendo casacos... Eu achei bizarro."
                yakozen "Casacos? Hahahahahahaha"
                show yakozen err
                yakozen "Aqueles itens mágicos podiam ser qualquer coisa, mas não \"apenas\" um casaco."
                show noname surpresa
                noname "Então você realmente tinha montado uma barraca no meio da floresta?"
                show yakozen
                yakozen "Não era \"no meio de uma floresta\", era um ponto estratégico de encontro de criaturas mágicas."
                yakozen "Se não me engano, a Pam tinha acabado de iniciar seu treinamento como bruxa, e foi até mim procurar uns catalisadores."
                yakozen "Então vendi à ela um casaco de proteção, que reflete projéteis."
                show noname surpresa
                noname "Então por que ela fala que era só um casaco?"
                show yakozen err
                yakozen "Se ela não sabe usá-lo, a culpa não é minha..."
                show yakozen
                yakozen "O que mais ela contou ao meu respeito?"
                show noname
                
                menu:
                    "Ela disse que você atacou o Onigiri ano passado.":
                        jump continuaYakozen3
                    "Ela disse que você é um cara mal.":
                        jump naoYakozen3
                        
                label naoYakozen3:
                    yakozen "Não entendo por que vocês dividem as pessoas em alinhamentos, como bem e mal. Mas..."
                    yakozen "Mesmo ela te avisando isso, você veio aqui para conversar comigo?"
                    show noname mas
                    noname "Sim, eu queria ver com meus próprios olhos se era realmente isso..."
                    jump naoYakozen2
                    
                label continuaYakozen3:
                    yakozen "Ela está absolutamente certa."
                    show noname mas
                    noname "Por que fez isso?"
                    yakozen "O que a Pam te contou?"
                    noname "Ela disse que você fez isso para vender partes do corpos dos moradores para o mercado negro..."
                    show yakozen err
                    yakozen "Órgãos, mais precisamente."
                    show noname err
                    noname "Sua motivação foi apenas dinheiro? Eu imaginava que você, como criatura mágica, não se importava com dinheiro."
                    yakozen "Depois de alguns anos, o dinheiro realmente perde o valor. Especialmente quando sua idade começa a ter quatro casas decimais."
                    show yakozen
                    show noname hm
                    yakozen "Mas eu não fiz pelo dinheiro. Eu não sou um dragão para ficar colecionando jóias e itens preciosos."
                    yakozen "Havia um homem que já tinha tentado atacar o Onigiri outras vezes."
                    show yakozen err
                    yakozen "Quer dizer, era mais um fantoche, o homem era quem estava sendo controlado, enfim."
                    show yakozen
                    yakozen "E ele tinha a ambição de criar um exército de quimeras, ou copycats, como ele chamava, e atacar a blogosfera como um todo, incluindo o Onigiri."
                    yakozen "O Onigiri é só uma grande concentração de pessoas, que é mais fácil pra juntar as partes das quimeras."
                    show noname
                    noname "Mas como aqui tem muita gente, tem muita gente que é bem forte também, né não?"
                    show yakozen err
                    yakozen "Sim, eu não estava contando com essa. É por isso que continuo preso."
                    
                    menu:
                        "Então você é só um lacaio desse cara?":
                            jump continuaYakozen4
                        "Então você foi com muita sede ao pote, subestimando as pessoas?":
                            jump continuaYakozen4
                    
                    label continuaYakozen4:
                        show yakozen aff
                        yakozen "Como assim?"
                        show noname mas
                        noname "Quer dizer, você só ouviu um cara qualquer, querendo fazer uma bagunça qualquer, que talvez nem era do seu interesse, não investigou seus inimigos e simplesmente atacou?"
                        yakozen "..."
                        noname "Bem..."
                        show yakozen err
                        yakozen "Falando assim, você me faz parecer um idiota..."
                        show noname mas
                        noname "Desculpa, não foi minha intenção!"
                        yakozen "Tudo bem, eu entendi o que quis dizer. Você acha que eu deveria ter esperado mais tempo para tomar alguma ação, não é mesmo?"
                        show noname
                        noname "Não é só esperar mais tempo, mas estudar também, pra você não ser capturado de novo por burrice."
                        noname "Independente da situação, você sempre se preparar bem, estudar bastante, pra minimizar seus erros."
                        show yakozen
                        yakozen "Eu gosto de como você pensa."
                        show noname envergonhada
                        show yakozen malvado
                        yakozen "O que você faria se tivesse ouvindo um cara falando de querer destruir a blogosfera?"
                        show noname err
                        
                        menu:
                            "Mas eu não quero destruir a blogosfera! Eu moro nela, quero viver minha vidinha em paz!":
                                jump continuaYakozen5
                            "Eu ia chamar a polícia, sem nem pensar duas vezes.":
                                jump naoYakozen4
                                
                        label naoYakozen4:
                            show yakozen aff
                            yakozen "Que original..."
                            noname "O que? Esse cara deve ser doente, sei lá. Se ele quer destruir a blogosfera, onde é que ele ia viver?"
                            show yakozen err
                            yakozen "As vezes a pessoa simplesmente não liga pra isso, só quer passar uma mensagem."
                            show noname
                            noname "Se ele destruir todo mundo, não vai ter ninguém para receber a mensagem, ora bolas."
                            show yakozen aff
                            yakozen "É o processo, minha flor. O processo da destruição que deixa as pessoas em alertas e..."
                            yakozen "Eu não vou mais perder meu tempo com você."
                            show yakozen err
                            yakozen "Você definitivamente não sabe o que faz."
                            show yakozen malvado
                            show noname err
                            yakozen "Talvez eu devesse..."
                            
                            jump aparecePamYakozen
                            
                        label continuaYakozen5:
                            show yakozen
                            yakozen "Você tem um ponto."
                            show noname
                            noname "Se você quer só destruir tudo para as pessoas ficarem com medo de você, ok, não é da minha conta. Mas eu quero ter uma boa vidinha."
                            show yakozen err
                            yakozen "Confesso que era essa a minha vontade mesmo."
                            show yakozen malvado
                            yakozen "Ver nos olhos dos outros o medo apenas por sentir a minha presença. Essa sensação de poder..."
                            show yakozen err
                            yakozen "Mas deu errado e estou aqui."
                            show noname mas
                            noname "Isso explica o motivo de você usar esse kimono de morte?"
                            show yakozen
                            yakozen "Sim, eu roubei da morte há alguns anos. Ela tinha deixado na lavanderia e sequer percebeu a falta."
                            noname "Que furtivo você."
                            yakozen "Meu animal não é uma raposa à toa."
                            
                            show noname surpresa
                            noname "Você pode virar uma raposinha!?"
                            yakozen "Hhaahahahaha"
                            yakozen "Raposinha não, um senhor raposa gigante pra você, minha flor."
                            show noname err
                            noname "Por que você não vira uma agora pra fugir daqui?"
                            show noname
                            yakozen "Eu já tentei, mas essas grades são mágicas. A Pam realmente fez um ótimo trabalho aqui."
                            noname "Bom, então você precisa de um plano pra roubar as chaves dela, não?"
                            show yakozen err
                            yakozen "Você não quer que eu fuja, quer?"
                            noname "Seu objetivo não é destruir tudo, só que as pessoas te respeitem como uma criatura mística, não?"
                            
                            show yakozen aff
                            yakozen "..."
                            
                            menu:
                                "Eu tinha visto em algum filme que antigamente lobos e raposas eram verdadeiros deuseus, que ajudava a humanidade com seus poderes mágicos. Você já foi um deus?":
                                    jump continuaYakozen6
                                "Eu tinha visto em algum filme que raposas geralmente são associadas a furto, roubo e talz só porque são raposas, mesmo que na verdade elas tenham boas intenções. É o seu caso?":
                                    jump naoYakozen5
                                    
                            label naoYakozen5:
                                show yakozen err
                                yakozen "Não, não é o meu caso."
                                show yakozen
                                yakozen "Se você realmente achou que vindo aqui conversando comigo iria me convencer a ser uma pessoa \"boa\", você é inocente demais."
                                show yakozen malvado
                                show noname err
                                yakozen "Talvez eu devesse..."
                                
                                jump aparecePamYakozen
                                
                            label continuaYakozen6:
                                show yakozen envergonhado
                                yakozen "..."
                                show noname feliz
                                noname "Então você era um deus?"
                                show yakozen
                                yakozen "Não exatamente..."
                                noname "Então você era servo de um?"
                                yakozen "Mais ou menos..."
                                noname "Era aquelas raposas que pregavam peças, né?"
                                show yakozen err
                                yakozen "Não fale dessa maneira que é muito simplista."
                                yakozen "Mas digamos que..."
                                show yakozen envergonhado
                                yakozen "Que eu era uma dessas raposas, só que deu errado."
                                show noname mas
                                noname "Como assim que deu errado?"
                                yakozen "Normalmente as \"kitsune\", como somos chamados, são mulheres. Eu no caso sou homem."
                                show yakozen err
                                yakozen "Então nem pelas minhas próprias irmãs eu sou respeitado."
                                noname "Kitsunes podem mudar a forma?"
                                yakozen "Podem..."
                                noname "Vira uma mulher, então."
                                show yakozen aff
                                yakozen "Não é por nada não, mas eu prefiro ser como eu sou, obrigado."
                                show noname err
                                noname "Ops..."
                                show yakozen
                                yakozen "Hahaha, está tudo bem. Não é tão ruim falar disso com alguém."
                                
                                show noname
                                menu:
                                    "Bom, você já pensou em lutar contra suas irmãs, então?":
                                        jump continuaYakozen7
                                    "E se ao invés de destuir as coisas, se você assombrasse as pessoas?":
                                        jump naoYakozen6
                                        
                                label naoYakozen6:
                                    yakozen "Eu tenho cara de Gasparzinho?"
                                    show noname
                                    noname "Foi só uma ideia..."
                                    yakozen "Noname, eu imagino que sua intenção de vir aqui foi me conhecer para ver se eu realmente era aquele cara \"mal\" que todo mundo te falou."
                                    show yakozen
                                    yakozen "E eu realmente sou. Eu não tenho intenção de assombrar as pessoas, como toda e qualquer kitsune, meu objetivo é muito maior que esse."
                                    show noname err
                                    yakozen "Apesar de ter rido de mim e de minhas histórias, você também não foi muito esperta em vir."
                                    
                                    jump aparecePamYakozen
                                    
                                label continuaYakozen7:
                                    yakozen "E causar o maior desiquilíbrio no mundo espiritual?"
                                    show noname hm
                                    noname "É o mundo espiritual, não o meu mundo. E foi só uma sugestão."
                                    show noname mas
                                    noname "E sem falar que, pela sua cara, meio que foi as suas irmãs que começaram a te pertubar e a te não respeitar."
                                    noname "A blogosfera não tem nada a ver com sua briguinha de família."
                                    
                                    show yakozen malvado
                                    yakozen "Confesso que a ideia não é ruim."
                                    
                                    show yakozen
                                    yakozen "Sabe, Noname, desde que você chegou aqui, eu sinto que você tem algo de diferente."
                                    show noname envergonhada
                                    yakozen "Diferente do pessoal do Onigiri, você conversa abertamente comigo. Sou muito grato pela sua atenção."
                                    show noname envergonhadissima
                                    yakozen "Prometo que se você encostar na grade, nada vai acontecer com você, já que você não tem magia. Porém, pode chegar mais perto?"
                                    noname "O-ok..."
                                    hide noname
                                    show noname envergonhadissima at center
                                    show yakozen envergonhado
                                    yakozen "Então, eu já não tenho muita noção do tempo porque já estou nesse mundo faz tempo já."
                                    yakozen "Mas acho que conversar com você foi um dos momentos mais preciosos que já tive nesses últimos anos."
                                    show yakozen
                                    yakozen "Tirei uns pesos das costas, desabafei também. Você é uma pessoa incrível, sabia?"
                                    show yakozen envergonhado
                                    yakozen "Queria achar uma forma de fazer você entender o quanto eu sou grato por essa conversa."
                                    show noname envergonhada
                                    noname "Ta-talvez... Ahn..."
                                    show yakozen
                                    
                                    show cs yakozen1 with dissolve
                                    pause(3.0)
                                    show cs yakozen2 with dissolve
                                    yakozen "Você sabe muito bem que kitsunes também conseguem possuir humanos, não sabe?"
                                    noname "Quê?"
                                    
                                    show black with Dissolve(3.0)
                                    pause(3.0)
                                    pam "Essa não... SIIIIII!!! SOCORRO! O YAKOZEN CONSEGUIU FUGIR!"
                                    jump fim
                                    
                            