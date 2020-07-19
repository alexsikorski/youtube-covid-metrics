import json
import os
import pickle

videos = []


def save_pkl(data, name):
    with open(name + "video_master.pkl", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def main():
    for subdir, dirs, files in os.walk(os.getcwd()):
        file_count = 0
        videos.clear()
        for file in files:
            if file.endswith(".json") and file.startswith("data"):
                file_location = os.path.join(subdir, file)
                try:
                    f = open(file_location, "r", encoding="utf8", errors="ignore")
                except FileNotFoundError:
                    print("\rAll done!", end="")
                    break

                file_data = json.load(f)
                print("\rOpening file... " + file_location, end="")

                items = file_data.get("items")
                for item in items:
                    video = {"title": None, "tags": None, "views": None, "comments": None, "likes": None,
                             "dislikes": None}
                    snippets = item.get("snippet")
                    statistics = item.get("statistics")

                    for key, value in snippets.items():
                        if key == "title":
                            video["title"] = value
                        elif key == "tags":
                            video["tags"] = value

                    for key, value in statistics.items():
                        if key == "viewCount":
                            video["views"] = value
                        elif key == "commentCount":
                            video["comments"] = value
                        elif key == "likeCount":
                            video["likes"] = value
                        elif key == "dislikeCount":
                            video["dislikes"] = value

                    videos.append(video)
                file_count += 1
        if file_count == 4:  # there can only be 4 files as there are only 4 pages retrieved from YouTube API
            save_pkl(videos, subdir + "/")


if __name__ == "__main__":
    main()
