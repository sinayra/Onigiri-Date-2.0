label kuroi:
    scene corredor with dissolve
    
    show noname mas at left
    noname "Hm... Será que foi um problema eu me inscrever diretamente com a Sii? Acho que o Kuroi pareceu um pouco incomodado com isso..."
    noname "Hm..."
    hide noname
    
    "Noname acaba esbarrando com alguém que também estava distraído no corredor"
    
    show noname err
    noname "Nossa! Perdão, eu estava completamente distraída!"
    show kuroi preocupado at right
    kuroi "Wáh, nossa, Noname, você está bem?"
    show noname surpresa
    noname "Kuroi, desculpa! Eu juro que não vi você."
    show noname mas
    noname "Nossa, as cartas do pessoal! Caiu tudo, deixa eu te ajudar."
    kuroi "Não não, Noname, calma, não precisa me ajudar não, tá tudo bem."
    
    hide noname
    hide kuroi
    
    "Noname acaba juntando as cartas e as entrega pro Kuroi"
    
    show noname mas at left
    show kuroi preocupado at right
    
    noname "Pronto, são só essas cinco mesmo? Tem mais nenhuma outra escondida?"
    kuroi "Não não, só são essas. É que essas cartas são as que tenho que entregar hoje pra esse bloco."
    
    show noname feliz
    menu:
        "Você quer ajuda? Aí eu aproveito e descubro como é mais ou menos o Onigiri e a rotina do pessoal daqui.":
            jump continuaKuroi1
        "Cinco dá pra terminar rapidinho, né? Depois de entregá-las, o que vai fazer?":
            jump naoKuroi1
            
    label naoKuroi1:
        show kuroi desconfiado
        kuroi "Bom, ainda não sei... Mas acho que eu vou voltar pro meu casebre."
        show noname mas
        noname "Ah, entendi..."
        show kuroi preocupado
        kuroi "É que eu tenho que fazer faxina ainda, desculpa..."
        show noname
        noname "Tudo bem, eu ainda tenho que dar um jeito no meu quarto também. Bom, boa sorte!"
        noname "Ah, o Jack falou pra você parar de procurar trabalho!"
        show kuroi feliz
        kuroi "Hahaha, típico, ele sempre se preocupa demais comigo. Até mais, Noname!"
        noname "Até!"
        
        jump noname
        
    label continuaKuroi1:
        kuroi "Não, não, não se preocupe com isso. Eu termino rapidinho aqui, juro. Você deve estar longe do seu apartamento, não?"
        noname "Não me custa nada, e além do mais, eu moro nesse bloco, só que no apartamento 250. Vamos, me entregue a metade."
        kuroi "Bom, não ia ser ruim acabar mais cedo... Ok, essas são as cartas dos apartamentos 252 e 253, é só deixar na caixinha mesmo."
        noname "Sem problemas!"
        
        scene corredor with dissolve
        "Noname colocou as duas cartas nas caixa de correio dos apartamento 252 e 253."
        show noname
        noname "Bom, resolvido. Difícil deve ser ter que andar pelos blocos, mas o trabalho de entregar cartas até que é bem tranquilo."
        hide noname
        show noname at left
        show kuroi at right with dissolve
        kuroi "Noname! Tudo certo?"
        show noname feliz
        noname "Tudo sim, Kuroi. Cartinhas entregue, senhor!"
        show kuroi feliz
        kuroi "Obrigado. Agora só falta essa do 260 e termino por hoje."
        
        menu:
            "Posso ir com você?":
                jump naoKuroi2
            "Bom, eu não tenho nada o que fazer agora. Posso te acompanhar até lá te pertubando sobre o Onigiri? É só mais alguns andares pra cima, né?":
                jump continuaKuroi2
                
        label naoKuroi2:
            show kuroi preocupado
            kuroi "Não precisa, Noname, já abusei demais da sua boa vontade. Sem falar que você ter um monte de problema de mudança pra resolver ainda, né?"
            noname "Eu realmente não me incomodo, Kuroi. Quero saber mais sobre você."
            show kuroi desconfiado
            kuroi "Perdão, Noname. É que hoje eu tô um pouco atarefado e não quero ficar tomando seu tempo com meu trabalho. Na próxima a gente conversa mais, pode ser?"
            show noname mas
            noname "Ah, tudo bem então. Vou pro meu quarto, qualquer coisa me chama."
            show kuroi
            kuroi "Se eu precisar de uma ajudinha com as cartas de novo, eu te chamo sim."
            
            jump noname
            
        label continuaKuroi2:
            show kuroi feliz
            kuroi "Hahahaha, ok ok. Você é bem humorada. Vamos lá, o que você quer saber do Onigiri?"
            show noname
            noname "A primeira pergunta é: por que ele se chama \"quase prédio\"?"
            show kuroi
            kuroi "Essa aí todo mundo pergunta mesmo. Antigamente o Onigiri só tinha um bloco, então fazia sentido a parte do \"prédio\"."
            kuroi "O \"quase\" é por conta das síndicas, atualmente só temos a Sii, fazer brincadeiras todo domingo de temas variados, sendo bem mais ativo que os outros prédios da vizinhança. Daí veio o \"quase\"."
            kuroi "Só que hoje em dia o Onigiri tem altos blocos, ele deveria mudar o nome pra \"condomínio\"."
            noname "Concordo. Condomínio faz bem mais sentido."
            kuroi "Acho que a Sii só não muda pra não perder a sigla \"OQP\"."
            show kuroi desconfiado
            kuroi "E talvez por preguiça mesmo."
            show noname feliz
            noname "Coitada da Sii!"
            show kuroi duvido
            kuroi "Mas é que eu sei que ela deixa de fazer um monte de coisa por pura preguiça. Ela tá arrastando o projeto de medalhinha a meses, daqui a pouco esse projeto completa 1 ano e nada dele sair."
            kuroi "Faz, sei lá, 8 meses que ele tá nos 50\% e nunca saiu disso."
            noname "Você fala isso, mas você gosta bastante dela, né?"
            show kuroi
            kuroi "Bom, ela, a Kih, a Kane e a Sofi me aceitaram aqui de braços abertos, né? É meio como se eu tivesse 3 mães e uma irmã que me enche o saco."
            
            menu:
                "Como que você achou o Onigiri?":
                    jump continuaKuroi3
                "Três mães? Isso deve ter sido difícil, né?":
                    jump naoKuroi3
                    
            label naoKuroi3:
                show kuroi desconfiado
                kuroi "Ahn, não exatamente, eu sou muito grato à elas. É uma família normal, recebi amor, carinho, bronca, tudo normal."
                show noname hm
                noname "Ah, isso é ótimo."
                show kuroi
                
                label naoKuroiFim:
                    kuroi "Bom, chegamos. É esse apartamento aqui. Noname, obrigado pela companhia."
                    show noname feliz
                    noname "De nada, Kuroi! O que vai fazer agora?"
                    kuroi "Bom, eu acho que vou voltar pro meu casebre que tenho uma faxina a fazer. Você deve estar atolada de coisa pra arrumar por conta da mudança, né?"
                    show noname
                    noname "Sim sim... Bom, quando você tiver livre, me chama! Vamos fazer alguma coisa juntos."
                    kuroi "Chamo sim, Noname. Até!"
                    noname "Até!"
                
                    jump noname
                
            label continuaKuroi3:
                show kuroi surpreso
                kuroi "Ah, bom... Ele era um imenso prédio laranja, né? Cem andares bem no meio do nada, foi fácil achar."
                show noname
                noname "Isso você tinha quantos anos?"
                kuroi "Na época... Eu deveria ter uns 11... Estamos em 2017, né?"
                noname "Isso."
                kuroi "Tão eu tinha uns 11 anos mesmo."
                show noname surpresa
                
                menu:
                    "Nossa, você tá a tanto tempo assim no Onigiri?":
                        jump continuaKuroi4
                    "Onze anos? Você fugiu de casa com 11 anos?":
                        jump naoKuroi4
                        
                label naoKuroi4:
                    show kuroi duvido
                    kuroi "Errrr... É uma longa história... Eu..."
                    pause (1.0)
                    show kuroi desconfiado
                    kuroi "Eu prefiro não me aprofundar muito nela. Nada pessoal, Noname."
                    show noname mas
                    noname "Nossa, perdão, Kuroi, não queria ter tocado nesse assunto delicado."
                    show kuroi preocupado
                    kuroi "Tudo bem. Sou eu quem não é de falar muito sobre isso..."
                    
                    jump naoKuroiFim
                        
                label continuaKuroi4:
                    show kuroi feliz
                    kuroi "Agora que me toquei. Poisé, já estou a 6 anos no Onigiri..."
                    noname "Não tem nenhum plano pra ir embora não? Acho que não, né?"
                    show kuroi
                    kuroi "É... Acho que não, eu gosto daqui, do pessoal, sempre aparece alguém novo... Dá pra fazer muitos amigos aqui, isso é certeza."
                    show kuroi envergonhado
                    kuroi "E... Bom, o que você tá achando do Onigiri?"
                    show noname feliz
                    noname "Nossa, cheguei hoje e já conheci você, o Jack, a Sii. De fato a Sii é meio biruta falando sobre \"você é o personagem principal de um jogo\", mas o pessoal daqui parece bacana."
                    show kuroi feliz
                    kuroi "Hahahahahaha, essa história de jogo... Pior eram os planos do Nekozawa."
                    show noname hm
                    noname "Nekozawa?"
                    show kuroi
                    kuroi "Era um vilão que ficava importunando o pessoal do Onigiri. Desde que a Sii e o pessoal foi pra uma dimensão maluca pra resgastar a Kih, ele sumiu pra sempre."
                    kuroi "Os planos dele era tipo: \"Vou criar um exército importal para destruir o Onigiri!\" ou \"Vou fazer um quase prédio também\"."
                    show noname err
                    noname "Hã?"
                    show kuroi desconfiado
                    kuroi "Ele era meio biruta... Era uma Sii só que malvada."
                    kuroi "Tem ainda outro vilão, só que esse a Sii prendeu aqui no prédio, que é o Yakozen. Esse é mais perigoso."
                    show noname mas
                    noname "Mais perigoso? E por que ela o prende aqui?"
                    show kuroi duvido
                    kuroi "Acho que se prendesse em qualquer outro lugar, ele se libertaria de lá fácil fácil. Estando preso aqui, ele tá sendo mais bem vigiado."
                    noname "Você já foi atacado por algum desses vilões?"
                    show kuroi
                    kuroi "Não não, eu ajudo os outros moradores a irem pro abrigo anti-vilão aqui do prédio e fico com eles pra garantir que todo mundo tá bem e seguro."
                    show noname feliz
                    noname "Ah, entendi! Então você é tipo um ajudante dos herois!"
                    show kuroi envergonhado
                    kuroi "Não com esse nome... Mas, é, talvez ajudante mesmo."
                    show noname
                    noname "Kuroi, esse é o 260, né não?"
                    show kuroi surpreso
                    kuroi "Nossa, eu ia passando direito! Opa. Obrigado por avisar."
                    show noname feliz
                    noname "O Jack que você era uma pessoa tímida, mas até que você fala bastante!"
                    show kuroi envergonhado
                    kuroi "Ahn? Não não... Não é como se... Ahn... Quem ficou enchendo o saco foi eu, né? Desculpa..."
                    show noname surpresa
                    noname "Quê? Não não, eu que queria saber mais na furada que tô me metendo morando aqui, hahahahaha."
                    
                    show noname feliz
                    menu:
                        "Se você não tiver nada pra fazer agora, a gente poderia dar uma volta no prédio. Talvez comer alguma coisa, o que acha?":
                            jump continuaKuroi6
                        "Bom, então não vou mais te atrapalhar. Pode trabalhar sossegado agora, Kuroi! Até!":
                            jump continuaKuroi5
                    
                    label continuaKuroi5:
                        show kuroi preocupado
                        kuroi "Até..."
                        hide noname
                        pause (1.0)
                        show kuroi envergonhado
                        pause (1.0)
                        kuroi "..."
                        show kuroi preocupado
                        kuroi "Noname! Noname, rapidinho!"
                        
                        show noname surpresa at left
                        show kuroi envergonhado
                        kuroi "Bom, como você chegou hoje, talvez você não conheça muito a vizinhança, né? Você... Bom..."
                        kuroi "Se você não tiver nada o que fazer agora, a gente podia... Bom... Comer alguma coisa? Tem um Neko Café aqui do lado..."
                        show noname envergonhada
                        noname "Ah... Eu ia achar ótimo. Tem problema pra você não?"
                        show kuroi feliz
                        pause (0.5)
                        show kuroi envergonhado
                        kuroi "Não não, pra mim está tudo bem. O Neko Café é gerenciado pela Yuzu, que mora no Onigiri também. Você vai adorar ela."
                        
                        jump continuaKuroi7
                        
                    label continuaKuroi6:
                        show kuroi envergonhado
                        kuroi "Poxa, eu ia achar ótimo. Tem um Neko Café aqui do lado, o Neko Party. Conhece?"
                        show noname feliz
                        noname "Ah! Acho que vi ele quando eu tava na entrada do prédio. É bom?"
                        show kuroi feliz
                        kuroi "Sim, a Yuzu é dona dele. Ela também é moradora do Onigiri, você vai adorar ela!"
                        
                    label continuaKuroi7:
                        scene bg cafe with dissolve
                            
                        show yuzu at center
                        yuzu "Bem-vindos ao Neko Party!"
                        show yuzu feliz
                        yuzu "Hoje o casal tá recebendo desconto, hein? Se pedir um milkshake, o segundo sai de graça!"
                        
                        show yuzu feliz at right
                        show noname envergonhadissima at left
                        show kuroi envergonhado at center
                        
                        noname "Ahn? Casal?"
                        kuroi "Calma, Yuzu, a gente não é um casal..."
                        show yuzu feliz
                        yuzu "Ata. Nunca te vi por essas bandas, Kuroi, ainda mais acompanhado."
                        show yuzu
                        yuzu "A parte do casal é brincadeira, meninos, se acalmem. Porém, a promoção ainda é válida. Vão querer milkshake para matar esse calor de agora de tarde?"
                        
                        kuroi "Bom, mas acho que milkshake não ia ser ruim. O que acha, Noname?"
                        show noname envergonhada
                        noname "Sim... Tem de ovomaltine?"
                        yuzu "Temos sim."
                        show kuroi
                        show noname
                        kuroi "Eu acho que vou querer um de chocolate mesmo."
                        yuzu "Chocolate normal mesmo ou de biscoito oreo?"
                        show kuroi surpreso
                        kuroi "Tem de oreo? Vou querer desse então."
                        noname "A gente divide a conta do milkshake, então? Já que um vai ser de graça."
                        show kuroi
                        kuroi "Me parece justo."
                        yuzu "Ok, um de ovomaltine e outro de oreo. Já já eu entrego, casalzinho."
                        show kuroi envergonhado
                        show noname envergonhadissima
                        show yuzu feliz
                        pause(1.0)
                        hide yuzu
                        
                        kuroi "Essa Yuzu..."
                        show noname envergonhada
                        noname "Ao menos é como você e o Jack falaram: todo mundo no Onigiri faz piada e não é pra levar ninguém a sério."
                        show noname feliz
                        show kuroi feliz
                        kuroi "Sim, sim, exato."
                        show kuroi envergonhado
                        kuroi "Bom, hm... Eu te trouxe aqui, mas nem sei se você gosta de gatos..."
                        show noname envergonhada
                        noname "Não, tudo bem, eu gosto de gatos."
                        show kuroi feliz
                        kuroi "Ah, então deixa te mostrar o Bolota."
                        
                        show cs kuroi with dissolve
                        kuroi "Olha só essas patinhazinhas fofinhas que dá vontade de apertar! Onhonhonhonho"
                        noname "É, como ele é fofo..."
                        kuroi "Como não achar o Bolota fofo, né mesmo?"
                        
                        jump fim
                                
                    