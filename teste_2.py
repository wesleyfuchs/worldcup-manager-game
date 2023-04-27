if userteam == match0[0]:
                        print("--Titulares--")
                        for jogador in team1.players:
                            print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))
                        print("--Reservas--")
                        for jogador in team1.reservas:
                            print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))
                        
                        # Solicita o número do jogador titular que será substituído
                        numero_titular = int(input("Digite o número do jogador titular que deseja substituir: "))

                        # Localiza o jogador titular correspondente e obtém sua posição original
                        for i, jogador in enumerate(team1.players):
                            if jogador.numero == numero_titular:
                                jogador_titular = jogador
                                posicao_original = i
                                team1.players.pop(i)
                                break
                    
                    else:
                        print("--Titulares--")
                        for jogador in team2.players:
                            print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))
                        print("--Reservas--")
                        for jogador in team2.reservas:
                            print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))
                        
                        # Solicita o número do jogador titular que será substituído
                        numero_titular = int(input("Digite o número do jogador titular que deseja substituir: "))

                        # Localiza o jogador titular correspondente e obtém sua posição original
                        for i, jogador in enumerate(team2.players):
                            if jogador.numero == numero_titular:
                                jogador_titular = jogador
                                posicao_original = i
                                team2.players.pop(i)
                                break              
                        # Solicita o número do jogador reserva que irá substituir o titular
                        numero_reserva = int(input("Digite o número do jogador reserva que irá substituir o titular: "))

                        # Localiza o jogador reserva correspondente e insere na posição original do titular
                        for i, jogador in enumerate(team2.reservas):
                            if jogador.numero == numero_reserva:
                                team2.reservas.pop(i)
                                team2.players.insert(posicao_original, jogador)
                                break
                        
                        for jogador in team2.players:
                            print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))    