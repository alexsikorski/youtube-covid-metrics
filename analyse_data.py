import os
import pickle


def load_pkl(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


def main():
    # Statistics
    video_count = 0
    total_views = 0
    total_comments = 0
    total_likes = 0
    total_dislikes = 0

    c_video_count = 0
    c_total_views = 0
    c_total_comments = 0
    c_total_likes = 0
    c_total_dislikes = 0
    # Statistics

    pkl_count = 0
    videos = []
    covid_videos = []

    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".pkl"):
                pkl_count += 1
                videos += load_pkl(subdir + "/" + file)

    # to use latest videos and remove duplicates
    seen = set()
    filtered_videos = []
    for video in videos:
        for (k, v) in video.items():
            if k == "title":
                # if it already exists, update
                if v in seen:
                    for filtered_video in filtered_videos:
                        for (f_k, f_v) in filtered_video.items():
                            if f_k == "title":
                                if f_v == v:
                                    filtered_videos.remove(filtered_video)
                                    filtered_videos.append(video)

                # if doesnt, add entry
                if v not in seen:
                    seen.add(v)
                    filtered_videos.append(video)

    video_count = len(filtered_videos)
    print("Total entries:", video_count)

    # for averages
    for video in filtered_videos:
        for (k, v) in video.items():
            if v is not None:
                if k == "views":
                    total_views += int(v)
                if k == "comments":
                    total_comments += int(v)
                if k == "likes":
                    total_likes += int(v)
                if k == "dislikes":
                    total_dislikes += int(v)

    # isolate COVID-19 related videos
    for video in filtered_videos:
        for (k, v) in video.items():
            if k == "title":
                temp_lower = v.lower()
                if "covid-19" in temp_lower or "covid" in temp_lower or "coronavirus" in temp_lower or "quarantine" in temp_lower:
                    covid_videos.append(video)

    c_video_count = len(covid_videos)

    # for COVID-19 averages
    for video in covid_videos:
        for (k, v) in video.items():
            if v is not None:
                if k == "views":
                    c_total_views += int(v)
                if k == "comments":
                    c_total_comments += int(v)
                if k == "likes":
                    c_total_likes += int(v)
                if k == "dislikes":
                    c_total_dislikes += int(v)

    print("Average views:", total_views/video_count)
    print("Average COVID-19 views:", c_total_views/c_video_count)
    print("Average comment per view", total_comments/total_views)
    print("Average COVID-19 comment per  view", c_total_comments/c_total_views)
    print("Average likes per view", total_likes/total_views)
    print("Average COVID-19 likes per comment", c_total_likes/c_total_views)
    print("Average dislikes per view", total_dislikes/total_views)
    print("Average COVID-19 dislikes per view", c_total_dislikes/c_total_views)
    print("")
    print("Average likes per comment", total_likes/total_comments)
    print("Average COVID-19 likes per comment", c_total_likes/c_total_comments)
    print("Average dislikes per comment", total_dislikes/total_comments)
    print("Average COVID-19 dislikes per comment", c_total_dislikes/c_total_comments)


if __name__ == "__main__":
    main()
