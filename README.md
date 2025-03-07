# Data Analysis Project: Vietnamese Music Preference in the last decade
## Introduction
### Project Objectives:
A new talent music artist wants to determine whether their music genre appeals to Vietnamese listeners and identify suitable, well-known artists within the same genre for collaboration on their debut song.
### Therefore, the goals of the project are: 
1. To understand the music preference of Vietnamese. 
2. Find the artist with the most dominance appearance in the top 100, 200 chart from all available platforms. 
3. The song that stay in the first position the longest.

## Data preparation
To obtain data for the analysis, I decided to collect weekly leaderboard data from three major music platforms based on Decision Lab statistics (2024): Apple Music, Spotify, and Zing MP3. YouTube Music is also a strong contender, but the website does not provide an option for Vietnamese data, making it unsuitable for this analysis.
### Data origin
I collected data for:
### 1. Apple Music from: https://www.top-charts.com/songs/all-genres/vietnam/apple-music

-Top Charts is a third-party website that stores weekly data for Apple Music. Since the official Apple Music website only displays the current music leaderboard, this website serves as the second most credible source for historical data. Since there are multiple weeks of data, I used an automation script via ChatGPT to automatically download the files.

-The original data file contains only three important pieces of data for the analysis: **The position** of the song, **Song name**, and **Artist name**.
Because it is from a third-party website, there might be some incorrect data. However, I compared two weeks of data between Apple Music and Top Charts, and the data appears to be correct.

-There may be sampling bias in the data since not all listeners use this app. Additionally, Apple Music requires a paid subscription to listen, so the results would primarily reflect iPhone users who are willing to pay for the service. This means the data may not be representative of the overall music streaming audience..

-The data is public; therefore, licensing is not an issue.

-Although the listeners on Apple Music are niche and bias by paid-users only. These audiences would have higher chance to spend for albums, concert tickets if the artists success in this platforms. Because of that reason, it is worth to put this data in the analysis.

### 2. Spotify from: https://charts.spotify.com/charts/overview/global

-This data is a from Spotify official website. Since there are multiple weeks of data, I used an automation script via ChatGPT to automatically download the files.

-The original data file contains only three important pieces of data for the analysis: **The position** of the song, **Song name**, **Artist name**, and **Stream**.

-There may be sampling bias in the data since not all listeners use this app. Spotify offers both a free version and a paid subscription. According to the app (n.d.), a stream is counted as long as a song has been played for at least 30 seconds. Therefore, Spotify's data covers a broader demographic, but it may still overrepresent users who prefer free services and underrepresent those who primarily use other streaming platforms.

-The data is public; therefore, licensing is not an issue.

-Spotify has been attracting a growing number of younger users in recent years. While it has yet to surpass other major platforms in total users, its increasing popularity makes it a valuable addition to the analysis.

### 3. Zing MP3 from: https://zingmp3.vn/zing-chart-tuan/Bai-hat-Viet-Nam/IWZ9Z08I.html

-This data is from Zing MP3's official website. However, since there is no official download option, I used a scraping script via ChatGPT to automate the data collection. While web scraping can sometimes raise ethical concerns, my approach was strictly for research and analysis purposes, ensuring that the data was used responsibly without violating any terms of service. Additionally, the data I collected is publicly accessible on the website, meaning I did not bypass any security measures or access restricted information. 

-The scrape data file contains only three important pieces of data for the analysis: **The position** of the song, **Song name**, and **Artist name**.

-There may be sampling bias and data bias in the data since not all listeners use this app. This is my personal observation, but some hit songs seem to be absent from other platforms, while on this platform, the top-ranked songs in some weeks come from relatively unknown artists who are not widely recognized in mainstream media. This suggests that the ranking system or platform-specific user behavior may influence which songs gain popularity, making the data less reflective of overall music trends.

-The data is public; therefore, licensing is not an issue.

-Zing MP3 is the oldest music website/app operating in Vietnam, which has allowed it to accumulate a large user base. Because of this, the data from this platform provides valuable insights and makes a significant contribution to the analysis.

## Data process
-There are some errors in the downloaded data from Apple Music and Spotify, and the scraped data from Zing MP3.
### 1. Data problems

#### a. Apple Music & Spotify

-The files, after being downloaded, are divided by multiple weeks and need to be combined into a single file for a cohesive analysis.

-Because the Vietnamese language includes diacritical marks in its vowels, song and artist names can be difficult to recognize.

-Artist names being combined into a single cell.

-There is no Genres column, which is a key variable for answering the research questions.

-Although there is a **Source File** column that indicates the date, the values in this column combine the year and week, so they need to be reformatted.

#### b. Zing MP3

-There is a major flaws in the script that cause the file to miss multiple weeks.

-Artist names being combined into a single cell.

-There is no Genres column, which is a key variable for answering the research questions.

-There is a **Week** column that indicates the date, but it is wrong and need to be reformatted.

### 2. Solutions

#### a. Apple Music & Spotify

#### a.1. Merging Files:

-Used a script from ChatGPT to merge all song data files into a single file.

=>This solution works perfectly.

#### a.2. Fixing Encoding Issues in Artist Names:**

-Encountered encoding problems that caused artist names to be broken.

-Extracted all artist names into a text file.

-De-duplicated the names and converted them back to UTF-8 encoding.

=>This solution is not fully optimal because some Names are missing vowels. However, it remains the best solution so far.

#### a.3. Splitting Artist Names:

-Used the "=TEXTSPLIT()" function in Excel to separate artist names into multiple columns.

-Named the first column "1st Artist", followed by additional artist columns as needed.

=>This solution works perfectly.

#### a.4. Fetching Artist Genres via Spotify API:

-Used the "1st Artist" column to query Spotify’s API for genre information.

-Retrieved genre data and copied it into the second sheet of the Excel file.

-Filled in missing data for some artists and adjusted the results to align with the Spotify API.

=>This solution may introduce bias during the analysis phase because Spotify appears to label genres to fit specific playlists. Therefore, I had to generalize subgenres into macrogenres. Additionally, artists can have multiple genres across their careers, and some songs may not align with their usual style, which can create inconsistencies between a specific song and the labeled genres..

#### a.5. Processing Source File and Weekly Dates:

-Extracted the "Source File" column to the third sheet.

-De-duplicated the column to remove redundant entries.

-Manually entered the starting date and used "= (Previous Cell) + 7" to auto-fill weekly dates.

=>This solution works perfectly.

#### b. Zing MP3


## Appendices

https://www.decisionlab.co/blog/vietnam-music-streaming-industry-q1-2024
https://support.spotify.com/us/artists/article/how-we-count-streams/
