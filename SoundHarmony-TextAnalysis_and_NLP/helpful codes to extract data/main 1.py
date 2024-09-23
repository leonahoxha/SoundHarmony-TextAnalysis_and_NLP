import praw
import csv
import pandas as pd
import os

reddit = praw.Reddit(
    client_id="atgBYswOC6paf68xkeOQ3w",
    client_secret="IQAdZJZ3h4CzBQ2-GJFeTb6vU3ldog",
    user_agent="project by u/Specialist_Act485"
)

# Search query for cyberbullying
search_query = "samsung galaxy buds fe"

# Initialize a DataFrame to store the data
samsunggalaxy_budsfe= pd.DataFrame(columns=['Subreddit', 'Post_Title', 'Post_ID', 'Post_Author', 'Post_URL', 'Post_Score', 'Num_Comments', 'Created', 'Comment', 'Comment_Author', 'Comment_Score'])

# Limit the search to top 10 posts
top_posts = reddit.subreddit("all").search(query=search_query, sort="relevance", time_filter="all", limit=10)

for post in top_posts:
    post_row = {
        'Subreddit': post.subreddit.display_name,
        'Post_Title': post.title,
        'Post_ID': post.id,
        'Post_Author': str(post.author),  # Convert author object to string
        'Post_URL': post.url,
        'Post_Score': post.score,
        'Num_Comments': len(post.comments), # Get number of comments for the post
        'Created': post.created_utc,
        'Comment': None,  # Placeholder for comment text
        'Comment_Author': None,  # Placeholder for comment author
        'Comment_Score': None  # Placeholder for comment score
    }
    post.comments.replace_more(limit=None)
    comments = post.comments.list()
    for comment in comments:
        comment_row = {
            'Subreddit': post.subreddit.display_name,
            'Post_Title': post.title,  # Include post title for comments
            'Post_ID': post.id,
            'Post_Author': str(post.author),  # Convert author object to string
            'Post_URL': post.url,
            'Post_Score': post.score, # Get score for each comment
            'Num_Comments': len(comments), # Total comments for the post
            'Created': comment.created_utc,
            'Comment': comment.body,
            'Comment_Author': str(comment.author),  # Convert author object to string
            'Comment_Score': comment.score
        }
        samsunggalaxy_budsfe = samsunggalaxy_budsfe.append(comment_row, ignore_index=True)

    # Append post without comments
    samsunggalaxy_budsfe = samsunggalaxy_budsfe.append(post_row, ignore_index=True)

# Specify the folder path
folder_path = "data"

# Save the DataFrame to a CSV file in the data folder
file_path = os.path.join(folder_path, 'samsunggalaxy_budsfe.csv')
samsunggalaxy_budsfe.to_csv(file_path, index=False)