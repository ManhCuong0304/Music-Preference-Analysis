# Data Analysis Project: Vietnamese Music Preference in the last decade
## Introduction
### Project Objectives:
A new talent music artist wants to determine whether their music genre appeals to Vietnamese listeners and identify suitable, well-known artists within the same genre for collaboration on their debut song.
### Therefore, the goals of the project are: 
1. To understand the music preference of Vietnamese. 
2. Find the artist with the most dominance appearance in the top 100, 200 chart from all available platforms. 
3. The song that stay in the first position the longest.

## Data preparation
To have the data for the analysis I decided to get the data from the weekly leaderboard for the these 3 platforms which are Apple Music, Spotify, Zing MP3. Youtube music is also a good contender but there has not an option for Vietnamese data in the website for the analysis.
### Data origin
I collected data for:
1. Apple Music from: https://www.top-charts.com/songs/all-genres/vietnam/apple-music

-Top Charts is a third-party website that stores weekly data for Apple Music. Since the official Apple Music website only displays the current music leaderboard, this website serves as the second most credible source for historical data. Since there are multiple weeks of data, I used an automation script via ChatGPT to automatically download the files.

-The original data file contains only three important pieces of data for the analysis: **The position** of the song, **Song name**, and **Artist name**.
Because it is from a third-party website, there might be some incorrect data. However, I compared two weeks of data between Apple Music and Top Charts, and the data appears to be correct.

-There may be bias in the data since not all listeners use this app. Additionally, Apple Music requires a paid subscription to listen, so the results would primarily reflect iPhone users.

-The data is public; therefore, licensing is not an issue.
