# What Drives the Price of Video Games on Steam?
## <span style="color: Teal; font-weight: bold"> Business Understanding & Assessing the Situation</span>

<span style="color: Teal; text-decoration: underline">**Determine Business Objectives:**</span> Video games are now <a href="https://www.forbes.com/sites/forbesagencycouncil/2023/11/17/the-gaming-industry-a-behemoth-with-unprecedented-global-reach/">one of the largest enterainment industries in the world</a>, and Steam is one of the largest platforms for the distribution and hosting of personal computer (PC) games, and has been for <a href="https://archive.vn/JkIMI">over a decade</a>. Many video game developers release a variety of games on Steam of different genres, budgets, and quality, all tailored to different market segments. Developers have a strong interest in predicting how popular their games will be and which price points to choose when selling their games. Therefore, high-quality data showing what characteristics of games are related to popularity and price are of great interest (and great value) to video game developers looking to distribute games to a wide PC audience.

<span style="color: Teal; text-decoration: underline">**Assess Situation:**</span> I am working with data from <a href="https://www.kaggle.com/datasets/artermiloff/steam-games-dataset/data">Kaggle</a>, scraped from the <a href="https://partner.steamgames.com/doc/sdk/api">Steamworks API</a>, containing data on video games sold on the Steam storefront. The data is up to date as of May 2024, which is recent enough to be relevant to developers currently forming/refining business strategies in their development and distribution of their games. The dataset contains data for games released many years ago but the price points given are those that are current as of May 2024, so some care will need to be taken regarding the release window of games--the price of games tend to go down within a year after their release and may steadily decrease in price after that. There are many features that consisting JSON-formatted strings holding multiple pieces of information (e.g., metadata tags, game genre, etc.), and these will have to be dealt with on a case-by-case basis, with decisions made about how to use this data to predict game price.

The main benefit from this analysis will be identifying the core characteristics of games that are associated with higher prices, but this data will not be able to show causal relationships. Foe example, it may be the case that games of a certain genre (e.g., first-person shooters) sell for more on average, and an economist may conclude that the high price is due to high demand. However, it may be the case that they sell for more because they are inherently more expensive to make and maintain, and so price points are higher for games of this genre. Furthermore, it may be the case that most games in this genre do not sell enough copies to recoup their expensive production and advertising costs. Identifying factors that predict both price and popularity will help to ameliorate this and similar questions, but because the data is cross-sectional and there are many considerations that go into how profitable a game will be beyond popularity and price, care should be taken in the interpretation of findings to ensure that the analysis is used to wisely influence business strategies.

<span style="color: Teal; text-decoration: underline">**Data Mining Goals:**</span> The goal of this project will be to identify the multivariate relationships in the data that predict (A) price point of games and (B) game popularity. The project will be deemed a success if one (or more) models can be built predicting the targets significantly above baseline and results in tangible advice that businesses could use to improve their business strategy.

<span style="color: Teal; text-decoration: underline">**Project Plan:**</span> The data has already been scarped from the internet, and only exploratory data analysis, data cleaning, and data modeling are left. The project will consist of the aforementioned data preprocessing and data processing steps, as well as writing a summary of findings.

## <span style="color: Teal; font-weight: bold">Data Understanding</span>
The data has already been cleaned and duplicates removed. The data has 46 features in total, but only a few will be used in modeling.
<p align="center">
<img src="images/df_initial_info.png">
<p></p>
I examined the target, video game price in May 2024 (<code>price</code>), and discovered that the variable was very positively skewed (i.e., there were a few games worth over $500) as well as many games with a $0 <code>price</code> (so-called "free to play" games, where developers make money through microstransactions and ads). I decided to focus my efforts on games with a price range between $10 and $100. However, <code>price</code> for these games was still significantly positively skewed, so I removed all games with a <code>price</code> greater than 3 standard deviations above the mean to remove outliers. To make the final distribution more normally distributed, I also applied a log transformation function. The final distribution for <code>price</code> looks like this:
<p align="center">
<img src="images/price hist_no xform.png">
<p></p>
<p align="center">
<img src="images/price hist_log xform.png">
<p></p>
After data cleaning, the data had 

This dataset has many possible predictors, and some of them are in unique JSON-like or list-like format. After extracting relevant information, I decided to focus on a few different categories of predictors:
<ul>
  <li><b>Support Features</b> (e.g., does the game have a dedicated website and support email) and <b>Language Availability</b> (i.e., how many languages does the game have text and audio for)</li>
  <li><b>Categories and Genres</b> of games, like 'Multi-player' (category) and 'Casual' (genre)</li>
  <li><b>Tags</b> of games (e.g., descriptors like 'Indie', 'Multiplayer', and 'Open World' that describe game elements)</li>
</ul>
There was a great deal of data munging required to transform categories and genres, and tags, into usable features. Each feature had over thirty values, and many values were barely represented in the data. I decided to keep only those tags which were present in at least 10% of the data, to avoid having too many unbalanced classes among the predictors. After all cleaning and transformation was complete, I kept the following representations of categories and genres, and tags, in the data:
<ul>
  <li><b>Categories and Genres</b>: I kept a feature representing whether a game had a specific category or genre mapped to it in the data</li>
  <li><b>Tags</b>: Tags can be added and voted on by players, and the number of players who signify that a game has a tag may be as important as the fact whether a game has a tag at all. To capture both possibilities, I created two datasets for tags: one capturing whether a game had a tag at all (with 0 and 1 values), and another dataset with the total number of times that each tag had been selected for each game.</li>
</ul>

## <span style="color: Teal; font-weight: bold">Exploratory Data Analysis</span>
After all necessary data transformation, I ran EDA to check the correlations between predictors and the target (<code>price_log</code>) and look at the distribution of <code>price_log</code> within categories and genres, and within tags. Due to their size, the full correlation matrices are not included below, but can be found <a href="">here</a>.
<p align="center">
<img src="images/correlations_mainline.png">
<p></p>

<p align="center">
<img src="images/price hist_log xform.png">
<p></p>

<p align="center">
<img src="images/price hist_log xform.png">
<p></p>



## <span style="color: Teal; font-weight: bold">Data Modeling</span>
