import matplotlib.pyplot as plt
import seaborn as sns
import math
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline

def plot_numeric_distribution(df, columns, cols_per_row=3):

    n_cols = cols_per_row
    n_rows = math.ceil(len(columns) / n_cols)

    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(5 * n_cols, 4 * n_rows)
    )

    axes = axes.flatten()

    for i, col in enumerate(columns):

        sns.histplot(
            df[col],
            kde=True,
            ax=axes[i]
        )

        axes[i].set_title(
            f"{col}",
            fontsize=12
        )

        axes[i].set_xlabel(
            col,
            fontsize=9
        )

        axes[i].set_ylabel(
            "Frequency",
            fontsize=9
        )

        axes[i].tick_params(
            axis='both',
            labelsize=8
        )

    
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
    return

def check_outliers(df, columns):
    outliers_per_feature = {}
    total_outliers = 0
    for col in columns:
        Q1=df[col].quantile(0.25)
        Q3=df[col].quantile(0.75)
        IQR=Q3-Q1
        lower_bound=Q1-1.5*IQR
        upper_bound=Q3+1.5*IQR
        n_outliers=(
            (df[col] < lower_bound) | 
            (df[col] > upper_bound)
        ).sum()
        outliers_per_feature[col] = n_outliers
        total_outliers += n_outliers
    print(f'There are {total_outliers} outliers in the dataset.')
    print('-' * 40)
    for feature, count in outliers_per_feature.items():
        print(f'{feature}: {count} outliers, which is {count/len(df)*100:.2f}% of the data.')
    return 


def plot_boxplot(df, columns):
    

    ncols = 3
    nrows = math.ceil(len(columns) / ncols)

    fig, axes = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        figsize=(18, 5 * nrows)
    )

    axes = axes.flatten()

    for i, col in enumerate(columns):
        sns.boxplot(y=df[col], ax=axes[i])
        axes[i].set_title(col)

    # Remove eixos vazios
    for i in range(len(columns), len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()
    return

def plot_scatter_vs_target(df, features, target):

    ncols = 3
    nrows = math.ceil(len(features) / ncols)

    fig, axes = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        figsize=(6*ncols, 5*nrows)
    )

    axes = axes.flatten()

    for i, feature in enumerate(features):
        sns.scatterplot(
            data=df,
            x=feature,
            y=target,
            ax=axes[i]
        )
        axes[i].set_title(f'{feature} vs {target}')

    for j in range(len(features), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
    return

def plot_categorical_distribution(df, columns):

    ncols = 3
    nrows = math.ceil(len(columns) / ncols)

    fig, axes = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        figsize=(18, 5 * nrows)
    )

    axes = axes.flatten()

    for i, col in enumerate(columns):

        sns.countplot(
            data=df,
            x=col,
            ax=axes[i],
            order=df[col].value_counts().index
        )

        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)

    for j in range(len(columns), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

def plot_categorical(df, features, top_n=10, n_cols=3):

    features = [col for col in features if col in df.columns]

    n = len(features)
    n_rows = (n + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(6*n_cols, 5*n_rows)
    )

    axes = axes.flatten()

    for i, col in enumerate(features):

        order = df[col].value_counts().head(top_n).index

        sns.countplot(
            data=df,
            y=col,              # agora é horizontal
            order=order,
            ax=axes[i]
        )

        axes[i].set_title(f"{col}")
        axes[i].set_xlabel("Quantidade")
        axes[i].set_ylabel("")

    for j in range(i+1, len(axes)):
        axes[j].remove()

    plt.tight_layout()
    plt.show()
def plot_boxplot_target(df, category, target, figsize=(12,6), order_by_median=True):
    
    plt.figure(figsize=figsize)
    
    if order_by_median:
        order = df.groupby(category)[target].median().sort_values().index
    else:
        order = None
    
    sns.boxplot(
        data=df,
        x=category,
        y=target,
        order=order
    )
    
    plt.xticks(rotation=45)
    plt.title(f"{target} Distribution by {category}")
    plt.xlabel(category)
    plt.ylabel(target)
    
    plt.tight_layout()
    plt.show()

def high_correlation_pairs(df, threshold=0.8):
    
    corr = df.select_dtypes(include="number").corr()
    
    pairs = []
    
    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i,j]) >= threshold:
                pairs.append(
                    (
                        corr.columns[i],
                        corr.columns[j],
                        corr.iloc[i,j]
                    )
                )
    
    return pd.DataFrame(
        pairs,
        columns=["Feature 1", "Feature 2", "Correlation"]
    )


def compare_models(models, preprocessor, X_train, y_train, folds=5):
    
    kfold = KFold(
        n_splits=folds,
        shuffle=True,
        random_state=42
    )

    results = []

    for name, model in models.items():

        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model)
            ]
        )

        scores = cross_val_score(
            pipeline,
            X_train,
            y_train,
            cv=kfold,
            scoring="neg_root_mean_squared_error"
        )

        results.append({
            "Model": name,
            "RMSE Mean": -scores.mean(),
            "RMSE Std": scores.std()
        })

    results_df = (
        pd.DataFrame(results)
        .sort_values(by="RMSE Mean")
        .reset_index(drop=True)
    )

    return results_df



def plot_model_comparison(results_df):
    
    df = results_df.sort_values(
        by="RMSE Mean",
        ascending=True
    )

    plt.figure(figsize=(5,4))

    plt.barh(
        df["Model"],
        df["RMSE Mean"]
    )

    plt.xlabel("RMSE")
    plt.ylabel("Model")
    plt.title("Model Performance Comparison")

    # adiciona os valores nas barras
    for i, value in enumerate(df["RMSE Mean"]):
        plt.text(
            value,
            i,
            f"{value:.4f}",
            va="center"
        )

    plt.gca().invert_yaxis()

    plt.show()
    return 