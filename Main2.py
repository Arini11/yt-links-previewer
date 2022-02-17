# -*- coding: utf-8 -*-
# Sample Python code for youtube.videos.list

import os
from urllib.parse import urlparse, parse_qs

import googleapiclient.discovery
import googleapiclient.errors


def getTitol(url):
    parsed_url = urlparse(url)
    print(parsed_url)
    video_id = parse_qs(parsed_url.query)['v'][0].strip()
    print(video_id.strip())

    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyCW-hP-GRQPDpvWjbktxYu6eOiyas5Fwx4"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    print(response)
    for video in response["items"]:
        print(video["snippet"]["title"])
        return video["snippet"]["title"]
