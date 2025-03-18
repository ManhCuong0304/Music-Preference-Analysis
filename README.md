# Data Analysis Project: Vietnamese Music Preference from 2018 to 2024
## Introduction
A new talent music artist wants to determine whether their music genre appeals to Vietnamese listeners and identify suitable, well-known artists within the same genre for collaboration on their debut album. The Analysis Project will help that artist to understand the overall listener demographic, the best candidate to invite for the collaboration, what platform that the artist's song would perform the best.
## Project Objectives: 
1. Analyze Vietnamese music preferences, including genre distribution and the influence of foreign versus local music.
2. Identify the most dominant artists based on their appearances in the charts across all available platforms.
3. Determine the songs that have held the first position multiple times.
4. Identify potential artists for collaboration, and the best platform to release the song.
## Tools that were used in analysis
1. Python/Visual Studio Code: To get the scripts for collecting raw data.
2. Excel: To store and organize the data.
3. Power BI: To create visualizations for the analysis.
## Skills
1. Knowing how websites are built to scrape data effectively.
2. Writing good prompts to generate the right scripts.
3. Cleaning data and solving problems along the way.
4. Creating clear and impactful visualizations.
5. Making decisions to match requirements based on data.
## About the Datasets (Look at Data preparation.doc for more information)
Orignal data: Song Name, Rank position (Num), Artist Name (Merge).

Add-in data: 1st Artist, 2nd Artist, etc, Genres, Date, Solo vs Featuring, Vietnamese vs Foreign.

Apple Music's weekly chart features 100 songs, Spotify's includes 200, and Zing MP3's chart consists of 40 songs.
## Visualizations & Data Analysis
### 1. Apple Music

### a.1. Overall Analysis Visualization

![image](https://github.com/user-attachments/assets/d2b40306-54d5-4050-a09e-ab38e583b23c)

### a.2. Overall Analysis

-Overall, on the Apple Music platform, Vietnamese listeners have gradually shifted their preference from US-UK pop to V-pop. As a result, music by Vietnamese artists has appeared more frequently in the Weekly Rank Chart since 2021.

-Sơn Tùng M-TP is undoubtedly the "King of V-pop" as he is the Most Dominant Artist on this platform, reaching the First position 26 times. He achieved this with seven different songs, with Chúng ta của hiện tại and Đừng làm trái tim anh đau being the two biggest hits, each reaching No.1 seven times. Additionally, Chúng ta của hiện tại stayed relevant for 194 weeks.

-Even though he has multiple hits, the Most Dominant Song does not belong to Sơn Tùng M-TP. Từng Quen by Wren Evans holds this title, ranking 1st for 15 weeks—an impressive feat for a young artist like him. Perhaps because of this success, both he and tlinh secured collaborations with Apple: "[Cứu lấy âm nhạc](https://www.youtube.com/watch?v=3K6PRfAp6O4)" and "[đừng làm nó phức tạp](https://www.youtube.com/watch?v=k2oCfQ5QOIk)".  It seems that Apple wanted to position itself as a young and energetic brand, as they actively promoted these two music videos. The Like-to-View ratio for Wren's song is only 0.11%, indicating that while the video was not highly engaging, it was seen by a large audience through advertising.

-To identify the perfect candidate for collaboration, an individual analysis is required. Among the top five artists in the Most Dominant Artists chart, three stand out as potential candidates. Sơn Tùng M-TP is primarily known for his solo songs, with his only collaboration being with a foreign artist, while Mono has had just one song reach the top. Therefore, Wren Evans, tlinh, and Đen have been selected for individual analysis.

### b.1. Individual Analysis Visualization 1

![image](https://github.com/user-attachments/assets/bd5ff59b-b9eb-4113-b0bd-f1fef6e6e040)

### b.2. Individual Analysis Visualization 2

![image](https://github.com/user-attachments/assets/fe5b581d-2dd3-4ebf-b7e9-5ae4a785a7e6)

### b.3. Individual Analysis

### b.3.1 Wren Evans

-From Visualization 1, although Wren Evans has multiple songs categorized as featuring songs, his main collaborator, itsnk, is a producer. The only true artist who contributed a verse was Evy, but that song did not achieve the same level of success as the others. From Visualization 2, Wren Evans' performance as a collaborator was decent. However, compared to other candidates, he struggled to compete.

### b.3.2 Đen

-When Đen is the main artist, he has introduced many talented artists like Biên, Nguyên Thảo, Ngọc Linh, and the latest young singer, Pia Linh, to the audience. On the other hand, the songs he was featured in were by well-known artists. Đen could be a great artist to collaborate with, as he helps boost the recognition of new artists. However, he seems to prioritize singers who excel in pop to balance the structure of his songs, given that he is a rapper.

### b.3.3 tlinh

-tlinh is the best candidate to be invited as a collaborator. She excels in her solo songs (with 215 weeks on the chart), in songs featuring a producer (2Pillz, with 124 weeks on the chart), and even more impressively, in songs where other artists featured her (132, 87, and 64 weeks on the chart from three different songs and artists, respectively).

### 2. Spotify

### a.1. Overall Analysis Visualization

![image](https://github.com/user-attachments/assets/e1a0d612-d3a1-4fe7-9585-9b6cab249a48)

### a.2. Overall Analysis

-Overall, the data from Spotify is relatively similar to Apple Music. V-pop songs have gradually replaced US-UK pop songs in the 2024 weekly charts. Additionally, local hip-hop has gained traction among Spotify listeners, becoming the second most popular genre for the Vietnamese audience. As a result, Vietnamese songs appeared a total of 8915 times in Spotify’s most-listened weekly charts in 2024, a significant increase from just 2051 appearances in 2018, highlighting the growing demand for Vietnamese music each year.

-Even though the preference for Korean music has declined since 2022, artists from Korea dominated the weekly first position, especially BTS and the group members (Jung Kook and Jimin). Even the "King of V-pop" struggled to overtake the first position from that idol band. There is a hypothesis that the fans of this band were dedicated enough to consistently "farm stream counts." This hypothesis will be discussed in the **Bonus section**. Aside from Korean artists, many foreign artists also held the No. 1 spot for several weeks. These findings suggest that while the overall preference is shifting toward local music, Vietnamese songs still face significant challenges in reaching the top.

-The most dominant song is "Seven (explicit version)" with 27 times at the top position, followed by "Seven (normal version)" in second place with 16 times. It wasn’t until the sixth position that a Vietnamese song appeared,"Chúng ta của hiện tại" by Sơn Tùng, with 12 times at number one. The top 10 most dominant songs consisted of 8 K-pop tracks, highlighting the intense competition for the top weekly song on the Spotify platform.

-To identify the perfect candidate for collaboration, an individual analysis is required. Since inviting foreign artists for collaboration is unrealistic for a new artist, foreign artist data was filtered out. The final top five were Sơn Tùng M-TP, Đen, Da LAB, Mỹ Tâm, and Vũ. Among these five, Sơn Tùng was not a good fit for collaboration, as previously discussed. Despite being repetitive, Đen was selected again because he is the second most successful Vietnamese artist on Spotify. Da LAB was chosen because the band had a song that reached the top position five times and remained relevant for 329 weeks. Vũ was selected as the final candidate for individual analysis due to having a song that appeared in nearly every weekly chart since its release. Additionally, he has featured in many collaborations, unlike Mỹ Tâm, who primarily focuses on solo projects.



