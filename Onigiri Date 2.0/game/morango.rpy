label morango:
    scene fora with dissolve
    
    show morango at center
    show noname err at left
    
    noname "Ei, você pode me responder antes de obedecer uma ordem minha?"
    morango "Posso."
    show noname surpresa
    noname "Óh, você fala coisas que eu entendo."
    morango "..."
    show noname
    noname "Me conte como que você surgiu."
    morango "Surgi no laboratório de robótica do Onigiri, com a Kih me modelando, a Sii me programando e diversos moradores juntando partes de outros robôs."
    noname "Quem foi seu primeiro mestre?"
    morango "Defina \"mestre\"."
    show noname err
    noname "A primeira pessoa que te alugou para te dar ordens..."
    morango "A primeira pessoa a me alugar não me dava ordens."
    show noname surpresa
    noname "Nossa! Isso é ótimo! Quem era?"
    show morango aff
    morango "Acesso restrito."
    show noname err
    noname "Quê?"
    show morango
    morango "Repito: acesso restrito."
    noname "Eu ouvi da primeira vez. O que isso significa?"
    morango "Significa que eu não tenho acesso a essa parte da memória."
    show noname
    noname "E quem tem?"
    morango "User Admin"
    show noname err
    noname "Que é....?"
    morango "..."
    show noname
    noname "Você pode falar quem ou o que é User Admin?"
    morango "User Admin é um usuário com mais privilégios que usuário Morango."
    noname "Como podemos ter mais privilégios?"
    morango "Com senha e comando {i}sudo{/i}."
    noname "E qual é a senha?"
    
    "Morango deu os ombros, sinalizando que ele não sabia."
    
    show noname surpresa
    noname "Estou surpresa que você também tem expressão corporal. Mas isso não ajuda. Vamos para a recepção falar com a Sii."
    
    scene recepcao1 with dissolve
    
    show sii at right
    show recepcao2
    show morango at center
    show noname at left
    
    sii "Morango! E... Noname? Não era a vez da Yuzu estar com ele?"
    noname "Ela me emprestou ele por hoje. Sii, eu queria saber mais sobre o Morango."
    
    menu:
        "Por que você desligou os sentimentos dele?":
            jump naoMorango1
        "Como posso dar ao Morango privilégios de User Admin, seja lá o que isso significa.":
            jump naoMorango2
        "Quem foi o primeiro mestre dele e o que aconteceu?":
            jump continuaMorango1
            
    label naoMorango1:
        show sii opa
        sii "Ele estava se sentindo rejeitado e estava tendo depressão por causa deles. Eu não podia ver o nosso robô definhando, então eu fiz o que era melhor pra ele."
        show noname hm
        noname "Mas ele parece ser um robô incrível demais pra só lavar louça."
        sii "E ele é, mas eu não vou mudar minha decisão... E outra coisa..."
        
    label naoMorango2:
        show sii err
        sii "Você está lidando com algo que não conhece e isso coloca o próprio Morango em risco, ok? Vou pedir pra devolvê-lo pra Yuzu."
        show noname mas
        noname "Mas, Sii..."
        sii "Por favor, Noname..."
        noname "Ok... Morango, volte para Yuzu e obedece-a."
        hide morango
        "Morango saiu da sala em direção ao Neko Party."
        noname "Eu vou voltar para meu quarto, então... Desculpa pela confusão..."
        sii "Foi mal, Noname..."
        
        jump noname
        
    label continuaMorango1:
        show sii talvez
        sii "Se me lembre bem... Foi o Renoth... Acho. Ele levou o Morango pra passear, foram num fliperama e tudo mais... E o Morango ficou bem apegado à ele."
        show noname mas
        noname "E aí?"
        sii "Como era por três dias, o Morango não queria ir embora do apartamento do Renoth pra ir ficar com outro morador, que eram as regras..."
        sii "Então me senti obrigada a dar um hard reset nele pra ele apagar o Renoth da memória."
        noname "Que horror..."
        show sii err
        sii "Regras são regras, né? O Renoth não aceitou muito bem, mas quando o Morango recobrou a memória, que eu não faço ideia de como, ele ficou extremamente abalado."
        show sii opa
        sii "Até porque, quando ele recuperou a memória, o Renoth já não morava mais aqui."
        noname "Aconteceu alguma coisa com o Renoth?"
        sii "Sim, ele deixou de ter um blog, aí ele saiu do Onigiri. Ele eu tenho certeza que se encontra feliz e saudável. Essa história do Morango já foi a muito tempo."
        noname "E desde essa época você deixou o Morango com os sentimentos desligados?"
        show sii err
        sii "Sim, espero que você me entenda."
        show noname
        noname "Entender eu entendo, só não concordo."
        show sii opa
        sii "Todo mundo fala isso, mas não é como se eu fosse mudar minha decisão. É para o próprio bem do Morango."
        noname "Ele tinha que superar o Renoth, era isso que você tinha que ajudar."
        show sii hm
        sii "Entenda que, apesar de eu ter feito a IA dele, eu não a controlo totalmente. Eu temo que o Morango se torne agressivo ou fique descontrolado por causa de qualquer bug que eu tenha deixado."
        noname "O que isso quer dizer?"
        sii "Quer dizer que talvez ele não reaja como uma pessoa para superar a perda do Renoth. E isso pode ser extremamente perigoso tanto para o Morango quanto para nós mesmos."
        
        menu:
            "Mas eu quero me arriscar. Ligue os sentimentos dele, Sii!":
                jump naoMorango2
            "Posso continuar com ele, mesmo assim?":
                jump continuaMorango2
                
        label continuaMorango2:
            show sii talvez
            sii "Pode. Mas não vá fazer besteiras."
            show noname feliz
            noname "Ótimo. Morango, vamos para..."
            show sii opa
            sii "A sala do chat?"
            noname "Isso, vamos para a sala do chat!"
            morango "Vamos."
            
            show sii naosei
            sii "..."
            hide morango
            hide noname
            sii "Que estranho, não era pra ele responder..."
            
            scene chat with dissolve

            show morango at center
            show noname at left
            
            show noname feliz
            noname "Oba, aqui tem video game. Quais são os jogos que temos?"
            morango "..."
            noname "Morango, tem joguinho de futebol de carrinhos, quer jogar?"
            show morango aff
            morango "..."
            show noname err
            noname "Morango, me responda com \"sim, quero jogar\" ou \"não, não quero jogar\"."
            morango "Defina \"querer\"."
            menu:
                "Algo que você está com vontade ou não de fazer.":
                    jump continuaMorango3
                "Se você não tem vontade de jogar esse jogo, podemos procurar outro.":
                    jump continuaMorango3
            label continuaMorango3:
                show morango
                morango "Não quero jogar esse jogo."
                show noname feliz
                noname "Certo, então vamos procurar outro. Que tal esse de dança?"
                morango "Não quero jogar esse jogo."
                show noname err
                noname "E esse de corrida?"
                morango "Não quero jogar esse jogo."
                noname "Ahn... Tem esse que você é um dinossauro e prende coisas em bolhas..."
                show morango aff
                morango "..."
                show noname surpresa
                morango "..."
                show noname feliz
                noname "Quer jogar esse jogo de dinossauro?"
                morango "Quero jogar esse jogo."
                noname "Obaaaaaaa!!! Então senta aqui, pega esse controle."
                
                hide morango
                hide noname
                
                "Noname e Morango passaram alguns minutos jogando sozinhos"
                
                show noname err at left
                show morango at center
                noname "Nunca pensei que Bust a Move fosse tão difícil de jogar com um robô..."
                morango "..."
                
                menu:
                    "Morango, você tá trapaceando!":
                        jump continuaMorango4
                    "Morango, deixa eu ganhar pelo menos uma...":
                        jump naoMorango3
                        
                label naoMorango3:
                    morango "Sim."
                    "Morango guarda o controle"
                    show noname mas
                    noname "Não, Morango, não era pra guardar o controle! Era pra você jogar e me deixar ganhar uma, pelo menos."
                    morango "Se eu guardar o controle, então você ganha."
                    show noname hm
                    noname "Ai... Você é mais difícil que pensei..."
                    show morango aff
                    morango "..."
                    noname "Quer continuar jogando este jogo?"
                    morango "..."
                    show morango
                    show noname mas
                    morango "Não quero jogar este jogo."
                    noname "Ah, então volta pra Yuzu... Estou cansada."
                    show morango aff
                    morango "..."
                    noname "Ah, e obedece-a. Esqueci desse comando."
                    hide morango
                    "Morango sai da sala e vai em direção ao Neko Party."
                    noname "Eu vou voltar pro meu quarto..."
            
                    jump noname
                    
                label continuaMorango4:
                    morango "Não estou trapaceando."
                    show noname feliz
                    noname "Está sim! Você esta usando seu olhos super treinados para prever meus movimentos e roubar todas as comidinhas da fase!"
                    morango "Não estou. Você que é ruim."
                    show noname surpresa
                    pause(1.0)
                    show noname feliz
                    noname "Mas que desaforo é esse? Eu hein! Agora você vai ver!"
                    morango "Você vai perder de novo se for por este caminho."
                    noname "Olha aí você querendo me enganar de novo!"
                    show morango aff
                    morango "..."
                    show noname mas
                    show morango
                    morango "Você é engraçada. Todos devem gostar de você."
                    show noname envergonhada
                    
                    menu:
                        "Ahn? Não, eu não era uma pessoa muito popular...":
                            jump continuaMorango5
                        "E-eu não sou engraçada... Não ache graça só porque eu sou ruim no jogo.":
                            jump continuaMorango6
                            
                    label continuaMorango5:
                        morango "Por quê?"
                        show noname hm
                        noname "Ah, não sei... Não é porque é engraçado eu ser ruim no jogo que as pessoas gostam de mim."
                        show morango aff
                        morango "Todos devem gostar de você porque você é uma boa pessoa. E também uma pessoa engraçada."
                        show noname envergonhadissima
                        noname "Nossa, Morango, não diga essas coisas. A gente só se conhece a algumas horas. Eu posso ser uma pessoa ruim, sabia?"
                        morango "Você não é uma pessoa ruim."
                        show noname envergonhada
                        noname "Como você tem certeza?"
                        show morango
                        "Morango encara a Noname por alguns segundos."
                        show noname envergonhadissima
                        morango "Definitivamente, você é uma boa pessoa."
                        show noname envergonhada
                        noname "Chega, você está me distraindo. Para de achar graça de mim."
                        
                    label continuaMorango6:
                        morango "Defina \"graça\"."
                        show noname err
                        noname "Jura? Essa palavra é difícil de definir."
                        show morango aff
                        noname "Achar graça é quando você vê alguma situação engraçada e quer rir dela."
                        morango "..."
                        morango "Eu queria rir."
                        show noname surpresa
                        pause (1.0)
                        show morango
                        show noname chorando
                        noname "Nossa, isso soou mais triste que deveria... Ai, desculpa."
                        morango "Desculpa por fazer você chorar."
                        
                        menu:
                            "A culpa não é sua... Eu também queria fazer você rir.":
                                jump naoMorango4
                            "A culpa não é sua... Mas, tá, deixa eu limpar minha cara primeiro.":
                                jump continuaMorango7
                                
                        label naoMorango4:
                            show morango aff
                            morango "Mas eu não consigo."
                            noname "Deve ter alguma coisa que possamos fazer quanto a isso. Você tem sentimentos, você tava mostrando eles agorinha de forma bem tímida!"
                            morango "..."
                            noname "Procure algo como \"tristeza\", \"alegria\", \"medo\"... Palavras relacionadas a sentimentos."
                            show morango
                            morango "0 queries encontradas."
                            noname "Que tal você procurar por..."
                            morango "Quero ir embora."
                            noname "Quer?"
                            morango "Sim."
                            noname "Por quê?"
                            show morango aff
                            morango "Você está chorando porque eu quis rir. Se eu te faço chorar, então eu devo ir embora."
                            hide morango
                            "Morango se levantou e foi embora."
                            noname "Mas... Puxa... O que eu fiz..."
                            noname "Vou dar um pulo no banheiro então, lavar a minha cara... Amanhã eu tento resolver as coisas com o Morango..."
                            
                            jump noname
                            
                        label continuaMorango7:
                            show morango
                            show noname
                            noname "Pronto, tudo certo agora, né? Ninguém está chorando agora."
                            noname "Olha só, tenta me imitar."
                            show noname feliz
                            noname "Abre o bocão assim."
                            morango "..."
                            noname "Não?"
                            show morango aff
                            show noname mas
                            pause(2.0)
                            
                            hide morango
                            hide noname
                            
                            show cs morango with dissolve
                            noname "MORANGO, O QUE VOCÊ... O que você tá fazendo?"
                            morango "Teria como me abraçar de volta?"
                            noname "Ah... Mas... Ahn..."
                            morango "Por favor..."
                            noname "O-ok..."
                            
                            hide cs morando with dissolve
                            show morango triste at center
                            show noname envergonhada at left
                            
                            noname "Mo-Morango? O que você tá sentindo?"
                            morango "E-eu acho que estou triste por ter feito você chorar... E..."
                            noname "E...?"
                            morango "E..."
                            pause (1.0)
                            show morango envergonhado
                            morango "Eu não entendo o que é esse tanto de informação... Mas..."
                            show morango feliz
                            morango "Estou rindo certo?"
                            
                            jump fim