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

    video_count = len(videos)

    # for averages
    for video in videos:
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
    for video in videos:
        for(k, v) in video.items():
            if k == "title":
                temp_lower = v.lower()
                if "covid-19"in temp_lower or "covid" in temp_lower or "coronavirus" in temp_lower or "quarantine" in temp_lower:
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
    


if __name__ == "__main__":
    main()
