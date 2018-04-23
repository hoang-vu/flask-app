import pickle

with open("python_lin_reg_model.pkl", "wb") as file_handler:
    pickle.dump(lin_reg, file_handler)

with open("python_lin_reg_model.pkl", "rb") as file_handler:
    loaded_pickle = pickle.load(file_handler)

loaded_pickle