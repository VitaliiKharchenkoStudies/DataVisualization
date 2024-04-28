import instaloader
import networkx as nx
import matplotlib.pyplot as plt

L = instaloader.Instaloader()

L.login("thisaccountcananyoneuse", "thisispassword2024")  # (login)

profile = instaloader.Profile.from_username(L.context, "thisaccountcananyoneuse")

followers_list = []
following_list = []

for follower in profile.get_followers():
    followers_list.append(follower.username)

for following in profile.get_followees():
    following_list.append(following.username)

G = nx.Graph()
main_account = "thisaccountcananyoneuse"


def GetDataToSet(data):
    list = []
    for info in data:
        list.append(info.username)
    return set(list)


G.add_node(main_account)

for follower in followers_list:
    G.add_edge(main_account, follower)

for following in following_list:
    G.add_edge(main_account, following)

for follower in followers_list:
    follower_profile = GetDataToSet(instaloader.Profile.from_username(L.context, follower).get_followers())
    for following in following_list:
        following_profile = GetDataToSet(instaloader.Profile.from_username(L.context, following).get_followees())
        if follower_profile.intersection(following_profile) or following_profile.intersection(
                follower_profile) or follower_profile.intersection(follower) or following_profile.intersection(
            following):
            G.add_edge(follower, following)

plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')
plt.title("Граф підписчиків Instagram")
plt.show()
