from random import randint

lista_npcs = []

player = {
    "nome": "Ydrill",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dano":25,

}
def criar_npc(level):
    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max":  100 * level,
        "exp": 7 * level,
}
    return novo_npc

def gerar_npcs(n_npcs):
    
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)

def exibir_npcs():
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']}//Level:{npc['level']}// Dano: {npc['dano']}//hp: {npc['hp']}// EXP: {npc['exp']}")
def exibir_npc(npc):
    print (
          print(f"Nome: {npc['nome']}//Level:{npc['level']}// Dano: {npc['dano']}//hp: {npc['hp']}// EXP: {npc['exp']}")
    )
def exibir_player(npc):
    print (
          print(f"Nome: {player['nome']}//Level:{player['level']}// Dano: {player['dano']}//hp: {player['hp']}/{player['hp_max']}// EXP: {player['exp']}/{player['exp_max']}")
    )
#reset
def reset_player():
    player['hp'] = player ['hp_max']

def reset_npc(npc):
    npc['hp'] = npc ['hp_max']

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= 2
        player['hp_max'] += 20
        player['hp'] = player ['hp_max']
        
# inicio
def iniciar_batalha(npc):
    while player['hp'] > 0 and npc["hp"] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
    if player["hp"] > 0:
        print(f"O {player['nome']} venceu e ganhou {npc['exp']} de EXP!")
        player['exp'] += npc['exp']
        exibir_player(npc)

    else:
        print(f"O {npc['nome']} venceu a batalha!")
        exibir_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)

#ataque
def atacar_player(npc):
    npc['hp'] -=  player['dano']

def atacar_npc(npc):
    player['hp'] -= npc['dano']
    
#info_batalha

def exibir_info_batalha(npc):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC {npc['nome']}: {npc['hp']}/{npc['hp_max']}")
    print("------------------")
gerar_npcs(5)   
# exibir_npcs()

npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)

