import os
import pickle


def load_pkl(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


def main():
    # Statistics
    video_count = 0
    total_views = 0
    # Statistics

    pkl_count = 0
    videos = []
    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".pkl"):
                pkl_count += 1
                videos = videos + load_pkl(subdir + "/" + file)

    video_count = len(videos)

    for video in videos:
        for (k, v) in video.items():
            if k == "views":
                total_views += int(v)

    print(total_views)
    print("Average views:", total_views/video_count)

if __name__ == "__main__":
    main()
