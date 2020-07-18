import json
import os
import pickle

videos = []


def save_pkl(data, name):
    with open(name + ".pkl", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def main():
    # Generate pkl files for each entry

    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".json") and file.startswith("data"):
                file_location = os.path.join(subdir, file)
                try:
                    f = open(file_location, "r", encoding="utf8", errors="ignore")
                except FileNotFoundError:
                    print("\rAll done!", end="")
                    break

                file_data = json.load(f)
                print("\rOpening file..." + file_location, end="")

                items = file_data.get("items")
                for item in items:
                    video = {"title": None, "views": None, "tags": None}
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

                    videos.append(video)

            save_pkl(videos, "vid_master")

    for video in videos:
        print(video)


if __name__ == "__main__":
    main()
