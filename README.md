# Data Analysis Project: Vietnamese Music Preference from 2018 to 2024
## I. Introduction
A new talent music artist wants to determine whether their music genre appeals to Vietnamese listeners and identify suitable, well-known artists within the same genre for collaboration on their debut album. The Analysis Project will help that artist to understand the overall listener demographic, the best candidate to invite for the collaboration, what platform that the artist's song would perform the best.

## II. Project Objectives: 
1. Analyze Vietnamese music preferences, including genre distribution and the influence of foreign versus local music.
2. Identify the most dominant artists based on their appearances in the charts across all available platforms.
3. Determine the songs that have held the first position multiple times.
4. Identify potential artists for collaboration, and the best platform to release the song.

## III. Tools that were used in analysis
1. Python/Visual Studio Code: To get the scripts for collecting raw data.
2. Excel: To store and organize the data.
3. Power BI: To create visualizations for the analysis.

## IV. Skills
1. Knowing how websites are built to scrape data effectively.
2. Writing good prompts to generate the right scripts.
3. Cleaning data and solving problems along the way.
4. Creating clear and impactful visualizations.
5. Making decisions to match requirements based on data.

## V. About the Datasets (Please review Data preparation.doc for more information)
1. Data sources:

Apple Music: https://www.top-charts.com/songs/all-genres/vietnam/apple-music

Spotify: https://charts.spotify.com/charts/view/regional-vn-weekly/latest

Zing MP3: https://zingmp3.vn/zing-chart-tuan/Bai-hat-Viet-Nam/IWZ9Z08I.html

2. Orignal data columns:

a. **Song Name:** The name of the Song

b. **Rank position (Integer):** The position of the Song in the week in number format

c. **Artist Name (Merge):** The name of the Artist(s) of that song

3. Add-in data:

a. **Rank position (String):** The position of the song in the week in ordinal format

b. **1st Artist:** The name of the 1st Artist of the song

c. **2nd Artist:** The name of the 2nd Artist of the song. There will be multiple columns for artists depending on the number of artists in the song.

d. **Genres:** The name of the Genres of the song

e. **Date:** The starting day of the week varies between platforms

f. **Solo vs Featuring:** To differentiate whether the song is a solo track or a collaboration

g. **Vietnamese vs Foreign:** To differentiate whether the song is made by Vietnamese artist(s) or foreign artist(s)

Apple Music's weekly chart features 100 songs, Spotify's includes 200, and Zing MP3's chart consists of 40 songs.

## VI. Metrics
-These will be the metrics used in the analyses:

1. **Vietnamese Music Genre Preferences (2018-2024):** To show the changes in listeners' genre preferences from 2018 to 2024

2. **Solo vs. Featuring Songs (Total Weeks on Chart):** Count the total number of Solo tracks and Featured tracks

3. **Vietnamese vs. Foreign Artists (Total Weeks on Chart):** Count the total number of Vietnamese tracks and Foreign tracks

4. **10 Artists with the Most Appearances in the Top 100, 200, or 40 (Total Weeks on Chart):** Count the total number of weekly chart appearances for the top 10 Artists

5. **10 Featured Artists with the Most Appearances in the Top 100, 200, or 40 (Total Weeks on Chart):** Count the total number of weekly chart appearances for the top 10 Featured Artists

6. **10 Songs That Stayed in the Top 100, 200, or 40 the Longest (Total Weeks on Chart):** Count the total number of weekly chart appearances for the top 10 Songs

7. **Vietnamese Music Genre Preferences of the Top Songs (2018-2024):** To show the changes in listeners' genre preferences for the songs that reached the 1st position from 2018 to 2024

8. **Solo vs. Featuring Songs (Total of Weeks #1):** Count the total number of Solo tracks and Featured tracks for the songs that reached the 1st position

9. **Vietnamese vs. Foreign Artists (Total Weeks #1):** Count the total number of Vietnamese tracks and Foreign tracks for the songs that reached the 1st position

10. **Most Dominant Artists in the Charts (Total of Weeks at #1):** Count the total number of weekly chart appearances for the Artists that reached the 1st position

11. **Most Dominant Featured Artists in the Charts (Total of Weeks at #1):** Count the total number of weekly chart appearances for the Featured Artists that reached the 1st position

12. **Most Dominant Songs in the Charts (Total of Weeks at #1):** Count the total number of weekly chart appearances for the Songs that reached the 1st position

13. **X's Song Performance (Total Weeks on Chart) (X will be the name of the Artist):** Count the total number of weekly chart appearances for X's Songs

14. **Artists Featured in Xs's Songs (Total Weeks on Chart) (X will be the name of the Artist):** Count the total number of weekly chart appearances for the Artists that featured in X's Songs

15. **Performance of Songs Featuring X (Total Weeks on Chart) (X will be the name of the Artist):** Count the total number of weekly chart appearances for the Songs that have X as the Featured Artist

16. **Artists Who Featured X (Total Weeks on Chart) (X will be the name of the Artist):** Count the total number of weekly chart appearances for the Artists that have X as the Featured Artist

## VII. Visualizations & Data Analysis
### 1. Apple Music

### a.1. Overall Analysis Visualization 1

### a.1.1. Visualization 1

![image](https://github.com/user-attachments/assets/c9fa3e5c-67ab-4daa-bf21-ce0b89acf866)

### a.1.2. Overall Analysis

-Overall, on the Apple Music platform, Vietnamese listeners have gradually shifted their preference from US-UK pop to V-pop. As a result, music by Vietnamese artists has appeared more frequently in the Weekly Rank Chart since 2021.

-Taylor Swift is the most relevant artist in the chart with 1035 appearances. Despite being a foreign artist in the Vietnamese preference chart and the overall decline in demand for US-UK pop, her songs still hold strong replay value.

-tlinh is the most relevant featured artist in the chart, with songs featuring her appearing 350 times in the weekly most-listened songs chart.

-The song that stayed in the Top 100 the longest is **Lối Nhỏ** by Đen with 252 appearances. It remained in the weekly chart for the entire years of 2021 and 2022, missing only 1 week in 2021 and 2023. However, in the latest year, it only stayed for 35 weeks.

### a.2. Overall Analysis Visualization 2

### a.2.1. Visualization 2

![image](https://github.com/user-attachments/assets/35d76324-4ee1-4b88-a915-7de021f9650d)

### a.2.2. Analysis

-The genre preferences of the top songs were quite diverse in 2021, but by 2024, only three genres dominated the competition for the top spots: V-pop, Pop, and K-pop.

-The gap between Vietnamese and foreign artists in securing the No.1 spot has narrowed, shifting from Vietnamese songs holding the top position 41 times versus foreign songs 11 times in 2022 to a closer 31-21 split in 2024.

-Sơn Tùng M-TP is undoubtedly the "King of V-pop" as he is the Most Dominant Artist on this platform, reaching the First position 26 times. He achieved this with seven different songs, with **Chúng ta của hiện tại** and **Đừng làm trái tim anh đau** being the two biggest hits, each reaching No.1 seven times. Additionally, Chúng ta của hiện tại stayed relevant for 194 weeks.

-itsnk is the Most Dominant Featured Artist, with two songs reaching the number 1 spot, one of which held the position 15 times.

-Even though Sơn Tùng has multiple hits, the Most Dominant Song does not belong to him. **Từng Quen** by Wren Evans holds this title, ranking 1st for 15 weeks—an impressive feat for a young artist like him. Perhaps because of this success, both he and tlinh secured collaborations with Apple: "[Cứu lấy âm nhạc](https://www.youtube.com/watch?v=3K6PRfAp6O4)" and "[đừng làm nó phức tạp](https://www.youtube.com/watch?v=k2oCfQ5QOIk)".  It seems that Apple wanted to position itself as a young and energetic brand, as they actively promoted these two music videos. The Like-to-View ratio for Wren's song is only 0.11%, indicating that while the video was not highly engaging, it was seen by a large audience through advertising.

_-To identify the perfect candidate for collaboration, an individual analysis is required. Among the top five artists in the Most Dominant Artists chart, three stand out as potential candidates. Sơn Tùng M-TP is primarily known for his solo songs, with his only collaboration being with a foreign artist, while Mono has had just one song reach the top. Therefore, Wren Evans, tlinh, and Đen have been selected for individual analysis._

### b.1. Individual Analysis Visualization 1

![image](https://github.com/user-attachments/assets/5a38714b-803f-47dc-af46-4f46fe61c8be)

### b.2. Individual Analysis Visualization 2

![image](https://github.com/user-attachments/assets/87397554-bfe2-4900-af99-28508bfb1c5c)

### b.3. Individual Analysis

### b.3.1 Wren Evans

-From Visualization 1, although Wren Evans has multiple songs categorized as featuring songs, his main collaborator, itsnk, is a producer. The only true artist who contributed a verse was Evy, but that song did not achieve the same level of success as the others. From Visualization 2, Wren Evans' performance as a collaborator was decent. However, compared to other candidates, he struggled to compete.

### b.3.2 Đen

-When Đen is the main artist, he has introduced many talented artists like Biên, Nguyên Thảo, Ngọc Linh, and the latest young singer, Pia Linh, to the audience. On the other hand, the songs he was featured in were by well-known artists. Đen could be a great artist to collaborate with, as he helps boost the recognition of new artists. However, he seems to prioritize singers who excel in pop to balance the structure of his songs, given that he is a rapper.

### b.3.3 tlinh

-tlinh is the best candidate to be invited as a collaborator. She excels in her solo songs (with 215 weeks on the chart), in songs featuring a producer (2Pillz, with 124 weeks on the chart), and even more impressively, in songs where other artists featured her (132, 87, and 64 weeks on the chart from three different songs and artists, respectively).

### 2. Spotify

### a.1. Overall Analysis Visualization 1

### a.1.1. Visualization 1

![image](https://github.com/user-attachments/assets/6b8d5ba3-8c78-4b93-bd73-6c7b4f385f16)

### a.1.2. Analysis

-Overall, the data from Spotify is relatively similar to Apple Music. V-pop songs have gradually replaced US-UK pop songs in the 2024 weekly charts. Additionally, local hip-hop has gained traction among Spotify listeners, becoming the second most popular genre for the Vietnamese audience. As a result, Vietnamese songs appeared a total of 8915 times in Spotify’s most-listened weekly charts in 2024, a significant increase from just 2051 appearances in 2018, highlighting the growing demand for Vietnamese music each year.

-BTS is the most relevant artist or in this case, the most dominant band with their songs appearing in the weekly chart a total of 3046 times. Notably, 2020 was their peak year, with 738 appearances over 53 weeks. This means that, on average, 14 out of the 200 songs on the chart each week belonged to BTS.

-Duongg is the featured artists with the most appearances on Spotify, with 607 times.

-"Lạ Lùng" by Vũ. is the song that stayed in the chart the longest with 351 consecutive week appearances.

### a.2. Overall Analysis Visualization 2

### a.2.1. Visualization 2

![image](https://github.com/user-attachments/assets/7b768e82-9ff1-4591-80fb-b01cffda45da)

### a.2.2. Analysis

-Even though the overall data shows that the preference for K-pop has declined since 2022, the Rank 1 data highlights its dominance, with K-pop holding the top spot for 46 out of 52 weeks in 2024.

-Aside from Korean artists, many foreign artists also held the No. 1 spot for several weeks. These findings suggest that while the overall preference is shifting toward local music, Vietnamese songs still face significant challenges in reaching the top.

-Artists from Korea dominated the weekly first position, with BTS leading the charge at 55 times in the top spot. Among its members, Jung Kook’s solo projects outperformed BTS, achieving the highest number of first-place appearances at 60 times, while Jimin ranked fourth with 26 times at number one. Even the "King of V-pop" struggled to surpass this idol group. A possible explanation is that BTS fans were highly dedicated, consistently "farming stream counts" to maintain their favorite artists at the top. This hypothesis will be further explored in the Bonus section.

-The most dominant featured artist is Latto, with 43 appearances across two versions of the same Jung Kook song.

-The most dominant song is Seven (explicit version) with 27 times at the top position, followed by Seven (normal version) in second place with 16 times. It wasn’t until the sixth position that a Vietnamese song appeared, Chúng ta của hiện tại by Sơn Tùng, with 12 times at number 1. The top 10 most dominant songs consisted of 8 K-pop tracks, highlighting the intense competition for the top weekly song on the Spotify platform.

_-To identify the perfect candidate for collaboration, an individual analysis is required. Since inviting foreign artists for collaboration is unrealistic for a new artist, foreign artist data was filtered out. The final top five were Sơn Tùng M-TP, Đen, Da LAB, Mỹ Tâm, and Vũ. Among these five, Sơn Tùng was not a good fit for collaboration, as previously discussed. Despite being repetitive, Đen was selected again because he is the second most successful Vietnamese artist on Spotify. Da LAB was chosen because the band had a song that reached the top position five times and remained relevant for 329 weeks. Vũ was selected as the final candidate for individual analysis due to having a song that appeared in nearly every weekly chart since its release. Additionally, he has featured in many collaborations, unlike Mỹ Tâm, who primarily focuses on solo projects._

### b.1. Individual Analysis Visualization 1

![image](https://github.com/user-attachments/assets/3f1638e1-42a9-402a-b51d-45272262f250)

### b.2. Individual Analysis Visualization 2

![image](https://github.com/user-attachments/assets/47044852-8885-47f3-af5c-970d47e5030e)

### b.3. Individual Analysis

### b.3.1. Đen

-Đen's performance as the main artist is relatively similar to Apple Music. However, when he is featured in other artists' songs, his performance is better on this platform in terms of the songs' relevance and the variety of artists he collaborates with. He is one of the best artist for the collaboration.

### b.3.2. Da LAB

-Da LAB, as a band, excels in their solo tracks. When featuring other artists, they typically collaborate with established names, with Juky San being the only emerging artist they have worked with. Their performance as featured artists was solid but not outstanding, as they are often featured alongside their member Emcee L in his solo projects.

### b.3.3. Vũ

-Vũ's solo tracks are phenomenal in terms of relevancy. He collaborates with both well-known artists like Hà Anh Tuấn, Binz, and Low G, as well as emerging talents like TRANG and Mạc Mai Sương. As a featured artist, he played a significant role in boosting Madihu's career with the song Vì Anh Đâu Có Biết from Madihu’s debut album.

### 3. Zing MP3

### a.1. Overall Analysis Visualization 1

### a.1.1. Visualization 1

![image](https://github.com/user-attachments/assets/3df63b9e-6824-467f-8a48-f797b6dcbedf)

### a.1.2. Analysis

-Since foreign songs have a separate chart, the genre data consists only of Vietnamese genres, with V-pop once again being the most popular. 

-The most relevant artist on this platform is Châu Khải Phong, with a total of 363 appearances. The listener demographics on this platform differ significantly from the other two, as the most relevant artists and songs contrast sharply with those on Apple Music and Spotify. Notably, artists like Hương Ly, Lê Bảo Bình, and even the most relevant artist, Châu Khải Phong, are relatively unfamiliar in mainstream media.

-ACV is the most relevant featured artist with 683 appearance times.

-"Cô Phòng" by Hồ Quang Hiếu is the most listed song in the weekly charts, with only 38 appearances. This is a relatively low figure, likely because Zing MP3’s weekly chart only features 40 songs, leading to lower total appearances.

### a.2. Overall Analysis Visualization 2

### a.2.1. Visualization 2

![image](https://github.com/user-attachments/assets/3181dd95-468d-4866-8e54-faaa41b328f0)

### a.2.2. Analysis

-The most dominant artist on Zing MP3 is Jack-J97, who held the top position 26 times, while the most dominant song is "Cắt đôi nỗi sầu" by Tăng Duy Tân, which reached No. 1 a total of 12 times. 

-The most dominant featured artist is ACV, with 23 appearances at the top position. ACV is an excellent featured artist on Zing MP3, having helped five artists reach the number 1 spot.

_-Although these artists seem not suitable for our artist since they are only thriving on Zing MP3, there will also be an individual analysis to ensure a fair judgment.The 3 prominent collaborators are Hương Ly, Châu Khải Phong, and Đạt G, as the other artists are either solo performers or prefer collaborating with producers._
 
### b.1. Individual Analysis Visualization 1

![image](https://github.com/user-attachments/assets/1f038cdd-dcc9-4b49-92b0-3eca0fcd16fe)

### b.2. Individual Analysis Visualization 2

![image](https://github.com/user-attachments/assets/208839cb-bbc2-4b00-90b2-d0cf02954027)

### b.3. Individual Analysis

### b.3.1. Hương Ly

-As the main artist, Hương Ly's performance is impressive. Although her solo tracks appeared more frequently on the chart, she has a fair share of songs featuring other artists. The variety of featured artists also showcases her versatility in music. As the guest artist in others' songs, her performance is strong, with one featured song appearing 20 times in the charts.

### b.3.2. Châu Khải Phong

-Châu Khải Phong's performance as the main artist is remarkable, with six songs appearing more than 20 times on the chart, one of which peaked at 32 appearances. ACV is his best collaborator, as they worked together on 10 tracks, while his other featured artists were lackluster in terms of song relevance. As the featured artist, his performance was not as strong compared to the other two potential collaborators.

### b.3.3. Đạt G

-Đạt G seems to prefer working on solo tracks or collaborating with Du Uyen. His songs as the main artist did not perform as well as the other two. Despite that, when it comes to being a featured artist, he is the best among the three.

## VIII. Conclusion
1. Analyze Vietnamese music preferences, including genre distribution and the influence of foreign versus local music.

-Overall, aside from Zing MP3, which consists solely of Vietnamese songs' genres, the other two platforms have shown a shift in preference from foreign songs' genres to Vietnamese songs' genres.

2. Identify the most dominant artists based on their appearances in the charts across all available platforms.

-The artist with the most overall appearances on Apple Music is Taylor Swift, with 1,035 appearances. The most dominant artist is Sơn Tùng M-TP, who held the first position for 26 weeks.

-The artist with the most overall appearances on Spotify is BTS, with 3,046 appearances. The most dominant artist is Jung Kook, who held the first position for 60 weeks.

-The artist with the most overall appearances on Zing MP3 is Châu Khải Phong, with 363 appearances. The most dominant artist is Jack-J97, who held the first position for 26 weeks.

3. Determine the songs that have held the first position multiple times.

-"Lối Nhỏ" by Đen is the most relevant song on Apple Music with 252 appearances. The most dominant song is "Từng Quen" by Wren Evans and itsnk, that held the first position for 15 weeks.

-"Lạ Lùng" by Vũ. is the most relevant song on Spotify with 351 appearances. The most dominant song is "Seven (Explicit Version)" by Jung Kook and Latto, that held the first position for 27 weeks.

-"Cô Phòng" by Hồ Quang Hiếu is the most relevant song on Zing MP3 with 38 appearances. The most dominant song is "Cắt đôi nỗi sầu" by Tăng Duy Tân, that held the first position for 12 weeks.

4. Identify potential artists for collaboration, and the best platform to release the song.

-On the Apple Music platform, both Đen and tlinh are perfect choices for collaboration. Đen is known for working with young artists, while songs where tlinh is a Featured Artist tend to remain on the weekly charts for multiple weeks.

-On the Spotify platform, both Đen and Vũ are excellent choices for collaboration. Đen's reason remains the same as on Apple Music, while Vũ has experience in promoting new artists, his collaboration with Madihu serves as solid evidence.

-On the Zing MP3 platform, Đạt G is the best choice for collaboration due to his experience working with various artists and his strong reputation in the past.
