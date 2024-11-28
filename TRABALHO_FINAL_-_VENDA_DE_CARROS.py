#DEFININDO BIBLIOTECA DE MARCA, MODELOS E VALORES QUE SERÃO UTILIZADOS PARA CONSULTA DE TABELA FIPE NO DECORRER DO CÓDIGO;
car_to_sell = {
    "AUDI":{"A3 SEDAN":125065, "A4 SEDAN":228335, "Q3":245976, "Q5":279815, "Q7": 180257},
    "BMW":{"320IA":300290, "320I":227424, "X1":228031, "X3":348725, "X4":533112},
    "LAND ROVER":{"DEFENDER":513466, "DISCOVERY":323991, "EVOQUE":220582, "SPORT":855195, "VELAR":525452},
    "MERCERDES-BENZ":{"A200":164462, "C180":228929, "GLB200":258648, "GLE63":1172707, "S63":1532757},
    "PORSCHE":{"911":1477120, "CAYENNE":1173516, "MACAN":563656, "PANAMERA":881018, "TAYCAN":876525}
}

#DEFININDO BIBLIOTECA DE MARCA E MODELOS E VALORES QUE SERÃO UTILIZADOS PARA VENDA, ALUGUEL E COMPRA NO DECORRER DO CÓDIGO;
car_list = {
    "AUDI":{"A3 SEDAN", "A4 SEDAN", "Q3", "Q5", "Q7"},
    "BMW":{"320IA", "320I", "X1", "X3", "X4"},
    "LAND ROVER":{"DEFENDER", "DISCOVERY", "EVOQUE", "SPORT", "VELAR"},
    "MERCERDES-BENZ":{"A200", "C180", "GLB200", "GLE63", "S63"},
    "PORSCHE":{"911", "CAYENNE", "MACAN", "PANAMERA", "TAYCAN"}
}

#INICIANDO O CÓDIGO SOLICITANDO ALGUMAS INFORMAÇÕES PESSOAIS DO USUÁRIO;
print("-- BEM-VINDO A ODRAZ VEÍCULOS --\n")
name = input("DIGITE O SEU NOME:").upper()
fone = int(input("DIGITE O SEU TELEFONE:"))
balance = float(input("DIGITE SEU SALDO BANCÁRIO ATUAL:"))
print("")

#INICIO O CÓDIGO COM UM LOOP PARA APARECER O MENU DE OPÇÕES ATÉ QUE O USUÁRIO ESCOLHA FINALIZAR AS OPERAÇÕES;
count = 1
while count > 0:
    print("-- MENU --")
    print("1 - VENDA DO SEU AUTOMÓVEL\n2 - ALUGUEL DE AUTOMÓVEL\n3 - COMPRA DE AUTOMÓVEL\n0 - SAIR")
    option = int(input("QUAL OPÇÃO VOCÊ DESEJA ACESSAR:"))

    #USAREI A ESTRUTURA MATCH CASE PARA QUE O USUÁRIO ESCOLHA ENTRE AS OPÇÕES DISPONIVEIS OU PARA QUE O SISTEMA SE ENCERRE;
    #CASO O USUÁRIO ESCOLHA ALGUMA OPÇÃO QUE NÃO ESTEJA DISPONÍVEL ELE RECEBERÁ UMA MENSAGEM DE AVISO E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS;
    match(option):
        
        #NESTE PRIMEIRO CASE O USUÁRIO ESCOLHEU FAZER A VENDA DO SEU PRÓPRIO AUTOMÓVEL;
        #O USUÁRIO ESTÁ RESTRITO A VENDER SEU AUTOMÓVEL CASO ELE SEJA SEMELHANTE A CARTELA OFERECIDA PREVIAMENTE PARA VENDAS FUTURAS AFIM DE MANTER O PADRÃO DE AUTOMÓVEIS DA REVENDEDORA;
        case 1:
            print("\n-- VENDA DO SEU AUTOMÓVEL --")
            print("\nMARCAS DISPONÍVEIS:")
            
            #APARECERÁ NA TELA PARA O USUÁRIO AS MARCAS QUE A REVENDEDORA TRABALHA;
            for brand in car_list:
                print(brand)
            brand = input("\nQUAL A MARCA DO SEU AUTOMÓVEL:").upper()
            
            #VERIFICAÇÃO SE A MARCA DO AUTOMÓVEL QUE O USUÁRIO DIGITARÁ ESTÁ DENTRO DA CARTELA PRÉVIA;
            if brand in car_list:
                print("\nAUTOMÓVEIS DISPONÍVEIS:")

                #APARECERÁ NA TELA PARA O USUÁRIO OS AUTOMÓVEIS DA CARTELA DA REVENDEDORA;
                for car in car_list[brand]:
                    print(car)
                car = input("\nQUAL O MODELO DO SEU AUTOMÓVEL:").upper()

                #VERIFICAÇÃO SE O MODELO DO AUTOMÓVEL QUE O USUÁRIO DIGITARÁ ESTÁ DENTRO DA CARTELA PRÉVIA;
                #CASO TODAS AS OPÇÕES SEJAM SATISFEITAS O SISTEMA MOSTRARÁ O VALOR DO AUTOMÓVEL DE ACORDO COM A TABELA FIPE E TAMBÉM O VALOR DE COMPRA DELE;
                if car in car_list[brand]:
                    price = car_to_sell[brand][car]
                    price_to_buy = price * 0.88
                    print(f"\nO VALOR DE ACORDO COM A TABELA FIPE DESSE AUTOMÓVEL É R${price:.2f}")
                    print(f"O VALOR DE COMPRA DESSE AUTOMÓVEL É R${price_to_buy:.2f}")

                    #APÓS ANALISE DE VALORES O USUÁRIO ESCOLHERÁ SE QUER REALIZAR A VENDA;
                    yes_no = input("\nDESEJA FINALIZAR A VENDA: (SIM/NÃO)").upper()
                    
                    #CASO O USUÁRIO OPTE POR REALIZAR A VENDA O SALDO BANCÁRIO DELE AUMENTARÁ COM O VALOR DA VENDA DO AUTOMÓVEL E ELE SERÁ INFORMADO DE SEU NOVO SALDO;
                    if yes_no == "SIM":
                        balance += price_to_buy
                        print(f"\nVENDA REALIZADA!\n{name}, SEU NOVO SALDO BANCÁRIO É DE R${balance:.2f}\n")

                    #CASO O USUÁRIO OPTE POR NÃO REALIZAR A VENDA O SISTEMA RETORNARÁ AO MENU INICIAL;
                    elif yes_no == "NÃO" or yes_no == "NAO":
                        print("\nRETORNO AO MENU INICIAL\n")
                    
                    #OS PRÓXIMOS 'ELSE' SERÃO APENAS PARA MOSTRAR AO USUÁRIO QUE A OPÇÃO QUE ELE ESCOLHEU É INVALIDA;
                    else:
                        print("\nOPÇÃO INVÁLIDA!\n")
                else:
                    print("\nOPÇÃO INVÁLIDA!\n")
            else:
                print("\nOPÇÃO INVÁLIDA!\n")

        #NESTE SEGUNDO CASE O USUÁRIO ESCOLHEU ALUGAR UM DOS AUTOMÓVEIS DA CARTELA DA REVENDEDORA;
        case 2:
            print("-- ALUGUEL DE AUTOMÓVEL --")
            print("\nMARCAS DISPONÍVEIS:")

            #APARECERÁ NA TELA PARA O USUÁRIO AS MARCAS QUE A REVENDEDORA TRABALHA;
            for brand in car_list:
                print(brand)
            brand = input("\nQUAL A MARCA VOCÊ DESEJA:").upper()
            
            #VERIFICAÇÃO SE A MARCA DO AUTOMÓVEL QUE O USUÁRIO DIGITARÁ ESTÁ DENTRO DA CARTELA PRÉVIA;
            if brand in car_list:
                print("\nAUTOMÓVEIS DISPONÍVEIS:")

                #APARECERÁ NA TELA PARA O USUÁRIO OS AUTOMÓVEIS DA CARTELA DA REVENDEDORA;
                for car in car_list[brand]:
                    print(car)
                car = input("\nQUAL AUTOMÓVEL VOCÊ DESEJA:").upper()
                
                #VERIFICAÇÃO SE O MODELO DO AUTOMÓVEL QUE O USUÁRIO DIGITARÁ ESTÁ DENTRO DA CARTELA PRÉVIA;
                #CASO TODAS AS OPÇÕES SEJAM SATISFEITAS O SISTEMA PERGUNTARÁ POR QUANTOS DIAS O USUÁRIO DESEJA FAZER ESSA RESERVA;
                #E ENTÃO APARECERÁ O VALOR DA DIÁRIA E O TOTAL;
                if car in car_list[brand]:
                    day = int(input(f"\nPOR QUANTOS DIAS DESEJA FAZER O ALUGUEL DO {brand} {car}:"))
                    price_to_rent = day * 77
                    print(f"\nA DIÁRIA DE ALUGUEL DO {brand} {car} É DE R$77,00")
                    print(f"O VALOR TOTAL É DE R${price_to_rent:.2f} POR {day} DIAS")

                    #CASO O SALDO DO CLIENTE SEJA SUFICIENTE PARA REALIZAR ESSA RESERVA O SISTEMA CONTINUARÁ;
                    if balance >= price_to_rent:

                        #APÓS ANALISE DE VALORES O USUÁRIO ESCOLHERÁ SE QUER REALIZAR A RESERVA;
                        yes_no = input("\nDESEJA FINALIZAR O ALUGUEL: (SIM/NÃO)").upper()

                        #CASO O USUÁRIO OPTE POR REALIZAR RESERVA O SALDO BANCÁRIO DELE DIMINUIRÁ COM O VALOR DAS DIÁRIAS DO AUTOMÓVEL E ELE SERÁ INFORMADO DE SEU NOVO SALDO;
                        #O AUTOMÓVEL TAMBÉM NÃO ESTARÁ DISPONIVEL PARA ALUGUEL E PARA VENDAS FUTURAS;
                        if yes_no == "SIM":
                            car_list[brand].remove(car)
                            balance -= price_to_rent
                            print(f"\nALUGUEL REALIZADO!\n{name}, SEU NOVO SALDO BANCÁRIO É DE R${balance:.2f}\n") 
                        
                        #CASO O USUÁRIO OPTE POR NÃO REALIZAR A RESERVA O SISTEMA RETORNARÁ AO MENU INICIAL;
                        elif yes_no == "NÃO" or yes_no == "NAO":
                            print("\nRETORNO AO MENU INICIAL\n")
                        
                        #OS PRÓXIMOS 'ELSE' SERÃO APENAS PARA MOSTRAR AO USUÁRIO QUE A OPÇÃO QUE ELE ESCOLHEU É INVALIDA;
                        else:
                            print("\nOPÇÃO INVÁLIDA!\n")
                    else:
                        print("\nSALDO INSUFICIENTE!\n")
                else:
                    print("\nOPÇÃO INVÁLIDA!\n")
            else:
                print("\nOPÇÃO INVÁLIDA!\n")

        #NESTE TERCEIRO CASE O USUÁRIO ESCOLHEU FAZER A COMPRA DE UM DOS AUTOMÓVEIS DA CARTELA DA REVENDEDORA;
        case 3:
            print("-- COMPRA DE AUTOMÓVEL --")
            print("\nMARCAS DISPONÍVEIS:")

            #APARECERÁ NA TELA PARA O USUÁRIO AS MARCAS QUE A REVENDEDORA TRABALHA;
            for brand in car_list:
                print(brand)
            brand = input("\nQUAL A MARCA VOCÊ DESEJA:").upper()

            #VERIFICAÇÃO SE A MARCA DO AUTOMÓVEL QUE O USUÁRIO DIGITARÁ ESTÁ DENTRO DA CARTELA PRÉVIA;
            if brand in car_list:
                print("\nAUTOMÓVEIS DISPONÍVEIS:")

                #APARECERÁ NA TELA PARA O USUÁRIO OS AUTOMÓVEIS DA CARTELA DA REVENDEDORA;
                for car in car_list[brand]:
                    print(car)
                car = input("\nQUAL AUTOMÓVEL VOCÊ DESEJA:").upper()

                #VERIFICAÇÃO SE O MODELO DO AUTOMÓVEL QUE O USUÁRIO DIGITARÁ ESTÁ DENTRO DA CARTELA PRÉVIA;
                #CASO TODAS AS OPÇÕES SEJAM SATISFEITAS O SISTEMA MOSTRARÁ O VALOR DO AUTOMÓVEL DE ACORDO COM A TABELA FIPE E TAMBÉM O VALOR DE VENDA DELE;
                if car in car_list[brand]:
                    price = car_to_sell[brand][car]
                    price_to_sell = price * 1.25
                    print(f"\nO VALOR DE ACORDO COM A TABELA FIPE DESSE AUTOMÓVEL É R${price:.2f}")
                    print(f"O VALOR DESSE VEÍCULO É R${price_to_sell:.2f}")
            
                    #CASO O SALDO DO CLIENTE SEJA SUFICIENTE PARA REALIZAR ESSA RESERVA O SISTEMA CONTINUARÁ;
                    if balance >= price_to_sell:
                        
                        #APÓS ANALISE DE VALORES O USUÁRIO ESCOLHERÁ SE QUER REALIZAR A COMPRA;
                        yes_no = input("\nDESEJA FINALIZAR A COMPRA: (SIM/NÃO)").upper()

                        #CASO O USUÁRIO OPTE POR REALIZAR A COMPRA O SALDO BANCÁRIO DELE DIMINUIRÁ COM O VALOR DA COMPRA DO AUTOMÓVEL E ELE SERÁ INFORMADO DE SEU NOVO SALDO;
                        #O AUTOMÓVEL TAMBÉM NÃO ESTARÁ DISPONIVEL PARA VENDAS FUTURAS;
                        if yes_no == "SIM":
                            car_list[brand].remove(car)
                            balance -= price_to_sell
                            print(f"\nCOMPRA REALIZADA!\n{name}, SEU NOVO SALDO BANCÁRIO É DE R${balance:.2f}\n") 
                        
                        #CASO O USUÁRIO OPTE POR NÃO REALIZAR A COMPRA O SISTEMA RETORNARÁ AO MENU INICIAL;
                        elif yes_no == "NÃO" or yes_no == "NAO":
                            print("\nRETORNO AO MENU INICIAL\n")
                        
                        #OS PRÓXIMOS 'ELSE' SERÃO APENAS PARA MOSTRAR AO USUÁRIO QUE A OPÇÃO QUE ELE ESCOLHEU É INVALIDA;
                        else:
                            print("\nOPÇÃO INVÁLIDA!\n")
                    else:
                        print("\nSALDO INSUFICIENTE!\n")
                else:
                    print("\nOPÇÃO INVÁLIDA!\n")
            else:
                print("\nOPÇÃO INVÁLIDA!\n")

        #NO CASE 0 O USUÁRIO OPTOU PELA SAÍDA TOTAL DO SISTEMA;                        
        case 0:
            count = 0

        #NO CASE INDEFINIDO O USUÁRIO RECEBERÁ UMA MENSAGEM DE AVISO PARA QUE ELE SAIBA QUE ESCOLHEU UMA OPÇÃO INVÁLIDA E O MENU TORNARÁ A APARECER COM AS OPÇÕES POSSÍVEIS TERÁ NO DISPLAY;
        case _:
            print("\nOPÇÃO INVÁLIDA!\n")