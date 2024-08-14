
from get_url import *
from get_match_data import *
from save import *

def main():
    event_url = 'https://www.vlr.gg/event/matches/2097/valorant-champions-2024/?series_id=all'
    match_url = get_match_url(event_url)
    match_name = get_match_name(match_url)
    # print(match_name)
    completed_urls = get_completed_url(match_url)
    splice_completed_url = splice_url(completed_urls)

    for i in range(len(splice_completed_url)):
        # print(url)
        match_no = get_match_no(splice_completed_url[i])
        map_no = coresponding_map_no(match_no)
        # print(map_no)
        spliced_match_url = splice_match_no(splice_completed_url[i],match_no)
        data = []
        for j in range(len(map_no)):
            detailed_data = get_data(spliced_match_url[j],map_no[j])
            data += detailed_data
        # print(data)

        save_to_csv(data,f'{match_name[i]}.csv','data')
        print(f'{match_name[i]} succesfully saved!')


if __name__ == "__main__":
    main()