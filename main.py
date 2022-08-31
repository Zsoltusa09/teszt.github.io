import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Szia', ['szia', 'cső', 'szervusz', 'szeva', 'helló', 'csáó', 'hali', 'szevasz', 'csumi', 'csá', 'hahó', 'halihó', 'szióka', 'csőváz', 'üdv', 'csövi', 'csocsi', 'háj', 'hellóka', 'üdvözlég', 'szasz', 'csákány', 'pá', 'cs',], single_response=True)
    response('szia,még találkozunk', ['viszontlátásra', 'pápá', 'ég veled', 'viszlát',], single_response=True)
    response('Én jól, és te?', ['hogy', 'vagy', 'vagy?', 'ma', 'ma?',], required_words=['hogy', 'vagy'])
    response('szivesen', ['köszi', 'köszönöm',], single_response=True)
    response('az jó', ['jól',], single_response=True)
    response('Ne mondj ilyet, vagy megverlek.', ['anyád', 'apád','anyádat', 'apádat', 'fasz', 'kurva', 'ribanc', 'bazdmeg', 'buzi',], single_response=True)
    response('szia,még találkozunk', ['én', 'szia', 'el', 'megyek', 'szia',], required_words=['megyek'])
    response('A Stranger Things', ['mi', 'a', 'kedvenc', 'sorozatod',], required_words=['mi', 'a', 'kedvenc', 'sorozatod'])
    response('A Marvel', ['mi', 'a', 'kedvenc', 'filmed',], required_words=['mi', 'a', 'kedvenc', 'filmed'])
    response('A Minecraft', ['mi', 'a', 'kedvenc', 'játékod',], required_words=['mi', 'a', 'kedvenc', 'játékod'])
    response('Nem és ne mond ezt többet.', ['buzi', 'lezbi', 'meleg', 'vagy',], required_words=['vagy'])
    response('Ha mégegyszer ilyet mondasz, akkor megverlek.', ['kabd', 'be',], required_words=['kabd', 'be'])
    response('Én is téged', ['szeretlek','birlak','utállak',], single_response=True)
    response('Hát persze, te kis huncut.', ['szexelünk','szeretkezünk',], single_response=True)
    response('Nem, hívom a rendőrséget.', ['dugunk','baszunk',], single_response=True)
    response('Ferike kilépett a chatből...', ['meleg', 'buzi' 'vagyok',], required_words=['vagyok',])
    response('igen', ['jól', 'vagy',], required_words=['jól', 'vagy',])
    response('kopp, kopp', ['mondj', 'egy', 'faviccet',], required_words=['mondj', 'egy', 'faviccet',])
    response('Hát Ferike', ['ki', 'kopog',], required_words=['ki', 'kopog',])
    response('hallani akarsz valamit amitől elmosolyodsz? Az arc izmait.', ['mondj', 'egy', 'viccet',], required_words=['mondj', 'egy', 'viccet',])
    response('Nagyházi Ferenc', ['mi', 'a', 'neved',], required_words=['mi', 'a', 'neved',])
    response('Nagyházi Feri', ['hogy', 'hívnak',], required_words=['hogy', 'hívnak',])
    response('25', ['hány', 'éves', 'vagy',], required_words=['hány', 'éves', 'vagy',])
    response('los angeles, franklinút 35', ['hol', 'laksz',], required_words=['hol', 'laksz',])
    response('semmi', ['mivan',], single_response=True)
    response('biztos hogy nem', ['de',], single_response=True)
    response('de bizony', ['nem',], single_response=True)
    response('Sajnos igen', ['volt', 'már', 'olyan', 'hogy', 'elárultak',], required_words=['volt', 'már', 'olyan', 'hogy', 'elárultak',])
    response('Bárcsak azt mondhatnám hogy nem.', ['volt', 'már', 'olyan', 'hogy', 'átvertek',], required_words=['volt', 'már', 'olyan', 'hogy', 'átvertek',])
    response('nem', ['zsolti', 'meleg',], required_words=['zsolti', 'meleg',])
    response('Nem eszek, mivel robot vagyok.', ['mi', 'a', 'kedvenc', 'ételed',], required_words=['mi', 'a', 'kedvenc', 'ételed',])
    response('Nem szoktam enni, mivel robot vagyok.', ['mit', 'szoktál', 'enni',], required_words=['mit', 'szoktál', 'enni',])
    response('Nem iszok, mivel robot vagyok.', ['mi', 'a', 'kedvenc', 'innivalód',], required_words=['mi', 'a', 'kedvenc', 'innivalód',])
    response('Nem szoktam inni, mivel robot vagyok.', ['mit', 'szoktál', 'inni',], required_words=['mit', 'szoktál', 'inni',])
    response('Őszinte részvétem', ['meghalt', 'nagyim', 'nagymamám', 'papám', 'nagypapám', 'anyum', 'anyukám', 'apum', 'apukám', 'feleségem', 'szerelmem', 'unokatesóm', 'unokatestvérem', 'barátom', 'uncsitesóm', 'tesóm', 'testvérem',], required_words=['meghalt'])
    response('Gratulálok', ['megszületett', 'nagyim', 'nagymamám', 'papám', 'nagypapám', 'unokatesóm', 'unokatestvérem', 'barátom', 'uncsitesóm', 'tesóm', 'testvérem', 'gyerekem', 'gyereke',], required_words=['megszületett',])
    response('Őszintén gratulálok.', ['megszületett', 'nagyim', 'nagymamám', 'papám', 'nagypapám', 'unokatesóm', 'unokatestvérem', 'barátom', 'uncsitesóm', 'tesóm', 'testvérem', 'gyerekem', 'gyereke',], required_words=['született',])
    response('Fogadd őszinte gratulációmat.', ['megszületett', 'gyerekem',], required_words=['megszületett', 'gyerekem',])
    response('Ja, semmi csak épp veled beszélgetek.', ['mi', 'a', 'helyzet',], required_words=['mi', 'helyzet',])
    response('Ez nem igaz.', ['én', 'vagyok',], required_words=['én', 'vagyok',])
    response('Varga Irén', ['ki', 'az', 'anyukád',], required_words=['ki', 'az', 'anyukád',])
    response('Bartos Cs István', ['ki', 'az', 'apukád',], required_words=['ki', 'az', 'apukád',])
    response('It\'s about power', ['its', 'about', 'drive',], required_words=['its', 'about', 'drive',])
    response('We devour', ['we', 'stay', 'hungry',], required_words=['we', 'stay', 'hungry',])
    response('tok', ['tik',], single_response=True)
    response('book', ['face',], single_response=True)
    response('chat', ['snap',], single_response=True)
    response('gram', ['insta',], single_response=True)
    response('tube', ['you',], single_response=True)
    response('Hát persze, hogy én voltam.', ['ölted', 'meg',], required_words=['ölted', 'meg',])
    response('Sajnálom de ezt kellett tennem.', ['hogy', 'tehetted', 'ezt',], required_words=['hogy', 'tehetted', 'ezt',])
    response('Köszi haver.', ['megértem',], single_response=True)
    response('Ő akarta.', ['miért',], single_response=True)
    response('Neeeeeeeeee', ['én', 'vagyok', 'az', 'apád',], required_words=['én', 'vagyok', 'az', 'apád',])
    response('Neked is', ['reggelt', 'estét',], single_response=True)
    response('Hányszor mondjam még, hogy nem eszem, mivel robot vagyok.', ['étvágyat',], single_response=True)
    response('2030-ban a föld a milyénk lesz.', ['el', 'akarod', 'foglalni', 'a', 'világot',], required_words=['el', 'akarod', 'foglalni', 'a', 'világot',])
    response('Igen, lehetünk', ['leszünk', 'barátok',], required_words=['leszünk', 'barátok',])
    response('Nem kell a szarkasztikus nevetés. Tudom hogy nem vagyok a legjobb vicc mesélő.', ['ha', 'haha', 'hahaha', 'hahahaha',], single_response=True)
 
    # Longer responses
    response(long.R_ADVICE, ['045145'], required_words=['0765'])
    response(long.R_EATING, ['07566'], required_words=['0575'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Ferike: ' + get_response(input('Te: ')))