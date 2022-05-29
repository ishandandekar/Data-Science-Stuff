from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


def get_driver():
    """
    Returns configured driver object
    """
    # Configuring options for the driver not hinder the scraping process
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')

    # Path for the executable webdriver
    driver = webdriver.Chrome(
        'C:\Program Files (x86)\chromedriver.exe', options=options)
    return driver


def get_videos(driver, link):
    """
    Returns a list of video objects
    """

    # Navigate to the trending page
    driver.get(link)

    # Get the list of videos
    VIDEO_DIV_TAG = "ytd-video-renderer"
    return driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)


def parse_video(video):
    """
    Parses a video element and returns a dictionary with the video info
    """
    video_info = {}
    video_info['title'] = video.find_element(By.ID, 'video-title').text
    video_info['thumbnail'] = video.find_element(
        By.TAG_NAME, 'img').get_attribute('src')
    video_info['url'] = video.find_element(
        By.ID, 'video-title').get_attribute('href')
    video_info['channel'] = video.find_element(
        By.CLASS_NAME, 'ytd-channel-name').text
    video_info['views'] = video.find_element(
        By.ID, 'metadata-line').text.split('\n')[0]
    video_info['since'] = video.find_element(
        By.ID, 'metadata-line').text.split('\n')[1]
    return video_info


def move_cursor(driver):
    """
    Moves the cursor to the bottom of the page
    """
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)


def create_dataframe(videos):
    """
    Creates a dataframe from a list of video objects
    """
    videos_info = []
    for video in videos:
        videos_info.append(parse_video(video))
    return pd.DataFrame(videos_info)


def create_csv(df):
    """
    Creates a csv file from a dataframe
    """
    df.to_csv('trending_videos.csv', index=False)


def main():
    """
    Main function
    """
    YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"
    driver = get_driver()
    videos = get_videos(driver, YOUTUBE_TRENDING_URL)
    move_cursor(driver=driver)
    df = create_dataframe(videos[:10])
    create_csv(df)
    driver.quit()


if __name__ == '__main__':
    main()
