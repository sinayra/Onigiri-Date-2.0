label sii:
    $perguntasSii = [1, 1, 1]
    scene recepcao1 with dissolve
    
    show sii at right
    show recepcao2
    
    show noname at left with dissolve
    
    sii "Noname! Dando um passeio pelo prédio?"
    noname "Sim, estou querendo conhecer mais sobre o lugar. E também, tenho algumas dúvidas."
    
    show sii naosei
    
    sii "Diga lá."
    
    show sii
    
    label perguntasSii:
        menu:
            "Quem são os crushs?" if perguntasSii[0] == 1:
                jump crushsSii
            "Quem são meus amigos?" if perguntasSii[1] == 1:
                jump amigosSii
            "Se eu errar uma escolha, posso voltar?" if perguntasSii[2] == 1:
                jump voltaSii
            "Acho que não tenho mais perguntas, para falar a verdade...":
                jump exibeCrushsSii
    
    label amigosSii:
        $perguntasSii[1] = 0
        sii "Seus amigos são os personagens com o nome em laranja. Ou seja, eu, o Jack, a Yuzu e a Pam."
        show sii opa
        sii "Cada amigo é meio que uma etapa anterior para você chegar no crush, então não precisa ser incoveniente com eles, né?"

        show sii
        jump perguntasSii
        
    label voltaSii:
        $perguntasSii[2] = 0
        show sii err
        sii "Oxe, não, só se eu deixei isso quando publiquei o jogo. "
        
        show sii
        jump perguntasSii
        
    label exibeCrushsSii:
        menu:
            "Acho que agora vou dar um passeio no prédio, que até agora só fui no meu bloco, no meu quarto e nessa recepção.":
                jump jack

            "Vou procurar a área de lazer aqui.":
                jump pam
            
            "Tinha um Neko Café lá fora, né? Acho que vou dar um pulo lá.":
                jump yuzu
                
    label crushsSii:
        $perguntasSii[0] = 0
        
        sii "Quando um crush falar alguma coisa, o nome dele vai estar em azul. Neste jogo, os crushs são os personagens originais do Onigiri, que são o Kuroi, o Morango e o Yakozen."
        
        show sii opa
        
        sii "Kuroi é o mensageiro do Onigiri. Apesar dele sempre mandar mensagens automáticas pro pessoal, nesse jogo ele é uma pessoa normal."
        sii "Morango é um robô que foi construído no minigame Zettai Kareshi, com intuito de ser o namorado perfeito. Porém, ele ficava muito triste por não ter namorada, então desliguei os sentimentos dele."
        sii "Yakozen é um cara do mal que está preso no subsolo do Bloco G. A Pam guarda as chaves da prisão dele porque... Meio que foi culpa dela do Yakozen ter soltado um exercíto zumbi ano passado."
        
        show sii
        menu:
            "Eu sou obrigada a escolher um deles?":
                jump obrigacaoSii

            "Só existem essas opções?":
                jump opcoesSii
        
            
        label obrigacaoSii:
            show sii opa
        
            sii "Bom, não exatamente. Ainda tem um final onde você pode só ficar de boa na lagoa."
            
            show sii
            jump perguntasSii
                
        label opcoesSii:
            show sii competitiva
            sii "Eu já deveria esperar uma pergunta dessa. Não, existe mais uma opção, mas ela é secreta."
            
            show noname mas
            noname "Secreta? Como assim?"
            
            show sii
            sii "Ao invés de aparecer com a cor azul, o crush secreto está disfarçado de amigo, então o nome dele estará em laranja."
            
            show noname surpresa
            noname "Sério?? Mas como vou saber se ele vai poder ser meu crush ou não?"
            
            sii "Tenha uma conversa amigável com ele, ora bolas."
            show noname
            
            menu:
                "Então você é um crush secreto, Sii?":
                    jump naoSii
                "Bom, seu cabelo é bonito.":
                    jump nao2Sii
                "Quantas vezes você já teve essa conversa comigo?":
                    jump continuaSii1
                    
            label naoSii:
                show sii err
                sii "Ahnn... Não... Eu só quebro a quarta parede desse jogo pra poder te ajudar."
                noname "Ah, entendi..."
                
                show sii
                jump perguntasSii
                    
            label nao2Sii:
                show sii feliz
                sii "Obrigada! As pessoas sempre desenham esse meu rabo de cavalo menor do que ele é realmente é, mas eu adoro meu cabelo também!"
                show noname feliz
                sii "..."
                noname "..."
                show sii
                show noname
                
                jump perguntasSii
                
            label continuaSii1:
                show sii naosei
                sii "Se você contar as vezes que tive que testar mais as vezes que o player tá jogando esse jogo... Algumas muitas vezes."
                
                show noname surpresa
                noname "É bem difícil ter que ficar testando jogo, né?"
                sii "Nem me fale. Pior mesmo foi o tempo, queria ter trabalhado melhor nesse jogo."
                
                menu:
                    "Melhor como?":
                        jump continuaSii2
                    "Do jeito que está, tá bom, não tá não?":
                        jump nao3Sii
                        
                label nao3Sii:
                    show sii opa
                    sii "Não, nossa, nem um pouco. Primeiro eu entreguei esse jogo atrasado, segundo que não consegui usar todos os recursos que a Yuzu e a Nallu fizeram..."
                    show sii err
                    sii "E outro que eu queria ter feito aquele esquema de dia, um mês para conquistar o crush e talz..."
                    
                    show noname hm
                    noname "Ah, ia ser bem legal se tivesse isso..."
                    sii "Não é?"
                    
                    show noname feliz
                    noname "Mas acho que o jogo do jeito que tá está bom, de verdade!"
                    sii "..."
                    
                    show sii
                    show noname
                    jump perguntasSii
                    
                label continuaSii2:
                    show sii feliz
                    sii "Eu queria ter colocado aquele esquema de dia, da pessoa ter um mês pra conquistar o crush, aprender os gostos dele, ter mais crushs secretos..."
                    show noname feliz
                    noname "Nossa, ia ser bem legal mesmo! Mas aí não ia dar pra jogar numa tarde, né não?"
                    
                    show sii talvez
                    sii "Hm, talvez..."
                    noname "Mas pra compensar isso, já que não deu tempo, você podia botar uns diálogos mais complexos entre os personagens, umas opções meio ambíguas também."
                    
                    show sii feliz
                    sii "Nossa, é mesmo!"
                    
                    show noname mas
                    noname "Mas aí não sei o quão complicado fica pra você fazer essas opções ambíguas..."
                    
                    show sii competitiva
                    sii "Isso é o de menos! Eu primeiro aceito a ideia e depois me viro pra fazer a ideia virar algo concreto."
                    
                    menu:
                        "Como você é determinada!":
                            jump nao4Sii
                        "Mas e se a ideia for complicada demais?":
                            jump continuaSii3
                        
                    label nao4Sii:
                        show noname feliz
                        show sii feliz
                        
                        sii "Eu me esforço! Hunf!"
                        
                        show noname
                        show sii
                        jump perguntasSii
                        
                    label continuaSii3:
                        show sii feliz
                        sii "Aí peço ajuda, paciência da galera, que se estressar pro negócio não adianta nada."
                        show noname feliz
                        noname "Tem razão, né? Então, e se..."
                        
                        menu:
                            "E se você fizesse um crush que na verdade é meio amigão?":
                                jump continuaSii4
                            "E se você fizesse um crush que você não se declara pra ele?":
                                jump continuaSii4
                                
                    label continuaSii4:
                        show sii naosei
                        sii "Como assim?"
                        
                        show noname hm
                        noname "Tipo, que você só vira amigo dele mesmo, ao invés de dar uns beijinhos e ele ser o amor da sua vida."
                        
                        sii "Tipo friendzone?"
                        
                        menu:
                            "Não exatamente, mas que o amor deles fosse algo mais inocente, sabe?":
                                jump continuaSii5
                            "Isso, tipo friendzone":
                                jump nao5Sii
                                
                        label nao5Sii:
                            sii "Hm, é algo de se pensar..."
                            show sii err
                            sii "Mas eu mesma não gosto dessa ideia de friendzone, sabe? Tem uns caras que fazem um drama demais com isso, mas ideia dele ser a fim da moça e ela nem {i}tchum{/i} pra ele é meio triste..."
                            
                            show noname
                            show sii
                            
                            jump perguntasSii
                            
                        label continuaSii5:
                            sii "Ahhh, tipo eles tarem batendo papo normal, assim, de boa, sendo amigos, e um deles ficar apaixonadinho tipo {i}uêpa{/i}?"
                            show noname feliz
                            noname "Tipo isso!"
                            show sii feliz
                            sii "Eu adoro esse tipo de amorzinho! Amei a ideia!"
                            noname "Que bom que gostou!"
                            
                            sii "A gente podia conversar mais sobre isso lá no Neko Café da Yuzu, que acha? Ou você é alérgica a gatos?"
                            
                            show sii err
                            sii "Que é melhor do que a gente aqui em pé discutindo isso, meu joelho já já me mata."
                            
                            menu:
                                "Podemos deixar pra próxima? Acho que quero andar mais um pouco pelo prédio.":
                                    jump nao6Sii
                                "Pode ser.":
                                    jump continuaSii6
                                    
                            label nao6Sii:
                                show sii feliz
                                sii "Claro, fofa, mais tarde você passa aqui então?"
                                show noname feliz
                                noname "Passo sim!"
                                
                                jump exibeCrushsSii
                                
                            label continuaSii6:
                                hide recepcao2
                                hide noname
                                hide sii
                                
                                scene bg cafe with dissolve
                                
                                show yuzu at center
                                yuzu "Bem-vindas ao Neko Party!"
                                show yuzu feliz
                                yuzu "Hoje o casal tá recebendo desconto, hein? Se pedir um milkshake, o segundo sai de graça!"
                                
                                show yuzu feliz at right
                                show noname envergonhada at left
                                show sii feliz at center
                                
                                sii "Opa, bom saber! Noname, qual milkshake você vai querer? Deixa que eu pago, já que você acabou de chegar no Onigiri."
                                noname "Hã? Casal? Não não, deixa que eu pago o meu, Sii, preocupa com isso não."
                                sii "Então eu vou escolher um pra você."
                                show sii
                                sii "Yuurei, o meu eu vou querer de banana com caramelo e, como a Noname tá com mimimi, o dela é de ovomaltine."
                                show sii opa
                                sii "Você gosta de ovomaltine, né?"
                                show noname envergonhadissima
                                noname "Gosto, mas, calma, não precisa pagar pra mim, é sé-"
                                show sii feliz
                                sii "Ufa, então o dela é de ovomaltine mesmo!"
                                yuzu "Anotado! Vão querer algo mais?"
                                show sii
                                sii "Acho que não por agora, mais tarde a gente vê o que vamos comer."
                                show yuzu
                                yuzu "Ok!"
                                show yuzu conselho
                                yuzu "Noname-chan, não fique tão preocupada com o desconto de casal, viu? É só uma promoçãozinha, e a parte do \"casal\" você pode levar na brincadeira."
                                show sii feliz
                                sii "E eu sei que é chato aceitar comida dos outros, mas aceite, você é uma pessoa bacana. Não é como se fosse me custar a mais por isso."
                                show noname envergonhada
                                noname "T-tá..."
                                
                                hide yuzu
                                
                                show sii
                                sii "Bom, enquanto o milkshake não chega, deixe-me perguntas umas coisas..."
                                show noname
                                sii "Como exatamente que o crush ficaria apaixonado pelo player? Que o player tá conversando de boa com o crush amiguinho lá, né, sem desconfiar de nada."
                                noname "Ah sim. Bom... Você tá fazendo o jogo do Onigiri quase Prédio, né?"
                                show sii naosei
                                sii "Sim, que é esse jogo que estamos agora. E aí?"
                                
                                menu:
                                    "Bom, então o player vai conversando sobre coisas banais com ele, sabe? Tipo, se ele precisa de ajuda na mudança, se ele quer entrar no quarto pra tomar um café, ou comer um... Miojo? Ou sei lá.":
                                        jump continueSii7
                                    "Bom, então o crush podia, sem intenção de nada, convidar o player pra dar um passeio pelo Onigiri. Conhecer o resto do prédio, se tem áreas de lazer ou não...":
                                        jump continueSii7
                                
                                label continueSii7:
                                    sii "Sim... E aí?"
                                
                                    menu:
                                        "Aí o crush acaba vendo que o player é uma pessoa bacana. Tipo {i}essa pessoa é bacana, a gente podia sair juntos pra algum lugar pra passar um tempo{/i}, aí convida o player pra tipo um fliperama, ou até mesmo um cinema.":
                                            jump continueSii8
                                        "Aí o crush pode acabar fazendo alguns favores pro player, tipo comprar uns presentinhos bobos, como ímã, chaveirinho, caneta... Algo que não seja tão óbvio.":
                                            jump continueSii8
                                
                                label continueSii8:
                                    show sii competitiva
                                    
                                    sii "Aham... Entendi. E aí?"
                                    
                                    noname "Bom, se ele fizer isso, ele já vai estar apaixonado pelo player, né?"
                                    
                                    show sii feliz
                                    sii "Concordo."
                                    noname "Aí o jogo poderia acabar nisso. Que dá um final fofinho, eu acho."
                                    
                                    show sii opa
                                    sii "Ah, jura?"
                                    show noname err
                                    noname "Gostou não?"
                                    
                                    show sii err
                                    sii "Ah, é muito anti-climático acabar assim... Podia acabar com o crush mostrando que ele tá a fim do player, né?"
                                    
                                    show noname
                                    noname "Ah, não sei... Acho que quem vai estar jogando meio que já vai saber, mas o personagem que ele tá controlando não sabe, aí fica aquelas historinhas de shoujo, sabe?"
                                    
                                    sii "Daqueles shoujos que os dois personagens se gostam mas levam trocentos episódios pra segurar a mão do outro?"
                                    
                                    show noname feliz
                                    noname "Ééééé! É tão fofinho e inocente."
                                    
                                    show sii opa
                                    sii "Ah não... Eu sempre fico meio frustada com esses shoujos..."
                                    show noname
                                    noname "Então o que você sugere?"
                                    
                                    show sii competitiva:
                                        xpos 0.48
                                    
                                    sii "Então... O crush podia ter convidado o player pra sair, como você tinha falado."
                                    noname "Certo."
                                    
                                    show sii talvez:
                                        xpos 0.45
                                    
                                    sii "Aí, ok, eles vão pra um lugar tranquilinho, bem amigável, família, e pah..."
                                    show noname envergonhada
                                    
                                    show sii talvez:
                                        xpos 0.43
                                    
                                    sii "Aí o crush podia falar algo como {i}depois daqui eu podia te ajudar com sua mudança, ou te apresentar ao pessoal daqui, todo mundo é muito gente fina{/i}. Mesma coisa que você tinha falado."
                                    noname "Aham..."
                                    
                                    show sii talvez:
                                        xpos 0.41
                                    sii "{i}Ou então a gente, sei lá, tá de tarde ainda, dá pra ir no shopping, a gente podia fazer alguma outra coisa. Tem carteirinha de estudante ainda? Podíamos ver o que tá passando no cinema.{/i}"
                                    sii "E então o player aceitava, né, que ele não é bobo, sabe o que tá acontecendo..."

                                    
                                    show sii competitiva
                                    sii "E então..."
                                    show noname envergonhadissima
                                    noname "Então?"
                                    
                                    pause(1.0)
                                    show sii naosei with ease
                                    sii "Não sei... Perdi o fio da meada."
                                    show noname err
                                    noname "Jura????"
                                    
                                    pause(1.0)
                                    show sii competitiva with ease
                                    
                                    show cs sii with dissolve
                                    sii "Você é uma fofa, sabia?"
                                    noname "SII! Não, calma, que-que você tá faze-endo, wah, va-va-vamos com calma, wah."
                                    
                                    jump fim
                                    
                                
                                

                                