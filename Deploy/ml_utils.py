import pandas as  pd
import re, json
import joblib as jb
from scipy.sparse import hstack, csr_matrix
import numpy as np



mdl_rf = jb.load("mdl_random_forest.pkl.z")
mdl_lgbm = jb.load("mdl_lgbm.pkl.z")
title_vec_rf = jb.load("title_vectorizer_rf.pkl.z")
title_vec_lgbm = jb.load("title_vectorizer_lgbm.pkl.z")


def compute_features(data):

    publish_date = pd.to_datetime(data['upload_date'])
    views = data['view_count']
    title = data['title']

    features = dict()

    features['time_since_pub'] = (pd.Timestamp.today() - publish_date) / np.timedelta64(1, 'D')
    features['views'] = views
    features['views_per_day'] = features['views'] / features['time_since_pub']
    del features['time_since_pub']

    vectorized_title1 = title_vec_rf.transform([title])
    vectorized_title2 = title_vec_lgbm.transform([title])

    num_features = np.array([features['views'], features['views_per_day']])
    feature_array1 = hstack([num_features, vectorized_title1])
    feature_array2 = hstack([num_features, vectorized_title2])

    return feature_array1, feature_array2


def compute_predictions(data):
    feature_array1, feature_array2 = compute_features(data)

    if feature_array1 is None:
        return 0

    if feature_array2 is None:
        return 0

    p_rf = mdl_rf.predict_proba(feature_array1)[0][1]
    p_lgbm = mdl_lgbm.predict_proba(feature_array2)[0][1]

    p = 0.5*p_rf + 0.5*p_lgbm

    return p
