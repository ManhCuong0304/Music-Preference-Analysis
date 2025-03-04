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
1. Apple Music from: https://www.top-charts.com/songs/all-genres/vietnam/apple-music

-Top Charts is a third-party website that stores weekly data for Apple Music. Since the official Apple Music website only displays the current music leaderboard, this website serves as the second most credible source for historical data. Since there are multiple weeks of data, I used an automation script via ChatGPT to automatically download the files.

-The original data file contains only three important pieces of data for the analysis: **The position** of the song, **Song name**, and **Artist name**.
Because it is from a third-party website, there might be some incorrect data. However, I compared two weeks of data between Apple Music and Top Charts, and the data appears to be correct.

-There may be bias in the data since not all listeners use this app. Additionally, Apple Music requires a paid subscription to listen, so the results would primarily reflect iPhone paid-users.

-The data is public; therefore, licensing is not an issue.

-Although the listeners on Apple Music are niche and bias by paid-users only. These audiences would have higher chance to spend for albums, concert tickets if the artists success in this platforms. Because of that reason, it is worth to put this data in the analysis.

2. Spotify from: https://charts.spotify.com/charts/overview/global

-This data is a from Spotify official website. Since there are multiple weeks of data, I used an automation script via ChatGPT to automatically download the files.

-The original data file contains only three important pieces of data for the analysis: **The position** of the song, **Song name**, **Artist name**, and **Stream**.

-There may be bias in the data since not all listeners use this app. Spotify offers both a free version and a paid subscription. According to the app (n.d.), a stream is counted as long as a song has been played for at least 30 seconds. Therefore, Spotify's data covers a broader demographic.

-The data is public; therefore, licensing is not an issue.

-Spotify has been attracting a growing number of younger users in recent years. While it has yet to surpass other major platforms in total users, its increasing popularity makes it a valuable addition to the analysis.



Appendix

https://www.decisionlab.co/blog/vietnam-music-streaming-industry-q1-2024
https://support.spotify.com/us/artists/article/how-we-count-streams/
