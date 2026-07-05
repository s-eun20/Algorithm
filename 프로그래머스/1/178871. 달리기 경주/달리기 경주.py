def solution(players, callings):
    rank = {}

    for i, player in enumerate(players):
        rank[player] = i

    for calling in callings:
        current_rank = rank[calling]
        front_player = players[current_rank - 1]

        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]

        rank[calling] -= 1
        rank[front_player] += 1

    return players