from generador import tablero,add_by_turns
from Game import Game,Player
from Nodo import Propiedad,Nodo,Servicio,Ferrocarril,Cofre,Suerte,Impuesto
from sound import theme
from start import asignar


theme()
g = Game(tablero)

turns = asignar()
print(turns)
add_by_turns(turns,g)


def show_menu(player:Player):
    print(player.name)
    on = True
    while on:
        print("1 Inventorio|2 Vender|3 Tirar Dados")
        sw = input()
        while sw not in ["1","2","3"]:
            print("no valido")
            sw = input()
        if sw=="1":
            print(player.inventory.valores)
        elif sw=="2":
            player.sell_menu()
        elif sw=="3":
                on = False

g.start() # Posiciona en inicio
while len(g.players)>1:
    for  player in g.players.copy().values(): # Por cada jugador
        player:Player
        
        show_menu(player)
        turnos = 1
        while turnos>0:
            
            if player.on_jail:
                print("Turno en carcel de ",player.name,"(encarcelado)")
                player.jugar_carcel()
                turnos -= 1
            
            if not player.on_jail:
                print("Turno de ",player.name,"ubicado en: ",player.pos) #Nombre y casilla
                repeat = player.jugar_turno()
                # mostrar(die,player)
                sitio = player.pos
                
                if isinstance(sitio,Suerte):
                    tipo,goal = g.sacar_carta("suerte.txt")
                    g.jugar_suerte(player,tipo,goal)
                    sitio = player.pos

                if isinstance(sitio,Propiedad): # Propiedad
                    print("Costo ",sitio.costo,"Renta ",sitio.renta
                            ," Dueño ",sitio.owner,"color ",sitio.color)
                    if sitio.owner is None:
                        print("comprar 1 si 2 no")
                        op = input()
                        while op!="1" and op!="2":
                            op = input()
                        if op =="1":
                            player.buy(sitio)
                        else:
                            print("No la ha comprado")
                    elif sitio.owner!=player.name:
                        print("debe pagar ",sitio.renta)
                        g.transfer(player.name,sitio.owner,sitio.renta)
                    else:
                        print("Te relajas en tu propiedad xd ")
                        
                
                
                elif isinstance(sitio,Servicio): #Servicio
                    print("Costo ",sitio.costo," Dueño ",sitio.owner)
                    if sitio.owner is None:
                        print("comprar 1 si 2 no")
                        op = int(input())
                        if op ==1:
                            player.buy(sitio)
                    elif sitio.owner!=player.name:
                        g.pagar_servicio(player,sitio.owner)
                    
                elif isinstance(sitio,Ferrocarril): # Ferrocarril
                    print("Costo ",sitio.costo," Dueño ",sitio.owner)
                    if sitio.owner is None:
                        print("comprar 1 si 2 no")
                        op = int(input())
                        if op ==1:
                            player.buy(sitio)
                    elif sitio.owner!=player.name:
                        g.pagar_ferrocarril(player,sitio.owner)

                elif isinstance(sitio,Cofre):
                    tipo,cant = g.sacar_carta("cofre.txt")
                    g.jugar_cofre(tipo,cant,player)

                elif isinstance(sitio,Impuesto):
                    print("Debe pagar ",sitio.pago)
                    player.withdraw(sitio.pago)
                    
                elif isinstance(sitio,Nodo):
                    print("sitio es",sitio," loc ",sitio.loc)
                    if sitio.loc==30:
                        print("A la carcel!")
                        g.imprison(player)  # Si Nodo es vayase a la carcel
                        turnos = 0

                if repeat ==0 :
                    turnos -=1

        op = input("Eliminar 1\n")
        if op =="1":
            g.remove_player(player.name)
        if player.balance<0:
            print("Deberia irse ")


