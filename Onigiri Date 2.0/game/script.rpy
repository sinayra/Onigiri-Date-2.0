# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define noname = Character("Noname", color="#F79889")
define unknow = Character("???", color="#F79889")

define yuzu = Character("Yuzu", color="#FF8000")
define pam = Character("Pam", color="#FF8000")
define jack = Character("Jack", color="#FF8000")
define sii = Character("Sii", color="#FF8000")

define kuroi = Character("Kuroi", color="#007FFF")
define morango = Character("Morango", color="#007FFF")
define yakozen = Character("Yakozen", color="#007FFF")


# The game starts here.

label start:

    scene bg fora with Dissolve(5.0)

    unknow "Bem, então esse é o Onigiri quase Prédio. Foi como me falaram, fica bem perto da estação de metrô."
    
    show noname surpresa with moveinleft

    unknow "Ele é realmente um grande condomínio laranja, acho que me preocupei à toa sobre me não achar ele. O bairro aqui tem também um Neko Café, escolas, várias agências de modelo..."
    
    show noname err
    
    unknow "Aquilo lá é um castelo?"

    show noname feliz
    
    unknow "De qualquer maneira, parece bem aconchegante. Vou procurar a recepção e me informar mais sobre o lugar."
    
    hide noname
    
    scene recepcao1 with dissolve
    
    show sii feliz at right
    
    show recepcao2
    
    sii "Eita, um visitante! Bem-vinda ao Onigiri quase Prédio, querida! Prazer, eu sou a síndica Sii. Como se chama?"
    
    show noname feliz at left
    
    noname "Prazer! Me chamo Noname."
    
    sii "Noname-chan? Que nome bonito, é europeu?"
    
    noname "Não não, eu não faço ideia de onde veio, pra ser sincera."
    
    sii "Bom, é sua primeira vez aqui no Onigiri?"
    
    noname "Sim. Como que funciona o aluguel dos quartos aqui?"
    
    sii "É tudo bem simples. Você só preenche esse formulário aqui com seu nome, email e seu blog, coloca um selinho ou link de texto em alguma parte fixa do seu blog e prontinho!"
    
    show noname err
    
    noname "Quê? Blog? Não não, eu quero só alugar um quarto..."
    
    sii "Então, é realmente só isso. Tendo um blog, site ou tumblr, colocando o selinho do Onigiri, pronto, tudo certo!"
    
    noname "E a parte do aluguel?"
    
    show sii
    
    sii "O aluguel a gente cobra a cada 6 meses, que a gente verifica se seu blog ainda tá no ar, se tem o selinho do Onigiri e se você o atualizou nos últimos 6 meses."
    
    noname "Não, pera, estou confusa... E a parte do dinheiro?"
    
    show sii naosei
    
    sii "Dinheiro? Não não, pra morar aqui é de graça mesmo."
    
    show sii feliz
    
    sii "A gente só pede mesmo divulgação no seu blog, nada demais."
    
    noname "Pera, de graça? Algo está errado..."
    
    show sii naosei
    
    sii "Ah, eu mesmo que pago os custos do Onigiri, como domínio e servidor, fica tranquila."
    
    noname "Pera, pra morar é de graça, você está falando de registro de blogs... Eu nem sequer sei o que é um blog..."
    
    show sii
    
    sii "Uai, mas você tá num jogo sobre um \"quase prédio\". Eu tô aqui justamente pra te explicar que jogo é esse e como jogar."
    
    label sobreJogo:
    show noname

    menu:

        "Jogo? Estou num jogo? Minha vida é uma mentira?!":
            jump sobre

        "Jogo? Eu tenho que ganhar alguma coisa?":
            jump objetivo
            
        "Ah... Ok... Acho que aceito... Posso, então, er, me inscrever no Onigiri?":
            jump continua

    label sobre:
        sii "Sim, você está num jogo, Noname-chan. O jogo é uma visual novel e você é a personagem principal!"
        
        show sii opa
        
        sii "A ideia original era fazer um dating simulator, mas acabou que eu me enrolei com o tempo."
        
        show noname err
                
        noname "Então você sabia desdo início quem era eu?"
        
        show sii talvez
        
        sii "Ahn, talvez..."
        
        show sii
        
        jump sobreJogo
        
    label objetivo:
            
        show sii err
            
        sii "Ganhar, não... Como o jogo virou apenas uma visual novel, ele tem diferentes finais... Acho que uns 3 ou 4, agora não me lembro. O objetivo mesmo seria você \"{i} viver a vida da Noname {/i}\", fazendo escolhas, coisa simples. "
        
        show sii
        
        sii "O jogo basicamente tem três tipos de personagens: você, seus amigos e os crushs. Os amigos você reconhece pela cor laranja, os crushs pela cor azul e você tem a cor vermelha."
        
        show sii talvez
        
        sii "O jogo é pra ser jogado numa tarde mesmo, máximo 5 minutos, apesar de ter demorado meses pra produzí-lo."
        
        show sii err
        
        sii "E ainda consegui atrasar a entrega dele... Ai ai... Daqui a pouco meus jogos serão tipo Kingdom Hearts 3, todo ano é adiado."
        
        show sii
        
        jump sobreJogo

    label continua: 
        
        show sii feliz
        
        show noname feliz
        
        sii "Claro, fofa!"
        
        hide noname
        hide sii
        
        "Muitos papéis assinados depois"
        
        hide recepcao2
        show sii feliz at right
        show recepcao2
        show noname at left
        
        sii "Tudo certo, seu apartamento é o 250, do bloco I. É o mesmo apartamento do outro jogo, pegou a referência?"
        
        show noname err
        
        noname "...??"
        
        show sii opa
        
        sii "... Foi mal... É que eu tô ficando velha e tem internas no Onigiri que não morrem, sabe como é, né..."
        
        noname "Ok...."
        
        show sii err
        
        sii "..."
        
        show sii
        
        sii "Enfim, deixe-me levá-la ao seu quarto, Noname-chan."
        
        hide noname
        hide sii
        hide recepcao2
        
        scene quarto with dissolve
        
        show sii at right
        show noname surpresa at left
        
        sii "Espero que goste dele. Ele é bem simples e, é claro, sinta-se livre para mobiliá-lo do jeito que quiser. Nós temos armários também, qualquer coisa é só dar um grito que eu te ajudo com ele."
        
        noname "Puxa, ele é bem bonitinho!"
        
        show sii feliz
        sii "Que bom que gostou!"
        
        show sii
        
        sii "Bom, eu vou voltar pra recepção. Qualquer dúvida sobre o jogo, pode me visitar por lá!"
        
        hide sii
        
        show noname hm at center
        
        noname "Bom... Foi mais fácil do que eu estava imaginando. Apesar de achar a Sii meio estranha, acho que esse tal de Onigiri vai ser um bom lugar pra morar. O que eu posso fazer agora?"
        
        menu:
            "Talvez seja melhor saber mais sobre como esse {i}jogo{/i} funciona.":
                jump sii

            "Eu podia dar um passeio no prédio, né?":
                jump jack
            
            "Tinha um Neko Café lá fora, né? Acho que vou dar um pulo lá.":
                jump yuzu
              
        label fim:
            show fim with fade
            window hide
            pause(3.0)
            return
