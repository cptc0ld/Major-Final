import pandas as pd
from datetime import datetime, timedelta

def merge_crypto__reddit(crypto_data_filename, reddit_data_filename, crypto_reddit_filename):
    crypto_data_df = pd.read_csv(crypto_data_filename, index_col=0)
    reddit_df = pd.read_csv(reddit_data_filename, index_col=0)
    result = pd.concat([crypto_data_df, reddit_df], axis=1)
    result.to_csv(crypto_reddit_filename)


if __name__ == '__main__':
    crypto_data_filename = 'crypto_data_master_cleaned.csv'
    reddit_data_filename = 'reddit_data_sentiment_bucketized.csv'
    crypto_reddit_filename = 'CryptoDatasetReddit.csv'
    merge_crypto__reddit(crypto_data_filename, reddit_data_filename, crypto_reddit_filename)