label jack:
    scene corredor with dissolve
    
    show noname at left
    noname "Os corredores aqui são bem grandes, dá pra se perder fácil fácil..."
    
    show jack at right
    jack "Boa tarde!"
    show noname feliz
    noname "Boa tarde!"
    
    show jack surpreso
    jack "Eu não estou te reconhecendo. Tu és nova por aqui?"
    noname "Aham, cheguei hoje. Me chamo Noname. E você?"
    show jack feliz
    jack "Muito prazer, Noname-chan! Eu me chamo Jack. Seja bem vinda ao Onigiri quase Prédio!"
    noname "Obrigada!"
    jack "Como tu chegaste hoje, imagino que não saibas nada sobre o Onigiri, né? Eu estava indo para o chat, quer ir comigo?"
    noname "Chat?"
    show jack
    jack "É onde todo mundo do Onigiri se reune para bater papo, comer gelatina, reclamar com a Sii sobre dever de matemática e essas coisas."
    
    menu:
        "É muita gentileza sua, Jack, mas acho que prefiro continuar explorando o Onigiri.":
            jump jackPam
            
        "Eu posso ir junto mesmo?":
            jump continuaJack1
            
    label jackPam:
        show noname
        show jack surpreso
        jack "Oh, tudo bem."
        show jack feliz
        jack "Mas cuidado que o Onigiri tem 9 blocos, viu? É bem fácil se perder."
        show noname err
        noname "Nossa..."
        jack "Antigamente era pior, que era só dois prédios onde um tinha 100 andares e outro 300. Hahahaha"
        noname "Oh..."
        show jack
        jack "Bom, vou-me indo nessa. Até mais, Noname!"
        show noname feliz
        noname "Até mais, Jack!"
        
        jump pam
        
    label continuaJack1:
        show jack feliz
        jack "É claro! Vamos, é por aqui."
        
        scene chat with fade
        show noname at left
        show jack at center
        show kuroi at right
        
        jack "Boa tarde, Kuroi!"
        kuroi "Jack, tudo bom? Ah, essa deve ser a Noname, né? Foi a Sii quem cuidou diretamente dos seus papéis?"
        noname "Oh, sim, me chamo Noname. Eu me inscrevi lá na recepção mesmo com a Sii, não é o normal?"
        kuroi "Normalmente quem cuida das inscrições dos moradores sou eu, que envio por carta todas as instruções. Bom, seja bem-vinda, Noname!"
        jack "Noname, este é o Kuroi, mensageiro do Onigiri quase Prédio. Ele quem normalmente vai até o seu apartamento te avisar sobre algum evento importante do Onigiri."
        noname "Ah sim. Muito prazer, Kuroi!"
        
        show jack feliz
        jack "Eu acabei encontrando andando pelos corredores, aí trouxe ela para conhecer a sala do chat."
        show kuroi feliz
        kuroi "Ah sim! Ainda bem que agora temos uma sala, até pouco tempo atrás era só uma caixa de papelão."
        show jack
        
        show noname err
        noname "Caixa de papelão?"
        show kuroi duvido
        kuroi "Sim, a Sii pra arrumar os problemas do Onigiri é uma lerdeza que só..."
        kuroi "Ela mó \"Ah, o povo se vira nessa caixa de papelão aqui de geladeira\", aí a gente tinha que se expremer dentro dela."
        show jack feliz
        jack "E ela ficava lá na recepção, ainda por cima. Hahahaha. Pelo menos eu dei a ideia de colocar umas almofadas dentro dela."
        show kuroi feliz
        kuroi "Os visitantes mó chegavam e \"Oxe, que que tem uma caixa de papelão ali? E ainda tem umas almofadinhas dentro... Ué?\"."
        noname "Nossa, isso parece horrível..."
        
        show kuroi
        kuroi "Se as pessoas levassem a sério mesmo, ia ser bem horrível, mas como todo mundo aqui leva na brincadeira, tá tudo certo."
        show jack surpreso
        jack "Sim, é uma regra da casa: nunca leve nada muito a sério aqui no Onigiri."
        show noname feliz
        show jack
        
        noname "Vocês estão aqui há quanto tempo?"
        show jack feliz
        jack "Eu me mudei pro Onigiri em... 2010? 2011? Por aí, já faz um bom tempo. Moro no bloco A e recentemente me mudei pro 1º apartamento."
        kuroi "Eu vim pra cá em 2011. Só que eu sou meio que um morador especial, porque não moro em nenhum dos blocos."
        show noname
        noname "Especial?"
        kuroi "É que eu pedi abrigo pra Sii e pra Kih, que era síndica na época. É uma longa história, mas desde que entrei, eu trabalho como mensageiro daqui."
        show noname surpresa
        noname "Nossa."
        kuroi "Bom, foi muito bom te conhecer, Noname. Jack, espero te ver mais vezes por aqui também."
        show jack surpreso
        jack "Já está indo embora, Kuroi?"
        kuroi "Já, tenho que ir lá no bloco I avisar um dos moradores que ele tá sem selo, eu só vim pra cá mais pra descansar as pernas mesmo. Até mais, gente!"
        
        hide kuroi with dissolve
        
        show jack
        jack "O Kuroi é um moço bem difícil de conversar, né?"
        show noname hm
        noname "Ele falou que é um morador especial, pediu abrigo... Como assim?"
        jack "Ele também não fala muito disso, só que quando ele era menor, teve muitos problemas com os pais, aí ele apareceu aqui e as síndicas anunciaram ele como mensageiro."
        noname "Puxa, coitado... Mas ele parece um amor de pessoa, por que teve problemas com os pais?"
        jack "Ele com certeza é um amor de pessoa, sem dúvida. Bem tímido quando o assunto é sobre ele mesmo, mas um amor de pessoa."
        show noname
        
        menu:
            "Jack, acho que vou indo nessa também. Acho que vou voltar pro meu quarto pra terminar de arrumar minhas coisas.":
                jump jackKuroi
            "Jack, acho que vou continuar dando uma volta no prédio.":
                jump jackPam
                
        label jackKuroi:
            show jack safado
            jack "Hm... Ok, Noname-chan. Se esbarrar no Kuroi, diga pra ele parar de procurar trabalho. Até!"
            noname "Ok, vou dizer. Até!"
            jump kuroi
                    
            
                
            