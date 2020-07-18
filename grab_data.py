import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from datetime import datetime

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    today = datetime.today()
    dir_name = str("./data/" + str(today.day) + "-"
                   + str(today.month) + "-" + str(today.year) + "/")
    dir_name_write = str("data/" + str(today.day) + "-"
                         + str(today.month) + "-" + str(today.year) + "/")

    create_folder(dir_name)

    page_count = 1
    file_name = "data-"

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    first_request = youtube.videos().list(
        part="snippet,contentDetails,statistics,topicDetails",
        chart="mostPopular",
        maxResults=50,
        regionCode="US"
    )
    first_response = first_request.execute()

    with open(dir_name_write + file_name + str(page_count) + ".json", "w") as outfile:
        json.dump(first_response, outfile)

    while True:
        next_page = obtain_page(dir_name_write + file_name + str(page_count) + ".json")
        if next_page is None:
            break
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics,topicDetails",
            chart="mostPopular",
            maxResults=50,
            pageToken=str(next_page),
            regionCode="US"
        )
        response = request.execute()
        print("\rWriting file data-" + str(page_count) + ".json", end="")
        page_count = page_count + 1

        with open(dir_name_write + file_name + str(page_count) + ".json", "w") as outfile:
            json.dump(response, outfile)

    print("\rWriting file data-" + str(page_count) + ".json... All done!", end="")


def obtain_page(data_file):
    f = open(data_file)
    data = json.load(f)
    for (k, v) in data.items():
        if k == "nextPageToken":
            return v


def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print('Error when creating directory. ' + path)


if __name__ == "__main__":
    main()
