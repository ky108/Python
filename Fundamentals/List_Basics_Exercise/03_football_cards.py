team_A, team_B = [0] * 11, [0] * 11
cards = input().split()
terminated = False
for card in set(cards):
    if 'A' in card:
        team_A.pop()
    else:
        team_B.pop()

    if len(team_A) < 7 or len(team_B) < 7:
        terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if terminated:
    print("Game was terminated")

# team_A, team_B = [int(x) for x in range(1, 12)], [int(x) for x in range(1, 12)]
# cards = input().split()
# terminated = False
# for card in set(cards):
#     if card.split("-")[0] == "A":
#         team_A.remove(int(card.split("-")[1]))
#     else:
#         team_B.remove(int(card.split("-")[1]))
#     if len(team_A) < 7 or len(team_B) < 7:
#         terminated = True
#         break
#
# print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
# if terminated:
#     print("Game was terminated")


# team_A, team_B = [int(x) for x in range(1, 12)], [int(x) for x in range(1, 12)]
# cards = input().split()
# terminated = False
# for card in cards:
#     temp = card.split("-")
#     team = temp[0]
#     player = int(temp[1])
#     if team == "A":
#         if player not in team_A:
#             continue
#         team_A.remove(player)
#         if len(team_A) < 7:
#             terminated = True
#             break
#     else:
#         if player not in team_B:
#             continue
#         team_B.remove(player)
#         if len(team_B) < 7:
#             terminated = True
#             break
#
# print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
# if terminated:
#     print("Game was terminated")

# A-1 A-5 A-10 B-2 A-10 A-7 A-3
