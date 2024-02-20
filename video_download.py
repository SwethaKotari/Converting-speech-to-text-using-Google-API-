# 1.Sets the Google Cloud credentials environment variable using the specified JSON file ("Key.json").
# 2.download the youtube video using url.
# 3.Take the video file as input and extract the audio from video file.
# 4.prints the transcription results using google online technique. 
# 5.write the transcription result in the text file 
# 6.Calling the function with a specific video file



import speech_recognition as sr
from yt_dlp import YoutubeDL
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import time
from optparse import OptionParser

def set_google_credentials(credentials_path):
    # Set the Google Cloud credentials environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

def download_video(youtube_url, output_path="."):
    # Download the YouTube video using yt_dlp
    ydl_opts = {'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s', 'no_check_certificate': True)}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
    return os.path.join(output_path, f"{info_dict['title']}.{info_dict['ext']}")

def extract_audio(video_path):
    # Extract audio from the video using moviepy
    audio_path = "temp_audio.wav"
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    return audio_path

def wait_for_download_completion(video_path):
    # Wait for the video file to be fully downloaded
    while not os.path.exists(video_path):
        time.sleep(1)

def transcribe_audio(audio_path, duration=30):
    # Transcribe the first 30 seconds of audio using SpeechRecognition
    r = sr.Recognizer()
    recognized_text = ""  # Initialize an empty string to store recognized text

    with sr.AudioFile(audio_path) as source:
        # Record the first 30 seconds of audio file
        audio_data = r.record(source, duration=duration)

        try:
            # Use online Google Speech Recognition API for the specified duration
            result = r.recognize_google(audio_data, language="en-US")
            transcription = f"Transcription: {result}\n"
            recognized_text += transcription
            print(transcription)
            print("Successfully extracted the text from  video")

        except sr.UnknownValueError:
            no_speech_message = "No speech found in the audio\n"
            recognized_text += no_speech_message
            print(no_speech_message)

        except sr.RequestError as e:
            error_message = f"Could not request results; {e}\n"
            recognized_text += error_message
            print(error_message)

    return recognized_text

def write_to_file(text, output_file='recognized.txt'):
    # Write the recognized text to a file
    with open(output_file, mode='w') as file:
        file.write("Recognized Speech:\n")
        file.write(text)

def main(youtube_url, credentials_path, output_file='recognized.txt', download_path="."):
    # Set Google Cloud credentials environment variable
    set_google_credentials(credentials_path)

    # Download the YouTube video
    video_path = download_video(youtube_url, download_path)

    # Extract audio from the video
    audio_path = extract_audio(video_path)

    # Wait for the video file to be fully downloaded
    wait_for_download_completion(video_path)

    # Transcribe the first 30 seconds of audio
    transcription_result = transcribe_audio(audio_path, duration=30)

    # Write the results to a file
    write_to_file(transcription_result, output_file)

if __name__ == "__main__":
    parser = OptionParser(description="Download and transcribe a YouTube video.")
    parser.add_option("-u", "--url", dest="youtube_url", help="URL of the YouTube video to transcribe", default="https://www.youtube.com/watch?v=-qngILxqGX0&t")
    parser.add_option("-c", "--credentials", dest="credentials_path", help="Path to the Google Cloud credentials JSON file", default="Key.json")
    parser.add_option("-o", "--output-file", dest="output_file", help="Path to the output file for transcription", default='recognized.txt')
    parser.add_option("-d", "--download-path", dest="download_path", help="Path to the folder where the video will be downloaded", default='downloaded_videos')
    options, _ = parser.parse_args()

    if not options.youtube_url or not options.credentials_path:
        parser.error("Both YouTube URL and credentials path are required.")

    # Call the main function with the specified options
    video_path = download_video(options.youtube_url, options.download_path)
    audio_path = extract_audio(video_path)
    wait_for_download_completion(video_path)
    transcription_result = transcribe_audio(audio_path, duration=30)
    write_to_file(transcription_result, options.output_file)
