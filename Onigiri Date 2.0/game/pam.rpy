label pam:
    scene fora with dissolve
    show noname
    
    noname "Nossa, realmente o Onigiri é bem grande... Tem até uns jardinzinhos entre os prédios. Será que de um prédio e outro, pode andar de bicicleta?"
    "Noname anda até a entrada de um dos blocos e encontra uma placa escrita \"Bloco G\"."
    show noname hm
    noname "Hm, diferente do I, esse aqui parece mais abandonado... Por que será?"
    "Noname decide entrar no bloco G."
    
    scene corredor with dissolve
    
    show noname feliz at left
    show pam at right
    
    noname "Boa tarde."
    pam "Boat tarde...?"
    pam "Hey, você é nova por aqui? Eu acho que nunca te vi aqui no Onigiri."
    noname "Aham, cheguei hoje. Prazer, me chamo Noname, moro no bloco I."
    pam "Prazer, Noname, eu chamo Pam, moro no H, aqui do lado. Uma pergunta..."
    show pam seria
    pam "O que te traz aqui no Bloco G? Não te avisaram que ele é mal-assombrado?"
    show noname mas
    noname "Mal-assombrado? Mas ele parece como um prédio normal no Onigiri."
    pam "Realmente tem pessoas que moram nesse aqui, mas elas são meio que caça-fantasmas. Você já lidou com espíritos ou coisa do tipo?"
    show noname err
    noname "Espíritos? Hã...?"
    show pam naocreio
    pam "..."
    show pam seria
    pam "Noname, aqui é um lugar muito perigoso. Vamos, deixa eu te acompanhar até a saída."
    
    show noname mas
    menu:
        "Não não, calma, por que aqui é mal-assombrado?":
            jump continuaPam1
        "Se aqui é um lugar mal-assombrado e as pessoas que ficam aqui são caça-fantasmas, você é uma também?":
            jump continuaPam2
            
    label continuaPam1:
        pam "Eu não sei por que este bloco ficou mal-assombrado, ele tem essa fama desde antes de eu entrar no Onigiri."
        pam "Perto do dia das bruxas, esse prédio vira um caos. Já ouvi casos de abrir um portal interdimensional nele, outro de ser lar dos Oni Onigiris..."
        noname "E você não tem medo?"
        show pam
        pam "Eu tinha no começo, hoje já sou um pouquinho mais forte. Se aparecer algum monstro que não conheço, com certeza vou ter medo, como qualquer pessoa normal."
        pam "Mas pelo menos já tenho um pouco mais de experiência contra os bichos daqui do Onigiri."
        show noname surpresa
        noname "Se você está aqui, então você é uma caça-fantasmas?"
    label continuaPam2:
        show pam seria
        pam "Não, eu não sou caça-fantasmas. Eu apenas ajudo o Onigiri com um problema que causei ano passado."
        show noname hm
        noname "Problema?"
        show pam naocreio
        pam "É, eu caí na besteira de falar pra um vilão sobre o Onigiri, aí ele decidiu atacar a gente ano passado."
        show pam
        pam "Aí eu meio que cuido que ele não fique à solta de novo."
        show noname surpresa
        noname "Mas não é ruim você ser responsável por algo tão perigoso?"
        show pam feliz
        pam "Não tanto assim, eu até me sinto como alguém importante, como uma bruxa bem poderosa, sabe?"
        show noname feliz
        noname "Que bom que você enxerga pelo lado positivo da coisa!"
        
        menu:
            "Mas quem é esse vilão que você falou?":
                jump continuaPam3
            "Eu posso ver quem é o vilão?":
                jump naoPam1
        
        label naoPam1:
            show pam seria
            pam "É claro que não. É extremamente perigoso e ele é bem persuasivo. Pra te convencer a soltá-lo é daqui pra lá."
            show noname mas
            
            scene fora with dissolve
            show pam at right
            show noname at left
            
            pam "Pronto, esse é o máximo que vou te levar. Tenho que voltar pro meu posto."
            show noname feliz
            noname "Ok, Pam! Foi muito bom te conhecer!"
            pam "Igualmente, Noname! A gente se vê por aí!"
            hide pam with dissolve
            show noname hm
            noname "Talvez tenha sido um erro ir no Bloco G. A curiosidade matou o gato. Acho que vou voltar pro meu quarto arrumar as minhas coisas de mudança..."
            
            jump noname
            
        label continuaPam3:
            show pam seria
            pam "Ele se chama Yakozen. Eu encontrei ele numa floresta não muito longe daqui. Ele meio que tinha montado uma barraquinha de roupas de frio em pleno verão, mas elas realmente bem quentinhas."
            show noname err
            noname "Você comprou roupas de frio de um cara que tava no meio da floresta?"
            show pam facepalm
            pam "Toda vez que conto essa história pra alguém, eu fico com vergonha de mim mesma..."
            show pam seria
            pam "Mas, é, comprei. Não sei se ele usou alguma magia ou se ele realmente era um excelente vendedor, mas acabei adquirindo o casaco."
            show noname surpresa
            noname "E aí?"
            pam "E aí ele perguntou de onde eu vinha, falei que era do Onigiri, a gente foi conversando, conversando, conversando... Ele era um cara simpático."
            show pam facepalm
            pam "Depois ele começou a rir e desapareceu. Alguns meses depois, atacou o Onigiri com zumbis que iam sequestrar os moradores pra vender as partes do corpo de todo mundo."
            show noname err
            noname "Eca."
            show pam seria
            pam "Mercado negro, sabe como é."
            
            show noname hm
            
            menu:
                "Nossa, eu realmente queria saber que tipo de pessoa ele é...":
                    jump naoPam2
                "Por que a gente mantém ele no Onigiri mesmo?":
                    jump continuaPam4
                    
            label naoPam2:
                show pam naocreio
                pam "Nem pense nisso. É minha função proteger os moradores do Onigiri da influência desse cara."
                show noname mas
                noname "E nem se você for comigo?"
                
                jump naoPam1
                
            label continuaPam4:
                show pam
                pam "Acho que um dos motivos é pra não soltar ele pela blogosfera mesmo. Melhor que eu me mudar ou me deslocar até uma suposta prisão, ele estando por perto num lugar que consigo chegar rápido, é melhor."
                show noname hm
                noname "Entendi..."
                
                scene fora with dissolve
                show pam at right
                show noname at left
                
                pam "Pronto, esse é o máximo que vou te levar. Tenho que voltar pro meu posto."
                show noname feliz
                noname "Ok, Pam! Foi muito bom te conhecer!"
                pam "Igualmente, Noname! A gente se vê por aí!"
                hide pam with dissolve
                show noname hm
                pause(1.0)
                menu:
                    "Eu acho que dar uma espiadinha assim não vai fazer tão mal... É só a Pam não saber.":
                        jump yakozen
                    "Acho que é melhor eu ficar na minha e voltar para meu quarto. Não quero atrapalhar o trabalho da Pam, ela é bem simpática.":
                        jump noname