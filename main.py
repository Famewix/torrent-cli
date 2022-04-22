from tpblite import TPB
from tpblite import CATEGORIES, ORDERS
from pick import pick
from termcolor import colored

categories = {
    "AUDIO":CATEGORIES.AUDIO.ALL,
    "VIDEO":CATEGORIES.VIDEO.ALL,
    "PORN":CATEGORIES.PORN.ALL,
}

def play_torrent(magnet_link):
    try:
        os.system(f'peerflix -k -l "{magnet_link}"')
    except KeyboardInterrupt:
        pass


def category_select():
    category, index = pick(list(categories.keys()), "Category")
    return category

def torrent_select(torrent_ls: list):
    torrent_options = [torrent for torrent in torrent_ls[:25]]
    torrent_name, torrent_index = pick(torrent_options, "Select Torrent to Watch")
    selected_torrent = torrent_ls[torrent_index]
    return selected_torrent



def search_torrents(t, search_q: str):
    print(colored(f"Searching for {search_q}", "green"))
    torrents = t.search(search_q)
    selected_tor = torrent_select(torrents)
    mg_torrent = selected_tor.magnetlink
    play_torrent(mg_torrent)

def browse_torrents(t):

    category = category_select()
    torrents = t.browse(category=categories[category], page=1, order=ORDERS.UPLOADED.DES)

    for torrent in torrents:
        print(torrent)

def top_torrents(t):
    category = category_select()

    torrents = t.top(category=categories[category])
    selected_tor = torrent_select(torrents)
    mg_torrent = selected_tor.magnetlink
    play_torrent(mg_torrent)

def main():
    t = TPB('https://tpb.party')
    title = 'Torrent CLI'
    os.system('cls')
    options = ['Search Torrents', 'Browse Torrents', 'Top 100']
    option, index = pick(options, title)
    if index == 0:
        search_query = input('Search: ')
        search_torrents(search_query, t)
    elif index == 1:
        browse_torrents(t)
    elif index == 2:
        top_torrents(t)

if __name__ == "__main__":
    main()