import streamlit as st
import pandas as pd
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')


def build_model(data):
    from xgboost import XGBClassifier
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2
    features = ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer",
                "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"]
    X = data[features[:11]]
    y = data['status']
    best_features = SelectKBest(score_func=chi2, k=3)
    fit = best_features.fit(X, y)
    scores = fit.scores_
    scores_df = pd.DataFrame({'Feature': X.columns, 'Score': scores})
    scores_df.sort_values('Score', ascending=False).reset_index(
        drop=True, inplace=True)
    X = data[scores_df.Feature[:3]]
    y = data['status']
    model = XGBClassifier()
    return model, X.columns


st.set_page_config(page_title="Parkinson's disease",
                   layout='wide')
st.write("""
# Predicting Parkinson's disease
We use Xgboost library to predict whether a person has Parkinson's disease or not.
Try adjusting the hyperparameters!
""")

parkinson_df = pd.read_csv(r'data/parkinsons.csv', index_col='name')
model, features = build_model(parkinson_df)
X = parkinson_df[features]
y = parkinson_df['status']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = metrics.accuracy_score(y_test, y_pred)
st.write("""
## Accuracy : """)
st.info(acc)

mdvp_fo = st.number_input("MDVP:Fo(Hz)", min_value=89.0,
                          max_value=260.0, value=119.992)
mdvp_fhi = st.number_input("MDVP:Fhi(Hz)", min_value=103.0,
                           max_value=590.0, value=157.302)
mdvp_flo = st.number_input("MDVP:Flo(Hz)", min_value=65.0,
                           max_value=239.0, value=74.997)
if st.button("Submit"):
    test = pd.DataFrame(
        {'MDVP:Fo(Hz)': [mdvp_fo], 'MDVP:Fhi(Hz)': [mdvp_fhi], 'MDVP:Flo(Hz)': [mdvp_flo]})
    st.write("""
    ### Result""")

    pred = model.predict(test)[0]
    if pred:
        st.error("The person has Parkinson's disease")
    else:
        st.success("The person does not have Parkinson's disease")
