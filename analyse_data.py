import os
import pickle


def load_pkl(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


def main():
    pkl_count = 0
    videos = []
    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".pkl"):
                pkl_count += 1
                videos.append(load_pkl(subdir + "/" + file))


if __name__ == "__main__":
    main()
