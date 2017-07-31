label yuzu:
    scene cafe with dissolve
    show yuzu at center
    
    yuzu "Bem vinda ao Neko Party!"
    show yuzu feliz
    yuzu "Se você trouxer um acompanhante hoje para tomar um milkshake, o segundo é de graça!"
    show noname at left
    noname "Obrigada. Onde posso ver o cardápio?"
    yuzu "É pra já, fofa!"
    
    "Noname procura no cardápio alguma comida"
    
    noname "Eu acho... Que vou querer esse breakfast ham. Ainda tá servindo ou é só pela manhã?"
    show yuzu
    yuzu "Posso fazer pra você, querida, sem problemas. Por sinal, morador do Onigiri quase Prédio tem desconto."
    show noname surpresa
    noname "Tem? Puxa, eu acabei de me mudar pra lá."
    yuzu "Jura? Qual o seu bloco?"
    noname "Moro no I."
    yuzu "Ah, que longe... Eu moro no bloco A. Prazer, eu me chamo Yuzu."
    noname "Prazer, Yuzu, eu me chamo Noname."
    yuzu "Já conhece as redondezas aqui do Onigiri?"
    show noname feliz
    noname "Ainda não. Esse Neko Café me chamou bem a atenção e resolvi experimentar."
    yuzu "Obaaa. Fico feliz que você tenha vindo num dia que eu trabalho aqui. Eu também sou dona do castelo Soul aqui perto e dona da escola Neko High, então tenho que ficar alternando."
    noname "Nossa, você tem tantos empregos quanto o \"por que\"."
    show yuzu feliz
    yuzu "Hhahahahaa. Mas alguém nessa casa tem que trabalhar, não é mesmo? Enfim, aqui está seu breakfast ham."
    show noname feliz
    noname "Muito obrigada."
    yuzu "Aceita um café ou suco para acompanhar?"
    noname "Aceito um suco. Tem de laranja?"
    yuzu "Tem sim, fofa. Aqui, óh."
    
    show noname hm
    noname "Uma pergunta só de curiosade, você trabalha nesses empregos todos sozinha?"
    show yuzu seria
    yuzu "Nãããão não. Eu tenho minha equipe para cuidar daqui, do castelo e da escola, mas aqui do Neko Party em especial, as vezes peço ajuda para o Morango."
    noname "Morango?"
    yuzu "É um robô que a Sii fez para os moradores do Onigiri. Ele é simplesmente perfeito, mas só falta emoção nele."
    yuzu "Morango! Pode dar um pulo aqui?"
    show morango at right with moveinright
    yuzu "Esse é o Morango, ele é um ótimo faxineiro, zelador, lava-louças, lava roupa, cozinheiro... Enfim, ele é ótimo."
    morango "..."
    show noname feliz
    noname "Prazer, Morango! Eu me chamo Noname."
    morango "..."
    show noname err
    yuzu "Nossa, nem perca seu tempo tentando falar com ele. Ele só recebe ordens. Morango, diga \"oi\" para a Noname."
    morango "Oi."
    noname "Nossa, que seco."
    show yuzu conselheira
    yuzu "Dizem que a Sii desligou os sentimentos dele porque ele tava apresentando uns defeitos, mas nunca achei nenhum botão nele ou coisa do gênero. Acho que ele nunca teve sentimentos, as histórias são todas lendas."
    
    show noname
    menu:
        "Desligar os sentimentos? Como assim?":
            jump continuaYuzu1
        "Todo morador do Onigiri pode usar o Morango?":
            jump naoYuzu1
            
    label naoYuzu1:
        show yuzu seria
        yuzu "Sim, é só fazer uma reserva com o Kuroi ou com a própria Sii. Quem estiver na recepção."
        show noname mas
        noname "Acha que ele pode me ajudar com minhas mudanças?"
        show yuzu feliz
        yuzu "Ele é o robô ideal pra isso!"
        show noname feliz
        noname "Oba! Depois vou ver como faz reserva, então."
        
        hide yuzu
        hide morango
        
        noname "Estava uma delícia. Acho que vou pagar essa comida e voltar pro meu quarto. Depois eu vejo como consigo emprestado o Morango."
        jump noname
        
    label continuaYuzu1:
        show yuzu seria
        yuzu "Então, é como eu te falei: eu acho que é lenda o fato desse robô ter tido algum dia sentimentos."
        yuzu "Morango, procure alguma tabela chamada \"sentimentos\" no seu banco de dados."
        morango "0 queries encontradas."
        yuzu "Viu só? Tem nada dentro dele."
        show noname hm
        noname "Talvez tenha outro nome? Eu não sei como banco de dados funciona."
        yuzu "Hm, acho que não."
        
        menu:
            "Quanto tempo você está com o Morango?":
                jump naoYuzu2
            "Alguém já tentou levar ele pra um médico?":
                jump continuaYuzu2
                
        label naoYuzu2:
            show yuzu conselheira
            yuzu "Então... Eu não sei... Eu sempre tento alugar ele nos fins de semana, que fica mais movimentado aqui."
            show noname mas
            noname "Tenta?"
            yuzu "As vezes a lista de espera é grande, aí você tem que esperar pela sua vez de ficar com ele. Mas o Morango existe desde 2009, já teve várias formas, inclusive."
            noname "A Sii vai aperfeiçoando ele aos poucos?"
            yuzu "Na verdade, todos os moradores tentam ajudar com um pouquinho. A gente leva partes de outros robôs pra Sii e ela dá um jeito de juntar elas, sem deixá-lo com cara de monstro."
            noname "Entendi..."
            
            show noname
            noname "Bom, a comida estava ótima! Muito obrigada, Yuzu!"
            yuzu "Volta sempre, fofa!"
            hide morango
            hide yuzu
            noname "Acho que agora eu vou só dar um pulinho no meu quarto pra arrumar minhas mudanças."
            
            jump noname
            
        label continuaYuzu2:
            show noname seria
            yuzu "Médico? Você quis dizer técnico?"
            show noname err
            noname "Isso. Quase a mesma coisa."
            yuzu "Bom, ele não tá quebrado pra levá-lo num técnico. Está?"
            noname "Pra mim ele parece ser complexo demais pra ser só um \"roomba\" que lava-louça."
            show yuzu feliz
            yuzu "Bom, você tem bastante interesse no Morango, né?"
            show noname surpresa
            noname "Hã? Sim, ele parece ser um robô incrível."
            yuzu "Eu deixo você ficar com ele hoje, que tal? Aí você descobre se ele realmente tem sentimentos. Pode ser?"
            show noname mas
            noname "Mas você não tava precisando dele pra te ajudar na loja?"
            yuzu "Nah, eu consigo me virar. Se ele ter sentimentos mesmo, vai ser uma descoberta e tanto!"
            show yuzu seria
            yuzu "Morango, você deve obedecer a Noname, agora."
            morango "..."
            yuzu "Pronto, agora ele vai te escutar."
            noname "Morango, se importa se a gente for pra fora?"
            "Morango se dirige à porta"
            hide morango
            show noname err
            noname "Esperaí!!!"
            hide noname
            show yuzu feliz
            yuzu "Hhahahahaha. Mas como ela é fofa."
            
            jump morango
        