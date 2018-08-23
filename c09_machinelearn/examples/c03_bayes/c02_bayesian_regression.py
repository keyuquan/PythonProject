import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import helper functions
from c09_machinelearn.mlfromscratch.utils.data_operation import mean_squared_error
from c09_machinelearn.mlfromscratch.utils.data_manipulation import train_test_split
from c09_machinelearn.mlfromscratch.supervised_learning import BayesianRegression


def main():
    # Load temperature data
    data = pd.read_csv('TempLinkoping.txt', sep="\t")

    X = np.atleast_2d(data["time"].as_matrix()).T
    y = np.atleast_2d(data["temp"].as_matrix()).T

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    n_samples, n_features = np.shape(X)

    mu0 = np.array([0] * n_features)
    omega0 = np.diag([.0001] * n_features)
    nu0 = 1
    sigma_sq0 = 100
    cred_int = 10

    clf = BayesianRegression(n_draws=2000,
                             poly_degree=4,
                             mu0=mu0,
                             omega0=omega0,
                             nu0=nu0,
                             sigma_sq0=sigma_sq0,
                             cred_int=cred_int)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # Get prediction line
    y_pred_, y_lower_, y_upper_ = clf.predict(X=X, eti=True)

    # Print the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    print ("Mean Squared Error:", mse)

    # Plot the results
    plt.scatter(366 * X_train, y_train, color="red", s=10)
    plt.scatter(366 * X_test, y_test, color="blue", s=10)
    plt.plot(366 * X, y_pred_, color="black", linewidth=2, label="Prediction")
    plt.plot(366 * X, y_lower_, color="gray", linewidth=2, label="{0}% Credible Interval".format(cred_int))
    plt.plot(366 * X, y_upper_, color="gray", linewidth=2)
    plt.axis((0, 366, -20, 25))
    plt.suptitle("Bayesian Regression")
    plt.title("MSE: %.2f" % mse, fontsize=10)
    plt.xlabel('Day')
    plt.ylabel('Temperature in Celcius')
    plt.legend(loc='lower right')
    # plt.legend((m1, m2), ("Training data", "Test data"), loc='lower right')
    plt.legend(loc='lower right')

    plt.show()


if __name__ == "__main__":
    main()
