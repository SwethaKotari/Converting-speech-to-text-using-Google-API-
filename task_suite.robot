*** Settings ***
Library    video_download.py

*** Variables ***
${YOUTUBE_URL}         https://www.youtube.com/watch?v=-qngILxqGX0&t
${CREDENTIALS_PATH}    Key.json
${OUTPUT_FILE}         recognized1.txt
${DOWNLOAD_PATH}       downloaded_videos

*** Tasks ***
Download and Transcribe YouTube Video
    Log    Starting the transcription process for the YouTube video
    Set Google Credentials    ${CREDENTIALS_PATH}
    Log    Google Cloud credentials set successfully
    ${video_path}=    Download Video    ${YOUTUBE_URL}    ${DOWNLOAD_PATH}
    Log    Video downloaded successfully to ${video_path}
    ${audio_path}=    Extract Audio    ${video_path}
    Log    Audio extracted successfully to ${audio_path}
    Wait For Download Completion    ${video_path}
    Log    Video download completed
    ${transcription}=    Transcribe Audio    ${audio_path}
    Log    Transcription completed: ${transcription}
    Write To File    ${transcription}    ${OUTPUT_FILE}
    Log    Transcription written to file: ${OUTPUT_FILE}
    Log    Transcription process completed

    